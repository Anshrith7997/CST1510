print("Data types:")
print(df.dtypes)

print("Summary statistics:")
print(df.describe())

print("Average grade:", df["Grade"].mean())

print("Maximum attendance:", df["Attendance"].max())

print("Youngest student's age:", df["Age"].min())
