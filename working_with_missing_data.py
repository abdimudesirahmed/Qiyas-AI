import pandas as pd
import numpy as np


Students = pd.DataFrame({
	"student_id":[101,102,103,104,105,106,107,108,109,110],
	"name":["Abel","Sara",None,"John","Marta",None,"David","Helen","Tom",None],
	"Department":["CS","IT","CS",None,"SE","IT","SE",None,"CS","IT"],
	"gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
	"scholarship":[5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]
	})
Students
print(Students.isnull())
print(Students.isnull().sum())
print((Students.isnull().sum()/len(Students))*100)
print(Students.columns[Students.isnull().any()])
print(Students[Students.isnull().any(axis=1)])
print(Students[Students["gpa"].isnull()])
print(Students[Students["scholarship"].isnull()])
#Students["name"] = Students["name"].fillna("Unknown")
#Students["gpa"] = Students["gpa"].fillna(Students["gpa"].mean())
#Students["gpa"] = Students["gpa"].fillna(Students["gpa"].median())
#Students["Department"] = Students["Department"].fillna(Students["Department"].mode()[0])
#Students["scholarship"] = Students["scholarship"].fillna(0)
#Students.dropna()
#Students.dropna(axis=1)
Students["gpa_missing"] = Students["gpa"].isnull()
print(Students)
print(Students.isnull().sum().idxmax())
print(Students.isnull().sum().idxmin())
print(100- (Students.isnull().sum().sum()/ Students.size)*100)
for col in Students.columns:
	print(col)
	print(col, Students[col].dtype)
