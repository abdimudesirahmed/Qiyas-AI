# Abdi MUdesir

import pandas as pd
import numpy as np


Students = pd.DataFrame({
	"student_id":[201,202,203,204,205,206,207,208,209,210],
	"name":["Abel","Sara",None,"John","Marta",None,"David","Helen","Tom",None],
	"Department":["CS","IT","CS",None,"SE","IT","SE",None,"CS","IT"],
	"gpa":[3.5,3.8,np.nan,2.9,3.7,np.nan,3.2,3.4,3.9,np.nan],
	"scholarship":[5000,np.nan,3000,2000,np.nan,4000,3500,np.nan,5000,np.nan]
	})
#Data cleaning
print(Students.isnull().sum())
print(Students.isnull().sum()/len(Students)*100)
Students["name"] = Students["name"].fillna("Unknown")
Students["Department"] = Students["Department"].fillna(Students["Department"].mode()[0])
Students["gpa"] = Students["gpa"].fillna(Students["gpa"].median())
Students["scholarship"] = Students["scholarship"].fillna(0)
print(Students)

#Data Analysis
print(Students["Department"].value_counts())
print((Students["scholarship"] > 0).sum())
print(Students["gpa"].max())
print(Students["gpa"].min())
print(Students["gpa"].mean())
print(Students["scholarship"].sum())
