#FetchMaker
import numpy as np
import fetchmaker
from scipy.stats import chi2_contingency
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
rottweiler_tl_mean = np.mean(rottweiler_tl)
rottweiler_tl_std = np.std(rottweiler_tl)
print rottweiler_tl
print rottweiler_tl_mean, rottweiler_tl_std

whippet_rescue = fetchmaker.get_is_rescue("whippet")
print whippet_rescue
num_whippet_rescues = np.count_nonzero(whippet_rescue)
print num_whippet_rescues
num_whippets = np.size(whippet_rescue)
print num_whippets

pval = binom_test(6, n=100, p=0.08)
print pval

a = fetchmaker.get_weight("whippet")
b = fetchmaker.get_weight("terrier")
c = fetchmaker.get_weight("pitbull")
fstat, pval = f_oneway(a,b,c)
print pval

v = np.concatenate([a, b, c])
labels = ['a'] * len(a) + ['b'] * len(b) + ['c'] * len(c)
tukey_results = pairwise_tukeyhsd(v, labels, 0.05)
print tukey_results

poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")

black_poodle = np.count_nonzero(poodle_colors == "black")
brown_poodle = np.count_nonzero(poodle_colors == "brown")
gold_poodle = np.count_nonzero(poodle_colors == "gold")
grey_poodle = np.count_nonzero(poodle_colors == "grey")
white_poodle = np.count_nonzero(poodle_colors == "white")
print black_poodle,brown_poodle,gold_poodle,grey_poodle,white_poodle

black_shihtzu = np.count_nonzero(shihtzu_colors == "black")
brown_shihtzu = np.count_nonzero(shihtzu_colors == "brown")
gold_shihtzu = np.count_nonzero(shihtzu_colors == "gold")
grey_shihtzu = np.count_nonzero(shihtzu_colors == "grey")
white_shihtzu = np.count_nonzero(shihtzu_colors == "white")
print black_shihtzu,brown_shihtzu,gold_shihtzu,grey_shihtzu,white_shihtzu

color_table = [[17, 10],
     [13, 36],
     [8, 6],
     [52,41],
     [10,7]]

chi2, pval, dof, expected = chi2_contingency(color_table)
print pval