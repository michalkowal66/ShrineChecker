from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('drawBeam.ui', self)
        self.show()

        self.fiInput = self.findChild(QtWidgets.QLineEdit, "fiInput")
        self.widthInput = self.findChild(QtWidgets.QLineEdit, "widthInput")
        self.heightInput = self.findChild(QtWidgets.QLineEdit, "heightInput")
        self.coverInput = self.findChild(QtWidgets.QLineEdit, "coverInput")
        self.bardistInput = self.findChild(QtWidgets.QLineEdit, "bardistInput")
        self.barsInput = self.findChild(QtWidgets.QLineEdit, "barsInput")
        self.drawCanvas = self.findChild(QtWidgets.QFrame, "drawCanvas")
        self.drawBtn = self.findChild(QtWidgets.QPushButton, "drawBtn")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()