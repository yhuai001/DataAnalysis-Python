#Stacked Bars
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

plt.figure(figsize=(10,8))

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)
#create your plot here
plt.bar(range(5),
        As,
        bottom=As)
plt.bar(range(5),
        Bs,
        bottom=Bs)
plt.bar(range(5),
        Cs,
        bottom=c_bottom)
plt.bar(range(5),
       	Ds,
        bottom=d_bottom)
plt.bar(range(5),
       	Fs,
        bottom=f_bottom)

ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics,rotation=20) 
plt.title('Grade distribution')
plt.xlabel('Unit')
plt.ylabel('Number of Students')

plt.savefig('my_stacked_bar.png')
plt.show()