import pandas as pd
import numpy as np

df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})

print("Original : ")
print(df)

# Output:
# Original : 
#      brand style  rating
# 0  Yum Yum   cup     4.0
# 1  Yum Yum   cup     4.0
# 2  Indomie   cup     3.5
# 3  Indomie  pack    15.0
# 4  Indomie  pack     5.0

print("find duplicated or not")
print(df.duplicated())

# Output:
# find duplicated or not
# 0    False
# 1     True
# 2    False
# 3    False
# 4    False
# dtype: bool

print("Duplicate in brand")
print(df.duplicated(subset=["brand"]))

# Output:
# Duplicate in brand
# 0    False
# 1     True
# 2    False
# 3     True
# 4     True
# dtype: bool

print("it removes duplicate rows based on all columns.")
df = df.drop_duplicates()
print(df)

# Output:
# it removes duplicate rows based on all columns.
#      brand style  rating
# 0  Yum Yum   cup     4.0
# 2  Indomie   cup     3.5
# 3  Indomie  pack    15.0
# 4  Indomie  pack     5.0


print("It removes suplicates based on brand")
print(df.drop_duplicates(subset="brand"))

# Output:
# It removes suplicates based on brand
#      brand style  rating
# 0  Yum Yum   cup     4.0
# 2  Indomie   cup     3.5