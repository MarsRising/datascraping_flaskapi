import requests
import lxml
from lxml import html
import sqlite3

connection = sqlite3.connect("db.sqlite3")

cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS flaskapi_table(id INTEGER PRIMARY KEY, quotes TEXT, author TEXT)"""
)

connection.commit()


def scrape(link):
    r = requests.get(link)
    response = html.fromstring(r.content)

    containers = response.xpath('//div[contains(@class, "quote")]')

    for container in containers:
        quote = container.xpath('.//span[@class="text"]/text()')
        if quote:
            quote = quote[0].replace("'", "''")
        else:
            quote = ""
        author = container.xpath('.//small[@class="author"]/text()')
        if author:
            author = author[0].replace("'", "''")
        else:
            author = ""
        cursor.execute(
            f"""INSERT INTO flaskapi_table(quotes, author) VALUES('{quote}', '{author}')"""
        )
        connection.commit()
        print(quote, author)


link = "https://quotes.toscrape.com/"
scrape(link)
