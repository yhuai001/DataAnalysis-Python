#Familiar: A Study In Data Analysis
import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
import numpy as np

vein_pack_lifespans = familiar.lifespans(package='vein')
vein_pack_lifespans_avg = np.mean(vein_pack_lifespans)
print vein_pack_lifespans_avg

tstat, pval = ttest_1samp(vein_pack_lifespans, 71)
print pval
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
if pval < 0.05:
	print "The Vein Pack Is Proven To Make You Live Longer!"
else:
  print "The Vein Pack Is Probably Good For You Somehow!"
  
  
  
   
artery_pack_lifespans = familiar.lifespans(package='artery')
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)

tstat, pval = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print pval

if pval<0.05:
		print "the Artery Package guarantees even stronger results!"
else:
 	 print "the Artery Package is also a great product!"


iron_contingency_table = familiar.iron_counts_for_package()

chi2,iron_pvalue, dof, expected = chi2_contingency(iron_contingency_table)
print iron_pvalue
if pval<0.05:
		print "The Artery Package Is Proven To Make You Healthier!"
else:
 	 print "While We Can't Say The Artery Package Will Help You, I Bet It's Nice!"