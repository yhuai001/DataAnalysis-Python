#1
from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, 
        labels=payment_method_names,
        autopct='%0.1f%%')
plt.axis('equal')
plt.legend(payment_method_names, loc=3)
plt.show()

#2
from matplotlib import pyplot as plt
from script import sales_times

plt.hist(sales_times, bins=20)
plt.show()

#3
from matplotlib import pyplot as plt
from script import sales_times1
from script import sales_times2

plt.hist(sales_times1, bins=20, alpha=0.4, normed=True,histtype='step')

plt.hist(sales_times2, bins=20, alpha=0.4, normed=True)
plt.show()