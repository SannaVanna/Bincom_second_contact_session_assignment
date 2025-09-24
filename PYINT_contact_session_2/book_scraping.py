import requests
from bs4 import BeautifulSoup
import csv

# Base URL for pages
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

# create and write into a CSV file to save results
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Book Name", "Price", "Stock", "Rating", "Description", "Product Info", "Category"])

    # Loop through the first 5 pages
    for page in range(1, 6):
        url = BASE_URL.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.select("article.product_pod h3 a")

        for book in books:
            # Visit each book's page
            book_url = "https://books.toscrape.com/catalogue/" + book["href"]
            book_res = requests.get(book_url)
            book_soup = BeautifulSoup(book_res.text, "html.parser")

            # Extract details
            book_name = book_soup.find("h1").text
            price = book_soup.find("p", class_="price_color").text
            stock = book_soup.find("p", class_="instock availability").text.strip()
            rating = book_soup.find("p", class_="star-rating")["class"][1]

            # Description
            desc_tag = book_soup.find("meta", {"name": "description"})
            description = desc_tag["content"].strip() if desc_tag else "No description"

            # Product information
            product_info_table = book_soup.find("table", class_="table")
            product_info = ""
            if product_info_table:
                rows = product_info_table.find_all("tr")
                for row in rows:
                    heading = row.find("th").text
                    value = row.find("td").text
                    product_info += f"{heading}: {value} | "

            # Category (from breadcrumb)
            category = book_soup.select("ul.breadcrumb li a")[-1].text

            # Save into CSV
            writer.writerow([book_name, price, stock, rating, description, product_info, category])

            # Print to screen while scraping
            print(f"{book_name} | {price} | {stock} | {rating} | {category}")

print("Books scraped and saved to books.csv")

