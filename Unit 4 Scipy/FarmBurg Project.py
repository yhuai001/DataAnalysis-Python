#FarmBurg Project
import pandas as pd

df = pd.read_csv("clicks.csv")
print df.head()

#Calculating Purchase Rates

df['is_purchase'] = df.click_day.apply(
  lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase'
)

purchase_counts = df.groupby(['group', 'is_purchase'])\
	.user_id.count().reset_index()

print purchase_counts

#Performing a Significance Test
num_visits = len(df)
p_clicks_099 = 1000/0.99/num_visits
p_clicks_199 = 1000/1.99/num_visits
p_clicks_499 = 1000/4.99/num_visits
print num_visits, p_clicks_099, p_clicks_199, p_clicks_499

#Calculating Necessary Purchase Rates
df = pd.read_csv('clicks.csv')

num_visits = len(df)
p_clicks_099 = 1000/0.99/num_visits
p_clicks_199 = 1000/1.99/num_visits
p_clicks_499 = 1000/4.99/num_visits
print num_visits, p_clicks_099, p_clicks_199, p_clicks_499


df['is_purchase'] = df.click_day.apply(
  lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase'
)

purchase_counts = df.groupby(['group', 'is_purchase'])\
	.user_id.count().reset_index()

print purchase_counts

num_visits = len(df)

p_clicks_099 = (1000 / 0.99) / num_visits
p_clicks_199 = (1000 / 1.99) / num_visits
p_clicks_499 = (1000 / 4.99) / num_visits

from scipy.stats import binom_test

pvalueA = binom_test(316, 1666, p_clicks_099)
pvalueB = binom_test(183, 1666, p_clicks_199)
pvalueC = binom_test(83, 1666, p_clicks_499)
print pvalueA,pvalueB,pvalueC
final_answer = 4.99