import pandas as pd
import numpy as np
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# one hot вид
unique_categories = data['whoAmI'].unique()
for category in unique_categories:
    data[category] = np.where(data['whoAmI'] == category, 1, 0)
print(data.head())