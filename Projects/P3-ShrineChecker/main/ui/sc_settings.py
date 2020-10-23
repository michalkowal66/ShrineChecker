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
        Dialog.resize(360, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(360, 360))
        Dialog.setMaximumSize(QtCore.QSize(360, 360))
        Dialog.setStyleSheet("QLabel#settings_lbl {\n"
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
"QPushButton:hover {\n"
"    color: white;\n"
"    font: 12pt \"Sylfaen\";\n"
"    background-color:#404040;\n"
"}\n"
"\n"
"QLabel#bg {\n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: white;\n"
"    font: 12pt \"Sylfaen\";\n"
"    background-color:#2F3538;\n"
"    selection-background-color:#2F3538;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: white;\n"
"    font: 12pt \"Sylfaen\";\n"
"    background-color:#2F3538;\n"
"    selection-background-color: #404040;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QScrollBar:vertical {    \n"
"    color: white;\n"
"    font: 12pt \"Sylfaen\";\n"
"    background:#404040;\n"
"}")
        self.tray_check = QtWidgets.QCheckBox(Dialog)
        self.tray_check.setGeometry(QtCore.QRect(10, 40, 200, 20))
        self.tray_check.setChecked(False)
        self.tray_check.setObjectName("tray_check")
        self.save_btn = QtWidgets.QPushButton(Dialog)
        self.save_btn.setGeometry(QtCore.QRect(90, 310, 80, 30))
        self.save_btn.setObjectName("save_btn")
        self.settings_lbl = QtWidgets.QLabel(Dialog)
        self.settings_lbl.setGeometry(QtCore.QRect(140, 10, 80, 25))
        self.settings_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_lbl.setObjectName("settings_lbl")
        self.reset_lbl = QtWidgets.QLabel(Dialog)
        self.reset_lbl.setGeometry(QtCore.QRect(160, 190, 190, 50))
        self.reset_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.reset_lbl.setWordWrap(True)
        self.reset_lbl.setObjectName("reset_lbl")
        self.startup_check = QtWidgets.QCheckBox(Dialog)
        self.startup_check.setGeometry(QtCore.QRect(10, 70, 200, 20))
        self.startup_check.setChecked(False)
        self.startup_check.setObjectName("startup_check")
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(QtCore.QRect(0, 0, 360, 360))
        self.bg.setStyleSheet("")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.reset_btn = QtWidgets.QPushButton(Dialog)
        self.reset_btn.setGeometry(QtCore.QRect(10, 200, 140, 30))
        self.reset_btn.setCheckable(False)
        self.reset_btn.setObjectName("reset_btn")
        self.close_btn = QtWidgets.QPushButton(Dialog)
        self.close_btn.setGeometry(QtCore.QRect(190, 310, 80, 30))
        self.close_btn.setObjectName("close_btn")
        self.notif_combo = QtWidgets.QComboBox(Dialog)
        self.notif_combo.setGeometry(QtCore.QRect(10, 100, 50, 30))
        self.notif_combo.setStyleSheet("")
        self.notif_combo.setObjectName("notif_combo")
        self.notif_combo.addItem("")
        self.notif_combo.addItem("")
        self.notif_combo.addItem("")
        self.notif_combo.addItem("")
        self.refr_combo = QtWidgets.QComboBox(Dialog)
        self.refr_combo.setGeometry(QtCore.QRect(10, 150, 50, 30))
        self.refr_combo.setStyleSheet("")
        self.refr_combo.setObjectName("refr_combo")
        self.refr_combo.addItem("")
        self.refr_combo.addItem("")
        self.refr_combo.addItem("")
        self.refr_combo.addItem("")
        self.notif_lbl = QtWidgets.QLabel(Dialog)
        self.notif_lbl.setGeometry(QtCore.QRect(70, 90, 280, 50))
        self.notif_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.notif_lbl.setWordWrap(True)
        self.notif_lbl.setObjectName("notif_lbl")
        self.refr_lbl = QtWidgets.QLabel(Dialog)
        self.refr_lbl.setGeometry(QtCore.QRect(70, 140, 280, 50))
        self.refr_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.refr_lbl.setWordWrap(True)
        self.refr_lbl.setObjectName("refr_lbl")
        self.reload_lbl = QtWidgets.QLabel(Dialog)
        self.reload_lbl.setGeometry(QtCore.QRect(160, 240, 190, 50))
        self.reload_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.reload_lbl.setWordWrap(True)
        self.reload_lbl.setObjectName("reload_lbl")
        self.reload_btn = QtWidgets.QPushButton(Dialog)
        self.reload_btn.setGeometry(QtCore.QRect(10, 250, 140, 30))
        self.reload_btn.setCheckable(False)
        self.reload_btn.setObjectName("reload_btn")
        self.about_btn = QtWidgets.QPushButton(Dialog)
        self.about_btn.setGeometry(QtCore.QRect(320, 10, 30, 30))
        self.about_btn.setStyleSheet("")
        self.about_btn.setObjectName("about_btn")
        self.bg.raise_()
        self.tray_check.raise_()
        self.save_btn.raise_()
        self.settings_lbl.raise_()
        self.reset_lbl.raise_()
        self.startup_check.raise_()
        self.reset_btn.raise_()
        self.close_btn.raise_()
        self.notif_combo.raise_()
        self.refr_combo.raise_()
        self.notif_lbl.raise_()
        self.refr_lbl.raise_()
        self.reload_lbl.raise_()
        self.reload_btn.raise_()
        self.about_btn.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.tray_check.setText(_translate("Dialog", "Minimize to tray on exit"))
        self.save_btn.setText(_translate("Dialog", "Save"))
        self.settings_lbl.setText(_translate("Dialog", "Settings"))
        self.reset_lbl.setText(_translate("Dialog", "Redownload local database of perks"))
        self.startup_check.setText(_translate("Dialog", "Run with startup"))
        self.reset_btn.setText(_translate("Dialog", "Reload perks"))
        self.close_btn.setText(_translate("Dialog", "Close"))
        self.notif_combo.setItemText(0, _translate("Dialog", "2"))
        self.notif_combo.setItemText(1, _translate("Dialog", "4"))
        self.notif_combo.setItemText(2, _translate("Dialog", "6"))
        self.notif_combo.setItemText(3, _translate("Dialog", "8"))
        self.refr_combo.setItemText(0, _translate("Dialog", "2"))
        self.refr_combo.setItemText(1, _translate("Dialog", "4"))
        self.refr_combo.setItemText(2, _translate("Dialog", "6"))
        self.refr_combo.setItemText(3, _translate("Dialog", "8"))
        self.notif_lbl.setText(_translate("Dialog", "Notification interval (hours)"))
        self.refr_lbl.setText(_translate("Dialog", "Auto-refresh interval (hours)"))
        self.reload_lbl.setText(_translate("Dialog", "Force shrine reload"))
        self.reload_btn.setText(_translate("Dialog", "Reload shrine"))
        self.about_btn.setText(_translate("Dialog", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
