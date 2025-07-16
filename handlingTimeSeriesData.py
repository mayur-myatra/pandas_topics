import pandas as pd

# Sample realistic data
data = {
    'Date': ['2025.01.01', '2025.01.02', '2025.01.03', '2025.01.04',
             '2025.01.10', '2025.01.15', '2025.02.01', '2025.02.05'],
    'Sales': [200, 250, 180, 300, 400, 350, 500, 450]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Output:
# Original Data:
#          Date  Sales
# 0  2025.01.01    200
# 1  2025.01.02    250
# 2  2025.01.03    180
# 3  2025.01.04    300
# 4  2025.01.10    400
# 5  2025.01.15    350
# 6  2025.02.01    500
# 7  2025.02.05    450

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as index for time series operations
df.set_index('Date', inplace=True)

print("Datetime-indexed DataFrame:")
print(df)

# Output:
# Datetime-indexed DataFrame:
#             Sales
# Date
# 2025-01-01    200
# 2025-01-02    250
# 2025-01-03    180
# 2025-01-04    300
# 2025-01-10    400
# 2025-01-15    350
# 2025-02-01    500
# 2025-02-05    450


monthly_sales = df.resample('ME').sum()
print("Monthly sales Total")
print(monthly_sales)