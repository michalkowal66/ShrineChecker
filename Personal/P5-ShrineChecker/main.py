from bs4 import BeautifulSoup as bs
import requests
import csv
from csv import reader
import io
#CREATE A BETTER PATH SYSTEM

class Informator:
    def __init__(self):
        self.surv_perks = []
        self.killer_perks = []
        self.current_shrine = []
        self.desired_perks = []
        self.surv_perks_csv = 'surv_perks.csv'
        self.killer_perks_csv = 'killer_perks.csv'
        self.desired_perks_csv = 'desired_perks.csv'
        self.load_local_data()
        self.dl_shrine()

    def load_local_data(self):
        with open(f'local/{self.surv_perks_csv}', newline='') as f:
            reader = csv.reader(f)
            for line in reader:
                self.surv_perks.append(line[0])    
        
        with open(f'local/{self.killer_perks_csv}', newline='') as f:
            reader = csv.reader(f)
            for line in reader:
                self.killer_perks.append(line[0])    

        with open(f'local/{self.desired_perks_csv}', newline='') as f:
            reader = csv.reader(f)
            for line in reader:
                self.desired_perks.append(line[0])   

    def dl_perks(self):
        perks_url = 'https://deadbydaylight.gamepedia.com/Perks'

        req_perks = requests.get(perks_url)
        soup_perks = bs(req_perks.content, 'lxml')

        surv_perks_table_raw, killer_perks_table_raw = soup_perks.find_all('table',{'class':'wikitable sortable'})
        surv_perks_table, killer_perks_table = surv_perks_table_raw.find('tbody').find_all('tr'), killer_perks_table_raw.find('tbody').find_all('tr')

        for row in surv_perks_table:
            cells = row.find_all('th')
            raw_perk = cells[1].get_text()
            if raw_perk.startswith('Name'):
                continue
            perk = raw_perk[:-1]
            img_tag = cells[0].find('a')
            if img_tag is not None:
                img_urls_tag = img_tag.find('img')['srcset']
                img_urls = img_urls_tag.split()
                with open(f'local/{perk}.png', 'wb') as f:
                    img = requests.get(img_urls[0])
                    f.write(img.content)
            self.surv_perks.append(perk)

        for row in killer_perks_table:
            cells = row.find_all('th')
            raw_perk = cells[1].get_text()
            if raw_perk.startswith('Name'):
                continue
            perk = raw_perk[:-1]
            img_tag = cells[0].find('a')
            if img_tag is not None:
                img_urls_tag = img_tag.find('img')['srcset']
                img_urls = img_urls_tag.split()
                if ':' in perk:
                    perk = perk.replace(':', '')
                with open(f'local/{perk}.png', 'wb') as f:
                    img = requests.get(img_urls[0])
                    f.write(img.content)
            self.killer_perks.append(perk)

        self.update_perks()

    def dl_shrine(self):
        shrine_url = 'https://deadbydaylight.gamepedia.com/Shrine_of_Secrets#Current_Shrine_of_Secrets'

        req_shrine = requests.get(shrine_url)
        soup_shrine = bs(req_shrine.content, 'lxml')    
    
        curr_shrine_table = soup_shrine.find('table',{'class':'wikitable'}).find('tbody').find_all('tr')

        for row in curr_shrine_table:
            cell = row.find('td')
            if cell is not None:
                perk = cell.get_text()
                self.current_shrine.append(perk[:-1])

    def update_perks(self):
        with io.open(f'local/{self.surv_perks_csv}', 'w', encoding='utf-8') as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in self.surv_perks:
                writer.writerow([val])

        with io.open(f'local/{self.killer_perks_csv}', 'w', encoding='utf-8') as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in self.killer_perks:
                writer.writerow([val])

    def add_desired_perk(self): #MAKE SAVING TO FILE UTILITY
        perk = str(input('Provide the name of desired perk: '))
        if perk in self.surv_perks or perk in self.killer_perks:
            self.desired_perks.append(perk)
            print('Perk added to checklist succesfully. You will be notified once it appears on Shrine of Secrets!')
        else:
            print('Dang, We do not seem to have such perk in a database. Check spelling or click update button and try again!')

    def check_shrine(self):
        for perk in self.desired_perks:
            if perk in self.current_shrine:
                print(F'\n{perk} is now available at Shrine of Secrets!')

    def print_shrine(self):
        if len(self.current_shrine) == 0:
            self.dl_shrine()
            print('\nCurrent shrine of secrets:', ', '.join(self.current_shrine))
        else:
            print('\nCurrent shrine of secrets:', ', '.join(self.current_shrine))

    def print_perks(self):
        if len(self.killer_perks) == 0 or len(self.surv_perks) == 0:
            self.dl_perks()
            print('\nSurvivor perks:', ', '.join(self.surv_perks))
            print('\nKiller perks:', ', '.join(self.killer_perks))
        else:
            print('\nSurvivor perks:', ', '.join(self.surv_perks))
            print('\nKiller perks:', ', '.join(self.killer_perks))

app = Informator()
app.print_shrine()
app.check_shrine()