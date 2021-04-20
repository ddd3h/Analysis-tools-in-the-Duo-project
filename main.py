
#definition
file_name = "test"
n = 1
sensorValue = 0
sensorMax = 4095
sensorOffset = 72
voltage = 0
kpa = 0
voltageMax = 5.0
kpaRangeTopVoltage = 4.5

csv_file = open(file_name+'.csv','a')
print('Complete loading ' + str(file_name)+'.csv')

binary_file = open(file_name+'.bin','rb')
print('Complete loading ' + str(file_name)+'.bin')

print("")

print('Converting...')
csv_file.write('No,sensorValue,voltage,kpa,Tempreture,Pressure\n')

while True:
  binary_data = binary_file.read(4)

  if len(binary_data) == 0:
    break

  sensorValue = int.from_bytes(binary_data,byteorder='big')

  voltage = sensorValue * (voltageMax / sensorMax)
  kpa = ((voltage / kpaRangeTopVoltage) - 0.04) / 0.018
  csv_file.write( str(n) + ',' + str(sensorValue) + ',' + str(voltage) + ',' + str(kpa))
  csv_file.write('\n')
  print('Complete: ' + str(n))
  n+=1

print('Done!')

csv_file.close()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(str(file_name)+'.csv')

print('Loading CSV File....')

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(df['No'], df['kpa'])
plt.ylabel('Differential Pressure')
plt.xlabel('Number of Data')

fig.savefig(str(file_name)+'.png')

print('complete saving ' + str(file_name)+'.png')

plt.show()
