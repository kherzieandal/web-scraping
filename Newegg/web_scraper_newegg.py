from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import csv

filename = 'products.csv'
f = open(filename, 'w', newline='')

header = ['brand', 'product_name', 'price']

writer = csv.writer(f)
writer.writerow(header)
num = 0
my_urls = ['https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709']
for i in range(2, 101):
    my_urls.append(f'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-{i}?Tid=7709')
for my_url in my_urls:

    num += 1
    print(num)

    client = urlopen(my_url)  # opens the web page
    page_html = client.read()  # reads the page
    client.close()  # closes client

    page_soup = soup(page_html, 'html.parser')
    containers = page_soup.findAll("div", {"class": "item-cell"})

    for container in containers:
        if container.find('div', {"class": "item-branding"}).a == None or container.find('div', {"class": "item-branding"}).a.img == None:
            brand = ''
        else:
            brand = container.find('div', {"class": "item-branding"}).a.img['title']
        if False:
            product_name = ''
        else:
            product_name = container.find("a", {"class": "item-title"}).text
        if container.find("li", {"class": "price-current"}).strong == None or container.find("li", {"class": "price-current"}).sup == None:
            price = ''
        else:
            price = container.find("li", {"class": "price-current"}).strong.text + container.find("li", {"class": "price-current"}).sup.text
        writer.writerow([brand, product_name, price])
f.close()