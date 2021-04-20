# import math
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('nose_data.csv')
# print(df.head())
# fig = plt.figure(figsize=(16,9))
# ax = fig.add_subplot(111)
# ax.plot(df['Time'],df['Pressure'])
# ax.set_ylabel('')
# ax.set_xlabel('Time')
# ax.set_ylim(900,1300)
# ax.set_xlim(14860,)
# plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# df = pd.read_csv('nose_data.csv')
# df2 = df[df['Time']>=14860]
# df2.to_csv('new.csv', mode='a')
df = pd.read_csv('nose_data_new.csv')
# plt.plot(df['Time'],df['Pressure'])
# plt.xlim(14860,14900)
# plt.ylim(900,1300)
# plt.show()
df2 = df[df['Time']<14862.90]
df3 = df[df['Time']<14904.23]
df4 = df[df['Time']<14874.07]
Pressure_0 = sum(df2['Pressure'])/len(df2['Pressure'])

print(Pressure_0)

Time = np.array(df4['Time'])
Pressure = np.array(df4['Pressure'])
Temperature = np.array(df4['Temperature'])

print(min(df4['Pressure']))

height = (((Pressure_0/Pressure)**(1/5.257) - 1.)*(Temperature+273.15))/0.0065
max = max(height)
tii = Time[np.argmax(height)]
print(max,tii)


Time = np.array(df3['Time'])
Pressure = np.array(df3['Pressure'])
Temperature = np.array(df3['Temperature'])
height = (((Pressure_0/Pressure)**(1/5.257) - 1.)*(Temperature+273.15))/0.0065

plt.plot(Time,height)
plt.scatter(tii,max,color='red')
plt.xlabel('Time [s]')
plt.ylabel('Height [m]')
# plt.title('Maximum altitude reached')
hh = list(height)
# print(hh,type(hh))
# print(tii,type(tii))
plt.vlines(14873.57, 0,max, "red", linestyles='dashed')
plt.hlines(max,Time[0],14873.57,'red',linestyles='dashed')
plt.text(14873.57,0,'  14873.57 [s]')
plt.text(Time[0],max,str(max)+' [m]')
plt.show()
