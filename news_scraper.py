import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "http://www.mynameismosh.com/"

response = requests.get(
	url,
	headers={
	"User-Agent": "Mozilla/5.0"
	}
)

soup = BeautifulSoup(
 response.text, 
 "html.parser"
	)

headers = []
data = []

for article in soup.find_all("h1"):

	title = article.get_text(strip= True)

if title:
	headers.append(
		{
		"title": title
		})
print("collected:", len(headers))


df= pd.DataFrame(headers)

df.to_csv(
	"Ethiopian News csv",
    index=False
	)

print(df.head())

for article in soup.find_all("h1"):

	link = article.find("a")

	

if link:
	title = link.get_text(strip= True)
	href = link.find("href")
	data.append(
		{
		"title": title,
		"link": link
		})



df= pd.DataFrame(headers)

df.to_csv(
	"Ethiopian News csv",
    index=False
	)

print("saved:", len(df))

