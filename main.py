""" Web Scraping project to gather info about the price of an amazon rice cooker"""

import requests
from bs4 import BeautifulSoup
import smtplib

from_email = YOUR_EMAIL
from_email_password = YOUR_PASSWORD


rice_cooker_url = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=dp_fod_1?pd_rd_i=B08PQ2KWHS&psc=1"

# the required headers to web scrape from amazon, gathering the html data. if you want to web scrape and gather
# the html info for a website, use this header
headers = {
    "Accept-Language": "en-us",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
}
response = requests.get(url=rice_cooker_url, headers=headers)
html_rice_cooker = response.text
soup = BeautifulSoup(html_rice_cooker, 'html.parser')
price_item = soup.find(name="span", class_="a-size-base a-color-price header-price a-text-normal", id="newBuyBoxPrice").string
price = float(price_item.split("$")[1])
link_tag = soup.find(name="link", rel="canonical")
link = link_tag.get("href")
title_tag = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break")
title = title_tag.get_text()
final_title = title.split("\n\n\n\n\n\n\n\n")[1].split('\n\n\n\n\n\n')[0]

target_price = 200.0
if price < target_price:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_email_password)
        message = f"Subject: We got a deal!\n\n {final_title}. Buy now for ${price}.\n{link}"
        encoded_message = message.encode('utf-8')
        connection.sendmail(from_addr=from_email, to_addrs=from_email, msg=encoded_message)