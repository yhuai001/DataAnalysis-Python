import pandas as pd

bakery = pd.read_csv('bakery.csv')
print bakery
ice_cream = pd.read_csv('ice_cream.csv')
print ice_cream

menu = pd.concat([bakery,ice_cream])
print menu




store_a = pd.read_csv('store_a.csv')
print store_a
store_b = pd.read_csv('store_b.csv')
print store_b

store_a_b_left = pd.merge(store_a,store_b,how='left')
store_b_a_left = pd.merge(store_b,store_a,how='left')
print(store_a_b_left)
print(store_b_a_left)




store_a_b_outer = pd.merge(store_a, store_b, how='outer')
print store_a_b_outer



orders_products = pd.merge(
	orders,
	products,
	left_on = 'product_id',
	right_on = 'id',
	suffixes = ['_orders', '_products']
)

print orders_products

merged_df = pd.merge(orders,products)
print merged_df



orders_products = pd.merge(
														orders,
														products.rename(columns={'id': 'product_id'}))
print orders_products





results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]


















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