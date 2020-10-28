import csv
import io
import os
import send2trash
import requests
import time
import winshell
import sys
import win32com.client
import pythoncom
import dateutil.relativedelta as REL
from csv import reader
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from templates.sc_ui import Ui_MainWindow
from templates.sc_settings import Ui_SettingsTemplate
from templates.sc_notification import Ui_NotificationTemplate
from templates.sc_progress import Ui_ProgressBarTemplate
from templates.sc_message import Ui_MessageTemplate
from rsc import rsc
from rsc import stylesheets

#TO DO LIST:
#Window bar - alternatives?
#Check periodically whether number of perks changed
#Better CSS - font type/size, buttons - UX rules

class Notifier(QtCore.QThread):
    found_signal = QtCore.pyqtSignal(list)
    empty_signal = QtCore.pyqtSignal()
    error_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        
    def check_shrine(self):
        print('Checking shrine in background')
        if window.dl_shrine() == 'Error':
            self.error_signal.emit('Data_download')
            self.empty_signal.emit()
        else:
            matches = window.check_shrine()
            if len(matches) > 0:
                self.found_signal.emit(matches)
            else:
                self.empty_signal.emit()
            
    @QtCore.pyqtSlot()
    def run(self):
        for _ in range(window.refr_notif*60*60):
            if not window.isHidden():
                print('Notifier thread interrupted')
                return None
            self.sleep(1)
        self.check_shrine()
        print('Thread finished')

class Loader(QtCore.QThread):
    finished_signal = QtCore.pyqtSignal(bool, float, float, str)
    error_signal = QtCore.pyqtSignal(str)

    def __init__(self, init=False, parent=None):
        super().__init__(parent)
        self.init = init

    @QtCore.pyqtSlot()
    def run(self):
        if self.init:
            window.load_local_data()
            try:
                window.dl_perks()
                window.dl_shrine(init=True)
            except:
                self.error_signal.emit('Data_download')
                self.finished_signal.emit(False, 1.0, 0.0, 'An error occured during download.')
                send2trash.send2trash(window.local_dir)
            else:
                window.load_content(init=True)
                window.load_shrine(init=True)
                self.finished_signal.emit(True, 1.0, 1.0, 'Finished work.')
        else:
            try:
                window.dl_perks()
            except:
                self.error_signal.emit('Data_download')
                self.finished_signal.emit(False, 1.0, 0.0, 'An error occured during download.')
                
            else:
                self.finished_signal.emit(True, 1.0, 1.0, 'Finished work.')

