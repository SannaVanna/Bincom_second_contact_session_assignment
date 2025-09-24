import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://quotes.toscrape.com/page/{}/"

# Create CSV file
with open("authors.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Author", "Nationlity" "Date of Birth", "Birth Place", "Description", "Quote"])

    authors_seen = set()
    page = 1

    while len(authors_seen) < 15:  # get about 10-20 authors
        url = BASE_URL.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.select("div.quote")

        if not quotes:
            break  # no more pages

        for q in quotes:
            author_name = q.find("small", class_="author").text
            quote_text = q.find("span", class_="text").text
            author_link = q.find("a")["href"]
            author_url = "https://quotes.toscrape.com" + author_link

            if author_name not in authors_seen:
                authors_seen.add(author_name)

                # Visit author page
                author_res = requests.get(author_url)
                author_soup = BeautifulSoup(author_res.text, "html.parser")

                born_date = author_soup.find("span", class_="author-born-date").text
                born_place = author_soup.find("span", class_="author-born-location").text
                desc = author_soup.find("div", class_="author-description").text.strip()

                writer.writerow([author_name, born_date, born_place, desc, quote_text])

        page += 1

print("✅ Authors and quotes scraped and saved to authors.csv")