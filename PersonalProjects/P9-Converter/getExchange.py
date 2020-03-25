from bs4 import BeautifulSoup
import requests

currRates = {}
def getCdB(cdB):
    
    source = requests.get("https://www.bankier.pl/waluty/kursy-walut/forex").text
    soup = BeautifulSoup(source, 'lxml')

    #Extracting currency trade rates from website

    currencydataBase = {}
    table = soup.find('tbody')

    for container in table.find_all('tr'):
        col = 1
        for data in container.find_all('td'):
            n = data.get("class")

            if n == None:
                break

            if col == 3 or col == 5 or col == 6:
                col += 1

            elif col == 1:
                currency = data.text
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
        currencydataBase[currency] = rate

    currencies = ["EUR", "USD", "PLN", "GBP", "CHF", "GBP", "CNH", "HKD", "JPY", "NOK", "HUF"]

    no_match = []
    for i in range(len(currencies)):
        for j in range(len(currencies)):
            if currencies[i] == currencies[j]:
                continue

            new_conv = currencies[i] + "/" + currencies[j]

            a = new_conv[:3]
            b = new_conv[4:]
            rev_conv = b + "/" + a

            if new_conv in cdB:
                continue
            else:
                if new_conv in currencydataBase.keys():
                    cdB[new_conv] = currencydataBase[new_conv]
                elif rev_conv in currencydataBase.keys():
                    cdB[new_conv] = (1/currencydataBase[rev_conv])
                else:
                    no_match.append(new_conv)
                    
    for comb in no_match:
        #convert to different currency
        if comb not in cdB.keys():
            for curr in currencies:
                comb1_curr = comb[:4] + curr
                curr_comb2 = curr + comb[3:]
                if comb[:3] == curr or comb[4:] == curr:
                    continue
                elif comb1_curr not in cdB.keys() or curr_comb2 not in cdB.keys():
                    continue
                else:
                    cdB[comb] = cdB[comb1_curr]*cdB[curr_comb2]
                    break


if __name__ == "__main__":
    getexRates(currRates)


    



