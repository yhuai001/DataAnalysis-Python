-- First query
SELECT COUNT(*)
FROM newspaper
WHERE start_month < 3
	AND end_month > 3;
  
-- Second query  
SELECT *
FROM newspaper
CROSS JOIN months;

-- Third query
SELECT *
FROM newspaper
CROSS JOIN months
WHERE month > start_month
	AND month < end_month;
  
SELECT month,
  COUNT(*) as subscribers
FROM newspaper
CROSS JOIN months
WHERE month > start_month
  AND month < end_month
GROUP BY month;

WITH previous_query AS(
SELECT customer_id,
       COUNT(subscription_id) as subscriptions
FROM orders
GROUP BY customer_id
)
SELECT customers.customer_name, previous_query.subscriptions
FROM previous_query
JOIN customers
ON previous_query.customer_id = customers.customer_id;