grades_df = df[["Name", "Course", "Grade"]]

print("First 8 rows:")
print(grades_df.head(8))

print("Rows 5 to 9:")
print(df.iloc[5:10])

print("Name and City at index 3:")
print(df.loc[3, ["Name", "City"]])