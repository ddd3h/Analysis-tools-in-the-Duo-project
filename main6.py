import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
speed = []
Time = []
variable = []

df = pd.read_csv('nose_data_new.csv')
df2 = df[df['Time']<14862.90]
df3 = df[df['Time']<14904.23]

Pressure_0 = sum(df2['Pressure'])/len(df2['Pressure'])
Pressure = np.array(df3['Pressure'])
Temperature = np.array(df3['Temperature'])
Height = (((Pressure_0/Pressure)**(1/5.257) - 1.)*(Temperature+273.15))/0.0065

df3['Height'] = Height
df4 = df3[(df3['Time']>=14862) & (df3['Time'] <= 14873)]
df4.to_csv('Hi.csv')
#
# for i in range(len(df3['Time'])-1):
#     if df3['Pressure'][i] == df3['Pressure'][i+1]:
#         continue
#     else:
#         variable.append(i)
#
# print(variable)
#
# for i in range(len(variable) - 1):
#     p = variable[i]
#     q = variable[i+1]
#     print(p,q)
#     averageTime = (df3['Time'][p] + df3['Time'][q])/2
#     Time.append(averageTime)
#     speed_cal = (df3['Height'][q] - df3['Height'][p])/(df3['Time'][q] - df3['Time'][p])
#     speed.append(speed_cal)
#
# data = pd.DataFrame(list(zip(Time,speed)),columns=['Time','Speed'])
# data.to_csv('hello.csv')
#
# plt.plot(Time,speed)
# plt.show()
