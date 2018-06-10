#Setting indices
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

df2 = df.loc[[1, 3, 5]]
print df2
df3 = df2.reset_index()

print df3

df2.reset_index(inplace = True, drop = True)

print df2




#Review
import pandas as pd

orders = pd.read_csv('shoefly.csv')

print orders.head()

emails = orders.email

frances_palmer = orders[(orders.first_name == 'Frances') | (orders.last_name == 'Palmer')]

comfy_shoes = orders[orders.shoe_type.isin(['clogs','boots','ballet flats'])]