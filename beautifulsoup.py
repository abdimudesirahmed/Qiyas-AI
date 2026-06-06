from bs4 import BeautifulSoup
html = """
 <html>
 <body>
    <h1> python web scriping </h1> 
 </body>
 </html>
"""
#intier html
soup = BeautifulSoup(html, "html.parser")
print(soup)
#h1 tag
heading = soup.find("h1")
print(heading)
print(heading.text)

#exercise 2

html = """
 <html>
 <body>
    <p> python</p> 
    <p> java</p> 
    <p> C++</p> 
 </body>
 </html>
"""
#intier html
soup = BeautifulSoup(html, "html.parser")
heading = soup.find("p")
print(heading)
print(heading.text)


#exercise 3

html = """
 <html>
 <body>
    <li> python</li> 
    <li> java</li> 
    <li> C#</li> 
    <li> Go</li> 
 </body>
 </html>
"""
soup = BeautifulSoup(html, "html.parser")
Lis = soup.find_all("li")
for Li in Lis:
	print(Li.text)


	#exercise 4

html = """
 <html>
 <body>
    <a href="https://google.com">Google</a> 
    <a href="https://github.com">Github </a> 
    <a href="https://python.org">Python </a> 
 </body>
 </html>
"""
soup = BeautifulSoup(html, "html.parser")
Links = soup.find_all("a")
for Link in Links:
	print(Link["href"])


		#exercise 5

html = """
 <html>
 <body>
    <div class="product">iphone</div> 
   <div class="product">samsung</div>  
   <div class="product">pixel</div> 
 </body>
 </html>
"""
soup = BeautifulSoup(html, "html.parser")
products = soup.find_all(class_="product")
for product in products:
	print(product.text)


	import requests
from bs4 import BeautifulSoup

query = "python tutorial"

url = f"https://www.google.com/search?q={query}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

for h3 in soup.find_all("h3"):
    print(h3.text)