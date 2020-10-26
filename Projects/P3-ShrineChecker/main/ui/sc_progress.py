# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sc_progress.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(360, 150))
        Dialog.setMaximumSize(QtCore.QSize(360, 150))
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(QtCore.QRect(0, 0, 360, 150))
        self.bg.setStyleSheet("")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.progress_bar = QtWidgets.QProgressBar(Dialog)
        self.progress_bar.setGeometry(QtCore.QRect(20, 65, 320, 30))
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar.setObjectName("progress_bar")
        self.wait_lbl = QtWidgets.QLabel(Dialog)
        self.wait_lbl.setGeometry(QtCore.QRect(0, 5, 360, 20))
        self.wait_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.wait_lbl.setObjectName("wait_lbl")
        self.msg_lbl = QtWidgets.QLabel(Dialog)
        self.msg_lbl.setGeometry(QtCore.QRect(20, 30, 320, 25))
        self.msg_lbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.msg_lbl.setWordWrap(True)
        self.msg_lbl.setObjectName("msg_lbl")
        self.close_btn = QtWidgets.QPushButton(Dialog)
        self.close_btn.setGeometry(QtCore.QRect(140, 105, 80, 30))
        self.close_btn.setStyleSheet("")
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.wait_lbl.setText(_translate("Dialog", "Please wait..."))
        self.msg_lbl.setText(_translate("Dialog", "Progress message"))
        self.close_btn.setText(_translate("Dialog", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
