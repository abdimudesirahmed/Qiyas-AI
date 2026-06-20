import sys
sys.stdout.reconfigure(encoding="utf-8")

import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# -----------------------------
# Website URL
# -----------------------------
BASE_URL = "https://www.waltainfo.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# -----------------------------
# Get Homepage
# -----------------------------
print("Connecting to website...")

response = requests.get(BASE_URL, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

# -----------------------------
# Collect Links
# -----------------------------
article_links = set()

for a in soup.find_all("a", href=True):

    href = a["href"]

    full_url = urljoin(BASE_URL, href)

    if "waltainfo.com" in full_url:
        article_links.add(full_url)

print("Total Links Found:", len(article_links))

# -----------------------------
# Scrape Articles
# -----------------------------
articles = []

for link in article_links:

    try:

        page = requests.get(
            link,
            headers=headers,
            timeout=10
        )

        article_soup = BeautifulSoup(
            page.text,
            "html.parser"
        )

        # -----------------------------
        # Title
        # -----------------------------
        title = ""

        h1 = article_soup.find("h1")

        if h1:
            title = h1.get_text(strip=True)

        # Skip pages without title
        if not title:
            continue

        # Skip unwanted pages
        if (
            title.startswith("Category:")
            or title.startswith("Author:")
            or title in [
                "Archives",
                "Polling",
                "403",
                "AW+ Podcast",
                "Important Link",
                "Vacancy Announcement",
                "Bids Announcement"
            ]
        ):
            continue

        # -----------------------------
        # Date
        # -----------------------------
        date = ""

        time_tag = article_soup.find("time")

        if time_tag:
            date = time_tag.get_text(strip=True)

        # -----------------------------
        # Content
        # -----------------------------
        paragraphs = article_soup.find_all("p")

        content = " ".join(
            p.get_text(" ", strip=True)
            for p in paragraphs
        )

        # Skip very small pages
        if len(content) < 100:
            continue

        articles.append({
            "Title": title,
            "URL": link,
            "Publication_Date": date,
            "Content": content
        })

        print("✓", title[:60])

    except Exception as e:

        print("Error processing page:")
        print(link)
        print(e)

# -----------------------------
# Create DataFrame
# -----------------------------
df = pd.DataFrame(articles)

# Remove duplicates
df.drop_duplicates(
    subset=["Title"],
    inplace=True
)

# -----------------------------
# Save CSV
# -----------------------------
csv_file = "walta_news.csv"

df.to_csv(
    csv_file,
    index=False,
    encoding="utf-8-sig"
)

# -----------------------------
# Results
# -----------------------------
print("\n" + "=" * 50)
print("SCRAPING COMPLETED")
print("=" * 50)

print("Articles Saved:", len(df))
print("CSV File:", csv_file)

print("\nFirst 5 Articles:")
print(df[["Title", "Publication_Date"]].head())