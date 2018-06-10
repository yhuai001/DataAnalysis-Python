#Binomial Test
from scipy.stats import binom_test
pval = binom_test(510, n=10000, p=0.06)
print pval
pval2 = binom_test(0.059*10000, n=10000, p=0.06)
print pval2


#Chi Square Test

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

