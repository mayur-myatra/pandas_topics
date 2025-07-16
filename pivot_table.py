import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Region': ['East', 'West', 'East', 'West', 'East', 'West'],
    'Product': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Sales': [100, 150, 120, 90, 110, 80]
}

df = pd.DataFrame(data)

print("OG Data")
print(df)


# create pivot table
pivot_df = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc='sum')

print("Pivot Table = ")
print(pivot_df)

# Output:
# OG Data
#   Region Product  Sales
# 0   East       A    100
# 1   West       B    150
# 2   East       A    120
# 3   West       C     90
# 4   East       B    110
# 5   West       A     80
# Pivot Table =
# Product      A      B     C
# Region
# East     220.0  110.0   NaN
# West      80.0  150.0  90.0

# ===================================== Pivot Table with realistic data ==========================================

dates = pd.to_datetime(pd.date_range(start='2024-01-01', periods=30, freq='D').to_list() * 3)
companies = ['Company A'] * 30 + ['Company B'] * 30 + ['Company C'] * 30
prices = np.random.rand(90) * 100 + 50

data = {
    'Date' : dates,
    'Company': companies,
    'Price': prices
}

df = pd.DataFrame(data)

print("OG with realistic data")
print(df)
# Create pivot table

pivot_df = pd.pivot_table(df, values='Price', index='Date', columns='Company', aggfunc='sum')

print("Pivot Table with realistic data")
print(pivot_df.head())

# Output:
# OG with realistic data
#          Date    Company       Price
# 0  2024-01-01  Company A   98.036496
# 1  2024-01-02  Company A  118.017049
# 2  2024-01-03  Company A  124.503382
# 3  2024-01-04  Company A   86.400863
# 4  2024-01-05  Company A  103.156615
# ..        ...        ...         ...
# 85 2024-01-26  Company C   95.560624
# 86 2024-01-27  Company C  101.854123
# 87 2024-01-28  Company C   80.961764
# 88 2024-01-29  Company C  103.142525
# 89 2024-01-30  Company C   91.232346

# [90 rows x 3 columns]
# Pivot Table with realistic data
# Company      Company A   Company B   Company C
# Date
# 2024-01-01   98.036496   69.694446   74.464756
# 2024-01-02  118.017049  131.185543  108.717259
# 2024-01-03  124.503382  119.346517   82.211667
# 2024-01-04   86.400863   96.470947   92.555943
# 2024-01-05  103.156615   75.294587  119.308465