import csv
from csv import reader
import io
import os
from bs4 import BeautifulSoup as bs
import requests
import time
from datetime import datetime
from sc_ui import *
from sc_settings import *
from sc_notification import *
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from win10toast import ToastNotifier

#To do list:
#Create sleep functionality and notifications
#Prepare the proper css

class Worker(QtCore.QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @QtCore.pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)   

class SC_Ui(Ui_MainWindow):
    tray_icon = None
    def __init__(self, parent=None):
        Ui_MainWindow.__init__(self)
        self.current_shrine = []
        self.desired_perks = []
        self.perks = []
        self.settings = []
        self.perks_csv = 'perks.csv'
        self.shrine_csv = 'shrine.csv'
        self.desired_perks_csv = 'desired_perks.csv'
        self.settings_csv = 'settings.csv'
        self.local_dir = os.path.expanduser('~') + '\Documents\ShrineChecker'
        self.local_data = self.local_dir + '\local'
        self.local_img = self.local_data + '\img'
        self.iterables = None
        self.min_to_tray = bool
        self.add_to_startup = bool
        self.threadpool = QtCore.QThreadPool()
        
    def setupUi(self, MainWindow):
        super(SC_Ui, self).setupUi(MainWindow)
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
        self.bg.setPixmap(QtGui.QPixmap('main/rsc/bg.png'))
        self.bg.setScaledContents(True)
        self.settings_btn.setIcon(QtGui.QIcon('main/rsc/settings.png'))
        
    def load_local_data(self):
        if not os.path.exists(self.local_dir):
            os.mkdir(self.local_dir)
            os.mkdir(self.local_data)
            os.mkdir(self.local_data + '\img')
            with open(f'{self.local_data}/{self.desired_perks_csv}', 'a'):
                os.utime(f'{self.local_data}/{self.desired_perks_csv}', None)
            with open(f'{self.local_data}/{self.desired_perks_csv}', 'a'):
                os.utime(f'{self.local_data}/{self.desired_perks_csv}', None)
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
        tray_icon = QSystemTrayIcon(QIcon('main/rsc/settings.png'), parent=app)
        tray_icon.show()
        menu = QMenu()
        showAction = menu.addAction('Show')
        showAction.triggered.connect(MainWindow.show)
        hideAction = menu.addAction('Hide')
        hideAction.triggered.connect(self.hide_ui)
        exitAction = menu.addAction('Exit')
        exitAction.triggered.connect(MainWindow.close)
        menu.show()
        tray_icon.setContextMenu(menu)

    def load_shrine(self):
        self.date_lbl.setText(self.current_shrine[0])
        for _ in range(1,5):
            d = self.iterables[f'img{_}']
            d.setPixmap(QtGui.QPixmap(self.local_img+f'\{self.current_shrine[_]}.png'))
            d.setScaledContents(True)
            e = self.iterables[f'perk{_}_lbl']
            e.setText(self.current_shrine[_])

    def check_shrine(self, init=False):
        if not MainWindow.isHidden() or init == True:
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
        else:
            while MainWindow.isHidden():
                time.sleep(60*60*2)
                matches = []
                print("Shrine checked while hidden")
                for perk in self.desired_perks:
                    if perk in self.current_shrine:
                        print(f'{perk} is now available in the Shrine of Secrets!')
                        matches.append(perk)
                        if len(matches) == 4:
                            toast.show_toast('Perks available:', f"{', '.join(matches)}", icon_path=None)
                toast.show_toast('Perks available:', f"{', '.join(matches)}", icon_path=None)
                self.dl_shrine()

    def add_perk(self):
        perk = self.perks_combo.currentText()
        items = self.perks_list.findItems(perk, QtCore.Qt.MatchExactly)
        if len(items) > 0:
            return
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
            return

    def open_settings(self):
        settings_dialog.tray_check.setChecked(self.min_to_tray)
        settings_dialog.startup_check.setChecked(self.add_to_startup)
        Dialog.show()

    def hide_ui(self):
        Dialog.close()
        MainWindow.hide()
        worker = Worker(self.check_shrine)
        self.threadpool.start(worker)
        
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

class Settings_ui(Ui_Dialog):
    def setupUi(self, Dialog, tray=bool, startup=bool):
        super(Settings_ui, self).setupUi(Dialog)
        self.tray_check.setChecked(tray)
        self.startup_check.setChecked(startup)
        self.bg.setPixmap(QtGui.QPixmap('main/rsc/bg.png'))
        self.save_btn.clicked.connect(self.save)

    def save(self):
        ui.min_to_tray = 1 if self.tray_check.isChecked() else 0
        ui.add_to_startup = 1 if self.startup_check.isChecked() else 0
        ui.data_loader('save', [ui.min_to_tray, ui.add_to_startup], ui.settings_csv)

    def reset(self):
        return

# class Notifiactions_ui(Ui_Form):
#     def setupUi(self, Dialog, tray=bool, startup=bool):
#         super(Notifiactions_ui, self).setupUi(Form)
#         self.bg.setPixmap(QtGui.QPixmap('main/rsc/bg.png'))
        
class ui_BaseClass(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        if not ui.min_to_tray or MainWindow.isHidden():
            event.accept()
        else:
            ui.hide_ui()
            event.ignore()

class settings_BaseClass(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)

# class notifications_BaseClass(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self)
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ui_BaseClass()
    Dialog = settings_BaseClass()
    # Form = notifications_BaseClass()
    # Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui = SC_Ui()
    ui.setupUi(MainWindow)
    settings_dialog = Settings_ui()
    settings_dialog.setupUi(Dialog, ui.min_to_tray, ui.add_to_startup)
    # notifications = Notifiactions_ui()
    # notifications.setupUi(Form)
    MainWindow.show()
    toast = ToastNotifier()
    sys.exit(app.exec_())