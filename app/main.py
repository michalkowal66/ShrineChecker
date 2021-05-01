from PyQt5 import QtCore, QtGui, QtWidgets
from templates.sc_ui import Ui_MainWindow
from rsc import rsc


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(self)
        self.bg.setPixmap(QtGui.QPixmap(':/Background/img/bg.png'))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
