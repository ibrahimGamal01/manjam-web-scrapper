# import requests
# from bs4 import BeautifulSoup
# import mysql.connector

# # Specify the URL of the website to scrape
# url = "https://eg.usembassy.gov/education-culture/exchange-opportunities/allexchanges/"

# # Send a request to the website and retrieve the HTML
# html = requests.get(url).text

# # Parse the HTML using BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')

# # Find the title of the webpage
# title = soup.title.string

# # Find the paragraphs containing the desired words
# paragraphs = []
# for p in soup.find_all("p"):
#   if "internship" in p.text or "event" in p.text or "scholarship" in p.text or "exchange program" in p.text or "scholarships" in p.text:
#     paragraphs.append(p.text)

# # Connect to the database
# cnx = mysql.connector.connect(user='<root>', password='<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>', host='<localhost>', database='<manjam>')
# cursor = cnx.cursor()

# # Insert the title and paragraphs into the table
# query = "INSERT INTO opportunity (title, details) VALUES (%s, %s)"
# values = (title, "\n".join(paragraphs))
# cursor.execute(query, values)


import requests
from bs4 import BeautifulSoup


url = "https://eg.usembassy.gov/education-culture/exchange-opportunities/allexchanges/"

# use sub3lister to get all subdomains from the link " use web security script from my github repo"

# Send a request to the website and retrieve the HTML
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

paragraph = []

# Find the first paragraph containing the desired word
for p in soup.find_all("p"):
    if "internship" in p.text or "event" in p.text or "scholarship" in p.text or "exchange program" in p.text or "scholarships" in p.text:
        paragraph.append(p.text)


print(paragraph[0])
print(paragraph[1])
print(paragraph[2])
