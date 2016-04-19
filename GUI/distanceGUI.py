
from PySide import QtGui
from PySide.QtGui import *
import sys

import distanceView
from distanceView import Ui_mainWindowDist

class MainDistanceView(QWidget, distanceView.Ui_mainWindowDist):

   def __init__(self, parent=None):
        QWidget.__init__(self, parent)



   #     self.connect(self.showButton, SIGNAL("clicked()"), self.ShowMessageBox)

  #  def ShowMessageBox(self):
   #     QMessageBox.information(self, "Hello!", "Hello there " + self.nameEdit.text() )




if __name__=="__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QMainWindow()
    ui = Ui_mainWindowDist()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
