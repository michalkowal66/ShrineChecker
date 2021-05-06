from bs4 import BeautifulSoup as bs
import requests
import lxml

def get_shrine(source=1):
    shrine_urls = {
        1: "https://deadbydaylight.fandom.com/wiki/Dead_by_Daylight_Wiki",
        2: "https://deadbydaylight.fandom.com/wiki/Shrine_of_Secrets"
    }
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
    perks_url = "https://deadbydaylight.gamepedia.com/Perks"
    perks = []

    request = requests.get(perks_url)
    soup = bs(request.content, "lxml")

    tables =  soup.find_all("table", {"class": "wikitable sortable"})
    survivor_table, killer_table = [table.find("tbody").find_all("tr") for table in tables]
    for table in [survivor_table, killer_table]:
        for row in table[1:]:
            if row.contents[7].get_text(strip=True) == "All":
                continue
            perk_img_url = row.contents[1].find("a").find("img")["src"]
            perk_name = row.contents[3].find("a").get_text(strip=True)

            perks.append((perk_name, perk_img_url))

    return perks

if __name__ == "__main__":
    print(get_shrine())
    print(get_perks())