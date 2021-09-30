# A-Price-Tracker-for-Amazon
Using BeautifulSoup, create a price tracker for an item you want to buy over the internet.

# Process
Using the requests module, you can make requests to a server in order to gather data about an item you want to buy over Amazon. After creating your "soup", using the BeautifulSoup class, you can gather the HTML text using a parser. After obtaining the text, you can use the soup object to find data, such as item price, or item link. If the price of the item drops to the price of your target price, an email will be sent to you to notify you. This code could be automated via PythonAnywhere, or another online IDE.
