from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import convWindow


class mainProgram(convWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)

        self.pcalcBtn.clicked.connect(self.checkVal)

    def checkVal(self):
        
        begUnit = self.pconvInput.text()

        try:
            float(begUnit)
            self.calcP()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ups...")
            msg.setInformativeText("Zły format danych.")
            msg.setWindowTitle("Ups...")
            msg.exec_()

    def calcP(self):
        begUnit = self.pconvFrom.currentText()
        finUnit = self.pconvTo.currentText()

        inputVal = float(self.pconvInput.text())

        if begUnit == finUnit:
            self.pconvOutput.setText(self.pconvInput.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainProgram()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())