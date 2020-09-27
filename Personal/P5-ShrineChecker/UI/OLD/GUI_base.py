# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_SC.ui'
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
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("\n"
"QLabel#perks_lbl {\n"
"font: 20pt \"Tahoma\";\n"
"color: white;\n"
"}\n"
"\n"
"QLabel#shrine_lbl {\n"
"font: 20pt \"Tahoma\";\n"
"color: white;\n"
"}\n"
"\n"
"QLabel#perk1_lbl {\n"
"font: 12pt \"Tahoma\";\n"
"color: white;\n"
"}\n"
"\n"
"QLabel#perk2_lbl  {\n"
"font: 12pt \"Tahoma\";\n"
"color: white;\n"
"}\n"
"\n"
"QLabel#perk3_lbl  {\n"
"font: 12pt \"Tahoma\";\n"
"color: white;\n"
"}\n"
"\n"
"QLabel#perk4_lbl  {\n"
"font: 12pt \"Tahoma\";\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #2A2828;\n"
"color: white;\n"
"font: 15pt \"Tahoma\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #3E3C3C;\n"
"color: white;\n"
"font: 15pt \"Tahoma\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #3E3C3C;\n"
"border: 1px, white;\n"
"color: white;\n"
"font: 15pt \"Tahoma\";\n"
"}\n"
"\n"
"QComboBox {\n"
"background-color: #A5A1A1;\n"
"border: 1px solid gray;\n"
"border-radius: 3px;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 6em;\n"
"font: 15pt \"Tahoma\";\n"
"}\n"
"\n"
"QListView {\n"
"background: rgba(152, 152, 153, 10);\n"
"border: none\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 109, 180, 31))
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 109, 100, 30))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 550, 150, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(770, 550, 100, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(40, 160, 301, 371))
        self.listView.setStyleSheet("")
        self.listView.setObjectName("listView")
        self.perk1_lbl = QtWidgets.QLabel(self.centralwidget)
        self.perk1_lbl.setGeometry(QtCore.QRect(590, 190, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.perk1_lbl.setFont(font)
        self.perk1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk1_lbl.setObjectName("perk1_lbl")
        self.perk2_lbl = QtWidgets.QLabel(self.centralwidget)
        self.perk2_lbl.setGeometry(QtCore.QRect(385, 370, 139, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.perk2_lbl.setFont(font)
        self.perk2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk2_lbl.setObjectName("perk2_lbl")
        self.perk3_lbl = QtWidgets.QLabel(self.centralwidget)
        self.perk3_lbl.setGeometry(QtCore.QRect(725, 370, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.perk3_lbl.setFont(font)
        self.perk3_lbl.setStyleSheet("")
        self.perk3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk3_lbl.setObjectName("perk3_lbl")
        self.perk4_lbl = QtWidgets.QLabel(self.centralwidget)
        self.perk4_lbl.setGeometry(QtCore.QRect(550, 540, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.perk4_lbl.setFont(font)
        self.perk4_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk4_lbl.setObjectName("perk4_lbl")
        self.shrine_lbl = QtWidgets.QLabel(self.centralwidget)
        self.shrine_lbl.setGeometry(QtCore.QRect(525, 5, 211, 71))
        self.shrine_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.shrine_lbl.setObjectName("shrine_lbl")
        self.perks_lbl = QtWidgets.QLabel(self.centralwidget)
        self.perks_lbl.setGeometry(QtCore.QRect(40, 20, 281, 71))
        self.perks_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perks_lbl.setObjectName("perks_lbl")
        self.perk1_img = QtWidgets.QLabel(self.centralwidget)
        self.perk1_img.setGeometry(QtCore.QRect(550, 80, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk1_img.sizePolicy().hasHeightForWidth())
        self.perk1_img.setSizePolicy(sizePolicy)
        self.perk1_img.setMinimumSize(QtCore.QSize(150, 150))
        self.perk1_img.setMaximumSize(QtCore.QSize(150, 150))
        self.perk1_img.setStyleSheet("")
        self.perk1_img.setObjectName("perk1_img")
        self.perk2_img = QtWidgets.QLabel(self.centralwidget)
        self.perk2_img.setGeometry(QtCore.QRect(380, 250, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk2_img.sizePolicy().hasHeightForWidth())
        self.perk2_img.setSizePolicy(sizePolicy)
        self.perk2_img.setMinimumSize(QtCore.QSize(150, 150))
        self.perk2_img.setMaximumSize(QtCore.QSize(150, 150))
        self.perk2_img.setStyleSheet("")
        self.perk2_img.setObjectName("perk2_img")
        self.perk3_img = QtWidgets.QLabel(self.centralwidget)
        self.perk3_img.setGeometry(QtCore.QRect(720, 250, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk3_img.sizePolicy().hasHeightForWidth())
        self.perk3_img.setSizePolicy(sizePolicy)
        self.perk3_img.setMinimumSize(QtCore.QSize(150, 150))
        self.perk3_img.setMaximumSize(QtCore.QSize(150, 150))
        self.perk3_img.setStyleSheet("")
        self.perk3_img.setObjectName("perk3_img")
        self.perk4_img = QtWidgets.QLabel(self.centralwidget)
        self.perk4_img.setGeometry(QtCore.QRect(550, 420, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk4_img.sizePolicy().hasHeightForWidth())
        self.perk4_img.setSizePolicy(sizePolicy)
        self.perk4_img.setMinimumSize(QtCore.QSize(150, 150))
        self.perk4_img.setMaximumSize(QtCore.QSize(150, 150))
        self.perk4_img.setStyleSheet("")
        self.perk4_img.setObjectName("perk4_img")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Agitation"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Adrenaline"))
        self.pushButton.setText(_translate("MainWindow", "Add Perk"))
        self.pushButton_2.setText(_translate("MainWindow", "Remove Perk"))
        self.pushButton_3.setText(_translate("MainWindow", "Refresh"))
        self.perk1_lbl.setText(_translate("MainWindow", "perk1"))
        self.perk2_lbl.setText(_translate("MainWindow", "perk2"))
        self.perk3_lbl.setText(_translate("MainWindow", "perk3"))
        self.perk4_lbl.setText(_translate("MainWindow", "perk4"))
        self.shrine_lbl.setText(_translate("MainWindow", "Shrine of Secrets"))
        self.perks_lbl.setText(_translate("MainWindow", "Desired perks:"))
        self.perk1_img.setText(_translate("MainWindow", "TextLabel"))
        self.perk2_img.setText(_translate("MainWindow", "TextLabel"))
        self.perk3_img.setText(_translate("MainWindow", "TextLabel"))
        self.perk4_img.setText(_translate("MainWindow", "TextLabel"))
