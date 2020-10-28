# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\designer\sc_progress.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProgressBarTemplate(object):
    def setupUi(self, ProgressBarTemplate):
        ProgressBarTemplate.setObjectName("ProgressBarTemplate")
        ProgressBarTemplate.resize(360, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressBarTemplate.sizePolicy().hasHeightForWidth())
        ProgressBarTemplate.setSizePolicy(sizePolicy)
        ProgressBarTemplate.setMinimumSize(QtCore.QSize(360, 150))
        ProgressBarTemplate.setMaximumSize(QtCore.QSize(360, 150))
        self.bg = QtWidgets.QLabel(ProgressBarTemplate)
        self.bg.setGeometry(QtCore.QRect(0, 0, 360, 150))
        self.bg.setStyleSheet("")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.progress_bar = QtWidgets.QProgressBar(ProgressBarTemplate)
        self.progress_bar.setGeometry(QtCore.QRect(20, 65, 320, 30))
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar.setObjectName("progress_bar")
        self.wait_lbl = QtWidgets.QLabel(ProgressBarTemplate)
        self.wait_lbl.setGeometry(QtCore.QRect(0, 5, 360, 20))
        self.wait_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.wait_lbl.setObjectName("wait_lbl")
        self.msg_lbl = QtWidgets.QLabel(ProgressBarTemplate)
        self.msg_lbl.setGeometry(QtCore.QRect(20, 30, 320, 25))
        self.msg_lbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.msg_lbl.setWordWrap(True)
        self.msg_lbl.setObjectName("msg_lbl")
        self.close_btn = QtWidgets.QPushButton(ProgressBarTemplate)
        self.close_btn.setGeometry(QtCore.QRect(140, 105, 80, 30))
        self.close_btn.setStyleSheet("")
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(ProgressBarTemplate)
        QtCore.QMetaObject.connectSlotsByName(ProgressBarTemplate)

    def retranslateUi(self, ProgressBarTemplate):
        _translate = QtCore.QCoreApplication.translate
        ProgressBarTemplate.setWindowTitle(_translate("ProgressBarTemplate", "Dialog"))
        self.wait_lbl.setText(_translate("ProgressBarTemplate", "Please wait..."))
        self.msg_lbl.setText(_translate("ProgressBarTemplate", "Progress message"))
        self.close_btn.setText(_translate("ProgressBarTemplate", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProgressBarTemplate = QtWidgets.QDialog()
    ui = Ui_ProgressBarTemplate()
    ui.setupUi(ProgressBarTemplate)
    ProgressBarTemplate.show()
    sys.exit(app.exec_())