class Refresher(QtCore.QThread):
    finished_signal = QtCore.pyqtSignal()
    error_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        
    def refresh_ui(self):
        print('Refreshing ui')
        if window.dl_shrine() == 'Error':
            self.error_signal.emit('Data_download')
            self.empty_signal.emit()
        else:
            window.check_shrine()
            self.finished_signal.emit()
            
    @QtCore.pyqtSlot()
    def run(self):
        for _ in range(window.refr_ui*60*60):
            if window.isHidden() or not window.settings_dialog.isHidden():
                print('Refresher thread interrupted')
                return None
            self.sleep(1)
        self.refresh_ui()
        print('Thread finished')

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    progress_signal = QtCore.pyqtSignal(float, float, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initVariables()
        self.setupUi(self)
        
    def initVariables(self):
        self.perks_csv = 'perks.csv'
        self.shrine_csv = 'shrine.csv'
        self.desired_perks_csv = 'desired_perks.csv'
        self.settings_csv = 'settings.csv'
        self.local_dir = os.path.expanduser('~') + '\\Documents\\ShrineChecker'
        self.local_data = self.local_dir + '\\local'
        self.local_img = self.local_data + '\\img'
        self.dialog_done = False
        self.current_shrine = [None for n in range(5)]
        self.desired_perks = []
        self.perks = []
        self.matching_perks = []
        self.settings = []
        self.iterables = None
        self.min_to_tray = 1
        self.add_to_startup = 1
        self.refr_notif = 2
        self.refr_ui = 2
        self.refr_intervals = [2, 4, 6, 8]
        self.total_tasks = 1.0
        self.today = None
        self.next_refr = None
        self.real_refr_date = None
        
    def initDialogs(self):
        self.progress_bar = ProgressBar()
        self.settings_dialog = Settings()
        self.notification_dialog = Notification()
        self.notification_dialog.signal.connect(self.start_threading)
        self.loader_thread = Loader()
        self.loader_thread.finished_signal.connect(self.loading_finished)
        self.loader_thread.error_signal.connect(self.showError)
        self.notifier_thread = Notifier()
        self.notifier_thread.found_signal.connect(self.notify)
        self.notifier_thread.empty_signal.connect(self.start_threading)
        self.notifier_thread.error_signal.connect(self.showError)
        self.refresher_thread = Refresher()
        self.refresher_thread.finished_signal.connect(self.refresh_ui)
        self.refresher_thread.error_signal.connect(self.showError)
        self.error_dialog = MessageDialog(dialog_type='Error')
        self.info_dialog = MessageDialog(dialog_type='Message')
        
    def initData(self):
        if not os.path.exists(self.local_dir):
            self.progress_bar.prepareUi()
            self.progress_bar.show()
            self.loader_thread.init = True
            self.loader_thread.start()
        else:
            self.load_local_data()
            try:
                self.dl_shrine()  
            except:
                self.showError('Data_download')
            finally:
                self.load_content(init=True)
                self.load_shrine(init=True)
                self.show()
                self.refresh_ui()
            
    def setupUi(self, MainWindow):
        super().setupUi(self)
        self.iterables = {'img1': self.img1, 'img2': self.img2, 'img3': self.img3,
                        'img4': self.img4, 'perk1_lbl': self.perk1_lbl,
                        'perk2_lbl': self.perk2_lbl, 'perk3_lbl': self.perk3_lbl,
                        'perk4_lbl': self.perk4_lbl, 'frame1': self.frame1,
                        'frame2': self.frame2, 'frame3': self.frame3,
                        'frame4': self.frame4} 
        self.add_btn.clicked.connect(self.add_perk)
        self.remove_btn.clicked.connect(self.remove_perk)
        self.settings_btn.clicked.connect(self.open_settings)
        self.bg.setPixmap(QtGui.QPixmap(':/Background/img/bg.png'))
        self.bg.setScaledContents(True)
        self.settings_btn.setIcon(QtGui.QIcon(':/Decorations/img/settings.png'))
        self.setWindowIcon(QtGui.QIcon(':/Icon/img/icon.ico'))
        self.setStyleSheet(stylesheets.ui_stylesheet)
        tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon(':/Icon/img/icon.ico'), parent=app)
        tray_icon.show()
        menu = QtWidgets.QMenu()
        showAction = menu.addAction('Show')
        showAction.triggered.connect(self.show_ui)
        hideAction = menu.addAction('Hide')
        hideAction.triggered.connect(self.start_threading)
        exitAction = menu.addAction('Exit')
        exitAction.triggered.connect(self.close)
        menu.show()
        tray_icon.setContextMenu(menu)
    
    def loading_finished(self, status, total_tasks, task, message):
        self.progress_bar.updateProgress(total_tasks, task, message)
        if self.isHidden() and status:
            self.show()
            self.refresh_ui()
        self.progress_bar.close_btn.setEnabled(True)
    
    def load_local_data(self):
        if not os.path.exists(self.local_dir):
            self.progress_signal.emit(self.total_tasks, 0.0, "Preparing local directory.")
            os.mkdir(self.local_dir)
            os.mkdir(self.local_data)
            os.mkdir(self.local_data + '\\img')
            with open(f'{self.local_data}/{self.desired_perks_csv}', 'a'):
                os.utime(f'{self.local_data}/{self.desired_perks_csv}', None)
            with open(f'{self.local_data}/{self.desired_perks_csv}', 'a'):
                os.utime(f'{self.local_data}/{self.desired_perks_csv}', None)
            self.data_loader('save', 
                             [self.min_to_tray, self.add_to_startup, 
                              self.refr_notif, self.refr_ui], 
                             self.settings_csv)
            self.enable_disable_autostart()
            self.progress_signal.emit(self.total_tasks, 1.0, "Prepared local directory.")
        else:   
            self.data_loader('load', self.desired_perks_csv, self.desired_perks)
            self.data_loader('load', self.perks_csv, self.perks)
            self.data_loader('load', self.shrine_csv, self.current_shrine)
            with open(f'{self.local_data}/{self.settings_csv}', newline='') as f:
                reader = csv.reader(f)
                for line in reader:
                    self.settings.append(int(line[0]))   
            self.min_to_tray, self.add_to_startup, self.refr_notif, self.refr_ui = self.settings
            self.enable_disable_autostart()

    def load_content(self, init=False):
        self.perks_combo.clear()
        for perk in self.perks:
            self.perks_combo.addItem(perk)
        if init==True:
            for _ in range(1,5):
                frame = self.iterables[f'frame{_}']
                frame.setPixmap(QtGui.QPixmap(':/Decorations/img/frame1.png'))
                frame.setScaledContents(True)
            if len(self.desired_perks) > 0:
                for perk in self.desired_perks:
                    self.perks_list.addItem(perk)
        print('Content loaded.')
        
    def load_shrine(self, init=False):
        self.real_refr_date = self.next_refr - timedelta(days=1)
        self.date_lbl.setText(f'Shrine refreshes on: {self.real_refr_date.strftime("%d/%m/%y")} GMT+0')
        for _ in range(1,5):
            d = self.iterables[f'img{_}']
            d.setPixmap(QtGui.QPixmap(self.local_img+f'\\{self.current_shrine[_]}.png'))
            d.setScaledContents(True)
            e = self.iterables[f'perk{_}_lbl']
            e.setText(self.current_shrine[_])
        print('Shrine loaded.')
        if not self.isHidden() or init==True:
            self.check_shrine()        
        
    def show_ui(self):
        if self.isHidden():
            try:
                self.dl_shrine()
                self.check_shrine()
            except:
                self.showError('Data_download')
            finally:
                self.show()
                self.refresh_ui()
        else:
            return None
    
    def start_threading(self):
        print('Starting threading - notifier')
        self.notifier_thread.start()

    def notify(self, matching_perks):
        self.notification_dialog.setup_notification(matching_perks)
        self.notification_dialog.show()

    def check_shrine(self):
        self.matching_perks.clear()
        for perk in self.current_shrine:
            if perk in self.desired_perks:
                self.matching_perks.append(perk)
        for perk in self.current_shrine[1:]:
            perk_index = self.current_shrine.index(perk)
            if perk in self.matching_perks:
                label = self.iterables[f'perk{perk_index}_lbl']
                label.setStyleSheet('color:white; font:bold')
                frame = self.iterables[f'frame{perk_index}']
                frame.setHidden(False)     
            else:
                label = self.iterables[f'perk{perk_index}_lbl']
                label.setStyleSheet('color:#6e6d6d;')
                img = self.iterables[f'img{perk_index}']
                img.setStyleSheet('border: none;')
                frame = self.iterables[f'frame{perk_index}']
                frame.setHidden(True)
        print('Shrine checked.')
        return self.matching_perks

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
        self.settings_dialog.notif_combo.setCurrentIndex(self.refr_intervals.index(self.refr_notif))
        self.settings_dialog.refr_combo.setCurrentIndex(self.refr_intervals.index(self.refr_ui))
        self.settings_dialog.show()

    def refresh_ui(self):
        print('Starting threading - ui refresher')
        self.refresher_thread.start()        
        
    def dl_perks(self):
        perks_url = 'https://deadbydaylight.gamepedia.com/Perks'
        req_perks = requests.get(perks_url)
        soup_perks = bs(req_perks.content, 'lxml')
        surv_perks_table_raw, killer_perks_table_raw = soup_perks.find_all('table',{'class':'wikitable sortable'})
        surv_perks_table, killer_perks_table = surv_perks_table_raw.find('tbody').find_all('tr'), killer_perks_table_raw.find('tbody').find_all('tr')
        surv_perks_count_raw = surv_perks_table_raw.find_previous_sibling()
        surv_perks_count = float(surv_perks_count_raw.find('span')['id'][-3:-1])
        killer_perks_count_raw = killer_perks_table_raw.find_previous_sibling()
        killer_perks_count = float(killer_perks_count_raw.find('span')['id'][-3:-1])
        current_task = 0.0
        total_tasks = surv_perks_count + killer_perks_count - 26.0
        self.perks.clear()
        for row in surv_perks_table:
            cells = row.find_all('th')
            if cells[2].find('a') is None:
                continue
            raw_perk = cells[1].get_text()
            if raw_perk.startswith('Name'):
                continue
            perk = raw_perk[:-1]
            print(f'\nDownloading: {perk}')
            self.progress_signal.emit(total_tasks, current_task, f'Downloading: {perk}')
            img_tag = cells[0].find('a')
            if img_tag is not None:
                img_url = img_tag.find('img')['src']
                with open(f'{self.local_data}/img/{perk}.png', 'wb') as f:
                    img = requests.get(img_url)
                    f.write(img.content)
            self.perks.append(perk)
            current_task += 1.0
            self.progress_signal.emit(total_tasks, current_task, f'{perk} downloaded!')
            print(f'{perk} downloaded!')

        for row in killer_perks_table:
            cells = row.find_all('th')
            if cells[2].find('a') is None:
                continue
            raw_perk = cells[1].get_text()
            if raw_perk.startswith('Name'):
                continue
            perk = raw_perk[:-1]
            print(f'\nDownloading: {perk}')
            self.progress_signal.emit(total_tasks, current_task, f'Downloading: {perk}')
            img_tag = cells[0].find('a')
            if img_tag is not None:
                img_url = img_tag.find('img')['src']
                if ':' in perk:
                    perk = perk.replace(':', '')
                with open(f'{self.local_data}/img/{perk}.png', 'wb') as f:
                    img = requests.get(img_url)
                    f.write(img.content)
            self.perks.append(perk)
            current_task += 1.0
            self.progress_signal.emit(total_tasks, current_task, f'{perk} downloaded!')
            print(f'{perk} downloaded!')
        self.progress_signal.emit(total_tasks, current_task, f'Finishing...')
        self.data_loader('save', self.perks, self.perks_csv)
        print('Perks downloaded and saved.')
         
    def dl_shrine(self, init=False, force=False):
        self.today = datetime.utcnow().date()
        rd = REL.relativedelta(days=1, weekday=REL.TH)
        self.next_refr = self.today + rd
        if init or force:
            pass
        else:
            shrine_dwnl_date = datetime.strptime(self.current_shrine[0], '%d/%m/%Y %H:%M').date()
            time_to_refr = ((self.next_refr - self.today).total_seconds())/86400
            if shrine_dwnl_date < self.next_refr and time_to_refr in range(1,8):
                if self.real_refr_date != self.next_refr - timedelta(days=1):
                    self.real_refr_date = self.next_refr - timedelta(days=1)
                    self.date_lbl.setText(f'Shrine refreshes on: {self.real_refr_date.strftime("%d/%m/%y")} GMT+0')
                print('No need to download shrine')
                return None
         
        shrine_url = 'https://deadbydaylight.gamepedia.com/Shrine_of_Secrets#Current_Shrine_of_Secrets'
        try:
            req_shrine = requests.get(shrine_url)
        except:
            self.showError('Data_download')
            return 'Error'
        else:
            self.current_shrine.clear()
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
            self.current_shrine.insert(0, str(datetime.utcnow().strftime('%d/%m/%Y %H:%M')))
            self.data_loader('save', self.current_shrine, self.shrine_csv)
            print('Shrine downloaded and saved.')
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
    
    def showError(self, source):
        self.error_dialog.dialog_message(source)
        self.error_dialog.show()
    
    def enable_disable_autostart(self):
        pythoncom.CoInitialize()
        startup = winshell.startup()
        path = os.path.join(startup, 'SC.lnk')
        if self.add_to_startup:
            target = sys.argv[0]
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WindowStyle = 7
            shortcut.save()
        else:
            if os.path.isfile(path):
                send2trash.send2trash(path)
    
    def closeEvent(self, event):
        if not self.min_to_tray or self.isHidden():
            self.settings_dialog.close()
            self.notification_dialog.close()
            event.accept()
        else:
            self.settings_dialog.close()
            self.hide()
            event.ignore()
            self.start_threading()

