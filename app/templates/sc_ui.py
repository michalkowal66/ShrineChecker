# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\app\designer\sc_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.stackedWidget.setObjectName("stackedWidget")
        self.loading = QtWidgets.QWidget()
        self.loading.setStyleSheet("QLabel#bg_loading {\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QLabel#wait_lbl{\n"
"    color: white;\n"
"    font: 20px \"Sylfaen\";\n"
"}\n"
"QLabel#msg_lbl {\n"
"    color: white;\n"
"    font: 16px \"Sylfaen\";\n"
"}\n"
"\n"
"QProgressBar{\n"
"    border: solid black;\n"
"    border-radius: 2px;\n"
"    color: black;\n"
"    background-color: #404040;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background-color: white;\n"
"}  \n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    font: 18px\"Sylfaen\";\n"
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
        self.loading.setObjectName("loading")
        self.msg_lbl = QtWidgets.QLabel(self.loading)
        self.msg_lbl.setGeometry(QtCore.QRect(290, 460, 320, 25))
        self.msg_lbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.msg_lbl.setWordWrap(True)
        self.msg_lbl.setObjectName("msg_lbl")
        self.done_btn = QtWidgets.QPushButton(self.loading)
        self.done_btn.setGeometry(QtCore.QRect(410, 550, 80, 30))
        self.done_btn.setStyleSheet("")
        self.done_btn.setObjectName("done_btn")
        self.bg_0 = QtWidgets.QLabel(self.loading)
        self.bg_0.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.bg_0.setStyleSheet("")
        self.bg_0.setText("")
        self.bg_0.setScaledContents(True)
        self.bg_0.setObjectName("bg_0")
        self.progress_bar = QtWidgets.QProgressBar(self.loading)
        self.progress_bar.setGeometry(QtCore.QRect(25, 500, 850, 30))
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar.setObjectName("progress_bar")
        self.wait_lbl = QtWidgets.QLabel(self.loading)
        self.wait_lbl.setGeometry(QtCore.QRect(290, 30, 320, 20))
        self.wait_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.wait_lbl.setObjectName("wait_lbl")
        self.bg_0.raise_()
        self.msg_lbl.raise_()
        self.done_btn.raise_()
        self.progress_bar.raise_()
        self.wait_lbl.raise_()
        self.stackedWidget.addWidget(self.loading)
        self.main = QtWidgets.QWidget()
        self.main.setStyleSheet("QLabel#info_lbl{\n"
"    font: 24px \"Sylfaen\";\n"
"    color: white;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QLabel#title_lbl{\n"
"    font: 30px \"Sylfaen\";\n"
"    color: white;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 18px \"Sylfaen\";\n"
"    color: white;\n"
"    background-color:#2F3538;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font: 18px \"Sylfaen\";\n"
"    color: white;\n"
"    background-color:#404040;\n"
"}\n"
"\n"
"QComboBox {\n"
"    font: 18px \"Sylfaen\";\n"
"    color: white;\n"
"    background-color:#2F3538;\n"
"    selection-background-color:#2F3538;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    font: 18px \"Sylfaen\";\n"
"    color: white;\n"
"    background-color:#2F3538;\n"
"    selection-background-color: #404040;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    font: 18px \"Sylfaen\";\n"
"    color: white;\n"
"    background:#404040;\n"
"}\n"
"\n"
"QPushButton#settings_btn{\n"
"    font: 18px \"Sylfaen\";\n"
"    color: white;\n"
"    qproperty-iconSize: 30px;\n"
"}\n"
"\n"
"QLabel#perk1_lbl {\n"
"    font: 20px \"Sylfaen\";\n"
"    color: #6e6d6d;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLabel#perk2_lbl {\n"
"    font: 20px \"Sylfaen\";\n"
"    color: #6e6d6d;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLabel#perk3_lbl {\n"
"    font: 20px \"Sylfaen\";\n"
"    color: #6e6d6d;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QLabel#perk4_lbl {\n"
"    font: 20px \"Sylfaen\";\n"
"    color: #6e6d6d;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QLabel#date_lbl {\n"
"    font: 16px \"Sylfaen\";\n"
"    color: #6e6d6d;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QListWidget{\n"
"    font: 18px \"Sylfaen\";\n"
"    color: white;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    outline: 0;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    font: 18px \"Sylfaen\";\n"
"    color: white;\n"
"    background-color: rgba(47, 53, 56, 0.3);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    font: 18px \"Sylfaen\";\n"
"    color: white;\n"
"    background-color: rgba(64, 64, 64, 0.3);\n"
"}\n"
"")
        self.main.setObjectName("main")
        self.perk1_frame = QtWidgets.QLabel(self.main)
        self.perk1_frame.setGeometry(QtCore.QRect(545, 75, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk1_frame.sizePolicy().hasHeightForWidth())
        self.perk1_frame.setSizePolicy(sizePolicy)
        self.perk1_frame.setMinimumSize(QtCore.QSize(150, 150))
        self.perk1_frame.setMaximumSize(QtCore.QSize(150, 150))
        self.perk1_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.perk1_frame.setToolTip("")
        self.perk1_frame.setWhatsThis("")
        self.perk1_frame.setStyleSheet("")
        self.perk1_frame.setText("")
        self.perk1_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.perk1_frame.setObjectName("perk1_frame")
        self.perk1_lbl = QtWidgets.QLabel(self.main)
        self.perk1_lbl.setGeometry(QtCore.QRect(480, 210, 280, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk1_lbl.sizePolicy().hasHeightForWidth())
        self.perk1_lbl.setSizePolicy(sizePolicy)
        self.perk1_lbl.setStyleSheet("")
        self.perk1_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.perk1_lbl.setObjectName("perk1_lbl")
        self.perks_combo = QtWidgets.QComboBox(self.main)
        self.perks_combo.setGeometry(QtCore.QRect(25, 80, 280, 30))
        self.perks_combo.setStyleSheet("")
        self.perks_combo.setObjectName("perks_combo")
        self.perk2_lbl = QtWidgets.QLabel(self.main)
        self.perk2_lbl.setGeometry(QtCore.QRect(330, 360, 280, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk2_lbl.sizePolicy().hasHeightForWidth())
        self.perk2_lbl.setSizePolicy(sizePolicy)
        self.perk2_lbl.setStyleSheet("")
        self.perk2_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.perk2_lbl.setObjectName("perk2_lbl")
        self.perks_list = QtWidgets.QListWidget(self.main)
        self.perks_list.setGeometry(QtCore.QRect(25, 120, 280, 390))
        self.perks_list.setStyleSheet("")
        self.perks_list.setObjectName("perks_list")
        self.info_lbl = QtWidgets.QLabel(self.main)
        self.info_lbl.setGeometry(QtCore.QRect(25, 40, 250, 30))
        self.info_lbl.setStyleSheet("")
        self.info_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.info_lbl.setObjectName("info_lbl")
        self.bg_1 = QtWidgets.QLabel(self.main)
        self.bg_1.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.bg_1.setStyleSheet("")
        self.bg_1.setText("")
        self.bg_1.setScaledContents(True)
        self.bg_1.setObjectName("bg_1")
        self.settings_btn = QtWidgets.QPushButton(self.main)
        self.settings_btn.setGeometry(QtCore.QRect(150, 520, 30, 30))
        self.settings_btn.setStyleSheet("")
        self.settings_btn.setText("")
        self.settings_btn.setObjectName("settings_btn")
        self.perk3_img = QtWidgets.QLabel(self.main)
        self.perk3_img.setGeometry(QtCore.QRect(720, 250, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk3_img.sizePolicy().hasHeightForWidth())
        self.perk3_img.setSizePolicy(sizePolicy)
        self.perk3_img.setMinimumSize(QtCore.QSize(100, 100))
        self.perk3_img.setMaximumSize(QtCore.QSize(100, 100))
        self.perk3_img.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.perk3_img.setStyleSheet("")
        self.perk3_img.setText("")
        self.perk3_img.setAlignment(QtCore.Qt.AlignCenter)
        self.perk3_img.setObjectName("perk3_img")
        self.perk4_lbl = QtWidgets.QLabel(self.main)
        self.perk4_lbl.setGeometry(QtCore.QRect(480, 510, 280, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk4_lbl.sizePolicy().hasHeightForWidth())
        self.perk4_lbl.setSizePolicy(sizePolicy)
        self.perk4_lbl.setStyleSheet("")
        self.perk4_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.perk4_lbl.setObjectName("perk4_lbl")
        self.perk3_frame = QtWidgets.QLabel(self.main)
        self.perk3_frame.setGeometry(QtCore.QRect(695, 225, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk3_frame.sizePolicy().hasHeightForWidth())
        self.perk3_frame.setSizePolicy(sizePolicy)
        self.perk3_frame.setMinimumSize(QtCore.QSize(150, 150))
        self.perk3_frame.setMaximumSize(QtCore.QSize(150, 150))
        self.perk3_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.perk3_frame.setToolTip("")
        self.perk3_frame.setWhatsThis("")
        self.perk3_frame.setStyleSheet("")
        self.perk3_frame.setText("")
        self.perk3_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.perk3_frame.setObjectName("perk3_frame")
        self.perk4_img = QtWidgets.QLabel(self.main)
        self.perk4_img.setGeometry(QtCore.QRect(570, 400, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk4_img.sizePolicy().hasHeightForWidth())
        self.perk4_img.setSizePolicy(sizePolicy)
        self.perk4_img.setMinimumSize(QtCore.QSize(100, 100))
        self.perk4_img.setMaximumSize(QtCore.QSize(100, 100))
        self.perk4_img.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.perk4_img.setStyleSheet("")
        self.perk4_img.setText("")
        self.perk4_img.setAlignment(QtCore.Qt.AlignCenter)
        self.perk4_img.setObjectName("perk4_img")
        self.perk4_frame = QtWidgets.QLabel(self.main)
        self.perk4_frame.setGeometry(QtCore.QRect(545, 375, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk4_frame.sizePolicy().hasHeightForWidth())
        self.perk4_frame.setSizePolicy(sizePolicy)
        self.perk4_frame.setMinimumSize(QtCore.QSize(150, 150))
        self.perk4_frame.setMaximumSize(QtCore.QSize(150, 150))
        self.perk4_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.perk4_frame.setToolTip("")
        self.perk4_frame.setWhatsThis("")
        self.perk4_frame.setStyleSheet("")
        self.perk4_frame.setText("")
        self.perk4_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.perk4_frame.setObjectName("perk4_frame")
        self.perk3_lbl = QtWidgets.QLabel(self.main)
        self.perk3_lbl.setGeometry(QtCore.QRect(630, 360, 280, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk3_lbl.sizePolicy().hasHeightForWidth())
        self.perk3_lbl.setSizePolicy(sizePolicy)
        self.perk3_lbl.setStyleSheet("")
        self.perk3_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.perk3_lbl.setObjectName("perk3_lbl")
        self.date_lbl = QtWidgets.QLabel(self.main)
        self.date_lbl.setGeometry(QtCore.QRect(565, 565, 330, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_lbl.sizePolicy().hasHeightForWidth())
        self.date_lbl.setSizePolicy(sizePolicy)
        self.date_lbl.setStyleSheet("")
        self.date_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.date_lbl.setObjectName("date_lbl")
        self.remove_btn = QtWidgets.QPushButton(self.main)
        self.remove_btn.setGeometry(QtCore.QRect(185, 520, 120, 30))
        self.remove_btn.setObjectName("remove_btn")
        self.perk1_img = QtWidgets.QLabel(self.main)
        self.perk1_img.setGeometry(QtCore.QRect(570, 100, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk1_img.sizePolicy().hasHeightForWidth())
        self.perk1_img.setSizePolicy(sizePolicy)
        self.perk1_img.setMinimumSize(QtCore.QSize(100, 100))
        self.perk1_img.setMaximumSize(QtCore.QSize(100, 100))
        self.perk1_img.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.perk1_img.setToolTip("")
        self.perk1_img.setWhatsThis("")
        self.perk1_img.setStyleSheet("")
        self.perk1_img.setText("")
        self.perk1_img.setAlignment(QtCore.Qt.AlignCenter)
        self.perk1_img.setObjectName("perk1_img")
        self.add_btn = QtWidgets.QPushButton(self.main)
        self.add_btn.setGeometry(QtCore.QRect(25, 520, 120, 30))
        self.add_btn.setStyleSheet("")
        self.add_btn.setObjectName("add_btn")
        self.perk2_frame = QtWidgets.QLabel(self.main)
        self.perk2_frame.setGeometry(QtCore.QRect(395, 225, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk2_frame.sizePolicy().hasHeightForWidth())
        self.perk2_frame.setSizePolicy(sizePolicy)
        self.perk2_frame.setMinimumSize(QtCore.QSize(150, 150))
        self.perk2_frame.setMaximumSize(QtCore.QSize(150, 150))
        self.perk2_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.perk2_frame.setToolTip("")
        self.perk2_frame.setWhatsThis("")
        self.perk2_frame.setStyleSheet("")
        self.perk2_frame.setText("")
        self.perk2_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.perk2_frame.setObjectName("perk2_frame")
        self.title_lbl = QtWidgets.QLabel(self.main)
        self.title_lbl.setGeometry(QtCore.QRect(470, 10, 300, 35))
        self.title_lbl.setStyleSheet("")
        self.title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lbl.setObjectName("title_lbl")
        self.perk2_img = QtWidgets.QLabel(self.main)
        self.perk2_img.setGeometry(QtCore.QRect(420, 250, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk2_img.sizePolicy().hasHeightForWidth())
        self.perk2_img.setSizePolicy(sizePolicy)
        self.perk2_img.setMinimumSize(QtCore.QSize(100, 100))
        self.perk2_img.setMaximumSize(QtCore.QSize(100, 100))
        self.perk2_img.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.perk2_img.setStyleSheet("")
        self.perk2_img.setText("")
        self.perk2_img.setAlignment(QtCore.Qt.AlignCenter)
        self.perk2_img.setObjectName("perk2_img")
        self.bg_1.raise_()
        self.perk1_frame.raise_()
        self.perk1_lbl.raise_()
        self.perks_combo.raise_()
        self.perk2_lbl.raise_()
        self.perks_list.raise_()
        self.info_lbl.raise_()
        self.settings_btn.raise_()
        self.perk3_img.raise_()
        self.perk4_lbl.raise_()
        self.perk3_frame.raise_()
        self.perk4_img.raise_()
        self.perk4_frame.raise_()
        self.perk3_lbl.raise_()
        self.date_lbl.raise_()
        self.remove_btn.raise_()
        self.perk1_img.raise_()
        self.add_btn.raise_()
        self.perk2_frame.raise_()
        self.title_lbl.raise_()
        self.perk2_img.raise_()
        self.stackedWidget.addWidget(self.main)
        self.settings = QtWidgets.QWidget()
        self.settings.setStyleSheet("QLabel#settings_lbl {\n"
"    color: white;\n"
"    font: 24px \"Sylfaen\";\n"
"}\n"
"\n"
"QLabel#authors_lbl {\n"
"    color: white;\n"
"    font: 24px \"Sylfaen\";\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;\n"
"    font: 18px \"Sylfaen\";\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    font: 18px \"Sylfaen\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    font: 18px \"Sylfaen\";\n"
"    background-color:#2F3538;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    font: 18px \"Sylfaen\";\n"
"    background-color:#404040;\n"
"}\n"
"\n"
"QLabel#bg_2 {\n"
"    border: 1px solid rgba(255, 255, 255, 0.2);\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: white;\n"
"    font: 18px \"Sylfaen\";\n"
"    background-color:#2F3538;\n"
"    selection-background-color:#2F3538;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: white;\n"
"    font: 18px \"Sylfaen\";\n"
"    background-color:#2F3538;\n"
"    selection-background-color: #404040;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QScrollBar:vertical {    \n"
"    color: white;\n"
"    font: 18px \"Sylfaen\";\n"
"    background:#404040;\n"
"}")
        self.settings.setObjectName("settings")
        self.startup_check = QtWidgets.QCheckBox(self.settings)
        self.startup_check.setGeometry(QtCore.QRect(20, 80, 600, 40))
        self.startup_check.setChecked(False)
        self.startup_check.setObjectName("startup_check")
        self.reset_lbl = QtWidgets.QLabel(self.settings)
        self.reset_lbl.setGeometry(QtCore.QRect(170, 220, 600, 50))
        self.reset_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.reset_lbl.setWordWrap(True)
        self.reset_lbl.setObjectName("reset_lbl")
        self.reload_btn = QtWidgets.QPushButton(self.settings)
        self.reload_btn.setGeometry(QtCore.QRect(20, 280, 140, 30))
        self.reload_btn.setCheckable(False)
        self.reload_btn.setObjectName("reload_btn")
        self.bg_2 = QtWidgets.QLabel(self.settings)
        self.bg_2.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.bg_2.setStyleSheet("")
        self.bg_2.setText("")
        self.bg_2.setScaledContents(True)
        self.bg_2.setObjectName("bg_2")
        self.tray_check = QtWidgets.QCheckBox(self.settings)
        self.tray_check.setGeometry(QtCore.QRect(20, 40, 600, 40))
        self.tray_check.setChecked(False)
        self.tray_check.setObjectName("tray_check")
        self.save_btn = QtWidgets.QPushButton(self.settings)
        self.save_btn.setGeometry(QtCore.QRect(360, 550, 80, 30))
        self.save_btn.setObjectName("save_btn")
        self.settings_lbl = QtWidgets.QLabel(self.settings)
        self.settings_lbl.setGeometry(QtCore.QRect(290, 5, 320, 35))
        self.settings_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_lbl.setObjectName("settings_lbl")
        self.notif_combo = QtWidgets.QComboBox(self.settings)
        self.notif_combo.setGeometry(QtCore.QRect(20, 130, 50, 30))
        self.notif_combo.setStyleSheet("")
        self.notif_combo.setObjectName("notif_combo")
        self.notif_combo.addItem("")
        self.notif_combo.addItem("")
        self.notif_combo.addItem("")
        self.notif_combo.addItem("")
        self.back_btn = QtWidgets.QPushButton(self.settings)
        self.back_btn.setGeometry(QtCore.QRect(460, 550, 80, 30))
        self.back_btn.setObjectName("back_btn")
        self.reload_lbl = QtWidgets.QLabel(self.settings)
        self.reload_lbl.setGeometry(QtCore.QRect(170, 270, 600, 50))
        self.reload_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.reload_lbl.setWordWrap(True)
        self.reload_lbl.setObjectName("reload_lbl")
        self.reset_btn = QtWidgets.QPushButton(self.settings)
        self.reset_btn.setGeometry(QtCore.QRect(20, 230, 140, 30))
        self.reset_btn.setCheckable(False)
        self.reset_btn.setObjectName("reset_btn")
        self.refr_combo = QtWidgets.QComboBox(self.settings)
        self.refr_combo.setGeometry(QtCore.QRect(20, 180, 50, 30))
        self.refr_combo.setStyleSheet("")
        self.refr_combo.setObjectName("refr_combo")
        self.refr_combo.addItem("")
        self.refr_combo.addItem("")
        self.refr_combo.addItem("")
        self.refr_combo.addItem("")
        self.notif_lbl = QtWidgets.QLabel(self.settings)
        self.notif_lbl.setGeometry(QtCore.QRect(80, 120, 600, 50))
        self.notif_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.notif_lbl.setWordWrap(True)
        self.notif_lbl.setObjectName("notif_lbl")
        self.refr_lbl = QtWidgets.QLabel(self.settings)
        self.refr_lbl.setGeometry(QtCore.QRect(80, 170, 600, 50))
        self.refr_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.refr_lbl.setWordWrap(True)
        self.refr_lbl.setObjectName("refr_lbl")
        self.authors_lbl = QtWidgets.QLabel(self.settings)
        self.authors_lbl.setGeometry(QtCore.QRect(290, 320, 320, 35))
        self.authors_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.authors_lbl.setObjectName("authors_lbl")
        self.author_lbl = QtWidgets.QLabel(self.settings)
        self.author_lbl.setGeometry(QtCore.QRect(20, 360, 600, 50))
        self.author_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.author_lbl.setWordWrap(True)
        self.author_lbl.setObjectName("author_lbl")
        self.designer_lbl = QtWidgets.QLabel(self.settings)
        self.designer_lbl.setGeometry(QtCore.QRect(20, 410, 600, 50))
        self.designer_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.designer_lbl.setWordWrap(True)
        self.designer_lbl.setObjectName("designer_lbl")
        self.bg_2.raise_()
        self.startup_check.raise_()
        self.reset_lbl.raise_()
        self.reload_btn.raise_()
        self.tray_check.raise_()
        self.save_btn.raise_()
        self.settings_lbl.raise_()
        self.notif_combo.raise_()
        self.back_btn.raise_()
        self.reload_lbl.raise_()
        self.reset_btn.raise_()
        self.refr_combo.raise_()
        self.notif_lbl.raise_()
        self.refr_lbl.raise_()
        self.authors_lbl.raise_()
        self.author_lbl.raise_()
        self.designer_lbl.raise_()
        self.stackedWidget.addWidget(self.settings)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shrine Checker"))
        self.msg_lbl.setText(_translate("MainWindow", "Progress message"))
        self.done_btn.setText(_translate("MainWindow", "Done"))
        self.wait_lbl.setText(_translate("MainWindow", "Please wait..."))
        self.perk1_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.perk2_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.info_lbl.setText(_translate("MainWindow", "Desired perks:"))
        self.perk4_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.perk3_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.date_lbl.setText(_translate("MainWindow", "Shrine refreshes on DD/MM/YY GMT+0"))
        self.remove_btn.setText(_translate("MainWindow", "Remove"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.title_lbl.setText(_translate("MainWindow", "Shrine of Secrets"))
        self.startup_check.setText(_translate("MainWindow", "Run with startup - Adds/Removes shortcut to the application executable to the Autostart direcory."))
        self.reset_lbl.setText(_translate("MainWindow", "Redownload local database of perks"))
        self.reload_btn.setText(_translate("MainWindow", "Reload shrine"))
        self.tray_check.setText(_translate("MainWindow", "Minimize to tray on exit - Enables/Disables working in the background."))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.settings_lbl.setText(_translate("MainWindow", "Settings"))
        self.notif_combo.setItemText(0, _translate("MainWindow", "2"))
        self.notif_combo.setItemText(1, _translate("MainWindow", "4"))
        self.notif_combo.setItemText(2, _translate("MainWindow", "6"))
        self.notif_combo.setItemText(3, _translate("MainWindow", "8"))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        self.reload_lbl.setText(_translate("MainWindow", "Force shrine reload"))
        self.reset_btn.setText(_translate("MainWindow", "Reload perks"))
        self.refr_combo.setItemText(0, _translate("MainWindow", "2"))
        self.refr_combo.setItemText(1, _translate("MainWindow", "4"))
        self.refr_combo.setItemText(2, _translate("MainWindow", "6"))
        self.refr_combo.setItemText(3, _translate("MainWindow", "8"))
        self.notif_lbl.setText(_translate("MainWindow", "Notification interval (hours) - Time between displaying a notification about matching perks."))
        self.refr_lbl.setText(_translate("MainWindow", "Auto-refresh interval (hours) - Time between checking for new shrine."))
        self.authors_lbl.setText(_translate("MainWindow", "App authors"))
        self.author_lbl.setText(_translate("MainWindow", "App author- Michał Kowal, michal.kowal.66@gmail.com, r/virtozenho"))
        self.designer_lbl.setText(_translate("MainWindow", "Graphics designer - Urszula Kowal, @kowalowna"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
