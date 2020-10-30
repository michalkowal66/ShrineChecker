import rsc
from PyQt5 import QtCore

def convert_stylesheet(path):
    fd = QtCore.QFile(path)
    if fd.open(QtCore.QIODevice.ReadOnly | QtCore.QFile.Text):
        text = QtCore.QTextStream(fd).readAll()
        fd.close()
        return text

ui_stylesheet = convert_stylesheet(':/Stylesheets/styles/ui_stylesheet.qss')
message_stylesheet = convert_stylesheet(':/Stylesheets/styles/message_stylesheet.qss')
notification_stylesheet = convert_stylesheet(':/Stylesheets/styles/notification_stylesheet.qss')
progress_stylesheet = convert_stylesheet(':/Stylesheets/styles/progress_stylesheet.qss')
settings_stylesheet = convert_stylesheet(':/Stylesheets/styles/settings_stylesheet.qss')

