import pandas as pd
import numpy as np

#--------------------------------
# section A: python fundamentals
#-------------------------------

personal_info = {
    "name": "Abdi",
    "age": 24,
    "favorite_programming_language": "python"
}
print("Name:", personal_info["name"])
print("Age:", personal_info["age"])
print("My Favorite Programming Language:", personal_info["favorite_programming_language"])

#arithmetic operations
df = pd.DataFrame({
    "Item": ["Pen", "Book", "Pencil", "Eraser", "Ruler"],
    "Price": [10, 50, 5, 3, 7],
    "Quantity": [2, 1, 4, 3, 2]
})


df["Total Cost"] = df["Price"] * df["Quantity"]

print(df)

#  totals
total_cost = df["Total Cost"].sum()
average_price = df["Price"].mean()

print("\nTotal Cost of All Items =", total_cost)
print("Average Price per Item =", average_price)

#user input


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate results
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2


print("Sum =", sum_result)
print("Difference =", difference)
print("Product =", product)

#conditional statements


score = float(input("Enter your score: "))


if score >= 50:
    print("Pass")
else:
    print("Fail")

#multiple conditions

mark = int(input("Enter the student's mark: "))


if mark >= 80 and mark <= 100:
    print("Grade: A")
elif mark >= 70 and mark <= 79:
    print("Grade: B")
elif mark >= 60 and mark <= 69:
    print("Grade: C")
else:
    print("Grade: F")
 
#for loop


for num in range(1, 21):
    if num % 2 == 0:
        print(num)


#while loop


total = 0
num = 1

while num <= 100:
    total += num
    num += 1

print("Sum =", total)

#functions
def rectangle_area(length, width):
    return length * width

area = rectangle_area(5, 3)
print("Area of the rectangle =", area)


# Lambda function to square a number
square = lambda x: x ** 2
for num in range(1, 11):
    print(f"{num} squared = {square(num)}")

# list comprehension
squares = [num ** 2 for num in range(1, 21)]

print(squares)

#-----------------
#section B: NumPy
#-----------------

# NumPy array 
arr = np.arange(1, 21)


print("Array:", arr)

# Display shape, data type, and size
print("Shape:", arr.shape)
print("Data Type:", arr.dtype)
print("Size:", arr.size)

#  array opration
a = np.array([10, 20, 30, 40])
b = np.array([5, 10, 15, 20])

#  operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#Statistics Using NumPy

# Array of exam scores
scores = np.array([78, 85, 92, 67, 88, 74, 95, 81, 69, 90])

# Statistics
print("Mean:", np.mean(scores))
print("Maximum Value:", np.max(scores))
print("Minimum Value:", np.min(scores))
print("Standard Deviation:", np.std(scores))

#----------------------------
#Section C: Pandas DataFrames
#----------------------------


#data frame
student_data = pd.DataFrame({
    "Name": ["Abel", "Sara", "John", "Helen", "Mike"],
    "Age": [20, 22, 19, 21, 23],
    "score": [85, 90, 78, 88, 92]
})

print(student_data.head(3))  

#Rows and columns
students = pd.DataFrame({
    "Name": ["Ali", "Sara", "John", "Muna", "David"],
    "Score": [85, 65, 90, 72, 58]
})
print(students["Name"])
print(students[students["Score"] > 70])


