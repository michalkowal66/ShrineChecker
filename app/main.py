from PyQt5 import QtCore, QtGui, QtWidgets
from templates.sc_ui import Ui_MainWindow
from templates.sc_notification import Ui_NotificationTemplate
from templates.sc_dialog import Ui_Dialog
from bs4 import BeautifulSoup as bs
from jsonschema import validate
from schemes import schemes
from rsc import rsc
from datetime import datetime, timedelta
from time import sleep
import dateutil.relativedelta as REL
import requests
import lxml
import os
import json
import shutil
import pythoncom
import winshell
import win32com.client


# TODO add screen with all perks and descriptions
# TODO find better way to catch exceptions
# TODO move error messages to separate file
# TODO try to modify data structure to make use of Qt objects naming


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    progress_signal = QtCore.pyqtSignal(int, int, str)

    def __init__(self):
        super().__init__()
        # Prepare path variables
        self.local_dir = os.path.expanduser('~') + '\\Documents\\ShrineChecker'
        self.local_img_dir = self.local_dir + '\\img'
        self.settings_path = self.local_dir + "\\settings.json"
        self.shrine_path = self.local_dir + "\\shrine.json"
        self.perks_path = self.local_dir + "\\perks.json"
        self.user_perks_path = self.local_dir + "\\user_perks.json"

        # Indicate whether app was run first time
        self.initial_run = None

        # Initialize tray icon
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)

        # Set up thread workers and connect signals with methods
        self.loader = Loader("first_run")
        self.progress_signal.connect(self.update_progress)

        self.refresher = Refresher()
        self.refresher.refresh.connect(self.reload_shrine)
        self.refresher.refresh.connect(self.refresher.start)

        self.notifier = Notifier()
        self.notifier.notify.connect(self.notify)
        self.notifier.notify.connect(self.notifier.start)

        self.reloader = Loader("reload")

        # Set up user interface
        self.setupUi(self)

        # Create data dictionaries
        self.settings = {
            "minimize": {"val": True, "container": self.tray_check},
            "startup": {"val": True, "container": self.startup_check},
            "notification": {"val": "2", "container": self.notif_combo},
            "refresh": {"val": "2", "container": self.refr_combo}
        }
        self.shrine = {
            "shrine_perk1": {
                "val": "perk1_name",
                "container": self.perk1_lbl,
                "img_container": self.perk1_img,
                "frame": self.perk1_frame
            },
            "shrine_perk2": {
                "val": "perk2_name",
                "container": self.perk2_lbl,
                "img_container": self.perk2_img,
                "frame": self.perk2_frame
            },
            "shrine_perk3": {
                "val": "perk3_name",
                "container": self.perk3_lbl,
                "img_container": self.perk3_img,
                "frame": self.perk3_frame
            },
            "shrine_perk4": {
                "val": "perk4_name",
                "container": self.perk4_lbl,
                "img_container": self.perk4_img,
                "frame": self.perk4_frame
            },
            "download_date": {
                "val": "dd.mm.yyyy hh:mm",
                "container": self.datedl_lbl
            },
            "refresh_date": {
                "val": "dd.mm.yyyy",
                "container": self.dateref_lbl
            }
        }
        self.perks = {
            "perks_list": {"val": [], "container": self.perks_combo},
            "descriptions": {"val": {}, "container": None}
        }
        self.user_perks = {
            "perks_list": {"val": [], "container": self.perks_list}
        }

        # Aggregate data dictionaries into one dictionary
        self.data_dict = {
            "settings": {
                "path": self.settings_path,
                "data": self.settings
            },
            "shrine": {
                "path": self.shrine_path,
                "data": self.shrine
            },
            "perks": {
                "path": self.perks_path,
                "data": self.perks
            },
            "user_perks": {
                "path": self.user_perks_path,
                "data": self.user_perks
            },
        }

        # Load schemes for json validation
        self.json_schemes = schemes.validation_schemes

        # Initialize dictionary for storing loaded local data before validation
        self.local_data = {}

    def setupUi(self, MainWindow):
        super().setupUi(self)

        # Set backgrounds
        self.bg_0.setPixmap(QtGui.QPixmap(':/Background/img/bg_0.png'))
        self.bg_1.setPixmap(QtGui.QPixmap(':/Background/img/bg_1.png'))
        self.bg_2.setPixmap(QtGui.QPixmap(':/Background/img/bg_2.png'))
        self.bg_3.setPixmap(QtGui.QPixmap(':/Background/img/bg_2.png'))

        # Load shrine perks frame images
        for _ in range(1, 5):
            frame = self.main_page.findChild(QtWidgets.QLabel, f"perk{_}_frame")
            frame.setPixmap(QtGui.QPixmap(':/Decorations/img/frame.png'))
            frame.setHidden(True)

        # Prepare loading screen
        self.progress_bar.setValue(0)
        self.msg_lbl.setText("Starting work...")

        # Set settings button icon
        self.settings_btn.setIcon(QtGui.QIcon(':/Decorations/img/settings.png'))

        # Set application window icon
        self.setWindowIcon(QtGui.QIcon(':/Icon/img/icon.ico'))

        # Set tray icon
        self.tray_icon.setIcon(QtGui.QIcon(':/Icon/img/icon.ico'))

        # Prepare tray context menu actions
        show_action = QtWidgets.QAction("Show", self)
        quit_action = QtWidgets.QAction("Exit", self)
        hide_action = QtWidgets.QAction("Hide", self)
        show_action.triggered.connect(self.show_ui)
        hide_action.triggered.connect(self.hide_ui)
        quit_action.triggered.connect(QtCore.QCoreApplication.quit)
        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)

        # Set up context menu
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # Connect navigation buttons with appropriate stackedWidget pages
        self.settings_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.back_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.done_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.error_back_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        # Connect functional buttons with appropriate functions
        self.save_btn.clicked.connect(self.save_settings)
        self.add_btn.clicked.connect(self.add_perk)
        self.remove_btn.clicked.connect(self.remove_perk)
        self.reset_btn.clicked.connect(self.reloader.start)
        self.reload_btn.clicked.connect(lambda: self.reload_shrine(force=True))

        # Disable button on error screen after pressing
        self.error_back_btn.clicked.connect(lambda: self.error_back_btn.setEnabled(False))

        # Disable button on loading screen after pressing
        self.done_btn.clicked.connect(lambda: self.done_btn.setEnabled(False))

        # Connect settings container with function catching change of state
        self.startup_check.stateChanged.connect(lambda: self.save_btn.setEnabled(True))
        self.tray_check.stateChanged.connect(lambda: self.save_btn.setEnabled(True))
        self.refr_combo.currentIndexChanged.connect(lambda: self.save_btn.setEnabled(True))
        self.notif_combo.currentIndexChanged.connect(lambda: self.save_btn.setEnabled(True))

        # Add event filter to shrine perks imgs
        for perk_img in [self.main_page.findChild(QtWidgets.QLabel, f"perk{i}_img") for i in range(1,5)]:
            perk_img.installEventFilter(self)

    def initial_check(self):
        # Check whether local directory exists
        if not os.path.exists(self.local_dir):
            self.initial_run = True
            self.stackedWidget.setCurrentIndex(0)
            self.show()
            # Try to create local directory via loader thread
            self.loader.start()
        else:
            self.initial_run = False
            self.initialize_data()

    def initialize_data(self):
        # Try to read local files to self.local_data
        self.progress_signal.emit(0, 1, "Initializing app information")
        if not self.read_local_files():
            # On error display error message
            self.error_occured("data reading", "Could not read local data")
            return False
        # Try to verify data with schemes
        if not self.verify_local_files():
            self.error_occured("files verification", "Some local files didn't pass the verification.")
            return False
        # Try to load data to self.data_dict
        if not self.load_local_data():
            self.error_occured("data loading", "Couldn't load local data.")
            return False
        # Try to update containers on main page, settings page, and check shrine
        self.update_main_containers()
        self.update_settings_containers()
        self.reload_shrine()
        self.check_shrine()
        # Disable save button on settings screen
        self.save_btn.setEnabled(False)
        self.progress_signal.emit(1, 1, "Application is ready!")
        # Enable button to proceed to main app screen
        if self.initial_run:
            self.done_btn.setEnabled(True)
        self.show_ui()

    def prepare_local_dir(self):
        try:
            # Create local folders
            self.progress_signal.emit(0, 1, "Creating local directory")
            os.mkdir(self.local_dir)
            os.mkdir(self.local_img_dir)
            self.progress_signal.emit(1, 1, "Created local directory")

            # Download and load shrine and perks to self.shrine and self.perks dicts
            self.progress_signal.emit(0, 1, "Downloading Shrine of Secrets")
            shrine = self.get_shrine()
            self.load_shrine(shrine=shrine)
            self.progress_signal.emit(1, 1, "Downloaded Shrine of Secrets")
            self.progress_signal.emit(0, 1, "Downloading survivor and killer perks")
            perks = self.get_perks()
            self.load_perks(perks=perks)
            self.progress_signal.emit(1, 1, "Downloaded survivor and killer perks")

            # Save settings data to json files in created directory
            self.progress_signal.emit(0, 1, "Saving data in the local directory")
            self.save_data(target="all")
            self.progress_signal.emit(0, 1, "Saved data in the local directory")

            # Download perk images to local directory
            self.progress_signal.emit(0, 1, "Downloading perk images")
            self.download_imgs(self.local_img_dir, perks_tuple=perks["perks"])
            self.progress_signal.emit(1, 1, "Downloaded perk images")
        except:
            # On error delete local directory and display error message
            if os.path.exists(self.local_dir):
                shutil.rmtree(self.local_dir)
            self.error_occured("creating directory", "Wasn't able to create a local directory properly")
        else:
            return True

    def read_local_files(self):
        try:
            # Read information from local json files to self.local_data dictionary
            for target_type in self.data_dict:
                path = self.data_dict[target_type]["path"]
                with open(path, "r") as f:
                    json_content = json.load(f)
                    self.local_data[target_type] = json_content
        except:
            return False
        else:
            return True

    def verify_local_files(self):
        # Call validator on each read dictionary in self.local_data
        if all([self.verify_json(self.local_data[key], key) for key in self.local_data]):
            return True
        return False

    def verify_json(self, json_dict, scheme):
        try:
            # Call validate from jsonschema with data dictionary and appropriate scheme
            validate(instance=json_dict, schema=self.json_schemes[scheme])
        except:
            return False
        else:
            return True

    def load_local_data(self, target="all"):
        try:
            # Load self.local_data dictionary to self.data_dict
            if target == "all":
                for target_type in self.data_dict:
                    for key in self.data_dict[target_type]["data"]:
                        self.data_dict[target_type]["data"][key]["val"] = self.local_data[target_type][key]
        except:
            return False
        else:
            return True

    def update_main_containers(self, target="ui"):
        try:
            # Update content of application containers in main screen using loaded data
            if target == "ui":
                targets = [self.shrine, self.perks, self.user_perks]
            else:
                targets = [self.data_dict[target]["data"]]
            for data_dict in targets:
                for key in data_dict:
                    self.load_value(data_dict, key)
        except:
            # On error display error message
            self.error_occured("updating main containers", "Wasn't able to update main ui containers")
            return False
        else:
            return True

    def update_settings_containers(self):
        try:
            # Update content of application containers in settings screen using loaded data
            for key in self.settings:
                value = self.settings[key]["val"]
                container = self.settings[key]["container"]
                self.set_value(container, value)
        except:
            # On error display error message
            self.error_occured("updating settings containers", "Wasn't able to update settings containers")
            return False
        else:
            return True

    def update_globally(self, target):
        # Update data_dict and files in local directory with data in container
        # e.g. load user perks to data dict and save to file
        for key in self.data_dict[target]["data"]:
            container = self.data_dict[target]["data"][key]["container"]
            self.data_dict[target]["data"][key]["val"] = self.read_value(container=container)
        self.save_data(target=target)

    def add_perk(self):
        # Add selected in QComboBox perk to QListWidget
        list_items = [self.perks_list.item(x).text() for x in range(self.perks_list.count())]
        perk = self.perks_combo.currentText()
        if perk not in list_items and len(perk) > 0:
            self.perks_list.addItem(perk)
            # Update data_dict and local files
            self.update_globally("user_perks")
            # Check shrine for matches
            self.check_shrine()

    def remove_perk(self):
        # Remove selected item in QListWidget
        selected_item = self.perks_list.currentItem()
        if selected_item is not None:
            self.perks_list.takeItem(self.perks_list.row(selected_item))
            # Update data_dict and local files
            self.update_globally("user_perks")
            # Check shrine for matches
            self.check_shrine()

    def check_shrine(self):
        # Check for matches between shrine perks and user perks
        matches = []
        list_items = [self.perks_list.item(x).text() for x in range(self.perks_list.count())]
        for perk_key in self.shrine:
            perk = self.shrine[perk_key]
            # Omit key containing download date
            if perk.get("frame") is None:
                continue
            if perk["val"] in list_items:
                # Show frame on match
                perk["frame"].setHidden(False)
                # Apply white color to perk name
                perk["container"].setStyleSheet("color: white")
                # Add matching perk to matches list
                matches.append(perk["val"])
            else:
                # Ensure frame is hidden when no match
                perk["frame"].setHidden(True)
                # Restore previous perk name color
                perk["container"].setStyleSheet("")
        return matches

    def error_occured(self, source ,message):
        if self.isHidden():
            self.show()
        if source == "network" and not self.initial_run:
            self.error_back_btn.setEnabled(True)
        # Change stackedWidget page to error page
        self.stackedWidget.setCurrentIndex(3)
        # Display error message
        self.error_msg_lbl.setText(message)

    def load_value(self, data_dict, key):
        value = data_dict[key]["val"]
        container = data_dict[key]["container"]
        img_container = None
        if key.startswith("shrine"):
            img_container = data_dict[key]["img_container"]

        # Load containers with data - used for main page
        if type(container) == QtWidgets.QLabel:
            # Catch image labels
            if img_container is not None:
                img_filename = value.replace(":", "_")
                # Load perk image
                img_container.setPixmap(QtGui.QPixmap(f"{self.local_img_dir}\\{img_filename}"))
                img_container.setScaledContents(True)
            # Load perk name
            container.setText(value)
        elif type(container) in [QtWidgets.QComboBox, QtWidgets.QListWidget]:
            # Add items to ComboBox or ListWidget
            container.addItems(value)

    def set_value(self, container, value):
        # Select proper state/data in containers - used for settings page
        if type(container) == QtWidgets.QCheckBox:
            # Set CheckBox checked/unchecked
            container.setChecked(value)
        elif type(container) == QtWidgets.QComboBox:
            # Set text in ComboBox
            container.setCurrentText(str(value))

    def read_value(self, container):
        # Reads current value from a container
        if type(container) == QtWidgets.QCheckBox:
            return container.isChecked()
        elif type(container) == QtWidgets.QListWidget:
            return [container.item(x).text() for x in range(container.count())]
        elif type(container) == QtWidgets.QComboBox:
            return container.currentText()

    def save_data(self, target):
        # Saves data to file
        if target == "all":
            targets = self.data_dict.keys()
        else:
            targets = [target]

        for target_type in targets:
            path = self.data_dict[target_type]["path"]
            target_data = self.data_dict[target_type]["data"]
            container = {key: target_data[key]["val"] for key in target_data}
            with open(path, 'w') as f:
                container_json = json.dumps(container, indent=4)
                f.write(container_json)

    def load_shrine(self, shrine):
        # Loads fetched shrine to the self.shrine dict
        for _ in range(1, 5):
            self.shrine[f"shrine_perk{_}"]["val"] = shrine["perks"][_-1]
        self.shrine["download_date"]["val"] = shrine["download_date"]
        self.shrine["refresh_date"]["val"] = shrine["refresh_date"]

    def load_perks(self, perks):
        # Loads fetched perks to the self.perks dict
        perks_stripped = [perk_tuple[0] for perk_tuple in perks["perks"]]
        self.perks["perks_list"]["val"] = perks_stripped
        self.perks["descriptions"]["val"] = perks["descriptions"]

    def get_shrine(self, source=2):
        shrine_urls = {
            1: "https://deadbydaylight.fandom.com/wiki/Dead_by_Daylight_Wiki",
            2: "https://deadbydaylight.fandom.com/wiki/Shrine_of_Secrets"
        }
        shrine = {
            "perks": [],
            "download_date": "DOWNLOAD DATE",
            "refresh_date": "REFRESH DATE"
        }
        today = datetime.now()
        rd = REL.relativedelta(days=1, weekday=REL.WE)
        next_refresh = today + rd

        request = requests.get(shrine_urls[source])
        soup = bs(request.content, "lxml")

        shrine_table = soup.find("table", {"class": "sosTable"}).find("tbody").find_all("tr")

        for row in shrine_table:
            cell = row.find("td")
            if cell is not None:
                perk = cell.get_text(strip=True)
                shrine["perks"].append(perk)
        shrine["download_date"] = str(today.strftime('%d/%m/%Y %H:%M'))
        shrine["refresh_date"] = str(next_refresh.strftime('%d/%m/%Y'))

        return shrine

    def get_perks(self):
        perks_url = "https://deadbydaylight.gamepedia.com/Perks"
        perks = {"perks": [],
                 "descriptions": {}}

        request = requests.get(perks_url)
        soup = bs(request.content, "lxml")

        tables = soup.find_all("table", {"class": "wikitable sortable"})
        survivor_table, killer_table = [table.find("tbody").find_all("tr") for table in tables]
        for table in [survivor_table, killer_table]:
            for row in table[1:]:
                if row.contents[7].get_text(strip=True) == "All":
                    continue
                perk_img_url = row.contents[1].find("a").find("img")["src"]
                perk_name = row.contents[3].find("a").get_text(strip=True)
                perk_description = row.contents[5].text

                perks["perks"].append((perk_name, perk_img_url))
                perks["descriptions"][perk_name] = perk_description

        return perks

    def download_imgs(self, directory, perks_tuple):
        try:
            for tuple in perks_tuple:
                perk, img_url = tuple
                self.progress_signal.emit(perks_tuple.index(tuple) + 1, len(perks_tuple), f"Downloading {perk}")
                if ":" in perk:
                    perk = perk.replace(":", "_")
                with open(f'{directory}/{perk}.png', 'wb') as f:
                    img = requests.get(img_url)
                    f.write(img.content)
        except:
            self.error_occured("download", "Error while downloading perk images. Check internet connection and try again.")

    def reload_perks(self):
        self.progress_signal.emit(0, 1, "Downloading perk images")
        self.stackedWidget.setCurrentIndex(0)
        try:
            perks = self.get_perks()
        except:
            self.error_occured("network", "Error while downloading perks. Check internet connection and try again.")
        else:
            self.download_imgs(self.local_img_dir, perks_tuple=perks["perks"])
            self.load_perks(perks)
            self.perks_combo.clear()
            self.update_main_containers("perks")
            self.update_main_containers("shrine")
            self.save_data("perks")
            self.progress_signal.emit(1, 1, "Perks reloaded")
            self.done_btn.setEnabled(True)

    def reload_shrine(self, force=False):
        today = datetime.now().date()
        next_refresh = datetime.strptime(self.shrine["refresh_date"]["val"], '%d/%m/%Y')
        days_to_refresh = ((next_refresh.date()+timedelta(days=1)) - today).days

        if not force:
            if days_to_refresh > 1 and days_to_refresh < 7:
                return False
        try:
            shrine = self.get_shrine()
        except:
            self.error_occured("network", "Error while downloading Shrine of Secrets. Check internet connection and try again.")
        else:
            self.load_shrine(shrine)
            self.update_main_containers("shrine")
            self.save_data("shrine")

    def update_progress(self, task, total_tasks, message):
        self.progress_bar.setValue(int(100*task/total_tasks))
        self.msg_lbl.setText(message)

    def closeEvent(self, event):
        conditions = [self.isHidden() == True,
                      not self.tray_check.isChecked(),
                      self.stackedWidget.currentIndex() == 3]
        if any(conditions):
            event.accept()
        else:
            event.ignore()
            self.hide_ui()

    def toggle_autostart(self):
        pythoncom.CoInitialize()
        startup = winshell.startup()
        shortcut_path = os.path.join(startup, 'SC.lnk')
        if self.startup_check.isChecked():
            target = sys.argv[0]
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = target
            shortcut.WindowStyle = 7
            shortcut.save()
        else:
            if os.path.isfile(shortcut_path):
                os.remove(shortcut_path)

    def notify(self):
        matches = self.check_shrine()
        if len(matches) == 0:
            print("No matches")
        else:
            if notification.isHidden():
                notification.setup_notification(matches)
                notification.show()

    def save_settings(self):
        self.toggle_autostart()
        if self.refr_combo.currentText() != self.settings["refresh"]["val"]:
            QtCore.QTimer.singleShot(2000, lambda: self.refresher.start())
        self.update_globally(target="settings")
        self.save_btn.setEnabled(False)

    def show_ui(self):
        self.reload_shrine()
        self.refresher.start()
        if self.isHidden():
            self.show()

    def hide_ui(self):
        self.hide()
        self.notifier.start()

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.Enter:
            label_name = object.objectName().replace("_img", "_lbl")
            perk_name = self.main_page.findChild(QtWidgets.QLabel, label_name).text()
            description = self.perks["descriptions"]["val"][perk_name]
            dialog.prepare_dialog(object, description)
            dialog.show()
            return True
        elif event.type() == QtCore.QEvent.Leave:
            dialog.hide()
        return False

