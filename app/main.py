from PyQt5 import QtCore, QtGui, QtWidgets
from templates.sc_ui import Ui_MainWindow
import os
import json
import shutil
from jsonschema import validate
from rsc import rsc


# TODO add scraper
# TODO add missing button actions
# TODO implement signals for loading data


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
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

        # Create data dictionaries
        self.settings = {
            "minimize": {"val": True, "container": self.tray_check},
            "startup": {"val": True, "container": self.startup_check},
            "notification": {"val": "2", "container": self.notif_combo},
            "refresh": {"val": "2", "container": self.refr_combo}
        }
        self.shrine = {
            "perk1": {"val": "perk1_name", "container": self.perk1_lbl, "frame": self.perk1_frame},
            "perk2": {"val": "perk2_name", "container": self.perk2_lbl, "frame": self.perk2_frame},
            "perk3": {"val": "perk3_name", "container": self.perk3_lbl, "frame": self.perk3_frame},
            "perk4": {"val": "perk4_name", "container": self.perk4_lbl, "frame": self.perk4_frame},
            "download_date": {"val": "dd.mm.yyyy hh:mm", "container": self.date_lbl}
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
                    "perk1": {"type": "string"},
                    "perk2": {"type": "string"},
                    "perk3": {"type": "string"},
                    "perk4": {"type": "string"},
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
        self.init_data()


    def setupUi(self, MainWindow):
        super().setupUi(self)

        # Set backgrounds
        self.bg_0.setPixmap(QtGui.QPixmap(':/Background/img/bg_0.png'))
        self.bg_1.setPixmap(QtGui.QPixmap(':/Background/img/bg_1.png'))
        self.bg_2.setPixmap(QtGui.QPixmap(':/Background/img/bg_2.png'))
        self.bg_3.setPixmap(QtGui.QPixmap(':/Background/img/bg_2.png'))

        # Load shrine perks frame images
        for _ in range(1,5):
            frame = self.main_page.findChild(QtWidgets.QLabel, f"perk{_}_frame")
            frame.setPixmap(QtGui.QPixmap(':/Decorations/img/frame.png'))
            frame.setHidden(True)

        # Set settings button icon
        self.settings_btn.setIcon(QtGui.QIcon(':/Decorations/img/settings.png'))

        # Set application window icon
        self.setWindowIcon(QtGui.QIcon(':/Icon/img/icon.ico'))

        # Connect navigation buttons with appropriate stackedWidget pages
        self.settings_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.back_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        # Connect functional buttons with appropriate functions
        self.save_btn.clicked.connect(lambda: self.update_globally(target="settings"))
        self.add_btn.clicked.connect(self.add_perk)
        self.remove_btn.clicked.connect(self.remove_perk)

    def init_data(self):
        # Check whether local directory exists
        if not os.path.exists(self.local_dir):
            # TODO loading screen
            # Try to create local directory
            if not self.prepare_local_dir():
                return False
        # Try to read local files to self.local_data
        if self.read_local_files():
            # Try to read data with schemes
            if self.verify_local_files():
                # Try to load data to self.data_dict
                if self.load_local_data():
                    # Try to update containers on main page, settings page, and check shrine
                    self.update_main_containers()
                    self.update_settings_containers()
                    self.check_shrine()
                    return True
        return False

    def prepare_local_dir(self):
        try:
            # Create local folders
            os.mkdir(self.local_dir)
            os.mkdir(self.local_img_dir)

            # Save settings data to json files in created directory
            self.save_data(target="all")
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
        if all([self.verifyJson(self.local_data[key], key) for key in self.local_data]):
            return True
        # On error display error message
        self.error_occured("Error while validating json")
        return False

    def verifyJson(self, jsonDict, scheme):
        try:
            # Call validate from jsonschema with data dictionary and appropriate scheme
            validate(instance=jsonDict, schema=self.json_schemes[scheme])
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
                target = [self.shrine, self.perks, self.user_perks]
            for data_dict in target:
                for key in data_dict:
                    value = data_dict[key]["val"]
                    container = data_dict[key]["container"]
                    self.load_value(container, value)
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
        # Update data_dict and flies in local directory
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
            else:
                # Ensure frame is hidden when no match
                perk["frame"].setHidden(True)

    def error_occured(self, message):
        # Change stackedWidget page to error page
        self.stackedWidget.setCurrentIndex(3)
        # Display error message
        self.error_msg_lbl.setText(message)

    def load_value(self, container, value):
        # Load containers with data - used for main page
        if type(container) == QtWidgets.QLabel:
            # Catch image labels
            if container.objectName().endswith("img"):
                # Load perk image
                container.setPixmap(QtGui.QPixmap(f"{self.local_img_dir}\\{value}"))
                container.setScaledContents(True)
            else:
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
                containerJson = json.dumps(container, indent=4)
                f.write(containerJson)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
