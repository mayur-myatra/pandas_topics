import pandas as pd
import numpy as np

left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)


right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)

print("OG Data")

print("Left Data")
print(left)

print("right data")
print(right)

print("Merge using Keys")

res = pd.merge(left, right, on="key")
print(res)

# Output:
# OG Data
# Left Data
#   key   A   B
# 0  K0  A0  B0
# 1  K1  A1  B1
# 2  K2  A2  B2
# 3  K3  A3  B3
# right data
#   key   C   D
# 0  K0  C0  D0
# 1  K1  C1  D1
# 2  K2  C2  D2
# 3  K3  C3  D3
# Merge using Keys
#   key   A   B   C   D
# 0  K0  A0  B0  C0  D0
# 1  K1  A1  B1  C1  D1
# 2  K2  A2  B2  C2  D2
# 3  K3  A3  B3  C3  D3

left = pd.DataFrame(
   {
      "key1": ["K0", "K0", "K1", "K2"],
      "key2": ["K0", "K1", "K0", "K1"],
      "A": ["A0", "A1", "A2", "A3"],
      "B": ["B0", "B1", "B2", "B3"],
   }
)


right = pd.DataFrame(
   {
      "key1": ["K0", "K1", "K1", "K2"],
      "key2": ["K0", "K0", "K0", "K0"],
      "C": ["C0", "C1", "C2", "C3"],
      "D": ["D0", "D1", "D2", "D3"],
   }
)

result = pd.merge(left, right, how='left', on=["key1", "key2"])
print("Merge Left join")
print(result)

# Output:
# Merge Left join
#   key1 key2   A   B    C    D
# 0   K0   K0  A0  B0   C0   D0
# 1   K0   K1  A1  B1  NaN  NaN
# 2   K1   K0  A2  B2   C1   D1
# 3   K1   K0  A2  B2   C2   D2
# 4   K2   K1  A3  B3  NaN  NaN

result = pd.merge(left, right, how='right', on=["key1", "key2"])
print("Merge Right Join")
print(result)

# Output
# Merge Right Join
#   key1 key2    A    B   C   D
# 0   K0   K0   A0   B0  C0  D0
# 1   K1   K0   A2   B2  C1  D1
# 2   K1   K0   A2   B2  C2  D2
# 3   K2   K0  NaN  NaN  C3  D3

result = pd.merge(left, right, how="outer", on=["key1", "key2"])
print("Merge Outer Join")
print(result)

# Output:
# Merge Outer Join
#   key1 key2    A    B    C    D
# 0   K0   K0   A0   B0   C0   D0
# 1   K0   K1   A1   B1  NaN  NaN
# 2   K1   K0   A2   B2   C1   D1
# 3   K1   K0   A2   B2   C2   D2
# 4   K2   K0  NaN  NaN   C3   D3
# 5   K2   K1   A3   B3  NaN  NaN

# ================================= Concate ========================================

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

df4 = pd.DataFrame({
    "B": ["B2", "B3", "B6", "B7"],
    "D": ["D2", "D3", "D6", "D7"],
    "F": ["F2", "F3", "F6", "F7"],
},
    index=[2, 3, 6, 7],
)

print("OG Data")
print("DF1 :")
print(df1)

print("DF4:")
print(df4)

print("Concated Data on particular axis = ")
result = pd.concat([df4, df1], axis=1)
print(result)

# Output:
# OG Data
# DF1 :
#     A   B   C   D
# 0  A0  B0  C0  D0
# 1  A1  B1  C1  D1
# 2  A2  B2  C2  D2
# 3  A3  B3  C3  D3
# DF4:
#     B   D   F
# 2  B2  D2  F2
# 3  B3  D3  F3
# 6  B6  D6  F6
# 7  B7  D7  F7
# Concated Data =
#      B    D    F    A    B    C    D
# 2   B2   D2   F2   A2   B2   C2   D2
# 3   B3   D3   F3   A3   B3   C3   D3
# 6   B6   D6   F6  NaN  NaN  NaN  NaN
# 7   B7   D7   F7  NaN  NaN  NaN  NaN
# 0  NaN  NaN  NaN   A0   B0   C0   D0
# 1  NaN  NaN  NaN   A1   B1   C1   D1

df_north = pd.DataFrame({'Month': ['Jan','Feb'], 'Sales': [100,120]})
df_south = pd.DataFrame({'Month': ['Jan','Feb'], 'Sales': [90,110]})

df_all = pd.concat([df_north, df_south], axis=0, ignore_index=True)
print("Concating vertically")
print(df_all)

# Output:
# Concating vertically
#   Month  Sales
# 0   Jan    100
# 1   Feb    120
# 2   Jan     90
# 3   Feb    110