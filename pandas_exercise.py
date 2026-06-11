import pandas as pd

data ={
	"Name":["Abel", "Sara", "Hana"],
	"Age":[20, 21, 22]
}

df = pd.DataFrame(data)
print(df)

Data ={
	"Department":["CS", "IT", "SE", "DS"]
}

df= pd.DataFrame(Data)
print(df)

Students={
	"Name":["Abel", "Sara","John", "Hana"],
	"Age":[20, 21, 22, 23],
	"CGPA":[3.5, 3.2, 3.6, 3.8]
}

df= pd.DataFrame(Students)
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head(3))
print(df.tail(2))
print(df["Name"])
print(df[["Name","CGPA"]])
print(df.loc[0])
print(df.iloc[2])
print(df.loc[1, "CGPA"])
print(df.iloc[1, 1])
print(df[df["Age"]> 20])
print(df[(df["CGPA"]> 3.5) & (df["Age"]>20)])
print((df["Department"] =="CS"|| "IT"))
