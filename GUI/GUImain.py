import sys, time
from PySide import QtCore, QtGui
from PySide.QtGui import *
from distanceView import Ui_mainWindowDist
from lightView import Ui_lightView

app = QtGui.QApplication(sys.argv)
dialog = QtGui.QMainWindow()


class Distance(QWidget, Ui_mainWindowDist):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        ui = Ui_mainWindowDist
        ui.setupUi(dialog)
        dialog.show()
        sys.exit(app.exec_())

