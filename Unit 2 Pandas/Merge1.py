#1
import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

customers = pd.read_csv('customers.csv')

print orders 
print products
print customers

order_3_description = 'thing-a-ma-jig'
order_5_phone_number = '112-358-1321'

#2
sales = pd.read_csv('sales.csv')
print sales
targets = pd.read_csv('targets.csv')
print targets

sales_vs_targets = pd.merge(sales,targets)
print sales_vs_targets
crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]
print crushing_it

#3
sales = pd.read_csv('sales.csv')

targets = pd.read_csv('targets.csv')

men_women = pd.read_csv('men_women_sales.csv')

all_data = sales.merge(targets)\
	.merge(men_women)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]


