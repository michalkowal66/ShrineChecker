import csv
from csv import reader
import io
import os
from sc_ui import *
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime

#To do list:
#Make the animation showing that desired perk is available
#Prepare the proper css

class SC_Ui(Ui_MainWindow):
    def __init__(self):
        self.current_shrine = []
        self.desired_perks = []
        self.perks = []
        self.perks_csv = 'perks.csv'
        self.shrine_csv = 'shrine.csv'
        self.desired_perks_csv = 'desired_perks.csv'
        self.local_dir = os.path.expanduser('~') + '\Documents\ShrineChecker'
        self.local_data = self.local_dir + '\local'
        self.local_img = self.local_data + '\img'
        
    def setupUi(self, MainWindow):
        super(SC_Ui, self).setupUi(MainWindow)
        self.iterables = {'img1': self.img1, 'img2': self.img2, 'img3': self.img3,
                        'img4': self.img4, 'perk1_lbl': self.perk1_lbl,
                        'perk2_lbl': self.perk2_lbl, 'perk3_lbl': self.perk3_lbl,
                        'perk4_lbl': self.perk4_lbl}
        self.load_local_data()
        self.load_content()
        self.load_shrine()
        self.check_shrine()
        self.add_btn.clicked.connect(self.add_perk)
        self.remove_btn.clicked.connect(self.remove_perk)
        self.reload_btn.clicked.connect(self.dl_shrine)

        self.bg.setPixmap(QtGui.QPixmap('bg3.png'))
        self.bg.setScaledContents(True)

    def load_local_data(self):
        if not os.path.exists(self.local_dir):
            #print("Seems like there is no local data to load, making new directory and downloading necessary data.")
            os.mkdir(self.local_dir)
            os.mkdir(self.local_data)
            os.mkdir(self.local_data + '\img')
            with open(f'{self.local_data}/{self.desired_perks_csv}', 'a'):
                os.utime(f'{self.local_data}/{self.desired_perks_csv}', None)
            self.dl_perks()
            self.dl_shrine()
        else:     
            self.data_loader("load", self.desired_perks_csv, self.desired_perks)
            self.data_loader("load", self.perks_csv, self.perks)
            self.data_loader("load", self.shrine_csv, self.current_shrine)

    def load_content(self):
        for perk in self.perks:
            self.perks_combo.addItem(perk)
        if len(self.desired_perks) > 0:
            for perk in self.desired_perks:
                self.perks_list.addItem(perk)
        
    def load_shrine(self):
        self.date_lbl.setText(self.current_shrine[0])

        for _ in range(1,5):
            d = self.iterables[f'img{_}']
            d.setPixmap(QtGui.QPixmap(self.local_img+f'\{self.current_shrine[_]}.png'))
            d.setScaledContents(True)
            e = self.iterables[f'perk{_}_lbl']
            e.setText(self.current_shrine[_])

    def check_shrine(self):
        for _ in range(1,5):
            e = self.iterables[f'perk{_}_lbl']
            e.setStyleSheet("color:white")
        for perk in self.desired_perks:
            if perk in self.current_shrine:
                perk_index = self.current_shrine.index(perk)
                if perk_index == 1:
                    self.perk1_lbl.setStyleSheet("color:red")
                elif perk_index == 2:
                    self.perk2_lbl.setStyleSheet("color:red")
                elif perk_index == 3:
                    self.perk3_lbl.setStyleSheet("color:red")
                elif perk_index == 4:
                    self.perk4_lbl.setStyleSheet("color:red")

    def add_perk(self):
        perk = self.perks_combo.currentText()
        items = self.perks_list.findItems(perk, QtCore.Qt.MatchExactly)
        if len(items) > 0:
            return
        else:
            self.perks_list.addItem(perk)
            self.desired_perks.append(perk)
            self.data_loader("save", perk, self.desired_perks_csv)
        self.check_shrine()
    
    def remove_perk(self):
        try:
            sel_perk_txt = self.perks_list.currentItem().text()
            sel_perks = self.perks_list.selectedItems()
            for perk in sel_perks:
                self.perks_list.takeItem(self.perks_list.row(perk))
                self.desired_perks.remove(sel_perk_txt)
                self.data_loader("save", self.desired_perks, self.desired_perks_csv)
            self.check_shrine()
        except:
            return
    
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
            self.perks.append(perk)
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
            self.perks.append(perk)
            print(f'{perk} downloaded!')

        self.data_loader("save", self.perks, self.perks_csv)
    
    def dl_shrine(self):
        self.current_shrine.clear()
        curr_time = str(datetime.date(datetime.now()))
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
                print(f'{perk} downloaded!')
        self.current_shrine.insert(0, curr_time)
        self.data_loader("save", self.current_shrine, self.shrine_csv)
        self.load_shrine()

    def data_loader(self, action, source, target):
        if action == 'save':
            if type(source) == list:
                with io.open(f'{self.local_data}/{target}', 'w', encoding='utf-8') as output:
                    writer = csv.writer(output, lineterminator='\n')
                    for val in source:
                        writer.writerow([val])
            elif type(source) == str:
                with io.open(f'{self.local_data}/{target}', 'a', encoding='utf-8') as output:
                    writer = csv.writer(output, lineterminator='\n')
                    writer.writerow([source])
        elif action == 'load':
            target.clear()
            with open(f'{self.local_data}/{source}', newline='') as f:
                reader = csv.reader(f)
                for line in reader:
                    target.append(line[0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SC_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
