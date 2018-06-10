#Distributions
import numpy as np
# Write matplotlib import here:
from matplotlib import pyplot as plt

commutes = np.genfromtxt('commutes.csv', delimiter=',')

# Plot histogram here:
plt.hist(commutes, bins=6,  range=(20,50))

plt.show()

import numpy as np
from matplotlib import pyplot as plt

# Brachiosaurus
b_data = np.random.normal(6.7, 0.7, size=1000)

# Fictionosaurus
f_data = np.random.normal(7.7, 0.3, size=1000)

plt.hist(b_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Brachiosaurus')
plt.hist(f_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Fictionosaurus')
plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()

mystery_dino = 'brachiosaurus'

answer = False

#Binomial
emails = np.random.binomial(500, 0.05, size=10000)

plt.hist(emails)
plt.show()

emails = np.random.binomial(500, 0.05, size=10000)

no_emails = np.mean(emails == 0)

b_test_emails = np.mean(emails > 40)

print no_emails, b_test_emails