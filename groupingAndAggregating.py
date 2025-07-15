import pandas as pd
import numpy as np


# Sample data
dates = pd.date_range('2023-01-01', periods=6, freq='M')
stocks = ['AAPL', 'GOOGL', 'AAPL', 'GOOGL', 'AAPL', 'GOOGL']
prices = [150, 2800, 155, 2850, np.nan, 2900]


df = pd.DataFrame({
    'Date': dates,
    'Stock': stocks,
    'Price': prices
})

print("OG Data")
print(df)

monthly = (df
    .groupby([df['Date'].dt.to_period('M'), 'Stock'])['Price']
    .mean()
    .unstack()
)

print("Monthly Average")
print(monthly)


# Output:
# OG Data
#         Date  Stock   Price
# 0 2023-01-31   AAPL   150.0
# 1 2023-02-28  GOOGL  2800.0
# 2 2023-03-31   AAPL   155.0
# 3 2023-04-30  GOOGL  2850.0
# 4 2023-05-31   AAPL     NaN
# 5 2023-06-30  GOOGL  2900.0
# Monthly Average
# Stock     AAPL   GOOGL
# Date
# 2023-01  150.0     NaN
# 2023-02    NaN  2800.0
# 2023-03  155.0     NaN
# 2023-04    NaN  2850.0
# 2023-05    NaN     NaN
# 2023-06    NaN  2900.0


# ==================================== For Aggregation =======================================

data = [
    ['Cake','Chocolate',250],
    ['Cake','Vanilla',220],
    ['Bread','WholeWheat',80],
    ['Pastry','Strawberry',120],
    ['Cake','Chocolate',250]
]

df = pd.DataFrame(data, columns=['Item', 'Flavour', 'Price'])
grouped = df.groupby('Item')['Price'].agg(['sum', 'mean', 'count'])


print("grouped with Aggregation")
print(grouped)

# Output:
# grouped with Aggregation
#         sum   mean  count
# Item
# Bread    80   80.0      1
# Cake    720  240.0      3
# Pastry  120  120.0      1


animals = pd.DataFrame({
    'kind': ['cat','dog','cat','dog'],
    'height': [9.1,6.0,9.5,34.0],
    'weight': [7.9,7.5,9.9,198.0]
})

result = animals.groupby('kind').agg(
    min_height=('height','min'),
    max_height=('height','max'),
    avg_weight=('weight', np.mean)
)
print(result)

# Output:
#       min_height  max_height  avg_weight
# kind
# cat          9.1         9.5        8.90
# dog          6.0        34.0      102.75