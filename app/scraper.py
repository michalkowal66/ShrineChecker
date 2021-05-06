from bs4 import BeautifulSoup as bs
import requests
import lxml

def get_shrine(source=1):
    shrine_urls = {1: "https://deadbydaylight.fandom.com/wiki/Dead_by_Daylight_Wiki",
                   2: "https://deadbydaylight.fandom.com/wiki/Shrine_of_Secrets"}
    shrine = []

    request = requests.get(shrine_urls[source])
    soup = bs(request.content, "lxml")

    shrine_table = soup.find("table", {"class": "wikitable"}).find("tbody").find_all("tr")

    for row in shrine_table:
        cell = row.find("td")
        if cell is not None:
            perk = cell.get_text(strip=True)
            shrine.append(perk)

    return shrine


def get_perks():
    perks = {}
    return perks

if __name__ == "__main__":
    print(get_shrine())
    print(get_perks())