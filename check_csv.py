
import pandas as pd

df = pd.read_csv(
    "data/Brigade_Bangalore_10_April_26 (1)bc6219c.csv"
)

print("Columns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())