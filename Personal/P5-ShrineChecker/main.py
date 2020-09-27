from bs4 import BeautifulSoup as bs
import requests
import csv
from csv import reader
import io
import os
from datetime import datetime

class Informator:
    def __init__(self):
        self.surv_perks = []
        self.killer_perks = []
        self.current_shrine = []
        self.desired_perks = []
        self.surv_perks_csv = 'surv_perks.csv'
        self.killer_perks_csv = 'killer_perks.csv'
        self.perks_csv = 'perks.csv'
        self.shrine_csv = 'shrine.csv'
        self.desired_perks_csv = 'desired_perks.csv'
        self.local_dir = os.path.expanduser('~') + '\Documents\ShrineChecker'
        self.local_data = self.local_dir + '\local'

    def load_local_data(self):
        if not os.path.exists(self.local_dir):
            print("Seems like there is no local data to load, making new directory and downloading necessary data.")
            os.mkdir(self.local_dir)
            os.mkdir(self.local_data)
            os.mkdir(self.local_data + '\img')
            with open(f'{self.local_data}/{self.desired_perks_csv}', 'a'):
                os.utime(f'{self.local_data}/{self.desired_perks_csv}', None)
            self.dl_perks()
        else:
            with open(f'{self.local_data}/{self.surv_perks_csv}', newline='') as f:
                reader = csv.reader(f)
                for line in reader:
                    self.surv_perks.append(line[0])    
            
            with open(f'{self.local_data}/{self.killer_perks_csv}', newline='') as f:
                reader = csv.reader(f)
                for line in reader:
                    self.killer_perks.append(line[0])    

            with open(f'{self.local_data}/{self.desired_perks_csv}', newline='') as f:
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
            print(f'\nDownloading: {perk}')
            img_tag = cells[0].find('a')
            if img_tag is not None:
                img_urls_tag = img_tag.find('img')['srcset']
                img_urls = img_urls_tag.split()
                with open(f'{self.local_data}/img/{perk}.png', 'wb') as f:
                    img = requests.get(img_urls[0])
                    f.write(img.content)
            self.surv_perks.append(perk)
            print(f'{perk} downloaded!')

        for row in killer_perks_table:
            cells = row.find_all('th')
            raw_perk = cells[1].get_text()
            if raw_perk.startswith('Name'):
                continue
            perk = raw_perk[:-1]
            print(f'\nDownloading: {perk}')
            img_tag = cells[0].find('a')
            if img_tag is not None:
                img_urls_tag = img_tag.find('img')['srcset']
                img_urls = img_urls_tag.split()
                if ':' in perk:
                    perk = perk.replace(':', '')
                with open(f'{self.local_data}/img/{perk}.png', 'wb') as f:
                    img = requests.get(img_urls[0])
                    f.write(img.content)
            self.killer_perks.append(perk)
            print(f'{perk} downloaded!')

        self.update_perks_database()

    def dl_shrine(self):
        shrine_url = 'https://deadbydaylight.gamepedia.com/Shrine_of_Secrets#Current_Shrine_of_Secrets'

        req_shrine = requests.get(shrine_url)
        soup_shrine = bs(req_shrine.content, 'lxml')    
    
        curr_shrine_table = soup_shrine.find('table',{'class':'wikitable'}).find('tbody').find_all('tr')

        for row in curr_shrine_table:
            cell = row.find('td')
            if cell is not None:
                perk = cell.get_text()
                if ':' in perk:
                    perk = perk.replace(':', '')
                self.current_shrine.append(perk[:-1])

        with io.open(f'{self.local_data}/{self.shrine_csv}', 'w', encoding='utf-8') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerow([datetime.date(datetime.now())])
            for val in self.current_shrine:
                writer.writerow([val])

    def update_perks_database(self):
        with io.open(f'{self.local_data}/{self.surv_perks_csv}', 'w', encoding='utf-8') as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in self.surv_perks:
                writer.writerow([val])

        with io.open(f'{self.local_data}/{self.killer_perks_csv}', 'w', encoding='utf-8') as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in self.killer_perks:
                writer.writerow([val])

        with io.open(f'{self.local_data}/{self.perks_csv}', 'w', encoding='utf-8') as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in self.surv_perks:
                writer.writerow([val])
            for val in self.killer_perks:
                writer.writerow([val])

        print('\nLocal database updated!')

    # def add_desired_perk(self):
    #     perks_raw = str(input('\nProvide the name/s of desired perk (in case of more than one divide them with a comma): '))
    #     perks = [x.strip().capitalize() for x in perks_raw.split(',')]
    #     for perk in perks:
    #         if perk in self.surv_perks or perk in self.killer_perks:
    #             self.desired_perks.append(perk)
    #             with io.open(f'{self.local_data}/{self.desired_perks_csv}', 'w', encoding='utf-8') as output:
    #                 writer = csv.writer(output, lineterminator='\n')
    #                 for val in self.desired_perks:
    #                     writer.writerow([val])
    #             print(f'\n{perk} added to checklist succesfully. You will be notified once it appears on Shrine of Secrets!')
    #         else:
    #             print(f'\nDang, We do not seem to have {perk} in a database. Check spelling or click update button and try again!')

    # def check_shrine(self):
    #     if len(self.desired_perks) == 0:
    #         print('\nSeems like you do not have any perks on the list yet.')
    #         self.add_desired_perk()
    #         self.check_shrine()
    #     else:
    #         self.print_shrine()    
    #         for perk in self.desired_perks:
    #             if perk in self.current_shrine:
    #                 print(F'\n{perk} is now available at Shrine of Secrets!')

    # def print_shrine(self):
    #     if len(self.current_shrine) == 0:
    #         self.dl_shrine()
    #         self.print_shrine()
    #     else:
    #         print('\nCurrent shrine of secrets:', ', '.join(self.current_shrine))

    # def print_perks(self):
    #     if len(self.killer_perks) == 0 or len(self.surv_perks) == 0:
    #         self.dl_perks()
    #         self.print_perks()
    #     else:
    #         print('\nSurvivor perks:', ', '.join(self.surv_perks))
    #         print('\nKiller perks:', ', '.join(self.killer_perks))

if __name__ == "__main__":
    app = Informator()
    app.dl_shrine()
    app.load_local_data()
    # app.check_shrine()
