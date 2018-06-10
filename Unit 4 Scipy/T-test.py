#1 Sample T-Testing
from scipy.stats import ttest_1samp
import numpy as np

ages = np.genfromtxt("ages.csv")
print ages
ages_mean = np.mean(ages)
tstat, pval = ttest_1samp(ages, 30)
print pval

correct_results = 1 # Start the counter at 0

daily_visitors = np.genfromtxt("daily_visitors.csv", delimiter=",")

for i in range(1000): # 1000 experiments
   #your ttest here:
   tstat, pval = ttest_1samp(daily_visitors[i], 30)
   #print the pvalue here:
   print pval
  
print "We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."
print "We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."


#2 Sample T-Test
from scipy.stats import ttest_ind
import numpy as np

week1 = np.genfromtxt("week1.csv",  delimiter=",")
week2 = np.genfromtxt("week2.csv",  delimiter=",")

week1_mean = np.mean(week1)
week2_mean = np.mean(week2)
week1_std = np.std(week1)
week2_std = np.std(week2)

tstat, pval = ttest_ind(week1, week2)
print pval



#3 Dangers of Multiple T-Tests
from scipy.stats import ttest_ind
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

a_mean = np.mean(a)
b_mean = np.mean(b)
c_mean = np.mean(c)
a_std = np.std(a)
b_std = np.std(b)
c_std = np.std(c)

tstat,a_b_pval = ttest_ind(a,b)
tstat,a_c_pval = ttest_ind(a,c)
tstat,b_c_pval = ttest_ind(b,c)

error_prob = 1 - 0.95**3