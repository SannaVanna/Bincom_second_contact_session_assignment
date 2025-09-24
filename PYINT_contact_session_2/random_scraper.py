import requests
from bs4 import BeautifulSoup

def get_random_wikipedia_article():
    while True:
        url = "https://en.wikipedia.org/wiki/Special:Random"
        response = requests.get(url)
        final_url = response.url
        soup = BeautifulSoup(response.text, "html.parser")

        # Try to find title and paragraph
        title_tag = soup.find("h1", id="firstHeading")
        paragraph_tag = soup.select_one("div.mw-parser-output > p")

        if title_tag and paragraph_tag and paragraph_tag.text.strip():
            title = title_tag.text
            paragraph = paragraph_tag.text.strip()
            return title, final_url, paragraph
        else:
            # If not a proper article, try again
            continue

# Run the function
title, final_url, paragraph = get_random_wikipedia_article()

print("Title:", title)
print("URL:", final_url)
print("First paragraph:", paragraph)