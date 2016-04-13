from PySide.QtCore import *
from PySide.QtGui import *
import sys

import lightView

class MainLightView(QDialog, lightView.Ui_lightView):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.centralwidget)


   #     self.connect(self.showButton, SIGNAL("clicked()"), self.ShowMessageBox)

  #  def ShowMessageBox(self):
   #     QMessageBox.information(self, "Hello!", "Hello there " + self.nameEdit.text() )




app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
