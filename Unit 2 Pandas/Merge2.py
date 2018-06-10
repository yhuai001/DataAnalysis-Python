#1
import pandas as pd

orders = pd.read_csv('orders.csv')
print orders
products = pd.read_csv('products.csv')
print products

orders_products = pd.merge(
														orders,
														products.rename(columns={'id': 'product_id'}))
print orders_products

#2
orders = pd.read_csv('orders.csv')
print orders
products = pd.read_csv('products.csv')
print products

orders_products = pd.merge(
	orders,
	products,
	left_on = 'product_id',
	right_on = 'id',
	suffixes = ['_orders', '_products']
)

print orders_products



#3
merged_df = pd.merge(orders,products)
print merged_df


#Outer 
store_a = pd.read_csv('store_a.csv')
print store_a
store_b = pd.read_csv('store_b.csv')
print store_b

store_a_b_outer = pd.merge(store_a, store_b, how='outer')
print store_a_b_outer


#Left
store_a = pd.read_csv('store_a.csv')
print store_a
store_b = pd.read_csv('store_b.csv')
print store_b

store_a_b_left = pd.merge(store_a,store_b,how='left')
store_b_a_left = pd.merge(store_b,store_a,how='left')
print(store_a_b_left)
print(store_b_a_left)

#Concatenate
bakery = pd.read_csv('bakery.csv')
print bakery
ice_cream = pd.read_csv('ice_cream.csv')
print ice_cream

menu = pd.concat([bakery,ice_cream])
print menu


#Review
visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])

print visits
print checkouts

v_to_c = pd.merge(visits,checkouts)
v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time
print v_to_c

print v_to_c.time.mean()