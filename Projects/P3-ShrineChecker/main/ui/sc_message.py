# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sc_message.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 250)
        Dialog.setMinimumSize(QtCore.QSize(360, 250))
        Dialog.setMaximumSize(QtCore.QSize(360, 250))
        Dialog.setStyleSheet("QLabel#bg {\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QLabel#msg_lbl{\n"
"    color: white;\n"
"    font: 16px \"Sylfaen\";\n"
"}\n"
"QLabel#title_lbl {\n"
"    color: white;\n"
"    font: 20px \"Sylfaen\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    font: 18px \"Sylfaen\";\n"
"    background-color:#2F3538;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#404040;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: black;\n"
"    background-color:#141718;\n"
"}\n"
"")
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(QtCore.QRect(0, 0, 360, 250))
        self.bg.setStyleSheet("")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.title_lbl = QtWidgets.QLabel(Dialog)
        self.title_lbl.setGeometry(QtCore.QRect(0, 10, 360, 30))
        self.title_lbl.setStyleSheet("")
        self.title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lbl.setObjectName("title_lbl")
        self.msg_lbl = QtWidgets.QLabel(Dialog)
        self.msg_lbl.setGeometry(QtCore.QRect(20, 40, 320, 160))
        self.msg_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_lbl.setWordWrap(True)
        self.msg_lbl.setObjectName("msg_lbl")
        self.close_btn = QtWidgets.QPushButton(Dialog)
        self.close_btn.setGeometry(QtCore.QRect(140, 205, 80, 30))
        self.close_btn.setStyleSheet("")
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_lbl.setText(_translate("Dialog", "Title"))
        self.msg_lbl.setText(_translate("Dialog", "Message"))
        self.close_btn.setText(_translate("Dialog", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
