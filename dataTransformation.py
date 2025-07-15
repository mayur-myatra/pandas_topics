import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [1, 2, 3], "B":[4, 5, 6]})

print("OG Df")
print(df)


df2 = df.rename(columns={"A": "a", "B": "b"})

print("Renamed DF")
print(df2)

# Output:
# OG Df
#    A  B
# 0  1  4
# 1  2  5
# 2  3  6
# Renamed DF
#    a  b
# 0  1  4
# 1  2  5
# 2  3  6


df3 = df2.rename(index={0: "x", 1: "y", 2: "z"})

print("renamed df index")
print(df3)

# Output:
# renamed df index
#    a  b
# x  1  4
# y  2  5
# z  3  6

data = {
    'prod': ['Laptop', 'Phone', 'Tablet'],
    'amt': [1000, 800, 300],
    'Region Code': ['N', 'S', 'E'],
    'temp_flag': [1, 0, 1]
}
df = pd.DataFrame(data)

df.rename(columns={
    'prod': 'product',
    'amt': 'revenue',
    'Region Code': 'region'
}, inplace=True)

# Clean remaining names
df.rename(columns=lambda x: x.strip().replace(' ', '_').lower(), inplace=True)
print(df.columns)