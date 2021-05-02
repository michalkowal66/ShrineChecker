from PyQt5 import QtCore, QtGui, QtWidgets
from templates.sc_ui import Ui_MainWindow
import os
import json
import shutil
from jsonschema import validate
from rsc import rsc


# TODO add scraper
# TODO add data loader method
# TODO add missing button actions
# TODO create data structure
# TODO implement signals for loading data


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.local_dir = os.path.expanduser('~') + '\\Documents\\ShrineChecker'
        self.local_img_dir = self.local_dir + '\\img'
        self.settings_path = self.local_dir + "\\settings.json"
        self.shrine_path = self.local_dir + "\\shrine.json"
        self.perks_path = self.local_dir + "\\perks.json"
        self.user_perks_path = self.local_dir + "\\user_perks.json"

        self.setupUi(self)

        self.data_dict = {
            "settings": {
                "path": self.settings_path,
                "data": {
                    "minimize": {"val": True, "container": self.tray_check},
                    "startup": {"val": True, "container": self.startup_check},
                    "notification": {"val": 2, "container": self.notif_combo},
                    "refresh": {"val": 2, "container": self.refr_combo}
                }
            },
            "shrine": {
                "path": self.shrine_path,
                "data": {
                    "perk1_name": {"val": "perk1_name", "container": self.perk1_lbl},
                    "perk1_img": {"val": "perk1_img", "container": self.perk1_img},
                    "perk2_name": {"val": "perk2_name", "container": self.perk2_lbl},
                    "perk2_img": {"val": "perk2_img", "container": self.perk2_img},
                    "perk3_name": {"val": "perk3_name", "container": self.perk3_lbl},
                    "perk3_img": {"val": "perk4_img", "container": self.perk3_img},
                    "perk4_name": {"val": "perk4_name", "container": self.perk4_lbl},
                    "perk4_img": {"val": "perk4_img", "container": self.perk4_img},
                    "download_date": {"val": "dd.mm.yyyy hh:mm", "container": self.date_lbl}
                }
            },
            "perks": {
                "path": self.perks_path,
                "data": {
                    "perks_list": {"val": [], "container": self.perks_combo}
                }
            },
            "user_perks": {
                "path": self.user_perks_path,
                "data": {
                    "perks_list": {"val": [], "container": self.perks_list}
                }
            },
        }
        self.json_schemes = {
            "settings": {
                "type": "object",
                "properties": {
                    "minimize": {"type": "boolean"},
                    "startup": {"type": "boolean"},
                    "notification": {"type": "integer"},
                    "refresh": {"type": "integer"}
                }
            },
            "shrine": {
                "type": "object",
                "properties": {
                    "perk1_name": {"type": "string"},
                    "perk1_img": {"type": "string"},
                    "perk2_name": {"type": "string"},
                    "perk2_img": {"type": "string"},
                    "perk3_name": {"type": "string"},
                    "perk3_img": {"type": "string"},
                    "perk4_name": {"type": "string"},
                    "perk4_img": {"type": "string"},
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
        self.local_data = {}

        self.init_data()


    def setupUi(self, MainWindow):
        super().setupUi(self)

        self.bg_0.setPixmap(QtGui.QPixmap(':/Background/img/bg_0.png'))
        self.bg_1.setPixmap(QtGui.QPixmap(':/Background/img/bg_1.png'))
        self.bg_2.setPixmap(QtGui.QPixmap(':/Background/img/bg_2.png'))
        self.bg_3.setPixmap(QtGui.QPixmap(':/Background/img/bg_2.png'))

        self.settings_btn.setIcon(QtGui.QIcon(':/Decorations/img/settings.png'))

        self.setWindowIcon(QtGui.QIcon(':/Icon/img/icon.ico'))

        self.settings_btn.clicked.connect(lambda n: self.stackedWidget.setCurrentIndex(2))
        self.back_btn.clicked.connect(lambda n: self.stackedWidget.setCurrentIndex(1))

    def init_data(self):
        if not os.path.exists(self.local_dir):
            # loading screen
            if not self.prepare_local_dir():
                return False
        if self.load_data():
            if self.verify_local_files():
                if self.update_data_dict():
                    if self.update_containers("ui"):
                        return True
        return False

    def prepare_local_dir(self):
        try:
            os.mkdir(self.local_dir)
            os.mkdir(self.local_img_dir)

            for target_type in self.data_dict:
                path = self.data_dict[target_type]["path"]
                target_data = self.data_dict[target_type]["data"]
                container = {key:target_data[key]["val"] for key in target_data}
                with open(path, 'w') as f:
                    containerJson = json.dumps(container, indent=4)
                    f.write(containerJson)
        except:
            if os.path.exists(self.local_dir):
                shutil.rmtree(self.local_dir)
            self.error_occured("Wasn't able to create a local directory properly")
        else:
            return True

    def load_data(self):
        try:
            for target_type in self.data_dict:
                path = self.data_dict[target_type]["path"]
                with open(path, "r") as f:
                    json_content = json.load(f)
                    self.local_data[target_type] = json_content
        except:
            self.error_occured("Could not load local data")
            return False
        else:
            return True

    def verify_local_files(self):
        try:
            validated = all([self.verifyJson(self.local_data[key], key) for key in self.local_data])
        except:
            self.error_occured("Error while validating json")
            return False
        else:
            return validated

    def verifyJson(self, jsonDict, scheme):
        try:
            validate(instance=jsonDict, schema=self.json_schemes[scheme])
        except:
            return False
        else:
            return True

    def update_data_dict(self, target="all"):
        if target == "all":
            for target_type in self.data_dict:
                for key in self.data_dict[target_type]["data"]:
                    self.data_dict[target_type]["data"][key]["val"] = self.local_data[target_type][key]
        return True

    def update_containers(self, target):
        if target == "ui":
            for target_type in ["shrine", "perks", "user_perks"]:
                target_data = self.data_dict[target_type]["data"]
                for key in target_data:
                    value = target_data[key]["val"]
                    container = target_data[key]["container"]
                    self.setValue(container, value)
        elif target == "settings":
            target_data = self.data_dict["settings"]["data"]
            # ...
        return True

    def error_occured(self, message):
        self.stackedWidget.setCurrentIndex(3)
        self.error_msg_lbl.setText(message)

    def setValue(self, container, value):
        if type(container) == QtWidgets.QCheckBox:
            container.setChecked(value)
        elif type(container) == QtWidgets.QLabel:
            if container.objectName().endswith("img"):
                container.setPixmap(QtGui.QPixmap(f"{self.local_img_dir}\\{value}"))
                container.setScaledContents(True)
            else:
                container.setText(value)
        elif type(container) in [QtWidgets.QComboBox, QtWidgets.QListWidget]:
            container.addItems(value)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
