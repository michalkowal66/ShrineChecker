import csv
import io
import os
import shutil
import requests
import time
from csv import reader
from bs4 import BeautifulSoup as bs
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.sc_ui import Ui_MainWindow
from ui.sc_notification import Ui_Dialog as NotificationTemplate

class Thread(QtCore.QThread):
    found_signal = QtCore.pyqtSignal(list)
    empty_signal = QtCore.pyqtSignal()

    def __init__(self, desired_perks, current_shrine):
        QtCore.QThread.__init__(self, parent=app)
        self.desired_perks = desired_perks
        self.current_shrine = current_shrine
        
    def check_shrine(self):
        print('Checking shrine in background')
        matches = []
        for perk in self.current_shrine:
            if perk in self.desired_perks:
                matches.append(perk)
        if len(matches) > 0:
            self.found_signal.emit(matches)
        else:
            self.empty_signal.emit()
            
    @QtCore.pyqtSlot()
    def run(self):
        time.sleep(5)
        self.check_shrine()
        
class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    signal = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.initVariables()
        self.setupUi(self)

    def initVariables(self):
        self.current_shrine = ['Saboteur', 'Vigil', 'Alert', 'Remember Me']
        self.desired_perks = ['Vigil', 'Adrenaline']
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
        self.notification_dialog = Notification()
        self.notification_dialog.signal.connect(self.start_threading)
        self.thread = Thread(self.desired_perks, self.current_shrine)
        self.thread.found_signal.connect(self.notify)
        self.thread.empty_signal.connect(self.start_threading)

    def setupUi(self, MainWindow):
        super().setupUi(self)
        self.bg.setPixmap(QtGui.QPixmap(f'{self.local_img}\\bg.png'))
        self.bg.setScaledContents(True)
        self.settings_btn.setIcon(QtGui.QIcon(f'{self.local_img}\\settings.png'))
        tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon(f'{self.local_img}\\icon.ico'), parent=app)
        tray_icon.show()
        menu = QtWidgets.QMenu()
        showAction = menu.addAction('Show')
        showAction.triggered.connect(self.show)
        hideAction = menu.addAction('Hide')
        hideAction.triggered.connect(self.hide)
        exitAction = menu.addAction('Exit')
        exitAction.triggered.connect(self.close)
        menu.show()
        tray_icon.setContextMenu(menu)

    def start_threading(self):
        self.thread.start()

    def notify(self, matching_perks):
        self.notification_dialog.setup_notification(matching_perks)
        self.notification_dialog.show()

    def closeEvent(self, event):
        if not self.min_to_tray or self.isHidden():
            self.notification_dialog.close()
            event.accept()
        else:
            self.hide()
            self.start_threading()
            event.ignore()

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
        self.iterables = {'img1': self.img1, 'img2': self.img2, 'img3': self.img3,
                        'img4': self.img4, 'perk1_lbl': self.perk1_lbl,
                        'perk2_lbl': self.perk2_lbl, 'perk3_lbl': self.perk3_lbl,
                        'perk4_lbl': self.perk4_lbl, 'msg1_lbl': self.msg1_lbl,
                        'msg2_lbl': self.msg2_lbl, 'msg3_lbl': self.msg3_lbl,
                        'msg4_lbl': self.msg4_lbl, 1: 180, 2: 320, 3: 460,
                        4: 600}
        self.bg.setPixmap(QtGui.QPixmap(f'{self.local_img}\\bg.png'))
        self.close_btn.clicked.connect(self.start_threading)
        self.show_btn.clicked.connect(self.show_ui)
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        widget = self.geometry()
        x = screen.width() - widget.width()
        self.move(x, 40)

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
        window.show()
        self.hide()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    n_dialog = Notification()
    window.show()
    sys.exit(app.exec_())