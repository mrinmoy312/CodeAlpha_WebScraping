# CodeAlpha - Task 1: Web Scraping

**Internship Domain**: Data Analytics  
**Intern Name**: Mrinmoy Jana  
**Organization**: CodeAlpha  
**Task**: Web Scraping using Python

---

## Objective

To scrape product data (book titles, prices, and ratings) from a public website and convert it into a structured tabular format (CSV) for further analysis.

This updated version includes web navigation by scraping multiple paginated pages (page 1 to 5) from the website, showcasing the ability to handle both HTML structure and page navigation.

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

---

## Video Explanation

[LinkedIn Video Link Here] *(Replace with your actual LinkedIn post URL once published)*

---

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