class Settings(QtWidgets.QDialog, Ui_SettingsTemplate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsTemplate()
        self.initVariables()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    
    def initVariables(self):
        self.local_dir = os.path.expanduser('~') + '\\Documents\\ShrineChecker'
        self.local_data = self.local_dir + '\\local'
        self.local_img = self.local_data + '\\img'
        
    def setupUi(self, Dialog, tray=True, startup=True):
        super().setupUi(self)
        self.tray_check.setChecked(tray)
        self.startup_check.setChecked(startup)
        self.setWindowIcon(QtGui.QIcon(':/Icon/img/icon.ico'))
        self.bg.setPixmap(QtGui.QPixmap(':/Background/img/bg.png'))
        self.setStyleSheet(stylesheets.settings_stylesheet)
        self.save_btn.clicked.connect(self.save)
        self.close_btn.clicked.connect(self.close)
        self.reset_btn.clicked.connect(self.reset)
        self.reload_btn.clicked.connect(self.reload)
        self.about_btn.clicked.connect(self.info_dialog)

    def save(self):
        window.min_to_tray = 1 if self.tray_check.isChecked() else 0
        window.add_to_startup = 1 if self.startup_check.isChecked() else 0
        window.enable_disable_autostart()
        window.refr_notif = int(self.notif_combo.currentText())
        window.refr_ui = int(self.refr_combo.currentText())
        window.data_loader('save', 
                           [window.min_to_tray, window.add_to_startup,
                            window.refr_notif, window.refr_ui],
                            window.settings_csv)
        
    def reset(self):
        window.progress_bar.prepareUi()
        window.progress_bar.show()
        window.loader_thread.init = False
        window.loader_thread.start()
            
    def reload(self):
        window.dl_shrine(force=True)        
            
    def info_dialog(self):
        window.info_dialog.show()
                   
    def closeEvent(self, event):
        if not self.isHidden():
            window.refresh_ui()      
            
class Notification(QtWidgets.QDialog, Ui_NotificationTemplate):
    signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initVariables()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def initVariables(self):
        self.local_dir = os.path.expanduser('~') + '\\Documents\\ShrineChecker'
        self.local_data = self.local_dir + '\\local'
        self.local_img = self.local_data + '\\img'

    def setupUi(self, Dialog):
        super().setupUi(self)
        self.iterables = {'img1': self.img1, 'img2': self.img2, 'img3': self.img3,
                        'img4': self.img4, 'perk1_lbl': self.perk1_lbl,
                        'perk2_lbl': self.perk2_lbl, 'perk3_lbl': self.perk3_lbl,
                        'perk4_lbl': self.perk4_lbl, 'msg1_lbl': self.msg1_lbl,
                        'msg2_lbl': self.msg2_lbl, 'msg3_lbl': self.msg3_lbl,
                        'msg4_lbl': self.msg4_lbl, 1: 180, 2: 320, 3: 460,
                        4: 600, 'frame1': self.frame1,
                        'frame2': self.frame2, 'frame3': self.frame3,
                        'frame4': self.frame4}
        self.setWindowIcon(QtGui.QIcon(':/Icon/img/icon.ico'))
        self.bg.setPixmap(QtGui.QPixmap(':/Background/img/bg.png'))
        self.setStyleSheet(stylesheets.notification_stylesheet)
        self.close_btn.clicked.connect(self.start_threading)
        self.show_btn.clicked.connect(self.show_ui)
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        widget = self.geometry()
        x = screen.width() - widget.width()
        self.move(x, 40)
        for _ in range(1,5):
                frame = self.iterables[f'frame{_}']
                frame.setPixmap(QtGui.QPixmap(':/Decorations/img/frame1.png'))
                frame.setScaledContents(True)
        
    def setup_notification(self, perks):
        self.resize(350, self.iterables[len(perks)])
        for _ in range(1, len(perks)+1):
            d = self.iterables[f'img{_}']
            d.setPixmap(QtGui.QPixmap(self.local_img+f'\\{perks[_-1]}.png'))
            d.setScaledContents(True)
            e = self.iterables[f'perk{_}_lbl']
            e.setText(perks[_-1])
            f = self.iterables[f'msg{_}_lbl']
            f.setText('Is now available!')
        
    def start_threading(self):
        self.hide()
        self.signal.emit()

    def show_ui(self):
        self.hide()
        window.show()
        window.refresh_ui()
        
class ProgressBar(QtWidgets.QDialog, Ui_ProgressBarTemplate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initVariables()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        window.progress_signal.connect(self.updateProgress)
    
    def initVariables(self):
        self.local_dir = os.path.expanduser('~') + '\\Documents\\ShrineChecker'
        self.local_data = self.local_dir + '\\local'
        self.local_img = self.local_data + '\\img'
        
    def setupUi(self, Dialog):
        super().setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/Icon/img/icon.ico'))
        self.bg.setPixmap(QtGui.QPixmap(':/Background/img/bg.png'))
        self.setStyleSheet(stylesheets.progress_stylesheet)
        self.progress_bar.setValue(0)
        self.msg_lbl.setText('Starting work...')
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setEnabled(False)
    
    def updateProgress(self, total_tasks, current_task, message):
        self.progress_bar.setValue(100.0*current_task/total_tasks)
        self.msg_lbl.setText(message)

    def prepareUi(self):
        self.progress_bar.setValue(0)
        self.msg_lbl.setText('Starting work...')

    def closeEvent(self, event):
        self.close_btn.setEnabled(False)
        event.accept()

class MessageDialog(QtWidgets.QDialog, Ui_MessageTemplate):
    def __init__(self, parent=None, dialog_type = 'Message' or 'Error'):
        super().__init__(parent)
        self.dialog_type = dialog_type
        self.initVariables()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    
    def initVariables(self):
        self.local_dir = os.path.expanduser('~') + '\\Documents\\ShrineChecker'
        self.local_data = self.local_dir + '\\local'
        self.local_img = self.local_data + '\\img'
        
    def setupUi(self, Dialog):
        super().setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/Icon/img/icon.ico'))
        self.bg.setPixmap(QtGui.QPixmap(':/Background/img/bg.png'))
        self.setStyleSheet(stylesheets.message_stylesheet)
        self.close_btn.clicked.connect(self.hide)
        if self.dialog_type == 'Message':
            self.title_lbl.setStyleSheet('font: 20px "Sylfaen" bold;')
            self.title_lbl.setText('About us:')
            self.msg_lbl.setText('Program author: Michal Kowal\nE-mail: kow.michal.66@gmail.com\nReddit: u/virtozenho\n\nArt designer: Urszula Kowal\nInstagram: _kowalowna_')
        elif self.dialog_type == 'Error':
            self.title_lbl.setText('Oops, something went wrong!')    
           
    def dialog_message(self, source):
        if source == 'Data_download':
            self.msg_lbl.setText("Wasn't able to download data. Check the internet connection and try again (interruption may damage existing files, remember to rerun the program after resolving problems).")
            
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.initDialogs()
    window.initData()
    sys.exit(app.exec_())