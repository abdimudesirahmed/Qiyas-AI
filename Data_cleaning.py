import pandas as pd
Students = {
	"student_id":[101,102,103,104,105,101],
	"name":["Abel","Sara","John","Sara","Helen","Abel"],
	"Score":[80,90,75,90,88,80],
	}
df = pd.DataFrame(Students)
print(df.duplicated())
print("Duplicate counts:", df.duplicated().sum())
df_clean = df.drop_duplicates()
df_last = df.drop_duplicates(keep='last')
print(df_clean)
print(df_last)

#duplicate email
df = pd.DataFrame({
    "id":[1,2,3,4],
    "email":["a@gmail.com",
             "b@gmail.com",
             "a@gmail.com",
             "c@gmail.com"
             ]
    })
duplicates = df[df.duplicated(subset=["email"])]
print(duplicates)
clean_df = df.drop_duplicates(subset=["email"])
print(clean_df)


#City Name

df = pd.DataFrame({
    "city":[
       "addis ababa",
       "ADDIS ABABA",
       "Addis Ababa",
       "adDis abAba"
    ]
    })
df["upper"]=df["city"].str.upper()
df["lower"]=df["city"].str.lower()
df["title"]=df["city"].str.title()
print(df)

#Remove extra space

df = pd.DataFrame({
    "name":[
       " Abel",
       "Sara ",
       " John ",
       " Helen"
    ]
    })
df["name"] = df["name"].str.strip()
print(df)

#standardise  Date

df = pd.DataFrame({
    "date":[
       "2026-01-05",
       "05/02/2026",
       "March 10, 2026",
       "2026.04.15"
    ]
    })
df["date"] = pd.to_datetime(df["date"], format="mixed")
df["formatted"] = df["date"].dt.strftime("%Y-%m-%d")
df["year"]  = df["date"].dt.year
df["month"] = df["date"].dt.month
print(df)

#kilograms to pound

df = pd.DataFrame({
    "weight_kg":[55,70,85,100]
    })
df["weight_lb"]=(df["weight_kg"]*2.20462).round(2)
print(df)

#celsius to fahrenheit

df = pd.DataFrame({
    "tem_c":[0,25,37,100]
    })
df["tem_f"]=(df["tem_c"]*9/5)+32
print(df)



df = pd.DataFrame({
    "salary":[3500,4000,4200,3900,4100,45000]
    })

q1= df["salary"].quantile(0.25)
q3= df["salary"].quantile(0.75)
IQR=q3 -q1
lower= q1-1.5*IQR
upper=q3+1.5*IQR

outlier= df[
     (df["salary"]<lower)|
     (df["salary"]>upper)
]  
print(outlier)   
clean_df = df[
      (df["salary"]>=lower)&
      (df["salary"]<=upper)
]
print(clean_df)