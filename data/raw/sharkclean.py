import pandas as pd

# Load the CSV file
df = pd.read_csv("SharkAttacks.csv")

# Columns to clean
columns_to_fill = ['Location', 'Area', 'Country', 'Activity', 'Name']

# Replace empty strings or NaN with 'unknown' in the selected columns
for col in columns_to_fill:
    df[col] = df[col].fillna("unknown")                     # Replace NaN
    df[col] = df[col].replace(r'^\s*$', 'unknown', regex=True)  # Replace blanks

# (Optional) Save the cleaned data to a new CSV
df.to_csv("shark_attacks_cleaned.csv", index=False)
