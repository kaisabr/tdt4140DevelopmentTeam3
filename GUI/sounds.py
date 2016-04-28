from PySide import QtGui
from PySide.QtGui import *

# import the UI from the generated file
from sounds_ui import Ui_MainWindow


# it's not stricly necessary to subclass Ui_MainWindow.

# Ui_MainWindow is imported from sounds_ui.py
class MyMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

    def keyPressEvent(self, event):
        # implement the method here
        self.label.setText(self.label.text() + 'a')

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QMainWindow()
    win = Ui_MainWindow()
    win.setupUi(Dialog)
    Dialog.show()
    app.exec_()

