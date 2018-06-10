#Calculating Column Statistics
#1
import pandas as pd
import numpy as np

orders = pd.read_csv('orders.csv')
print orders.head(10)

most_expensive = orders.price.max()
print most_expensive

num_colors = orders.shoe_color.nunique()
print num_colors


#2
orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max()
print pricey_shoes
print (type(pricey_shoes))

#3
orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()

print pricey_shoes

print type(pricey_shoes)


#4
orders = pd.read_csv('orders.csv')

cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()

print cheap_shoes


#5
orders = pd.read_csv('orders.csv')
print orders
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

shoe_counts = shoe_counts.rename(columns={'id':'counts'})
print shoe_counts