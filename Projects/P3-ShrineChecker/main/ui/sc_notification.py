# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sc_notification.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(350, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(350, 140))
        Form.setMaximumSize(QtCore.QSize(350, 560))
        Form.setStyleSheet("font: 12pt \"Sylfaen\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.bg = QtWidgets.QLabel(Form)
        self.bg.setGeometry(QtCore.QRect(0, 0, 900, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bg.sizePolicy().hasHeightForWidth())
        self.bg.setSizePolicy(sizePolicy)
        self.bg.setStyleSheet("")
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("../rsc/bg.png"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.img1 = QtWidgets.QLabel(Form)
        self.img1.setGeometry(QtCore.QRect(20, 20, 100, 100))
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
        self.perk1_lbl = QtWidgets.QLabel(Form)
        self.perk1_lbl.setGeometry(QtCore.QRect(130, 20, 200, 35))
        self.perk1_lbl.setStyleSheet("font: 14pt \"Sylfaen\";\n"
"background-color: rgba(0, 0, 0, 0);")
        self.perk1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk1_lbl.setObjectName("perk1_lbl")
        self.msg1_lbl = QtWidgets.QLabel(Form)
        self.msg1_lbl.setGeometry(QtCore.QRect(140, 60, 200, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg1_lbl.sizePolicy().hasHeightForWidth())
        self.msg1_lbl.setSizePolicy(sizePolicy)
        self.msg1_lbl.setStyleSheet("")
        self.msg1_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.msg1_lbl.setWordWrap(True)
        self.msg1_lbl.setObjectName("msg1_lbl")
        self.img2 = QtWidgets.QLabel(Form)
        self.img2.setGeometry(QtCore.QRect(20, 160, 100, 100))
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
        self.perk2_lbl = QtWidgets.QLabel(Form)
        self.perk2_lbl.setGeometry(QtCore.QRect(130, 160, 200, 35))
        self.perk2_lbl.setStyleSheet("font: 14pt \"Sylfaen\";\n"
"background-color: rgba(0, 0, 0, 0);")
        self.perk2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk2_lbl.setObjectName("perk2_lbl")
        self.msg2_lbl = QtWidgets.QLabel(Form)
        self.msg2_lbl.setGeometry(QtCore.QRect(140, 200, 200, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg2_lbl.sizePolicy().hasHeightForWidth())
        self.msg2_lbl.setSizePolicy(sizePolicy)
        self.msg2_lbl.setStyleSheet("")
        self.msg2_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.msg2_lbl.setWordWrap(True)
        self.msg2_lbl.setObjectName("msg2_lbl")
        self.img3 = QtWidgets.QLabel(Form)
        self.img3.setGeometry(QtCore.QRect(20, 300, 100, 100))
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
        self.msg3_lbl = QtWidgets.QLabel(Form)
        self.msg3_lbl.setGeometry(QtCore.QRect(140, 340, 200, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg3_lbl.sizePolicy().hasHeightForWidth())
        self.msg3_lbl.setSizePolicy(sizePolicy)
        self.msg3_lbl.setStyleSheet("")
        self.msg3_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.msg3_lbl.setWordWrap(True)
        self.msg3_lbl.setObjectName("msg3_lbl")
        self.perk3_lbl = QtWidgets.QLabel(Form)
        self.perk3_lbl.setGeometry(QtCore.QRect(130, 300, 200, 35))
        self.perk3_lbl.setStyleSheet("font: 14pt \"Sylfaen\";\n"
"background-color: rgba(0, 0, 0, 0);")
        self.perk3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk3_lbl.setObjectName("perk3_lbl")
        self.perk4_lbl = QtWidgets.QLabel(Form)
        self.perk4_lbl.setGeometry(QtCore.QRect(130, 440, 200, 35))
        self.perk4_lbl.setStyleSheet("font: 14pt \"Sylfaen\";\n"
"background-color: rgba(0, 0, 0, 0);")
        self.perk4_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.perk4_lbl.setObjectName("perk4_lbl")
        self.img4 = QtWidgets.QLabel(Form)
        self.img4.setGeometry(QtCore.QRect(20, 440, 100, 100))
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
        self.msg4_lbl = QtWidgets.QLabel(Form)
        self.msg4_lbl.setGeometry(QtCore.QRect(140, 480, 200, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg4_lbl.sizePolicy().hasHeightForWidth())
        self.msg4_lbl.setSizePolicy(sizePolicy)
        self.msg4_lbl.setStyleSheet("")
        self.msg4_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.msg4_lbl.setWordWrap(True)
        self.msg4_lbl.setObjectName("msg4_lbl")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.perk1_lbl.setText(_translate("Form", "Perk"))
        self.msg1_lbl.setText(_translate("Form", "message"))
        self.perk2_lbl.setText(_translate("Form", "Perk"))
        self.msg2_lbl.setText(_translate("Form", "message"))
        self.msg3_lbl.setText(_translate("Form", "message"))
        self.perk3_lbl.setText(_translate("Form", "Perk"))
        self.perk4_lbl.setText(_translate("Form", "Perk"))
        self.msg4_lbl.setText(_translate("Form", "message"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
