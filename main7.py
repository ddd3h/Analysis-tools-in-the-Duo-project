import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

df = pd.read_csv('nose_data_new.csv')

plt.plot(df['Time'],df['sensorValue'])
plt.xlabel('Time [s]')
plt.ylabel('sensorValue [-]')
plt.ylim(-10,200)
plt.show()

sensorValue = np.array(df['sensorValue'])
offset = sum(df['sensorValue'][0:20])/len(df['sensorValue'][0:20])

sensorValueA = sensorValue - offset
sensorValueB = abs(sensorValueA)
sensorMax = 4023
voltage = 0
kpa = 0
voltageMax = 5
kpaRangeTopVoltage = 4.5
bb = 5/3.25
#
sensorValueC = sensorValueB*bb
#
voltage = sensorValueC * (voltageMax / sensorMax)
# kpa = ((voltage / kpaRangeTopVoltage)) / 0.018
kpa = 10*voltage

# print(voltage)
# print(kpa)
#
Pressure = np.array(df['Pressure'])
Temperature = np.array(df['Temperature'])
#
# print(Pressure)
# print(Temperature)
#
R = 2.87
#
rho = Pressure/(R*(Temperature+273.15))
# print(rho)
Velocity = (2*kpa*1000/rho)**(1/2)
# print(Velocity)
#
plt.plot(df['Time'], Velocity)
plt.ylim(0,50)
plt.xlim(14862,14863)
# plt.plot(df['Time'],df['Height'])
plt.show()
