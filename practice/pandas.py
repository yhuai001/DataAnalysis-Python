add_two = lambda my_input: my_input + 2
check_if_A  = lambda grade: 'Got an A!' if grade >=90 else 'Did not get an A...'


import pandas as pd

inventory = pd.read_csv('inventory.csv')
total_value = lambda row:(row.quantity * row.price)
inventory['total_value'] = inventory.apply(total_value, axis=1)

staten_island = inventory.head(10)
staten_island['product_request'] = staten_island.product_description

inventory['in_stock'] = inventory.quantity.apply(lambda x: True
                                                 if x > 0
                                                 else False)

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print inventory.head(10)
print staten_island