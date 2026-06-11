import pandas as pd


Employee={
	"Name":["Abdi", "Meftuha", "saron"],
	"Age":[20, 21, 30],
	"salary":[10000, 140000, 4000000],
	"Status": ["Active", "Active", "idol"]
}

df= pd.DataFrame(Employee)
print(df)

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head(2))
print(df.tail(2))
print(df["Name"])
print(df[["Name","salary"]])
print(df.loc[0])
print(df.iloc[2])
print(df.loc[1, "salary"])
print(df.iloc[1, 1])
print(df[df["Age"]> 20])
print(df[(df["Age"]>20) & (df["Status"] == "Active")])
df["Net_salary"] = df["salary"] * 0.15
print(df)


Student={
	"Name": ["a", "b","c","d"],
	"Cgpa": [2.3, 3.2, 4, 3.5]
}

df = pd.DataFrame(Student)
print(df)

print(df.max())
print(df.min())
print(df["Cgpa"].mean())
