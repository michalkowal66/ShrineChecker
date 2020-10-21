# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sc_ui_base.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        MainWindow.setStyleSheet("font: 12pt \"Sylfaen\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
"QPushButton {\n"
"    background-color:#2F3538;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#404040;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color:#2F3538;\n"
"    selection-background-color:#2F3538;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color:#2F3538;\n"
"    selection-background-color: #404040;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QScrollBar:vertical {    \n"
"    background:#404040;\n"
"}\n"
"\n"
"QPushButton#settings_btn{\n"
"    qproperty-iconSize: 30px;\n"
"}\n"
"\n"
"QLabel#perk1_lbl {\n"
"    font: 14pt \"Sylfaen\";\n"
"    color: #6e6d6d;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLabel#perk2_lbl {\n"
"    font: 14pt \"Sylfaen\";\n"
"    color: #6e6d6d;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLabel#perk3_lbl {\n"
"    font: 14pt \"Sylfaen\";\n"
"    color: #6e6d6d;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLabel#perk4_lbl {\n"
"    font: 14pt \"Sylfaen\";\n"
"    color: #6e6d6d;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QListWidget{\n"
"    color: white;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    outline: 0;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    color: white;\n"
"    background-color: rgba(47, 53, 56, 0.3);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    color: white;\n"
"    background-color: rgba(64, 64, 64, 0.3);\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.perks_combo = QtWidgets.QComboBox(self.centralwidget)
        self.perks_combo.setGeometry(QtCore.QRect(25, 80, 280, 30))
        self.perks_combo.setStyleSheet("")
        self.perks_combo.setObjectName("perks_combo")
        self.perks_list = QtWidgets.QListWidget(self.centralwidget)
        self.perks_list.setGeometry(QtCore.QRect(25, 120, 280, 390))
        self.perks_list.setStyleSheet("")
        self.perks_list.setObjectName("perks_list")
        self.lbl1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl1.setGeometry(QtCore.QRect(25, 40, 250, 30))
        self.lbl1.setStyleSheet("font: 14pt \"Sylfaen\";\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lbl1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl1.setObjectName("lbl1")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(25, 520, 120, 30))
        self.add_btn.setStyleSheet("")
        self.add_btn.setObjectName("add_btn")
        self.remove_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_btn.setGeometry(QtCore.QRect(185, 520, 120, 30))
        self.remove_btn.setObjectName("remove_btn")
        self.img1 = QtWidgets.QLabel(self.centralwidget)
        self.img1.setGeometry(QtCore.QRect(570, 100, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img1.sizePolicy().hasHeightForWidth())
        self.img1.setSizePolicy(sizePolicy)
        self.img1.setMinimumSize(QtCore.QSize(100, 100))
        self.img1.setMaximumSize(QtCore.QSize(100, 100))
        self.img1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.img1.setToolTip("")
        self.img1.setWhatsThis("")
        self.img1.setStyleSheet("")
        self.img1.setText("")
        self.img1.setAlignment(QtCore.Qt.AlignCenter)
        self.img1.setObjectName("img1")
        self.img2 = QtWidgets.QLabel(self.centralwidget)
        self.img2.setGeometry(QtCore.QRect(420, 250, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img2.sizePolicy().hasHeightForWidth())
        self.img2.setSizePolicy(sizePolicy)
        self.img2.setMinimumSize(QtCore.QSize(100, 100))
        self.img2.setMaximumSize(QtCore.QSize(100, 100))
        self.img2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.img2.setStyleSheet("")
        self.img2.setText("")
        self.img2.setAlignment(QtCore.Qt.AlignCenter)
        self.img2.setObjectName("img2")
        self.img3 = QtWidgets.QLabel(self.centralwidget)
        self.img3.setGeometry(QtCore.QRect(720, 250, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img3.sizePolicy().hasHeightForWidth())
        self.img3.setSizePolicy(sizePolicy)
        self.img3.setMinimumSize(QtCore.QSize(100, 100))
        self.img3.setMaximumSize(QtCore.QSize(100, 100))
        self.img3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.img3.setStyleSheet("")
        self.img3.setText("")
        self.img3.setAlignment(QtCore.Qt.AlignCenter)
        self.img3.setObjectName("img3")
        self.img4 = QtWidgets.QLabel(self.centralwidget)
        self.img4.setGeometry(QtCore.QRect(570, 400, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img4.sizePolicy().hasHeightForWidth())
        self.img4.setSizePolicy(sizePolicy)
        self.img4.setMinimumSize(QtCore.QSize(100, 100))
        self.img4.setMaximumSize(QtCore.QSize(100, 100))
        self.img4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.img4.setStyleSheet("")
        self.img4.setText("")
        self.img4.setAlignment(QtCore.Qt.AlignCenter)
        self.img4.setObjectName("img4")
        self.perk1_lbl = QtWidgets.QLabel(self.centralwidget)
        self.perk1_lbl.setGeometry(QtCore.QRect(520, 210, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk1_lbl.sizePolicy().hasHeightForWidth())
        self.perk1_lbl.setSizePolicy(sizePolicy)
        self.perk1_lbl.setStyleSheet("")
        self.perk1_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.perk1_lbl.setObjectName("perk1_lbl")
        self.perk2_lbl = QtWidgets.QLabel(self.centralwidget)
        self.perk2_lbl.setGeometry(QtCore.QRect(370, 360, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk2_lbl.sizePolicy().hasHeightForWidth())
        self.perk2_lbl.setSizePolicy(sizePolicy)
        self.perk2_lbl.setStyleSheet("")
        self.perk2_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.perk2_lbl.setObjectName("perk2_lbl")
        self.perk3_lbl = QtWidgets.QLabel(self.centralwidget)
        self.perk3_lbl.setGeometry(QtCore.QRect(670, 360, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk3_lbl.sizePolicy().hasHeightForWidth())
        self.perk3_lbl.setSizePolicy(sizePolicy)
        self.perk3_lbl.setStyleSheet("")
        self.perk3_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.perk3_lbl.setObjectName("perk3_lbl")
        self.perk4_lbl = QtWidgets.QLabel(self.centralwidget)
        self.perk4_lbl.setGeometry(QtCore.QRect(520, 510, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk4_lbl.sizePolicy().hasHeightForWidth())
        self.perk4_lbl.setSizePolicy(sizePolicy)
        self.perk4_lbl.setStyleSheet("")
        self.perk4_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.perk4_lbl.setObjectName("perk4_lbl")
        self.lbl1_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl1_2.setGeometry(QtCore.QRect(470, 10, 300, 35))
        self.lbl1_2.setStyleSheet("font: 24pt \"Sylfaen\";\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lbl1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl1_2.setObjectName("lbl1_2")
        self.date_lbl = QtWidgets.QLabel(self.centralwidget)
        self.date_lbl.setGeometry(QtCore.QRect(25, 565, 280, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_lbl.sizePolicy().hasHeightForWidth())
        self.date_lbl.setSizePolicy(sizePolicy)
        self.date_lbl.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.date_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.date_lbl.setObjectName("date_lbl")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.bg.setStyleSheet("")
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("../rsc/bg.png"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.settings_btn = QtWidgets.QPushButton(self.centralwidget)
        self.settings_btn.setGeometry(QtCore.QRect(150, 520, 30, 30))
        self.settings_btn.setStyleSheet("")
        self.settings_btn.setText("")
        self.settings_btn.setObjectName("settings_btn")
        self.frame1 = QtWidgets.QLabel(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(545, 75, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setMinimumSize(QtCore.QSize(150, 150))
        self.frame1.setMaximumSize(QtCore.QSize(150, 150))
        self.frame1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame1.setToolTip("")
        self.frame1.setWhatsThis("")
        self.frame1.setStyleSheet("")
        self.frame1.setText("")
        self.frame1.setAlignment(QtCore.Qt.AlignCenter)
        self.frame1.setObjectName("frame1")
        self.frame2 = QtWidgets.QLabel(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(395, 225, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setMinimumSize(QtCore.QSize(150, 150))
        self.frame2.setMaximumSize(QtCore.QSize(150, 150))
        self.frame2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame2.setToolTip("")
        self.frame2.setWhatsThis("")
        self.frame2.setStyleSheet("")
        self.frame2.setText("")
        self.frame2.setAlignment(QtCore.Qt.AlignCenter)
        self.frame2.setObjectName("frame2")
        self.frame3 = QtWidgets.QLabel(self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(695, 225, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame3.sizePolicy().hasHeightForWidth())
        self.frame3.setSizePolicy(sizePolicy)
        self.frame3.setMinimumSize(QtCore.QSize(150, 150))
        self.frame3.setMaximumSize(QtCore.QSize(150, 150))
        self.frame3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame3.setToolTip("")
        self.frame3.setWhatsThis("")
        self.frame3.setStyleSheet("")
        self.frame3.setText("")
        self.frame3.setAlignment(QtCore.Qt.AlignCenter)
        self.frame3.setObjectName("frame3")
        self.frame4 = QtWidgets.QLabel(self.centralwidget)
        self.frame4.setGeometry(QtCore.QRect(545, 375, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame4.sizePolicy().hasHeightForWidth())
        self.frame4.setSizePolicy(sizePolicy)
        self.frame4.setMinimumSize(QtCore.QSize(150, 150))
        self.frame4.setMaximumSize(QtCore.QSize(150, 150))
        self.frame4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame4.setToolTip("")
        self.frame4.setWhatsThis("")
        self.frame4.setStyleSheet("")
        self.frame4.setText("")
        self.frame4.setAlignment(QtCore.Qt.AlignCenter)
        self.frame4.setObjectName("frame4")
        self.bg.raise_()
        self.perks_combo.raise_()
        self.perks_list.raise_()
        self.lbl1.raise_()
        self.add_btn.raise_()
        self.remove_btn.raise_()
        self.img1.raise_()
        self.img2.raise_()
        self.img3.raise_()
        self.img4.raise_()
        self.perk1_lbl.raise_()
        self.perk2_lbl.raise_()
        self.perk3_lbl.raise_()
        self.perk4_lbl.raise_()
        self.lbl1_2.raise_()
        self.date_lbl.raise_()
        self.settings_btn.raise_()
        self.frame1.raise_()
        self.frame2.raise_()
        self.frame3.raise_()
        self.frame4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.perks_combo, self.perks_list)
        MainWindow.setTabOrder(self.perks_list, self.add_btn)
        MainWindow.setTabOrder(self.add_btn, self.remove_btn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shrine Checker"))
        self.lbl1.setText(_translate("MainWindow", "Desired perks:"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.remove_btn.setText(_translate("MainWindow", "Remove"))
        self.perk1_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.perk2_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.perk3_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.perk4_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.lbl1_2.setText(_translate("MainWindow", "Shrine of Secrets"))
        self.date_lbl.setText(_translate("MainWindow", "YYYY-MM-DD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
