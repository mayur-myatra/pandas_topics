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

# Output:
# Index(['product', 'revenue', 'region', 'temp_flag'], dtype='object')


# ========================= Mapping The Data ====================================

initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'],
        'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'],
        'Age': [42, 52, 36, 21, 23],
        'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']}

df = pd.DataFrame(initial_data, columns=['First_name','Last_name', 'Age', 'City'])

print("OG Data = ")
print(df)

# Create new column using dictionary
new_data = { "Ram":"B.Com",
            "Mohan":"IAS",
            "Tina":"LLB",
            "Jeetu":"B.Tech",
            "Meera":"MBBS" }

# combine this new data with existing DataFrame
df["Qualification"] = df["First_name"].map(new_data)
print("Mapping the data")
print(df)

# Output:
# OG Data =
#   First_name Last_name  Age    City
# 0        Ram     Kumar   42  Mumbai
# 1      Mohan    Sharma   52   Noida
# 2       Tina       Ali   36    Pune
# 3      Jeetu    Gandhi   21   Delhi
# 4      Meera    Kumari   23   Bihar
# Mapping the data
#   First_name Last_name  Age    City Qualification
# 0        Ram     Kumar   42  Mumbai         B.Com
# 1      Mohan    Sharma   52   Noida           IAS
# 2       Tina       Ali   36    Pune           LLB
# 3      Jeetu    Gandhi   21   Delhi        B.Tech
# 4      Meera    Kumari   23   Bihar          MBBS


# ==================================  Applying Functions ===================================

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print("OG Df")
print(df)
# Apply a function to each column

df['A_squared'] = df['A'].apply(lambda x:x ** 2)

print("Squared DF using apply")
print(df)

# Output:
# OG Df
#    A  B
# 0  1  4
# 1  2  5
# 2  3  6
# Squared DF using apply
#    A  B  A_squared
# 0  1  4          1
# 1  2  5          4
# 2  3  6          9

df['sum_row'] = df.apply(lambda row: row['A'] + row['B'], axis=1)

print("Sum of Df row")
print(df)

#  Use of Transform func and group by

df = pd.DataFrame({'Group': ['X', 'Y', 'X'], 'Value': [10, 20, 15]})

print("OG DF")
print(df)

df["Group_mean"] = df.groupby('Group')['Value'].transform('mean')

print("DF with group mean")
print(df)

# Output:
# OG DF
#   Group  Value
# 0     X     10
# 1     Y     20
# 2     X     15
# DF with group mean
#   Group  Value  Group_mean
# 0     X     10        12.5
# 1     Y     20        20.0
# 2     X     15        12.5


# ==================================== String Operations ====================================

data = {'text_column': ['Hello World!','python   pandas', 'DATA Science 123', 'Machine Learning']}
df = pd.DataFrame(data)

print("OG Data")
print(df)

# Convert Lower case
df['lower_case'] = df['text_column'].str.lower()
print("Lower case Column")
print(df[['text_column', 'lower_case']])

# remove leading and trailing whitespace
df['stripped_text'] = df['text_column'].str.strip()
print("Stripped text column:")
print(df[['text_column', 'stripped_text']])

# Check if a string contains "pandas"
df['contains_pandas'] = df['text_column'].str.contains('pandas', case=False)
print("Contain Pandas column (case-insensitive):")
print(df[['text_column', 'contains_pandas']])

# extracted numbers columns
df['numbers'] = df['text_column'].str.extract(r'(\d+)')
print("Extracted Column:")
print(df[['text_column', 'numbers']])

# Split string by space and get the first word
df['first_word'] = df['text_column'].str.split().str[0]
print("First word column:")
print(df[['text_column', 'first_word']])


# Output:
# OG Data
#         text_column
# 0      Hello World!
# 1   python   pandas
# 2  DATA Science 123
# 3  Machine Learning
# Lower case Column
#         text_column        lower_case
# 0      Hello World!      hello world!
# 1   python   pandas   python   pandas
# 2  DATA Science 123  data science 123
# 3  Machine Learning  machine learning
# Stripped text column:
#         text_column     stripped_text
# 0      Hello World!      Hello World!
# 1   python   pandas   python   pandas
# 2  DATA Science 123  DATA Science 123
# 3  Machine Learning  Machine Learning
# Contain Pandas column (case-insensitive):
#         text_column  contains_pandas
# 0      Hello World!            False
# 1   python   pandas             True
# 2  DATA Science 123            False
# 3  Machine Learning            False
# Extracted Column:
#         text_column numbers
# 0      Hello World!     NaN
# 1   python   pandas     NaN
# 2  DATA Science 123     123
# 3  Machine Learning     NaN
# First word column:
#         text_column first_word
# 0      Hello World!      Hello
# 1   python   pandas     python
# 2  DATA Science 123       DATA
# 3  Machine Learning    Machine