import csv
import io
import os
import shutil
import requests
import time
from threading import Thread
from csv import reader
from bs4 import BeautifulSoup as bs
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.sc_ui import Ui_MainWindow
from ui.sc_settings import Ui_Dialog as SettingsTemplate
from ui.sc_notification import Ui_Dialog as NotificationTemplate

#TO DO LIST:
#Implement better threading
#Proper CSS

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    signal = QtCore.pyqtSignal()
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.initVariables()
        self.setupUi(self)
        
        self.settings_dialog = Settings()
        self.notification_dialog = Notification()
        
    def initVariables(self):
        self.dialog_done = False
        self.current_shrine = []
        self.desired_perks = []
        self.perks = []
        self.settings = []
        self.perks_csv = 'perks.csv'
        self.shrine_csv = 'shrine.csv'
        self.desired_perks_csv = 'desired_perks.csv'
        self.settings_csv = 'settings.csv'
        self.local_dir = os.path.expanduser('~') + '\\Documents\\ShrineChecker'
        self.local_data = self.local_dir + '\\local'
        self.local_img = self.local_data + '\\img'
        self.iterables = None
        self.min_to_tray = 1
        self.add_to_startup = 1
        
    def setupUi(self, MainWindow):
        super().setupUi(self)
        self.iterables = {'img1': self.img1, 'img2': self.img2, 'img3': self.img3,
                        'img4': self.img4, 'perk1_lbl': self.perk1_lbl,
                        'perk2_lbl': self.perk2_lbl, 'perk3_lbl': self.perk3_lbl,
                        'perk4_lbl': self.perk4_lbl, 'frame1': self.frame1,
                        'frame2': self.frame2, 'frame3': self.frame3,
                        'frame4': self.frame4}        
        self.load_local_data()
        self.load_content()
        self.load_shrine()
        self.check_shrine(init=True)
        self.add_btn.clicked.connect(self.add_perk)
        self.remove_btn.clicked.connect(self.remove_perk)
        self.reload_btn.clicked.connect(self.dl_shrine)
        self.settings_btn.clicked.connect(self.open_settings)
        self.bg.setPixmap(QtGui.QPixmap(f'{self.local_img}\\bg.png'))
        self.bg.setScaledContents(True)
        self.settings_btn.setIcon(QtGui.QIcon(f'{self.local_img}\\settings.png'))
    
    def load_local_data(self):
        if not os.path.exists(self.local_dir):
            os.mkdir(self.local_dir)
            os.mkdir(self.local_data)
            os.mkdir(self.local_data + '\\img')
            with open(f'{self.local_data}/{self.desired_perks_csv}', 'a'):
                os.utime(f'{self.local_data}/{self.desired_perks_csv}', None)
            with open(f'{self.local_data}/{self.desired_perks_csv}', 'a'):
                os.utime(f'{self.local_data}/{self.desired_perks_csv}', None)
            self.data_loader('save', [self.min_to_tray, self.add_to_startup], self.settings_csv)
            self.dl_perks()
            self.dl_shrine()
        else:     
            self.data_loader('load', self.desired_perks_csv, self.desired_perks)
            self.data_loader('load', self.perks_csv, self.perks)
            self.data_loader('load', self.shrine_csv, self.current_shrine)
            with open(f'{self.local_data}/{self.settings_csv}', newline='') as f:
                reader = csv.reader(f)
                for line in reader:
                    self.settings.append(int(line[0]))   
            self.min_to_tray, self.add_to_startup = self.settings
            if str(datetime.date(datetime.now())) != self.current_shrine[0]:
                self.dl_shrine()

    def load_content(self):
        for perk in self.perks:
            self.perks_combo.addItem(perk)
        if len(self.desired_perks) > 0:
            for perk in self.desired_perks:
                self.perks_list.addItem(perk)
        for _ in range(1,5):
            frame = self.iterables[f'frame{_}']
            frame.setPixmap(QtGui.QPixmap(self.local_img+f'/frame1.png'))
            frame.setScaledContents(True)
        tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon(f'{self.local_img}\\icon.ico'), parent=app)
        tray_icon.show()
        menu = QtWidgets.QMenu()
        showAction = menu.addAction('Show')
        showAction.triggered.connect(self.show)
        hideAction = menu.addAction('Hide')
        hideAction.triggered.connect(self.start_thread)
        exitAction = menu.addAction('Exit')
        exitAction.triggered.connect(self.close)
        menu.show()
        tray_icon.setContextMenu(menu)

    def load_shrine(self):
        self.date_lbl.setText(self.current_shrine[0])
        for _ in range(1,5):
            d = self.iterables[f'img{_}']
            d.setPixmap(QtGui.QPixmap(self.local_img+f'\\{self.current_shrine[_]}.png'))
            d.setScaledContents(True)
            e = self.iterables[f'perk{_}_lbl']
            e.setText(self.current_shrine[_])

    def check_shrine(self, init=False):
        if not self.isHidden() or init == True:
            for _ in range(1,5):
                label = self.iterables[f'perk{_}_lbl']
                label.setStyleSheet('color:#6e6d6d;')
                img = self.iterables[f'img{_}']
                img.setStyleSheet('border: none;')
                frame = self.iterables[f'frame{_}']
                frame.setHidden(True)
            for perk in self.desired_perks:
                if perk in self.current_shrine:
                    perk_index = self.current_shrine.index(perk)
                    label = self.iterables[f'perk{perk_index}_lbl']
                    label.setStyleSheet('color:white; font:bold')
                    frame = self.iterables[f'frame{perk_index}']
                    frame.setHidden(False)
        elif self.isHidden():
            self.signal.emit()
            print("I'd check the shrine now!")    

    def add_perk(self):
        perk = self.perks_combo.currentText()
        items = self.perks_list.findItems(perk, QtCore.Qt.MatchExactly)
        if len(items) > 0:
            return None
        else:
            self.perks_list.addItem(perk)
            self.desired_perks.append(perk)
            self.data_loader('save', perk, self.desired_perks_csv)
        self.check_shrine()
    
    def remove_perk(self):
        try:
            sel_perk_txt = self.perks_list.currentItem().text()
            sel_perks = self.perks_list.selectedItems()
            for perk in sel_perks:
                self.perks_list.takeItem(self.perks_list.row(perk))
                self.desired_perks.remove(sel_perk_txt)
                self.data_loader('save', self.desired_perks, self.desired_perks_csv)
            self.check_shrine()
        except:
            return None

    def open_settings(self):
        self.settings_dialog.tray_check.setChecked(self.min_to_tray)
        self.settings_dialog.startup_check.setChecked(self.add_to_startup)
        self.settings_dialog.show()
        
    def start_thread(self):
        print("Threading started")
        t = Thread(target=self.show_dialog)
        t.daemon = True
        t.start()
            
    def show_dialog(self):
        self.signal.emit()
        self.wait_for_dialog()
        
    def complete_dialog(self):
        self.dialog_done = True
        self.show()

    def wait_for_dialog(self):
        while not self.dialog_done:
            pass
        self.dialog_done = False

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
            if perk == 'Déjà Vu':
                    perk = 'Deja Vu'
            print(f'\nDownloading: {perk}')
            img_tag = cells[0].find('a')
            if img_tag is not None:
                img_url = img_tag.find('img')['src']
                with open(f'{self.local_data}/img/{perk}.png', 'wb') as f:
                    img = requests.get(img_url)
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
                img_url = img_tag.find('img')['src']
                if ':' in perk:
                    perk = perk.replace(':', '')
                with open(f'{self.local_data}/img/{perk}.png', 'wb') as f:
                    img = requests.get(img_url)
                    f.write(img.content)
            self.perks.append(perk)
            print(f'{perk} downloaded!')
        self.data_loader('save', self.perks, self.perks_csv)
        print('Perks downloaded and saved.')
    
    def dl_shrine(self):
        self.current_shrine.clear()
        shrine_url = 'https://deadbydaylight.gamepedia.com/Shrine_of_Secrets#Current_Shrine_of_Secrets'
        req_shrine = requests.get(shrine_url)
        soup_shrine = bs(req_shrine.content, 'lxml')    
        curr_shrine_table = soup_shrine.find('table',{'class':'wikitable'}).find('tbody').find_all('tr')
        for row in curr_shrine_table:
            cell = row.find('td')
            if cell is not None:
                perk = cell.get_text()
                if perk == 'Déjà Vu':
                    perk = 'Deja Vu'
                elif ':' in perk:
                    perk = perk.replace(':', '')
                self.current_shrine.append(perk[:-1])
        self.current_shrine.insert(0, str(datetime.date(datetime.now())))
        self.data_loader('save', self.current_shrine, self.shrine_csv)
        print('Shrine downloaded and saved.')
        self.load_shrine()
        print('Shrine loaded.')

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
    
    def closeEvent(self, event):
        if not self.min_to_tray or self.isHidden():
            self.settings_dialog.close()
            self.notification_dialog.close()
            event.accept()
        else:
            self.settings_dialog.close()
            self.hide()
            event.ignore()
            self.start_thread()

