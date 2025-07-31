
# Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define URL
url = "http://books.toscrape.com/"
response = requests.get(url)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

# Step 3: Initialize empty lists
titles = []
prices = []
ratings = []

# Step 4: Extract data
for book in books:
    # Title
    title_element = book.h3.a
    title = title_element["title"] if title_element and "title" in title_element.attrs else None
    titles.append(title)

    # Price
    price_element = book.find("p", class_="price_color")
    if price_element:
        price_text = price_element.text.replace('£', '').replace('Â', '')
        try:
            price = float(price_text)
        except ValueError:
            price = None # Handle cases where price is not a valid number
    else:
        price = None
    prices.append(price)

    # Rating (converted from class name)
    rating_element = book.find("p", class_="star-rating")
    if rating_element and rating_element.get("class"):
        rating_class = rating_element.get("class")[1]
        rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating = rating_dict.get(rating_class, 0)
    else:
        rating = 0 # Default to 0 or None if rating is missing
    ratings.append(rating)

# Step 5: Create DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price (£)": prices,
    "Rating": ratings
})

# Step 6: Save CSV
df.to_csv("books_scraped.csv", index=False)
print(" CSV file saved successfully!")

# Step 7: Enable download in Colab
from google.colab import files
files.download("books_scraped.csv")
