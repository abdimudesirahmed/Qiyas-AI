import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://www.w3schools.com/html/html_tables.asp"

# Get webpage
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find table
table = soup.find("table", id="customers")

# Find all rows
rows = table.find_all("tr")

# Skip header row
for row in rows[1:]:
    cols = row.find_all("td")

    company = cols[0].text.strip()
    contact = cols[1].text.strip()
    country = cols[2].text.strip()

    print("Company:", company)
    print("Contact:", contact)
    print("Country:", country)
    print("-" * 30)