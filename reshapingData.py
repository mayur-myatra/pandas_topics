import pandas as pd
import numpy as np


# Sample data
data = {
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 81],
    'English': [89, 76, 85]
}

df = pd.DataFrame(data)

print("OG Data for melt")
print(df)

# ===================================== Melt() ==================================

df_melted = pd.melt(df, id_vars=['Student'], var_name='Subject', value_name='Grade')

print("Melted DF")
print(df_melted)

# Output:
# OG Data for melt
#    Student  Math  Science  English
# 0    Alice    85       92       89
# 1      Bob    90       88       76
# 2  Charlie    78       81       85
# Melted DF
#    Student  Subject  Grade
# 0    Alice     Math     85
# 1      Bob     Math     90
# 2  Charlie     Math     78
# 3    Alice  Science     92
# 4      Bob  Science     88
# 5  Charlie  Science     81
# 6    Alice  English     89
# 7      Bob  English     76
# 8  Charlie  English     85

# ===================================== Stack() ==================================

df_indexed = df.set_index('Student')
stacked = df_indexed.stack()
print("Stacked Data")
print(stacked)

# Output:
# Stacked Data
# Student
# Alice    Math       85
#          Science    92
#          English    89
# Bob      Math       90
#          Science    88
#          English    76
# Charlie  Math       78
#          Science    81
#          English    85
# dtype: int64

# ===================================== unstack() ==================================

unstacked = stacked.unstack()
print("Unstacked Data")
print(unstacked)

# Output:
# Unstacked Data
#          Math  Science  English
# Student
# Alice      85       92       89
# Bob        90       88       76
# Charlie    78       81       85



# ================================= with realistic data ==================================

# Create a sample sales DataFrame
data = {
    'Employee': ['John', 'Sara', 'Tim'],
    'Jan_Sales': [1200, 1500, 1600],
    'Feb_Sales': [1100, 1450, 1700],
    'Mar_Sales': [1300, 1600, 1800]
}

df = pd.DataFrame(data)
print("Original data")
print(df)

# ===================================== Melt() ==================================

df_melted = pd.melt(df, id_vars=['Employee'], var_name='Month', value_name='Sales')
print('Melted Data')
print(df_melted)

# ===================================== Stack() ==================================
df_indexed = df.set_index('Employee')
stacked = df_indexed.stack()
print("Stacked data")
print(stacked)

# ===================================== unstack() ==================================
unstack = stacked.unstack()
print("Unstacked data")
print(unstack)