class Notification(QtWidgets.QDialog, Ui_NotificationTemplate):
    def __init__(self):
        super().__init__()
        self.local_dir = os.path.expanduser('~') + '\\Documents\\ShrineChecker'
        self.local_img_dir = self.local_dir + '\\img'
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_ShowWithoutActivating)

    def setupUi(self, Dialog):
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon(':/Icon/img/icon.ico'))
        self.bg.setPixmap(QtGui.QPixmap(':/Background/img/bg_1.png'))

        self.close_btn.clicked.connect(window.notifier.start)
        self.close_btn.clicked.connect(self.hide)
        self.show_btn.clicked.connect(window.show_ui)
        self.show_btn.clicked.connect(self.hide)

        screen = QtWidgets.QDesktopWidget().screenGeometry()
        widget = self.geometry()
        x = screen.width() - widget.width()
        self.move(x, 40)

        frames = [label for label in self.findChildren(QtWidgets.QLabel) if label.objectName().startswith("frame")]
        for frame in frames:
            frame.setPixmap(QtGui.QPixmap(':/Decorations/img/frame.png'))
            frame.setScaledContents(True)

    def setup_notification(self, matches):
        self.resize(350, 180+(len(matches)-1)*140)
        for _ in range(len(matches)):
            img = self.findChild(QtWidgets.QLabel, f"img{_ + 1}")
            img.setPixmap(QtGui.QPixmap(f"{self.local_img_dir}\\{matches[_]}.png"))
            img.setScaledContents(True)
            perk_name = self.findChild(QtWidgets.QLabel, f"perk{_ + 1}_lbl")
            perk_name.setText(matches[_])
            message = self.findChild(QtWidgets.QLabel, f"msg{_ + 1}_lbl")
            message.setText("is now available!")


