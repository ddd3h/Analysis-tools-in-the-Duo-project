import pandas as pd
import matplotlib.pyplot as plt

file_name = 'nose_data.csv'

df = pd.read_csv(file_name)

fig = plt.figure(figsize=(16,9))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)

Xlable_name = 'Time [s]'
t1 = 14860
t2 = 15000

ax1.plot(df['Time'],df['sensorValue'])
ax1.set_ylabel('sensorValue')
ax1.set_xlabel(Xlable_name)
ax1.set_ylim(-10,3)
ax1.set_xlim(t1,t2)

ax2.plot(df['Time'],df['Temperature'])
ax2.set_ylabel('Temperature [°C]')
ax2.set_xlabel(Xlable_name)
ax2.set_ylim(18,30)
ax2.set_xlim(t1,t2)

ax3.plot(df['Time'],df['Pressure'])
ax3.set_ylabel('Pressure [hPa]')
ax3.set_xlabel(Xlable_name)
ax3.set_ylim(930,1030)
ax3.set_xlim(t1,t2)

# ax4.plot(df['Time'],df['Velocity'])
# ax4.set_ylabel('Velocity [m/s]')
# ax4.set_xlabel(Xlable_name)
# ax4.set_ylim(0,120)
# ax4.set_xlim(t1,t2)

# plt.plot(df['Time'],df['sensorValue'])
# plt.xlabel('Time [s]')
# plt.ylabel('sensorValue')
# plt.xlim(14860, 14880)
# plt.ylim(-10, 100)

plt.show()
