import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
prices = []
ratings = []

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

for page_num in range(1, 6):
    url = base_url.format(page_num)
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Page {page_num} not found. Stopping...")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title_element = book.h3.a
        title = title_element["title"] if title_element and "title" in title_element.attrs else None
        titles.append(title)

        price_element = book.find("p", class_="price_color")
        if price_element:
            price_text = price_element.text.replace('£', '').replace('Â', '')
            try:
                price = float(price_text)
            except ValueError:
                price = None
        else:
            price = None
        prices.append(price)

        rating_element = book.find("p", class_="star-rating")
        if rating_element and rating_element.get("class"):
            rating_class = rating_element.get("class")[1]
            rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            rating = rating_dict.get(rating_class, 0)
        else:
            rating = 0
        ratings.append(rating)

df = pd.DataFrame({
    "Title": titles,
    "Price (£)": prices,
    "Rating": ratings
})

df.to_csv("books_scraped.csv", index=False)
print("✅ CSV file saved successfully!")

from google.colab import files
files.download("books_scraped.csv")
