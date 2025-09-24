 Web Scraping Assignments  

This repository contains three different *web scraping assignments* completed using *Python, **Requests, and **BeautifulSoup*.  
Each assignment focuses on scraping different websites and extracting structured data into CSV files.  

---

## Book Scraper Assignment  

### Task  
- Scrape book details from a website.  
- Extract information such as *Title, Price, Availability, Rating, and URL*.  
- Save the data into a *CSV file* for further use.  

### Tools Used  
- Python  
- Requests (to fetch web pages)  
- BeautifulSoup (to parse HTML)  
- CSV module (to store scraped data)  

### Output  
The script generates a file named:
With columns:  
- Title  
- Price  
- Availability  
- Rating  
- Book URL  

---

## Quotes & Authors Scraper Assignment  

### Task  
- Scrape quotes and authors from [Quotes to Scrape](https://quotes.toscrape.com).  
- For each author, extract additional details such as:  
  - *Name*  
  - *Date of Birth*  
  - *Birth Place*  
  - *Nationality* (inferred from birthplace)  
  - *Short Biography/Description*  
  - *Quote*  

### Tools Used  
- Python  
- Requests  
- BeautifulSoup  
- CSV module  

### Output  
The script generates a file named:
With columns:  
- Author  
- Date of Birth  
- Birth Place  
- Nationality  
- Description  
- Quote  

---

## Random Wikipedia Scraper Assignment  

### Task  
- Visit a *random Wikipedia page*.  
- Extract the following details:  
  - *Page Title*  
  - *First Paragraph (Introduction)*  
  - *All Headings (H2, H3, etc.)*  
  - *References or External Links (if available)*  

### Tools Used  
- Python  
- Requests  
- BeautifulSoup  

### Output  
The script generates a file named:
With Columns:
- Title
- Introduction
- Headings 
- Reference / links
