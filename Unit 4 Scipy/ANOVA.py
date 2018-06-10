#ANOVA
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

fstat, pval = f_oneway(a,b,c)
print pval

#Assumptions of Numerical Hypothesis Tests
import codecademylib
import numpy as np
import matplotlib.pyplot as plt

dist_1 = np.genfromtxt("1.csv",  delimiter=",")
dist_2 = np.genfromtxt("2.csv",  delimiter=",")
dist_3 = np.genfromtxt("3.csv",  delimiter=",")
dist_4 = np.genfromtxt("4.csv",  delimiter=",")

#plot your histogram here
plt.hist(dist_1)
plt.show()
plt.hist(dist_2)
plt.show()
plt.hist(dist_3)
plt.show()
plt.hist(dist_4)
plt.show()
not_normal = 2
ratio = np.std(dist_2)/np.std(dist_3)
print ratio



