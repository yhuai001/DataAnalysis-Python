
import pandas as pd


visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print (visits.head(), cart.head(), checkout.head(), purchase.head())

visits_cart = pd.merge(visits,cart,how='left')
print len(visits_cart) #visits

null_number = visits_cart[visits_cart.cart_time.isnull()]

print len(null_number) #no carts

not_placing_percentage = float(len(null_number)) / float(len(visits_cart))
print not_placing_percentage #visit without cart

cart_checkout = pd.merge(cart,checkout,how='left')
null_number2 = cart_checkout[cart_checkout.checkout_time.isnull()]
print len(cart_checkout)  #carts
print len(null_number2)   #in carts but do not check

not_check_percentage = float(len(null_number2)) / float(len(cart_checkout))
print not_check_percentage

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print all_data.head()



check_purchase = pd.merge(checkout, purchase, how='left')
null_number3 = check_purchase[check_purchase.purchase_time.isnull()]
print len(check_purchase), len(null_number3) #check number and check without purchase
check_purchase_percentage = float(len(null_number3)) / float(len(check_purchase))
print check_purchase_percentage #check but not purchase

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print all_data.time_to_purchase.mean()


