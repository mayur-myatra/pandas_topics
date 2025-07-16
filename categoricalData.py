import pandas as pd
import numpy as np
import time

data = {
    'Customer': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
    'Segment': ['Premium', 'Regular', 'Premium', 'Regular', 'Premium']
}

df = pd.DataFrame(data)

# Convert to categorical type
df['Segment'] = df['Segment'].astype('category')

print(df)
print("\nData types:\n", df.dtypes)

# Output:
#   Customer  Segment
# 0    Alice  Premium
# 1      Bob  Regular
# 2  Charlie  Premium
# 3    Diana  Regular
# 4     Evan  Premium

# Data types:
#  Customer      object
# Segment     category
# dtype: object

# Simulate 1 million rows
n = 1_000_000
np.random.seed(0)
segments = ['Regular', 'Premium', 'VIP']

df_obj = pd.DataFrame({
    'CustomerID': range(n),
    'Segment': np.random.choice(segments, size=n),
    'Sales': np.random.randint(100, 1000, size=n)
})

print("OG Data")
print(df_obj)



df_cat = df_obj.copy()
df_cat['Segment'] = df_cat['Segment'].astype('category')

# Group By Segment
start = time.time()
df_obj.groupby('Segment')['Sales'].sum()
print("Object GroupBy Time: ", round(time.time() - start, 4), "seconds")

# Group by Segment (categorical type)
start = time.time()
df_cat.groupby('Segment')['Sales'].sum()
print("Categorical groupby time:", round(time.time() - start, 4), "seconds")


print("Memory usage (Segment as object):")
print(df_obj['Segment'].memory_usage(deep=True))

print("Memory usage (Segment as category):")
print(df_cat['Segment'].memory_usage(deep=True))
