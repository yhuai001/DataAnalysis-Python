import pandas as pd

df = pd.read_csv('employees.csv')

# Add columns here

df['last_name'] = df.name.apply(lambda x: x.split()[-1])
print df

#Applying a Lambda to a Row
import pandas as pd

df = pd.read_csv('employees.csv')
total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) *   	   								(row.hours_worked - 40)) \
							 if row.hours_worked > 40 \
 							 else row.hourly_wage * row.hours_worked
  
df['total_earned'] = df.apply(total_earned, axis = 1)

print df

#Renaming Columns
import pandas as pd

df = pd.read_csv('imdb.csv')

# Rename columns here
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print df

df.rename(columns={
  'name': 'movie_title'},
  inplace = True
         )
print df