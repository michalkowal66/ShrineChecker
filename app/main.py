from PyQt5 import QtCore, QtGui, QtWidgets
from templates.sc_ui import Ui_MainWindow
from bs4 import BeautifulSoup as bs
import requests
import lxml
import os
import json
import shutil
from jsonschema import validate
from rsc import rsc

# TODO add missing button actions
# TODO implement signals for loading data
# TODO try to modify data structure to make use of Qt objects naming
# TODO add shrine refresh logic


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

        # Set up user interface
        self.setupUi(self)

        # Set up thread workers
        self.loader = Loader(task="init")
        self.loader.finish_signal.connect(lambda: self.done_btn.setDisabled(False))
        self.progress_signal.connect(self.update_progress)

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
                "container": self.date_lbl
            }
        }
        self.perks = {
            "perks_list": {"val": [], "container": self.perks_combo}
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
        # Create schemes for json validation
        self.json_schemes = {
            "settings": {
                "type": "object",
                "properties": {
                    "minimize": {"type": "boolean"},
                    "startup": {"type": "boolean"},
                    "notification": {"type": "string"},
                    "refresh": {"type": "string"}
                }
            },
            "shrine": {
                "type": "object",
                "properties": {
                    "shrine_perk1": {"type": "string"},
                    "shrine_perk2": {"type": "string"},
                    "shrine_perk3": {"type": "string"},
                    "shrine_perk4": {"type": "string"},
                    "download_date": {"type": "string"}
                }
            },
            "perks": {
                "type": "object",
                "properties": {
                    "perks_list": {"type": "array"}
                }
            },
            "user_perks": {
                "type": "object",
                "properties": {
                    "perks_list": {"type": "array"}
                }
            }
        }
        # Initialize dictionary for storing loaded local data before validation
        self.local_data = {}
        # Initialize all data to user interface
        self.initial_check()

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

        # Disable done button on loading screen
        self.done_btn.setDisabled(True)

        # Connect navigation buttons with appropriate stackedWidget pages
        self.settings_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.back_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.done_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        # Connect functional buttons with appropriate functions
        self.save_btn.clicked.connect(lambda: self.update_globally(target="settings"))
        self.add_btn.clicked.connect(self.add_perk)
        self.remove_btn.clicked.connect(self.remove_perk)
        self.reset_btn.clicked.connect(self.reload_perks)
        self.reload_btn.clicked.connect(lambda: self.reload_shrine(force=True))

    def initial_check(self):
        # Check whether local directory exists
        if not os.path.exists(self.local_dir):
            self.stackedWidget.setCurrentIndex(0)
            self.show()
            # Try to create local directory via loader thread
            self.loader.start()
            # self.prepare_local_dir()
        else:
            self.initialize_data()


    def initialize_data(self):
        # Try to read local files to self.local_data
        self.read_local_files()
        # Try to read data with schemes
        self.verify_local_files()
        # Try to load data to self.data_dict
        self.load_local_data()
        # Try to update containers on main page, settings page, and check shrine
        self.update_main_containers()
        self.update_settings_containers()
        self.check_shrine()
        self.show()

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
            self.progress_signal.emit(1, 1, "Downloaded shrine")
            self.progress_signal.emit(0, 1, "Downloading survivor and killer perks")
            perks = self.get_perks()
            self.load_perks(perks=perks)
            self.progress_signal.emit(1, 1, "Survivor and killer perks")

            # Save settings data to json files in created directory
            self.progress_signal.emit(0, 1, "Saving data in the local directory")
            self.save_data(target="all")
            self.progress_signal.emit(0, 1, "Saved data in the local directory")

            # Download perk images to local directory
            self.progress_signal.emit(0, 1, "Downloading perk images")
            self.download_imgs(self.local_img_dir, perks_tuple=perks)
            self.progress_signal.emit(1, 1, "Application is ready!")
        except:
            # On error delete local directory and display error message
            if os.path.exists(self.local_dir):
                shutil.rmtree(self.local_dir)
            self.error_occured("Wasn't able to create a local directory properly")
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
            # On error display error message
            self.error_occured("Could not read local data")
            return False
        else:
            return True

    def verify_local_files(self):
        # Call validator on each read dictionary in self.local_data
        if all([self.verify_json(self.local_data[key], key) for key in self.local_data]):
            return True
        # On error display error message
        self.error_occured("Error while validating json")
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
            self.error_occured("Wasn't able to update main ui containers")
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
            self.error_occured("Wasn't able to update settings containers")
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
            else:
                # Ensure frame is hidden when no match
                perk["frame"].setHidden(True)
                # Restore previous perk name color
                perk["container"].setStyleSheet("")

    def error_occured(self, message):
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
            self.shrine[f"shrine_perk{_}"]["val"] = shrine[_-1]
        self.shrine["download_date"]["val"] = "DATE_PLACEHOLDER"

    def load_perks(self, perks):
        # Loads fetched perks to the self.perks dict
        perks_stripped = [perk_tuple[0] for perk_tuple in perks]
        self.perks["perks_list"]["val"] = perks_stripped

    def get_shrine(self, source=1):
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

    def get_perks(self):
        perks_url = "https://deadbydaylight.gamepedia.com/Perks"
        perks = []

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

                perks.append((perk_name, perk_img_url))

        return perks

    def download_imgs(self, directory, perks_tuple):
        for tuple in perks_tuple:
            perk, img_url = tuple
            self.progress_signal.emit(perks_tuple.index(tuple) + 1, len(perks_tuple), f"Downloading {perk}")
            if ":" in perk:
                perk = perk.replace(":", "_")
            with open(f'{directory}/{perk}.png', 'wb') as f:
                img = requests.get(img_url)
                f.write(img.content)

    def reload_perks(self):
        perks = self.get_perks()
        self.load_perks(perks)
        self.perks_combo.clear()
        self.update_main_containers("perks")
        self.save_data("perks")

    def reload_shrine(self, force=False):
        if not force:
            # time logic
            pass
        shrine = self.get_shrine()
        self.load_shrine(shrine)
        self.update_main_containers("shrine")
        self.save_data("shrine")

    def update_progress(self, task, total_tasks, message):
        self.progress_bar.setValue(100.0 * task / total_tasks)
        self.msg_lbl.setText(message)


class Loader(QtCore.QThread):
    finish_signal = QtCore.pyqtSignal()

    def __init__(self, task, parent=None):
        super().__init__(parent)
        self.task = task

    @QtCore.pyqtSlot()
    def run(self):
        if self.task == "init":
            window.prepare_local_dir()
            window.initialize_data()
            window.done_btn.setDisabled(False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
