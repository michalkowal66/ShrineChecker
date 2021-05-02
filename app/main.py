from PyQt5 import QtCore, QtGui, QtWidgets
from templates.sc_ui import Ui_MainWindow
import os
import json
import shutil
from jsonschema import validate
from rsc import rsc


# TODO add scraper
# TODO add initialization method
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

        self.local_data = {
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
                    "perk1_frame": {"val": False, "container": self.perk1_frame},
                    "perk2_name": {"val": "perk2_name", "container": self.perk2_lbl},
                    "perk2_img": {"val": "perk2_img", "container": self.perk2_img},
                    "perk2_frame": {"val": False, "container": self.perk2_frame},
                    "perk3_name": {"val": "perk3_name", "container": self.perk3_lbl},
                    "perk3_img": {"val": "perk4_img", "container": self.perk3_img},
                    "perk3_frame": {"val": False, "container": self.perk3_frame},
                    "perk4_name": {"val": "perk4_name", "container": self.perk4_lbl},
                    "perk4_img": {"val": "perk4_img", "container": self.perk4_img},
                    "perk4_frame": {"val": False, "container": self.perk4_frame},
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
                # stay at loading screen, done button disabled
                print("Wasn't able to create a local directory properly")
                return False
        if self.verify_local_files():
            if self.load_data():
                # change screen to main
                return True
        else:
            # move to error screen
            print("Error while initializing data")
            return False

    def prepare_local_dir(self):
        try:
            os.mkdir(self.local_dir)
            os.mkdir(self.local_img_dir)

            for data_container in self.local_data:
                path = self.local_data[data_container]["path"]
                dict_data = self.local_data[data_container]["data"]
                container = { key:dict_data[key]["val"] for key in dict_data}
                with open(path, 'w') as f:
                    containerJson = json.dumps(container, indent=4)
                    f.write(containerJson)
        except:
            print("Error while creating directory")
            if os.path.exists(self.local_dir):
                shutil.rmtree(self.local_dir)
            return False
        else:
            print("Local directory created")
            return True

    def verify_local_files(self):
        return True

    def verifyJson(self, jsonFile, scheme):
        return True

    def load_data(self):
        return True


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
