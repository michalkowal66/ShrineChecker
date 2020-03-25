from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
import sys
import getExchange
from getExchange import getCdB
import datetime

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('convGui.ui', self)
        self.show()

        #Load pressure conversion
        self.pconvFrom = self.findChild(QtWidgets.QComboBox, "pconvFrom")
        self.pconvInput = self.findChild(QtWidgets.QLineEdit, "pconvInput")
        self.pconvOutput = self.findChild(QtWidgets.QLineEdit, "pconvOutput")
        self.pconvTo = self.findChild(QtWidgets.QComboBox, "pconvTo")
        self.pcalcBtn = self.findChild(QtWidgets.QPushButton, "pcalcBtn")

        #Load length conversion
        self.lconvFrom = self.findChild(QtWidgets.QComboBox, "lconvFrom")
        self.lconvInput = self.findChild(QtWidgets.QLineEdit, "lconvInput")
        self.lconvOutput = self.findChild(QtWidgets.QLineEdit, "lconvOutput")
        self.lconvTo = self.findChild(QtWidgets.QComboBox, "lconvTo")
        self.lcalcBtn = self.findChild(QtWidgets.QPushButton, "lcalcBtn")

        #Load currency exchange
        self.exchangeFrom = self.findChild(QtWidgets.QComboBox, "exchangeFrom")
        self.exchangeInput = self.findChild(QtWidgets.QLineEdit, "exchangeInput")
        self.exchangeOutput = self.findChild(QtWidgets.QLineEdit, "exchangeOutput")
        self.exchangeTo = self.findChild(QtWidgets.QComboBox, "exchangeTo")
        self.exchangeBtn = self.findChild(QtWidgets.QPushButton, "exchangeBtn")
        self.refreshBtn = self.findChild(QtWidgets.QPushButton, "refreshBtn")
        self.dateLabel = self.findChild(QtWidgets.QLabel, "dateLabel")

        #Load currency exchange rates

        self.cdB = {}
        self.getExRates()     #try to get exchange rates
        
        ############################################

        self.pcalcBtn.clicked.connect(self.checkPVal)
        self.lcalcBtn.clicked.connect(self.checkLVal)
        self.exchangeBtn.clicked.connect(self.checkExVal)
        self.refreshBtn.clicked.connect(self.refreshRates)

    def getExRates(self):
        try:
            getCdB(self.cdB)
        except:
            box = QMessageBox()
            box.setIcon(QMessageBox.Question)
            box.setWindowTitle('Ups...')
            box.setText('Coś poszło nie tak w trakcie pobierania kursów walut. \nSprawdź połączenie z siecią i spróbuj jeszcze raz lub zignoruj to ostrzeżenie.')
            box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            buttonY = box.button(QMessageBox.Yes)
            buttonY.setText('Ponów')
            buttonN = box.button(QMessageBox.No)
            buttonN.setText('Ignoruj')
            box.exec_()
            self.dateLabel.setText("Problem z siecią")
            if box.clickedButton() == buttonY:
                self.getExRates()
        else:
            self.raw_time = datetime.datetime.now()
            self.time = self.raw_time.strftime("%Y-%m-%d %H:%M:%S")

            self.dateLabel.setText(self.time) #Show initial data download time

    
    def checkPVal(self):
        checkFormat = self.pconvInput.text()

        try:
            float(checkFormat)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ups...")
            msg.setInformativeText("Zły format danych.")
            msg.setWindowTitle("Ups...")
            msg.exec_()
        else:
            self.calcP()

    def checkLVal(self):
        checkFormat = self.lconvInput.text()

        try:
            float(checkFormat)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ups...")
            msg.setInformativeText("Zły format danych.")
            msg.setWindowTitle("Ups...")
            msg.exec_()
        else:
            self.calcL()

    def calcP(self):
        from convRates import pRates
        begUnit = self.pconvFrom.currentText()
        finUnit = self.pconvTo.currentText()

        conversion = str(begUnit + "/" + finUnit)
        rev_conversion = finUnit + "/" + begUnit
        inputVal = float(self.pconvInput.text())

        if begUnit == finUnit:
            self.pconvOutput.setText(self.pconvInput.text())

        elif conversion in pRates.keys():
            rate = pRates[conversion]
            result = str(inputVal*rate)
            self.pconvOutput.setText(result)

        elif rev_conversion in pRates.keys():
            rate = 1/pRates[rev_conversion]
            result = str(inputVal*rate)
            self.pconvOutput.setText(result)
    
    def calcL(self):
        from convRates import lRates
        begUnit = self.lconvFrom.currentText()
        finUnit = self.lconvTo.currentText()

        conversion = str(begUnit + "/" + finUnit)
        rev_conversion = finUnit + "/" + begUnit
        inputVal = float(self.lconvInput.text())

        if begUnit == finUnit:
            self.lconvOutput.setText(self.lconvInput.text())

        elif conversion in lRates.keys():
            rate = lRates[conversion]
            result = str(inputVal*rate)
            self.lconvOutput.setText(result)

        elif rev_conversion in lRates.keys():
            rate = 1/lRates[rev_conversion]
            result = str(inputVal*rate)
            self.lconvOutput.setText(result)

    def checkExVal(self):
        checkFormat = self.exchangeInput.text()

        try:
            float(checkFormat)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ups...")
            msg.setInformativeText("Zły format danych.")
            msg.setWindowTitle("Ups...")
            msg.exec_()
        else:
            self.calcE(self.cdB)

    def calcE(self, cdB):
        if len(cdB) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ups...")
            msg.setInformativeText("Wygląda na to, że przy pierwszycm uruchomieniu aplikacji nie udało się pobrać kursów walut.\nUżyj przycisku 'odśwież', w prawym górnym rogu, kiedy będziesz już połączony z siecią.")
            msg.setWindowTitle("Ups...")
            msg.exec_()

        begCurr = self.exchangeFrom.currentText()
        finCurr = self.exchangeTo.currentText()

        conversion = begCurr + "/" + finCurr
        # rev_conversion = finCurr + "/" + begCurr
        inputVal = float(self.exchangeInput.text())

        if begCurr == finCurr:
            self.exchangeOutput.setText(self.exchangeInput.text())

        elif conversion in cdB.keys():
            rate = cdB[conversion]
            result = str(round(inputVal*rate,2))
            self.exchangeOutput.setText(result)

        # elif rev_conversion in cdB.keys():
        #     rate = 1/cdB[rev_conversion]
        #     result = str(round(inputVal*rate,2))
        #     self.exchangeOutput.setText(result)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ups...")
            msg.setInformativeText("Coś poszło nie tak! Skontaktuj się z autorem aplikacji.")
            msg.setWindowTitle("Ups...")
            msg.exec_()

    def refreshRates(self):
        self.getExRates()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()