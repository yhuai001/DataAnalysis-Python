import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print ad_clicks.head()

most_views = ad_clicks.groupby('utm_source').user_id.count().reset_index().rename(columns={'user_id':'counts'})
print most_views


ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index().rename(columns={'user_id':'counts'})

print clicks_by_source

clicks_pivot = clicks_by_source.pivot(columns='is_click',index='utm_source',values='counts').reset_index()
print clicks_pivot

clicks_pivot['percent_clicked'] = clicks_pivot[True]/ (clicks_pivot[True]+ clicks_pivot[False])
print clicks_pivot

A_or_B = ad_clicks.groupby('experimental_group').user_id.count().reset_index().rename(columns={'user_id':'counts'})
print A_or_B

A_or_B_percentage = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index().rename(columns={'user_id':'counts'})

print A_or_B_percentage

A_or_B_pivot = A_or_B_percentage.pivot(columns='is_click',index='experimental_group',values='counts').reset_index()
print A_or_B_pivot

A_or_B_pivot['percent_clicked'] = A_or_B_pivot[True]/ (A_or_B_pivot[True]+ A_or_B_pivot[False])

print A_or_B_pivot

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

print a_clicks
print b_clicks

a_clicks_day = a_clicks.groupby(['is_click','day']).user_id.count().reset_index().rename(columns={'user_id':'counts'})
print a_clicks_day 

a_clicks_day_pivot = a_clicks_day.pivot(columns='is_click',index='day',values='counts').reset_index()
print a_clicks_day_pivot

a_clicks_day_pivot['percent_clicked'] = a_clicks_day_pivot[True]/ (a_clicks_day_pivot[True]+ a_clicks_day_pivot[False])

print a_clicks_day_pivot





b_clicks_day = b_clicks.groupby(['is_click','day']).user_id.count().reset_index().rename(columns={'user_id':'counts'})
print b_clicks_day 

b_clicks_day_pivot = b_clicks_day.pivot(columns='is_click',index='day',values='counts').reset_index()
print b_clicks_day_pivot

b_clicks_day_pivot['percent_clicked'] = b_clicks_day_pivot[True]/ (b_clicks_day_pivot[True]+ b_clicks_day_pivot[False])

print b_clicks_day_pivot

