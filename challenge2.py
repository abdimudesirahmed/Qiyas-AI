import numpy as np
import pandas as pd

#  Create a NumPy array of 20 numbers and find the mean
arr = np.array([10, 20, 30, 40, 50,
                60, 70, 80, 90, 100,
                110, 120, 130, 140, 150,
                160, 170, 180, 190, 200])

print(arr.mean())


# Create a 5×5 matrix and find its transpose
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

print(matrix)
print(matrix.T)


#Create a DataFrame of 10 students
data = {
    "Name": [
        "Abdi", "Saron", "Meftuha", "Hana", "Robel",
        "Ruth", "Abel", "Ali", "Sara", "John"
    ],

    "Department": [
        "CS", "SE", "IT", "CS", "SE",
        "IT", "CS", "SE", "IT", "CS"
    ],

    "Year": [1, 2, 3, 4, 2, 1, 3, 4, 2, 1]
}

df = pd.DataFrame(data)
print(df)


# Add a CGPA column
df["CGPA"] = [3.5, 3.8, 3.2, 3.9, 3.1,
              3.7, 3.6, 3.0, 3.4, 3.3]

print(df)


# Find the highest CGPA
print(df["CGPA"].max())


# Find the lowest CGPA
print(df["CGPA"].min())


# Display only student names
print(df["Name"])


# 8. Rename a column
df.rename(columns={"Department": "Major"},
          inplace=True)

print(df)


# 9. Delete a column
df.drop("Year", axis=1,
        inplace=True)

print(df)


# 10. Save the DataFrame to CSV
df.to_csv("students.csv",
          index=False)

print("CSV file saved successfully")