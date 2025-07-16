import pandas as pd

# Sample sales data
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Region': ['West', 'East', 'North', 'West'],
    'Sales': [2500, 4000, 3200, 4000]
}

df = pd.DataFrame(data)
print("OG DF")
print(df)

# Output:
# OG DF
#   Employee Region  Sales
# 0    Alice   West   2500
# 1      Bob   East   4000
# 2  Charlie  North   3200
# 3    Diana   West   4000

# ========================================== Sort array =================================================
df_sorted = df.sort_values(by="Sales", ascending=False)
print("Sorted DF to dedcending Order")
print(df_sorted)

# Output:
# Sorted DF to dedcending Order
#   Employee Region  Sales
# 1      Bob   East   4000
# 3    Diana   West   4000
# 2  Charlie  North   3200
# 0    Alice   West   2500


df_sorted2 = df.sort_index()
print(df_sorted2)


# ========================================== Rank array ==========================================

df['Sales_Rank'] = df['Sales'].rank(method='min', ascending=False)
print("Ranked Array descending order")
print(df)