class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_ShowWithoutActivating)

    def setupUi(self, Dialog):
        super().setupUi(self)
        self.bg.setPixmap(QtGui.QPixmap(':/Background/img/bg_1.png'))

    def prepare_dialog(self, source, description):
        if description.endswith("\n"):
            description = description[:-2]
        elif description.endswith("\n\n"):
            description = description[:-4]
        # TODO think of alternative to if statement and while loop
        self.description_lbl.setText(description)
        self.description_lbl.adjustSize()
        new_height = 50+self.description_lbl.height()
        self.resize(520, new_height)
        self.bg.resize(520, new_height)
        dialog_x = int(window.x()+source.x()-(self.width()/2-50))
        dialog_y = int(window.y()+source.y()+175)
        self.move(dialog_x, dialog_y)


class Loader(QtCore.QThread):
    def __init__(self, role):
        super().__init__()
        self.role = role

    def run(self):
        if self.role == "first_run":
            window.prepare_local_dir()
            window.initialize_data()
        elif self.role == "reload":
            window.reload_perks()


class Refresher(QtCore.QThread):
    refresh = QtCore.pyqtSignal()

    def run(self):
        print("Starting refreshing")
        refresh_interval = int(window.settings["refresh"]["val"])
        for _ in range(refresh_interval*60*60):
            sleep(1)
            check_interval = int(window.settings["refresh"]["val"])
            conditions = [window.isHidden(),
                          refresh_interval != check_interval,
                          window.stackedWidget.currentIndex() == 3]
            if any(conditions):
                print("Refresher thread interrupted")
                return None
        self.refresh.emit()
        print("Ending refreshing thread")


class Notifier(QtCore.QThread):
    notify = QtCore.pyqtSignal()

    def run(self):
        print("Starting notification thread")
        notification_interval = int(window.settings["notification"]["val"])
        for _ in range(notification_interval*60*60):
            sleep(1)
            if not window.isHidden():
                print("Notification thread interrupted")
                return None
        self.notify.emit()
        print("Ending notification thread")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    notification = Notification()
    dialog = Dialog()
    window.initial_check()
    sys.exit(app.exec_())

