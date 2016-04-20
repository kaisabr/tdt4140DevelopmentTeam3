# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mathilde Theisen\PycharmProjects\tdt4140DevelopmentTeam3\GUI\blindzone.ui'
#
# Created: Wed Apr 20 13:40:30 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 391)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.blindzoneLabel = QtGui.QLabel(self.centralwidget)
        self.blindzoneLabel.setGeometry(QtCore.QRect(0, 0, 655, 370))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.blindzoneLabel.setFont(font)
        self.blindzoneLabel.setStyleSheet("#blindzoneLabel{background-color: red}")
        self.blindzoneLabel.setTextFormat(QtCore.Qt.AutoText)
        self.blindzoneLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.blindzoneLabel.setWordWrap(True)
        self.blindzoneLabel.setObjectName("blindzoneLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 21))
        self.menubar.setObjectName("menubar")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSound = QtGui.QMenu(self.menubar)
        self.menuSound.setObjectName("menuSound")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSpeed_and_distance = QtGui.QAction(MainWindow)
        self.actionSpeed_and_distance.setObjectName("actionSpeed_and_distance")
        self.actionLight_mode = QtGui.QAction(MainWindow)
        self.actionLight_mode.setObjectName("actionLight_mode")
        self.actionRecent_messages = QtGui.QAction(MainWindow)
        self.actionRecent_messages.setObjectName("actionRecent_messages")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuView.addAction(self.actionSpeed_and_distance)
        self.menuView.addAction(self.actionLight_mode)
        self.menuView.addAction(self.actionRecent_messages)
        self.menuView.addAction(self.actionQuit)
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSound.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Code Red - Blinzone", None, QtGui.QApplication.UnicodeUTF8))
        self.blindzoneLabel.setText(QtGui.QApplication.translate("MainWindow", "OBJECT DETECTED                                      IN BLINDZONE", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSound.setTitle(QtGui.QApplication.translate("MainWindow", "Sound", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSpeed_and_distance.setText(QtGui.QApplication.translate("MainWindow", "Speed and distance", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLight_mode.setText(QtGui.QApplication.translate("MainWindow", "Light mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_messages.setText(QtGui.QApplication.translate("MainWindow", "Recent messages", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

