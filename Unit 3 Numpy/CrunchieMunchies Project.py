#CrunchieMunchies
import codecademylib
import numpy as np
calorie_stats = np.genfromtxt('cereal.csv', delimiter=",")
average_calories = np.mean(calorie_stats)
calorie_stats_sorted = np.sort(calorie_stats)
median_calories = np.median(calorie_stats)
print median_calories
nth_percentile = np.percentile(calorie_stats,3.2899)
print nth_percentile
more_calories = np.mean(calorie_stats > 60)
print more_calories
calorie_sted = np.std(calorie_stats)
print calorie_sted