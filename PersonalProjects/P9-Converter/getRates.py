from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.bankier.pl/waluty/kursy-walut/forex").text

soup = BeautifulSoup(source, 'lxml')

#Extracting currency trade rates from website

table = soup.find('tbody')

dataBase = {}
for container in table.find_all('tr'):
    col = 1
    for data in container.find_all('td'):
        n = data.get("class")

        if n == None:
            break

        if col == 3 or col == 5 or col == 6:
            col += 1

        elif col == 1:
            currencies = data.text
            col += 1

        elif col == 2:
            buy = data.text
            buy = float(buy.replace(',','.'))
            col += 1

        elif col == 4:
            sell = data.text
            sell = float(sell.replace(',','.'))
            col += 1

    rate = (buy + sell)/2
    dataBase[currencies] = rate

print(dataBase)




