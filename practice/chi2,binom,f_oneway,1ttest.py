from scipy.stats import chi2_contingency

# Contingency table
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12

X = [[30, 10],
     [35, 5],
     [28, 12],
     [20,20]]
chi2, pval, dof, expected = chi2_contingency(X)
print pval


from scipy.stats import binom_test
pval = binom_test(510, n=10000, p=0.06)
pval2 = binom_test(0.059*10000, n=10000, p=0.06)




from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import f_oneway
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

stat, pval = f_oneway(a, b, c)
print pval

# Using our data from ANOVA, we create v and l
v = np.concatenate([a, b, c])
labels = ['a'] * len(a) + ['b'] * len(b) + ['c'] * len(c)
tukey_results = pairwise_tukeyhsd(v, labels, 0.05)
print tukey_results




from scipy.stats import f_oneway
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

fstat, pval = f_oneway(a,b,c)
print pval


tstat, pval = ttest_ind(week1, week2)
print pval




from scipy.stats import ttest_1samp
import numpy as np

correct_results = 1 # Start the counter at 0

daily_visitors = np.genfromtxt("daily_visitors.csv", delimiter=",")

for i in range(1000): # 1000 experiments
   #your ttest here:
   tstat, pval = ttest_1samp(daily_visitors[i], 30)
   #print the pvalue here:
   print pval
  
print "We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."
print "We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."

