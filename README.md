# CodeAlpha - Task 1: Web Scraping

**Internship Domain**: Data Analytics  
**Intern Name**: Mrinmoy Jana  
**Organization**: CodeAlpha  
**Task**: Web Scraping using Python

---


## Objective

The objective of this task is to extract relevant product data from a public website using Python-based web scraping techniques. The project demonstrates the ability to navigate through multiple web pages (pagination), handle HTML structure effectively, and collect structured data (custom dataset) suitable for analysis. This task is completed using libraries such as BeautifulSoup, requests, and pandas.

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

The script iterates through multiple pages of book listings to collect a larger dataset.

---

## Sample Output (CSV Preview)

| Title                | Price (£) | Rating |
|----------------------|-----------|--------|
| A Light in the Attic | 51.77     | 3      |
| Tipping the Velvet   | 53.74     | 1      |
| Soumission           | 50.10     | 1      |

The data is saved in a file named `books_scraped.csv`.

---

## How to Run

1. Open the notebook in Google Colab or any Python environment.
2. Install dependencies if required:
3. Run the script. The CSV file will be generated.
4. If using Colab, the file will be automatically downloaded to your device.


## Repository Contents

- `books_scraper.py` – Python script for scraping
- `books_scraped.csv` – Output dataset with multiple pages
- `README.md` – Project documentation

---

## Acknowledgment

Thanks to CodeAlpha for the opportunity to apply and grow my Python and data analytics skills through this hands-on task.

---

## Tags

**Tags:**  
`#WebScraping` `#Python` `#BeautifulSoup` `#DataAnalytics` `#Internship` `#CodeAlpha`

