from bs4 import BeautifulSoup

import requests

url = "http://www.epc-co.com/epc/Products/eGaNFETsandICs.aspx"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")

for fets in soup.find_all('tr'):
    for row in fets.find_all('td'):

        print row.get_text()
