import numpy as np
from matplotlib import pyplot as plt

sunflowers = np.genfromtxt('sunflower_heights.csv',
                           delimiter=',')

# Calculate mean and std of sunflowers here:
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)

# Calculate sunflowers_normal here:
sunflowers_normal = np.random.normal(sunflowers_mean, sunflowers_std, size=5000)

plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='observed', normed=True)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='normal', normed=True)
plt.legend()
plt.show()

# Calculate probabilities here:
experiments = np.random.binomial(200, 0.1, size=5000)
prob = np.mean(experiments < 20)
print prob







import numpy as np
cupcakes = np.array([2, 0.75, 2, 1, 0.5])
recipes = np.genfromtxt('recipes.csv', delimiter=',')
print recipes

eggs = recipes[0:, 2]
print eggs

cookies = recipes[2,0:]
print cookies

double_batch = cupcakes + cupcakes
print double_batch







grocery_list = cookies + double_batch
print grocery_list
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