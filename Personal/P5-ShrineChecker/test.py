#Img download tool
from bs4 import BeautifulSoup as bs
import requests
import os

surv_perks = []
killer_perks = []

perks_url = 'https://deadbydaylight.gamepedia.com/Perks'
req_perks = requests.get(perks_url)
soup_perks = bs(req_perks.content, 'lxml')

surv_perks_table_raw, killer_perks_table_raw = soup_perks.find_all('table',{'class':'wikitable sortable'})
surv_perks_table, killer_perks_table = surv_perks_table_raw.find('tbody').find_all('tr'), killer_perks_table_raw.find('tbody').find_all('tr')

# for row in surv_perks_table:
#     cells = row.find_all('th')
#     raw_perk = cells[1].get_text()
#     if raw_perk.startswith('Name'):
#         continue
#     perk = raw_perk[:-1]
#     img_tag = cells[0].find('a')
#     if img_tag is not None:
#         img_urls_tag = img_tag.find('img')['srcset']
#         img_urls = img_urls_tag.split()
#         with open(f'imgs/{perk}.png', 'wb') as f:
#             img = requests.get(img_urls[0])
#             f.write(img.content)
#     surv_perks.append(perk)

# for row in killer_perks_table:
#     cells = row.find_all('th')
#     raw_perk = cells[1].get_text()
#     if raw_perk.startswith('Name'):
#         continue
#     perk = raw_perk[:-1]
#     img_tag = cells[0].find('a')
#     if img_tag is not None:
#         img_urls_tag = img_tag.find('img')['srcset']
#         img_urls = img_urls_tag.split()
#         if ":" in perk:
#             perk = perk.replace(":", "")
#         with open(f'imgs/{perk}.png', 'wb') as f:
#             img = requests.get(img_urls[0])
#             f.write(img.content)
#     killer_perks.append(perk)
path = os.path.abspath()
print(path)
