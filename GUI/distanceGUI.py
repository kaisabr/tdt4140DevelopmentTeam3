
from PySide import QtGui
from PySide.QtGui import *
from PySide.QtCore import QObject, Signal, Slot
import sys

import distanceView
from distanceView import Ui_mainWindowDist

class MainDistanceView(QWidget, distanceView.Ui_mainWindowDist):

    def __init__(self, parent=None):
       QWidget.__init__(self, parent)



    def DistanceSignalChanged(self):
       self.changedState.emit()

    # Change the color and text if the driver drives too fast
    def changeLabelColor(self):
       self.QLabel.setText("Too fast")
       self.QLabel.setStyleSheet("{background-color: red}")





if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QMainWindow()
    ui = Ui_mainWindowDist()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

