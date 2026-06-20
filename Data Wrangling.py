import pandas as pd
import numpy as np

#=======================================
#Hospital Patient Registration Cleaning
#=======================================

data = {
'Patient_ID':['P001','P002','P003','P004','P004'],
'Full_Name':['Abebe Kebede',' Hana Tesfaye ','Samuel Bekele',

'Meron Alemu','Meron Alemu'],

'Age':[35,np.nan,42,29,29],
'Address':[
'Bole Road, Addis Ababa, Bole, 03, H125',
'CMC Road, Addis Ababa, Yeka, 10, H201',
'Piassa, Addis Ababa, Arada, 01, H505',
'Megenagna, Addis Ababa, Bole, 05, H901',
'Megenagna, Addis Ababa, Bole, 05, H901'
]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print(df.isnull().sum())
df["age"] =df["Age"].fillna(df["Age"].mean(), inplace=True)
df = df.drop_duplicates()
df["Full_Name"] = df["Full_Name"].str.strip()
df[["First_Name", "Last_Name"]] = df["Full_Name"].str.split(" ", expand=True)
df[["Street", "City", "Subcity", "Woreda", "House_No"]] = df["Address"].str.split(", ", expand=True)
print(df)

#=================================
#Online Store Sales Report
#=================================

data = {
'Month':['Jan','Jan','Feb','Feb','Mar','Mar'],
'Product':['Laptop','Phone','Laptop','Phone','Laptop','Phone'],
'Sales':[15,np.nan,18,20,15,25]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print(df.isnull().sum())
print(df.fillna(0))
total_sales = df["Sales"].sum()
print(f"Total Sales: {total_sales}")

pivat_table = df.pivot_table(
    index='Month',
    columns='Product',
    values='Sales',
)
pivat_table = pivat_table.fillna(0)
print(pivat_table)

#=================================
#Employee Email Processing
#=================================

data = {
'Employee_ID':['E1','E2','E3','E4'],
'Email':[
'abebe@gmail.com',
'hana@yahoo.com',
'samuel@outlook.com',
'meron@gmail.com'
]
}

df = pd.DataFrame(data)
df[["Username","Domain"]] = df["Email"].str.split("@", expand=True)
print(df)