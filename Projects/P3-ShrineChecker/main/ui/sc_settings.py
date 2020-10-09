# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sc_settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(360, 200))
        Dialog.setMaximumSize(QtCore.QSize(360, 200))
        Dialog.setStyleSheet("\n"
"QLabel#settings_lbl {\n"
"    color: white;\n"
"    font: 14pt \"Sylfaen\";\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;\n"
"    font: 12pt \"Sylfaen\";\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    font: 12pt \"Sylfaen\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    font: 12pt \"Sylfaen\";\n"
"    background-color:#2F3538;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    font: 12pt \"Sylfaen\";\n"
"    background-color:#404040;\n"
"}")
        self.tray_check = QtWidgets.QCheckBox(Dialog)
        self.tray_check.setGeometry(QtCore.QRect(30, 40, 200, 20))
        self.tray_check.setChecked(False)
        self.tray_check.setObjectName("tray_check")
        self.save_btn = QtWidgets.QPushButton(Dialog)
        self.save_btn.setGeometry(QtCore.QRect(140, 150, 80, 30))
        self.save_btn.setObjectName("save_btn")
        self.settings_lbl = QtWidgets.QLabel(Dialog)
        self.settings_lbl.setGeometry(QtCore.QRect(140, 10, 80, 25))
        self.settings_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_lbl.setObjectName("settings_lbl")
        self.reset_lbl = QtWidgets.QLabel(Dialog)
        self.reset_lbl.setGeometry(QtCore.QRect(120, 100, 230, 30))
        self.reset_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.reset_lbl.setWordWrap(True)
        self.reset_lbl.setObjectName("reset_lbl")
        self.startup_check = QtWidgets.QCheckBox(Dialog)
        self.startup_check.setGeometry(QtCore.QRect(30, 70, 200, 20))
        self.startup_check.setChecked(False)
        self.startup_check.setObjectName("startup_check")
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(QtCore.QRect(0, 0, 360, 200))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("../rsc/bg.png"))
        self.bg.setObjectName("bg")
        self.reset_btn = QtWidgets.QPushButton(Dialog)
        self.reset_btn.setGeometry(QtCore.QRect(30, 100, 80, 30))
        self.reset_btn.setCheckable(False)
        self.reset_btn.setObjectName("reset_btn")
        self.bg.raise_()
        self.tray_check.raise_()
        self.save_btn.raise_()
        self.settings_lbl.raise_()
        self.reset_lbl.raise_()
        self.startup_check.raise_()
        self.reset_btn.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.tray_check.setText(_translate("Dialog", "Minimize to tray on exit"))
        self.save_btn.setText(_translate("Dialog", "Save"))
        self.settings_lbl.setText(_translate("Dialog", "Settings"))
        self.reset_lbl.setText(_translate("Dialog", "Erase and download all local data."))
        self.startup_check.setText(_translate("Dialog", "Run with startup"))
        self.reset_btn.setText(_translate("Dialog", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
