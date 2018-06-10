import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)
print total_visitor_count, paying_visitor_count

baseline_percent = 100 * 93/500
print baseline_percent

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
print average_payment

new_customers_needed = np.ceil(1240 / average_payment)
print new_customers_needed

percentage_point_increase = 100 * 47/500
print percentage_point_increase

minimum_detectable_effect = 100 * 9/18
print minimum_detectable_effect


ab_sample_size = 310