# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sc_notification.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 600)
        Dialog.setMinimumSize(QtCore.QSize(380, 140))
        Dialog.setMaximumSize(QtCore.QSize(380, 600))
        Dialog.setStyleSheet("QLabel#perk1_lbl {\n"
"    font: 20px \"Sylfaen\";\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel#msg1_lbl {\n"
"    font: 16px \"Sylfaen\";\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel#perk2_lbl {\n"
"    font: 20px \"Sylfaen\";\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel#msg2_lbl {\n"
"    font: 16px \"Sylfaen\";\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel#perk3_lbl {\n"
"    font: 20px \"Sylfaen\";\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel#msg3_lbl {\n"
"    font: 16px \"Sylfaen\";\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel#perk4_lbl {\n"
"    font: 20px \"Sylfaen\";\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel#msg4_lbl {\n"
"    font: 16px \"Sylfaen\";\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font: 18px \"Sylfaen\";\n"
"    background-color:#2F3538;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font: 18px \"Sylfaen\";\n"
"    background-color:#404040;\n"
"    color: white;\n"
"}\n"
"")
        self.msg4_lbl = QtWidgets.QLabel(Dialog)
        self.msg4_lbl.setGeometry(QtCore.QRect(130, 520, 250, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg4_lbl.sizePolicy().hasHeightForWidth())
        self.msg4_lbl.setSizePolicy(sizePolicy)
        self.msg4_lbl.setStyleSheet("")
        self.msg4_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.msg4_lbl.setWordWrap(True)
        self.msg4_lbl.setObjectName("msg4_lbl")
        self.img1 = QtWidgets.QLabel(Dialog)
        self.img1.setGeometry(QtCore.QRect(25, 60, 100, 100))
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
        self.perk3_lbl = QtWidgets.QLabel(Dialog)
        self.perk3_lbl.setGeometry(QtCore.QRect(130, 340, 250, 35))
        self.perk3_lbl.setStyleSheet("")
        self.perk3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk3_lbl.setObjectName("perk3_lbl")
        self.perk1_lbl = QtWidgets.QLabel(Dialog)
        self.perk1_lbl.setGeometry(QtCore.QRect(130, 60, 250, 35))
        self.perk1_lbl.setStyleSheet("")
        self.perk1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk1_lbl.setObjectName("perk1_lbl")
        self.img3 = QtWidgets.QLabel(Dialog)
        self.img3.setGeometry(QtCore.QRect(25, 340, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img3.sizePolicy().hasHeightForWidth())
        self.img3.setSizePolicy(sizePolicy)
        self.img3.setMinimumSize(QtCore.QSize(100, 100))
        self.img3.setMaximumSize(QtCore.QSize(100, 100))
        self.img3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.img3.setToolTip("")
        self.img3.setWhatsThis("")
        self.img3.setStyleSheet("")
        self.img3.setText("")
        self.img3.setAlignment(QtCore.Qt.AlignCenter)
        self.img3.setObjectName("img3")
        self.msg3_lbl = QtWidgets.QLabel(Dialog)
        self.msg3_lbl.setGeometry(QtCore.QRect(130, 380, 250, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg3_lbl.sizePolicy().hasHeightForWidth())
        self.msg3_lbl.setSizePolicy(sizePolicy)
        self.msg3_lbl.setStyleSheet("")
        self.msg3_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.msg3_lbl.setWordWrap(True)
        self.msg3_lbl.setObjectName("msg3_lbl")
        self.msg2_lbl = QtWidgets.QLabel(Dialog)
        self.msg2_lbl.setGeometry(QtCore.QRect(130, 240, 250, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg2_lbl.sizePolicy().hasHeightForWidth())
        self.msg2_lbl.setSizePolicy(sizePolicy)
        self.msg2_lbl.setStyleSheet("")
        self.msg2_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.msg2_lbl.setWordWrap(True)
        self.msg2_lbl.setObjectName("msg2_lbl")
        self.img4 = QtWidgets.QLabel(Dialog)
        self.img4.setGeometry(QtCore.QRect(25, 480, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img4.sizePolicy().hasHeightForWidth())
        self.img4.setSizePolicy(sizePolicy)
        self.img4.setMinimumSize(QtCore.QSize(100, 100))
        self.img4.setMaximumSize(QtCore.QSize(100, 100))
        self.img4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.img4.setToolTip("")
        self.img4.setWhatsThis("")
        self.img4.setStyleSheet("")
        self.img4.setText("")
        self.img4.setAlignment(QtCore.Qt.AlignCenter)
        self.img4.setObjectName("img4")
        self.img2 = QtWidgets.QLabel(Dialog)
        self.img2.setGeometry(QtCore.QRect(25, 200, 100, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img2.sizePolicy().hasHeightForWidth())
        self.img2.setSizePolicy(sizePolicy)
        self.img2.setMinimumSize(QtCore.QSize(100, 100))
        self.img2.setMaximumSize(QtCore.QSize(100, 100))
        self.img2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.img2.setToolTip("")
        self.img2.setWhatsThis("")
        self.img2.setStyleSheet("")
        self.img2.setText("")
        self.img2.setAlignment(QtCore.Qt.AlignCenter)
        self.img2.setObjectName("img2")
        self.perk4_lbl = QtWidgets.QLabel(Dialog)
        self.perk4_lbl.setGeometry(QtCore.QRect(130, 480, 250, 35))
        self.perk4_lbl.setStyleSheet("")
        self.perk4_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk4_lbl.setObjectName("perk4_lbl")
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(QtCore.QRect(0, 0, 380, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bg.sizePolicy().hasHeightForWidth())
        self.bg.setSizePolicy(sizePolicy)
        self.bg.setStyleSheet("")
        self.bg.setText("")
        self.bg.setScaledContents(False)
        self.bg.setObjectName("bg")
        self.msg1_lbl = QtWidgets.QLabel(Dialog)
        self.msg1_lbl.setGeometry(QtCore.QRect(130, 100, 250, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg1_lbl.sizePolicy().hasHeightForWidth())
        self.msg1_lbl.setSizePolicy(sizePolicy)
        self.msg1_lbl.setStyleSheet("")
        self.msg1_lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.msg1_lbl.setWordWrap(True)
        self.msg1_lbl.setObjectName("msg1_lbl")
        self.perk2_lbl = QtWidgets.QLabel(Dialog)
        self.perk2_lbl.setGeometry(QtCore.QRect(130, 200, 250, 35))
        self.perk2_lbl.setStyleSheet("")
        self.perk2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk2_lbl.setObjectName("perk2_lbl")
        self.show_btn = QtWidgets.QPushButton(Dialog)
        self.show_btn.setGeometry(QtCore.QRect(110, 10, 80, 30))
        self.show_btn.setStyleSheet("")
        self.show_btn.setObjectName("show_btn")
        self.close_btn = QtWidgets.QPushButton(Dialog)
        self.close_btn.setGeometry(QtCore.QRect(200, 10, 80, 30))
        self.close_btn.setStyleSheet("")
        self.close_btn.setObjectName("close_btn")
        self.frame1 = QtWidgets.QLabel(Dialog)
        self.frame1.setGeometry(QtCore.QRect(0, 35, 150, 150))
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
        self.frame2 = QtWidgets.QLabel(Dialog)
        self.frame2.setGeometry(QtCore.QRect(0, 175, 150, 150))
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
        self.frame3 = QtWidgets.QLabel(Dialog)
        self.frame3.setGeometry(QtCore.QRect(0, 315, 150, 150))
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
        self.frame4 = QtWidgets.QLabel(Dialog)
        self.frame4.setGeometry(QtCore.QRect(0, 455, 150, 150))
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
        self.msg4_lbl.raise_()
        self.img1.raise_()
        self.perk3_lbl.raise_()
        self.perk1_lbl.raise_()
        self.img3.raise_()
        self.msg3_lbl.raise_()
        self.msg2_lbl.raise_()
        self.img4.raise_()
        self.img2.raise_()
        self.perk4_lbl.raise_()
        self.msg1_lbl.raise_()
        self.perk2_lbl.raise_()
        self.show_btn.raise_()
        self.close_btn.raise_()
        self.frame1.raise_()
        self.frame2.raise_()
        self.frame3.raise_()
        self.frame4.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.msg4_lbl.setText(_translate("Dialog", "message"))
        self.perk3_lbl.setText(_translate("Dialog", "Perk"))
        self.perk1_lbl.setText(_translate("Dialog", "Perk"))
        self.msg3_lbl.setText(_translate("Dialog", "message"))
        self.msg2_lbl.setText(_translate("Dialog", "message"))
        self.perk4_lbl.setText(_translate("Dialog", "Perk"))
        self.msg1_lbl.setText(_translate("Dialog", "message"))
        self.perk2_lbl.setText(_translate("Dialog", "Perk"))
        self.show_btn.setText(_translate("Dialog", "Show"))
        self.close_btn.setText(_translate("Dialog", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
