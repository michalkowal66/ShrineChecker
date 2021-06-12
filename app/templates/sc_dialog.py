# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\app\designer\sc_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(520, 200))
        Dialog.setMaximumSize(QtCore.QSize(520, 1200))
        Dialog.setStyleSheet("QLabel#bg {\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QLabel#info_lbl{\n"
"    color: white;\n"
"    font: 20px \"Sylfaen\";\n"
"}\n"
"QLabel#description_lbl {\n"
"    color: white;\n"
"    font: 16px \"Sylfaen\";\n"
"}\n"
"")
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(QtCore.QRect(0, 0, 520, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bg.sizePolicy().hasHeightForWidth())
        self.bg.setSizePolicy(sizePolicy)
        self.bg.setMinimumSize(QtCore.QSize(520, 200))
        self.bg.setMaximumSize(QtCore.QSize(520, 16777215))
        self.bg.setStyleSheet("")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.info_lbl = QtWidgets.QLabel(Dialog)
        self.info_lbl.setGeometry(QtCore.QRect(20, 5, 480, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_lbl.sizePolicy().hasHeightForWidth())
        self.info_lbl.setSizePolicy(sizePolicy)
        self.info_lbl.setMinimumSize(QtCore.QSize(480, 0))
        self.info_lbl.setMaximumSize(QtCore.QSize(480, 16777215))
        self.info_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.info_lbl.setObjectName("info_lbl")
        self.description_lbl = QtWidgets.QLabel(Dialog)
        self.description_lbl.setGeometry(QtCore.QRect(20, 30, 480, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description_lbl.sizePolicy().hasHeightForWidth())
        self.description_lbl.setSizePolicy(sizePolicy)
        self.description_lbl.setMinimumSize(QtCore.QSize(480, 150))
        self.description_lbl.setMaximumSize(QtCore.QSize(480, 1200))
        self.description_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_lbl.setWordWrap(True)
        self.description_lbl.setObjectName("description_lbl")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.info_lbl.setText(_translate("Dialog", "Perk description:"))
        self.description_lbl.setText(_translate("Dialog", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
