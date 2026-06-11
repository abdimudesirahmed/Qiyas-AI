
import numpy as np
import pandas as pd

#Integer Array
arr = np.array([10, 20, 30, 40])
print(arr.dtype)

#Float Array
arr = np.array([1.5, 2.5, 3.5])
print(arr.dtype)

#String Array
arr = np.array(["python", "java", "sql"])
print(arr.dtype)

#Explicit int32
arr = np.array([1, 2, 3, 4],
dtype=np.int32)
print(arr.dtype)

#Explicit float32
arr = np.array([1, 2, 3, 4],
dtype=np.float32)
print(arr.dtype)

#Type Conversion
arr = np.array([1, 2, 3, 4])
new_arr = arr.astype(float)
print(new_arr)

#Memory Usage
arr = np.array([1, 2, 3, 4])
print(arr.nbytes)

#Array Shape
arr = np.array([[1, 2, 3 ], [4,5,6]])
print(arr.shape)

#Array Size
arr = np.array([[1, 2, 3 ], [4,5,6]])
print(arr.size)

#Array Addition
a= np.array([1, 2, 3  ])
b=np.array([4,5,6])
print(a+b)

#Array Subtraction
a= np.array([1, 2, 3  ])
b=np.array([4,5,6])
print(a-b)

#Square Root
arr = np.array([4, 9, 16, 25])
print(np.sqrt(arr))

#variance
arr = np.array([4, 9, 16, 25])
print(np.var(arr))

#standard deviation
arr = np.array([4, 9, 16, 25])
print(np.std(arr))

#15: Matrix Addition
c= np.array([[1,2],[3,4]])
d=np.array([[5,6],[7,8]])
print(c+d)

#Matrix Transpose
A = np.array([[1,2,3],[4,5,6]])
print(A.T)

#Matrix Multiplication
e= np.array([[1,2],[3,4]])
f=np.array([[5,6],[7,8]])
print(np.dot(e,f))

#PANDAS DATAFRAME CREATION


#DataFrame from List
course = ["python","java", "sql"]

df = pd.DataFrame(course)
print(df)

#DataFrame from Dictionary
data= {
	"Name":["Meftuha","Abdi","Saron"],
	"Age":[24, 26, 23]
}

df=pd.DataFrame(data)
print(df)

#Student DataFrame
data= {
	"Name":["Meftuha","Abdi","Saron"],
	"Department":["cs","software","Software"],
	"year":[2, 4, 3]
}

df=pd.DataFrame(data)
print(df)

#Employee DataFrame
data= {
	"Employe":["Meftuha","Abdi","Saron"],
	"salary":[1000000, 40000, 300000]
}

df=pd.DataFrame(data)
print(df)

#custom index
Data= {
	"Name":["Meftuha","Abdi","Saron"]
}

df=pd.DataFrame(Data, index=["s1","s2","s3"])
print(df)

###########
data= {
	"Name":["Meftuha","Abdi","Saron"],
	"Department":["cs","software","Software"],
	"year":[2, 4, 3]
}

df=pd.DataFrame(data)
print(df["Name"])
print(df[["Name","Department"]])
df["CGPA"] = [3.5,3.8,3.2]
df.rename(columns={ "Department":"Major"}, inplace=True)
df.drop("CGPA", axis=1, inplace=True)
print(df)
df.index=[101,102,103]
print(df.loc[102])
print(df.loc[[101,103]])
print(df.iloc[0])
print(df.iloc[0:2])
print(df.iloc[0,0])

#Real World data analysis

Data= {
	"Name":["abel","Hana", "Robel"],
	"Maths":[80,90,70]
}
df=pd.DataFrame(Data)
print(df["Maths"].mean())
print(df["Maths"].max())
print(df["Maths"].min())

Data= {
	"Employee":["A","B", "C"],
	"Salary":[8000000,900000,7000000]
}
df=pd.DataFrame(Data)
print(df["Salary"].mean())
print(df["Salary"].max())
print(df["Salary"].min())
print(df[df["Salary"] > 50000])

Dta= {
	"Course":["CS","IT", "SE","DS"],
	"Students":[120,100,90,70]
}
df=pd.DataFrame(Dta)
print(df["Students"].sum())
print(df.loc[df["Students"].idxmax()])

#MINI PROJECT

Data= {
	"Name":["abel","Hana", "Robel","Ruth"],
	"Maths":[80,95,60,85],
	"Physics":[70,88,75,90],
	"Chemistry":[90,91,70,95]
}
df=pd.DataFrame(Data)
df["Total"]=(df["Maths"]+ df["Physics"]+ df["Chemistry"])
df["Average"]=(df["Total"]/3)
print(df)
top_student= df.sort_values(by="Average", ascending=False)
print(top_student)
