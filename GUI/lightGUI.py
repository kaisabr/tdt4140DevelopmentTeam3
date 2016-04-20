from PySide import QtGui
from PySide.QtGui import *
import sys

import distanceView
from lightView import Ui_lightView
import lightView
import VAR2_DefectLightbulb.lightbulbAnalyzer


class MainLightView(QWidget, Ui_lightView):

   def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        bLabel = Ui_lightView.back_label
        fLabel = Ui_lightView.front_label
        iLabel = self.interior_label
        rLabel = self.reg_label

        if(VAR2_DefectLightbulb.lightbulbAnalyzer.lightBulbAnalyzer.isFrontLightOff(self, frontLightSensor=0, carSignal=1)):
            fLabel.setStyleSheet("#front_label{background-color: red;}")
            fLabel.setText("Check light")




   #     self.connect(self.showButton, SIGNAL("clicked()"), self.ShowMessageBox)

  #  def ShowMessageBox(self):
   #     QMessageBox.information(self, "Hello!", "Hello there " + self.nameEdit.text() )




if __name__=="__main__":

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QMainWindow()
    ui = Ui_lightView()
    ui.setupUi(Dialog)
    Dialog.show()
    MainLightView.__init__(MainLightView(), parent=None)
    sys.exit(app.exec_())
