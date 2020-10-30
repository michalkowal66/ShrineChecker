# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\designer\sc_message.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MessageTemplate(object):
    def setupUi(self, MessageTemplate):
        MessageTemplate.setObjectName("MessageTemplate")
        MessageTemplate.resize(360, 250)
        MessageTemplate.setMinimumSize(QtCore.QSize(360, 250))
        MessageTemplate.setMaximumSize(QtCore.QSize(360, 250))
        self.bg = QtWidgets.QLabel(MessageTemplate)
        self.bg.setGeometry(QtCore.QRect(0, 0, 360, 250))
        self.bg.setStyleSheet("")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.title_lbl = QtWidgets.QLabel(MessageTemplate)
        self.title_lbl.setGeometry(QtCore.QRect(0, 10, 360, 30))
        self.title_lbl.setStyleSheet("")
        self.title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lbl.setObjectName("title_lbl")
        self.msg_lbl = QtWidgets.QLabel(MessageTemplate)
        self.msg_lbl.setGeometry(QtCore.QRect(20, 40, 320, 160))
        self.msg_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_lbl.setWordWrap(True)
        self.msg_lbl.setObjectName("msg_lbl")
        self.close_btn = QtWidgets.QPushButton(MessageTemplate)
        self.close_btn.setGeometry(QtCore.QRect(140, 205, 80, 30))
        self.close_btn.setStyleSheet("")
        self.close_btn.setObjectName("close_btn")

        self.retranslateUi(MessageTemplate)
        QtCore.QMetaObject.connectSlotsByName(MessageTemplate)

    def retranslateUi(self, MessageTemplate):
        _translate = QtCore.QCoreApplication.translate
        MessageTemplate.setWindowTitle(_translate("MessageTemplate", "Dialog"))
        self.title_lbl.setText(_translate("MessageTemplate", "Title"))
        self.msg_lbl.setText(_translate("MessageTemplate", "Message"))
        self.close_btn.setText(_translate("MessageTemplate", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MessageTemplate = QtWidgets.QDialog()
    ui = Ui_MessageTemplate()
    ui.setupUi(MessageTemplate)
    MessageTemplate.show()
    sys.exit(app.exec_())
