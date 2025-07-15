import pandas as pd
import numpy as np

s = pd.Series([1, 2], dtype=np.int64).reindex([0, 1, 2])
print(s)

# Output:
# 0    1.0
# 1    2.0
# 2    NaN
# dtype: float64

s = pd.Series([1, 2], dtype=np.dtype("timedelta64[ns]")).reindex(([0, 1, 2]))
print("With Timestamp neno seconds null is saying NaT")
print(s)

s = pd.Series([1, 2], dtype=np.dtype("datetime64[ns]")).reindex([0, 1, 2])
print("With Date and time null is saying NaT")
print(s)

s = pd.Series(["2020", "2020"], dtype=pd.PeriodDtype("D")).reindex([0, 1, 2])
print("With Date null is saying NaT")
print(s)

# Output:
# With Timestamp neno seconds null is saying NaT
# 0   0 days 00:00:00.000000001
# 1   0 days 00:00:00.000000002
# 2                         NaT
# dtype: timedelta64[ns]
# With Date and time null is saying NaT
# 0   1970-01-01 00:00:00.000000001
# 1   1970-01-01 00:00:00.000000002
# 2                             NaT
# dtype: datetime64[ns]
# With Date null is saying NaT
# 0    2020-01-01
# 1    2020-01-01
# 2           NaT
# dtype: period[D]

df = pd.DataFrame({
    'Name': ["Max", "Mek", None],
    "Age": [25, np.nan, 30]
})

print("Original DF:")
print(df)

print("check is Null")
print(df.isnull())

print("check is Not Null")
print(df.notnull())


# Output:
# Original DF:
#    Name   Age
# 0   Max  25.0
# 1   Mek   NaN
# 2  None  30.0
# check is Null
#     Name    Age
# 0  False  False
# 1  False   True
# 2   True  False
# check is Not Null
#     Name    Age
# 0   True   True
# 1   True  False
# 2  False   True

print("Fill NA with -")
print(df.fillna("-"))

print("Droping NA Rows")
print(df.dropna())

# Output:
# Fill NA with -
#   Name   Age
# 0  Max  25.0
# 1  Mek     -
# 2    -  30.0
# Droping NA
#   Name   Age
# 0  Max  25.0


df = pd.DataFrame(
    {
        "A": [1, 2.1, np.nan, 4.7, 5.6, 6.8],
        "B": [0.25, np.nan, np.nan, 4, 12.2, 14.4],
    }
)

print(df)

# Output:
#      A      B
# 0  1.0   0.25
# 1  2.1    NaN
# 2  NaN    NaN
# 3  4.7   4.00
# 4  5.6  12.20
# 5  6.8  14.40

print("Basic Interpolation")
print(df.interpolate())

# Output:
# Basic Interpolation
#      A      B
# 0  1.0   0.25
# 1  2.1   1.50
# 2  3.4   2.75
# 3  4.7   4.00
# 4  5.6  12.20
# 5  6.8  14.40


print("Linear interpolation")
s = pd.Series([0, 1, np.nan, 3])
print(s.interpolate())

# Output:
# Linear interpolation
# 0    0.0
# 1    1.0
# 2    2.0
# 3    3.0
# dtype: float64

#  Sample weekly data with missing values
dates = pd.date_range('2022-01-02', periods=10, freq="W-Sun")
values = [1.5, np.nan, 2.1, np.nan, 6.3, np.nan, 4.6, 5.1, np.nan, 8.9]
ser = pd.Series(values, index=dates)

print("Before Interpolation")
print(ser)

# Fill gaps using time aware inerpolation
ser_interpol = ser.interpolate(method='time')

print("/Befor Interpolate")
print(ser_interpol)

# Output:
# Before Interpolation
# 2022-01-02    1.5
# 2022-01-09    NaN
# 2022-01-16    2.1
# 2022-01-23    NaN
# 2022-01-30    6.3
# 2022-02-06    NaN
# 2022-02-13    4.6
# 2022-02-20    5.1
# 2022-02-27    NaN
# 2022-03-06    8.9
# Freq: W-SUN, dtype: float64
# /Befor Interpolate
# 2022-01-02    1.50
# 2022-01-09    1.80
# 2022-01-16    2.10
# 2022-01-23    4.20
# 2022-01-30    6.30
# 2022-02-06    5.45
# 2022-02-13    4.60
# 2022-02-20    5.10
# 2022-02-27    7.00
# 2022-03-06    8.90
# Freq: W-SUN, dtype: float64

# =============================Polynomal
date_range = pd.date_range('2025-01-01', periods=10, freq='D')
values = [1, np.nan, 4, 4, 5, 6, np.nan, 8, np.nan, 10]
df = pd.DataFrame({'Date': date_range, 'Value': values})
df['Value_poly'] = df['Value'].interpolate(method='polynomial', order=2)

print("Using Polynomal")
print(df)

# Output:
# Using Polynomal
#         Date  Value  Value_poly
# 0 2025-01-01    1.0    1.000000
# 1 2025-01-02    NaN    3.117455
# 2 2025-01-03    4.0    4.000000
# 3 2025-01-04    4.0    4.000000
# 4 2025-01-05    5.0    5.000000
# 5 2025-01-06    6.0    6.000000
# 6 2025-01-07    NaN    6.993382
# 7 2025-01-08    8.0    8.000000
# 8 2025-01-09    NaN    9.002206
# 9 2025-01-10   10.0   10.000000



# Create monthly dates
dates = pd.date_range(start='2024-01-01', periods=12, freq='M')

# Simulate sales data with gaps
sales = [100, 120, np.nan, 150, 170, np.nan, np.nan, 200, 220, np.nan, 260, 280]
df = pd.DataFrame({'Sales': sales}, index=dates)

print("Original data:\n", df)

# df["Sales_poly"] = df["Sales"].interpolate(method='polynomial' order=2)

df['Sales_spline'] = df['Sales'].interpolate(method='spline', order=2)

print(df)