class Settings(QtWidgets.QDialog, SettingsTemplate):
    signal = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = SettingsTemplate()
        self.initVariables()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    
    def initVariables(self):
        self.local_dir = os.path.expanduser('~') + '\\Documents\\ShrineChecker'
        self.local_data = self.local_dir + '\\local'
        self.local_img = self.local_data + '\\img'
        
    def setupUi(self, Dialog, tray=True, startup=True):
        super().setupUi(self)
        self.tray_check.setChecked(tray)
        self.startup_check.setChecked(startup)
        self.bg.setPixmap(QtGui.QPixmap(f'{self.local_img}\\bg.png'))
        self.save_btn.clicked.connect(self.save)
        self.reset_btn.clicked.connect(self.reset)
        self.close_btn.clicked.connect(self.close)

    def save(self):
        window.min_to_tray = 1 if self.tray_check.isChecked() else 0
        window.add_to_startup = 1 if self.startup_check.isChecked() else 0
        window.data_loader('save', [window.min_to_tray, window.add_to_startup], window.settings_csv)

    def reset(self):
        shutil.rmtree(window.local_dir)
        window.load_local_data()   
            
class Notification(QtWidgets.QDialog, NotificationTemplate):
    signal = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = NotificationTemplate()
        self.initVariables()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
    def initVariables(self):
        self.local_dir = os.path.expanduser('~') + '\\Documents\\ShrineChecker'
        self.local_data = self.local_dir + '\\local'
        self.local_img = self.local_data + '\\img'
        
    def setupUi(self, Dialog):
        super().setupUi(self)
        self.bg.setPixmap(QtGui.QPixmap(f'{self.local_img}\\bg.png'))
        self.close_btn.clicked.connect(self.close)
        
    def show_notification(self):
        super(Notification, self).exec_()
        self.signal.emit()
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    s_dialog = Settings()
    n_dialog = Notification()
    window.show()
    window.signal.connect(n_dialog.show_notification)
    n_dialog.signal.connect(window.complete_dialog)
    sys.exit(app.exec_())