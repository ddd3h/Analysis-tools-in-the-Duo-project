# -*- coding: utf-8 -*-
#このファイルはノーズ電装が取得したバイナリコードを自動的にCSVファイルに変換し，解析を行うコードです．

import math

file_name = "nose_data"
n = 1
sensorValue = 0
sensorMax = 4095
#sensorOffset = 200
voltage = 0
kpa = 0
voltageMax = 5.0
sensorOffset = 0
kpaRangeTopVoltage = 4.5
array = [0,0,0,0,0,0,0,0]
R = 2.87
SAMPLING_RATE = 200

csv_file = open(file_name+'.csv','a')
print('Complete loading ' + str(file_name)+'.csv')

binary_file = open(file_name+'.bin','rb')
print('Complete loading ' + str(file_name)+'.bin')

print("")

print('Converting...')
csv_file.write('No,Time,sensorValue,voltage,kpa,Temperature,Pressure,Velocity\n')

while True:
  binary_data_d = binary_file.read(4)
  binary_data_t = binary_file.read(4)
  binary_data_p = binary_file.read(4)

  if n == 0:
    continue
  elif len(binary_data_d) == 0 or len(binary_data_t) == 0 or len(binary_data_p) == 0:
    break

  int_data_d = int.from_bytes(binary_data_d,byteorder='big')
  int_data_t = int.from_bytes(binary_data_t,byteorder='big')
  int_data_p = int.from_bytes(binary_data_p,byteorder='big')

  sensorValue = int_data_d
  Temperature = int_data_t/100
  Pressure = int_data_p/10000

  sensorValueC = sensorValue - sensorOffset
  voltage = sensorValueC * (voltageMax / sensorMax)
  kpa = ((voltage / kpaRangeTopVoltage) - 0.04) / 0.018
  rho = Pressure/(R*(Temperature+273.15))
  Velocity = math.sqrt(2*abs(kpa)*10/rho)

  array[0] = str(n)
  array[1] = str(n/SAMPLING_RATE)
  array[2] = str(sensorValue)
  array[3] = str(voltage)
  array[4] = str(kpa)
  array[5] = str(Temperature)
  array[6] = str(Pressure)
  array[7] = str(Velocity)

  for i in range(8):
    csv_file.write(array[i])
    if i == 7:
      continue
    csv_file.write(',')

  csv_file.write('\n')
  print('Complete: ' + str(n))
  n+=1

print('Done!')

csv_file.close()

print('Installing Analyze module....')
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(str(file_name)+'.csv')

print('Loading CSV File....')

fig = plt.figure(figsize=(16,9))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

Xlable_name = 'Time [s]'

ax1.plot(df['Time'],df['kpa'])
ax1.set_ylabel('Differential Pressure [kPa]')
ax1.set_xlabel(Xlable_name)
ax1.set_ylim(0,40)

ax2.plot(df['Time'],df['Temperature'])
ax2.set_ylabel('Temperature [degree]')
ax2.set_xlabel(Xlable_name)
ax2.set_ylim(18,30)

ax3.plot(df['Time'],df['Pressure'])
ax3.set_ylabel('Pressure [hPa]')
ax3.set_xlabel(Xlable_name)
ax3.set_ylim(990,1030)

ax4.plot(df['Time'],df['Velocity'])
ax4.set_ylabel('Velocity [m/s]')
ax4.set_xlabel(Xlable_name)
ax4.set_ylim(0,120)

fig.savefig(str(file_name)+'.png')

print('complete saving ' + str(file_name)+'.png')

plt.show()
