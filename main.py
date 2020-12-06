from bs4 import BeautifulSoup
import requests, csv

URL = 'https://www.learnpython.org'
html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', id= 'inner-text')
list = div.find('ul')
links = list.find_all('a')
f = csv.writer(open("output.csv", "w"))
f.writerow(["Name", "Link"])
for link in links:
    names = link.contents
    fullLink = URL + link.get('href')
    f.writerow([names, fullLink])
