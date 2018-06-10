#1
from matplotlib import pyplot as plt

x = [0,1,2,3,4,5]
y1 = [2000,2001,2002,2003,2004,2005]
y2 = [2010,2011,2012,2013,2014,2015]

plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color='gray', marker='o')
plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.legend(['1-axis','2-axis'], loc=4)
plt.show()


#2
from matplotlib import pyplot as plt

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1, 2, 1)
plt.plot(months, temperature)

plt.subplot(1, 2, 2)
plt.plot(temperature, flights_to_hawaii, ":")

plt.show()