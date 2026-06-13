import pandas as pd

Student={
	"StudentID":[1,2,3,4,5],
	"Name":["Abe", "Kebe", "Chala", "Chaltu", "Murshida"],
	"Department":["CS", "IS", "SE", "IT", "DS"],
	"Age":[23,24,21,30,35],
	"CGPA":[3.5, 2, 1.79,3.89,3]
}

df= pd.DataFrame(Student)
print("Average", df["CGPA"].mean())
print("minimum", df.min(), "max", df.max())
df["percentage"] = df["CGPA"]* 25
print(df)