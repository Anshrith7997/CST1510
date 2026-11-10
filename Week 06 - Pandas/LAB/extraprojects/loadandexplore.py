import pandas as pd

df = pd.read_csv("DATA/students.csv")

print("First 5 rows:")
print(df.head())

print("Last 3 rows:")
print(df.tail(3))

print("Shape:", df.shape)

print("Columns:", list(df.columns))