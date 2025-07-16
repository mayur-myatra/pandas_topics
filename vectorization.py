import pandas as pd
import numpy as np
import time

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

# df_cat = df_obj.copy()
# df_cat['Segment'] = df_cat['Segment'].astype('category')

# # Group By Segment
# start = time.time()
# df_obj.groupby('Segment')['Sales'].sum()
# print("Object GroupBy Time: ", round(time.time() - start, 4), "seconds")

# # Group by Segment (categorical type)
# start = time.time()
# df_cat.groupby('Segment')['Sales'].sum()
# print("Categorical groupby time:", round(time.time() - start, 4), "seconds")


# ========================================= Loop Based Approach =========================================
start = time.time()
df_obj['WithTax_Loop'] = [sale * 1.10 for sale in df_obj['Sales']]
print("Loop time:", round(time.time() - start, 4), "seconds")


# ============================================= Vectorised Approach =======================================
start = time.time()
df_obj['WithTax_Vectorized'] = df_obj['Sales'] * 1.10
print("Vectorized time:", round(time.time() - start, 4), "seconds")
print(df_obj)


# Output:
# OG Data
#         CustomerID  Segment  Sales
# 0                0  Regular    365
# 1                1  Premium    378
# 2                2  Regular    317
# 3                3  Premium    176
# 4                4  Premium    813
# ...            ...      ...    ...
# 999995      999995      VIP    529
# 999996      999996  Regular    303
# 999997      999997      VIP    154
# 999998      999998  Premium    758
# 999999      999999  Regular    803

# [1000000 rows x 3 columns]
# Loop time: 0.1547 seconds
# Vectorized time: 0.0035 seconds
#         CustomerID  Segment  Sales  WithTax_Loop  WithTax_Vectorized
# 0                0  Regular    365         401.5               401.5
# 1                1  Premium    378         415.8               415.8
# 2                2  Regular    317         348.7               348.7
# 3                3  Premium    176         193.6               193.6
# 4                4  Premium    813         894.3               894.3
# ...            ...      ...    ...           ...                 ...
# 999995      999995      VIP    529         581.9               581.9
# 999996      999996  Regular    303         333.3               333.3
# 999997      999997      VIP    154         169.4               169.4
# 999998      999998  Premium    758         833.8               833.8
# 999999      999999  Regular    803         883.3               883.3

# [1000000 rows x 5 columns]