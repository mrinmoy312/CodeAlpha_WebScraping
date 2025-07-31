# CodeAlpha - Task 1: Web Scraping

Internship Domain: Data Analytics  
Intern Name: Mrinmoy Jana  
Organization: CodeAlpha  
Task: Web Scraping using Python

---

## Objective

To scrape product data (book titles, prices, and ratings) from a public website and convert it into structured tabular format (CSV) for further analysis.

---

## Website Scraped

- URL: http://books.toscrape.com  
- Purpose: Practice site for web scraping projects

---

## Tools & Libraries Used

- Python 3
- requests
- BeautifulSoup (from bs4)
- pandas

---

## Extracted Features

Each row in the dataset contains:
- Book Title
- Price (in £)
- Rating (1 to 5, converted from class name)

---

## Sample Output (CSV Preview)

| Title                | Price (£) | Rating |
|----------------------|-----------|--------|
| A Light in the Attic | 51.77     | 3      |
| Tipping the Velvet   | 53.74     | 1      |
| Soumission           | 50.10     | 1      |

The data is saved in a file named `books_scraped.csv`.

---