# adding column
students["Status"] = students["Score"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

print(students)


#summary statistic

students_Data = pd.DataFrame({
    "Name": ["Ali", "Sara", "John", "Muna", "David"],
    "Score": [85, 45, 90, 72, 38]
})


summary = students_Data["Score"].describe()

print(summary)

print("\nMean:", summary["mean"])
print("Standard Deviation:", summary["std"])
print("Minimum:", summary["min"])
print("Maximum:", summary["max"])

#------------------------
#Section D: Data Cleaning
#------------------------

# DataFrame with missing values
students = pd.DataFrame({
    "Name": ["Ali", "Sara", np.nan, "Muna", "David"],
    "Score": [85, np.nan, 90, 72, 38],
    "Age": [20, 21, np.nan, 22, np.nan]
})

print("DataFrame:")
print(students)


print("\nMissing values in each column:")
print(students.isnull().sum())


total_missing = students.isnull().sum().sum()
print("\nTotal missing values:", total_missing)


#DataFrame with missing values
students = pd.DataFrame({
    "Name": ["Ali", "Sara", np.nan, "Muna", "David"],
    "Score": [85, np.nan, 90, 72, 38]
})

print("Original DataFrame:")
print(students)

# Replace missing values using Mean
mean_filled = students.copy()
mean_value = mean_filled["Score"].mean()
mean_filled["Score"] = mean_filled["Score"].fillna(mean_value)

# Replace missing values using Median
median_filled = students.copy()
median_value = median_filled["Score"].median()
median_filled["Score"] = median_filled["Score"].fillna(median_value)

print("\nMean Imputation:")
print(mean_filled)

print("\nMedian Imputation:")
print(median_filled)

#dataset with duplicate employee 
employees = pd.DataFrame({
    "EmpID": [101, 102, 103, 101, 104, 103],
    "Name": ["Ali", "Sara", "John", "Ali", "Muna", "John"],
    "Salary": [5000, 6000, 7000, 5000, 5500, 7000]
})

print("Original Employee DataFrame:")
print(employees)


duplicates = employees[employees.duplicated()]
print("\nDuplicate Records:")
print(duplicates)


print("\nNumber of duplicate rows:", employees.duplicated().sum())


cleaned_employees = employees.drop_duplicates()

print("\nDataFrame after removing duplicates:")
print(cleaned_employees)

#city names
cities = ["addis ababa", "ADDIS ABABA", "Addis Ababa", "adDis abaBa"]

df = pd.DataFrame({"City": cities})

print("Original Data:")
print(df)


df["City"] = df["City"].str.lower().str.title()

print("\nStandardized Data:")
print(df)

#ages with errors
ages = [21, 25, 230, 30, 19, -5, 27]

df = pd.DataFrame({"Age": ages})

print("Original Data:")
print(df)


df["Age"] = df["Age"].apply(lambda x: x if 0 <= x <= 100 else np.nan)

print("\nCleaned Data:")
print(df)

#--------------------------------------
#Section E: Integrated Data Wrangling
#--------------------------------------

# Customer dataset 
customers = pd.DataFrame({
    "CustID": [1, 2, 3, 3, 4, 5, 5],
    "Name": ["Ali", "Sara", "john", "John", "MUNA", "muna", "David"],
    "City": ["addis ababa", "ADDIS ABABA", np.nan, "Addis Ababa", "adDis abaBa", "Hawassa", "HAWASSA"],
    "Age": [21, 25, 230, 30, np.nan, 27, 27]
})

print("Original Dataset:")
print(customers)


customers = customers.drop_duplicates()


customers["Name"] = customers["Name"].str.title()
customers["City"] = customers["City"].str.lower().str.title()


customers["Age"] = customers["Age"].fillna(customers["Age"].mean())


customers["Age"] = customers["Age"].apply(lambda x: x if 0 <= x <= 100 else np.nan)


customers["Age"] = customers["Age"].fillna(customers["Age"].median())

print("\nCleaned Dataset:")
print(customers)


#outlier Detection


# Sales dataset
sales = pd.DataFrame({
    "Sales": [120, 150, 130, 170, 200, 210, 190, 300, 1000, 160, 180, 140]
})

print("Original Sales Data:")
print(sales)


Q1 = sales["Sales"].quantile(0.25)
Q3 = sales["Sales"].quantile(0.75)


IQR = Q3 - Q1


lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR


outliers = sales[(sales["Sales"] < lower_bound) | (sales["Sales"] > upper_bound)]

print("\nQ1 =", Q1)
print("Q3 =", Q3)
print("IQR =", IQR)
print("Lower Bound =", lower_bound)
print("Upper Bound =", upper_bound)

print("\nOutliers:")
print(outliers)



# Outlier Handling and Complete Data Cleaning Pipeline

df = pd.DataFrame({
    "EmpID": [101, 102, 103, 103, 104, 105, 105, 106],
    "Name": ["ali", "SARA", "john", "John", "mUna", "David", "david", "Sara"],
    "City": ["addis ababa", "ADDIS ABABA", np.nan, "Addis Ababa", "hawassa", "Hawassa", "HAWASSA", "Bahir dar"],
    "Salary": [5000, 6000, 7000, 7000, np.nan, 12000, 50000, 3000]
})

print("Original Dataset:\n")
print(df)


# 1. Detect missing values

print("\nMissing values per column:\n")
print(df.isnull().sum())

# 2. Fill missing values

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["City"] = df["City"].fillna("Unknown")


# 3. Remove duplicate rows

df = df.drop_duplicates()


# 4. Standardize text values

df["Name"] = df["Name"].str.title()
df["City"] = df["City"].str.lower().str.title()


# 5. Detect outliers using IQR

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\nIQR Summary:")
print("Q1:", Q1)
print("Q3:", Q3)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)


# 6. Remove or cap outliers 

df["Salary"] = np.where(df["Salary"] < lower_bound, lower_bound,
                        np.where(df["Salary"] > upper_bound, upper_bound, df["Salary"]))


# 7. Final cleaned dataset


print("\nFinal Cleaned Dataset:\n")
print(df)