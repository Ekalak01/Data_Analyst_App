import sys
from PyQt5 import QtGui, QtCore,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        MainWindow.__init__(self)
        self.menubar = self.menuBar()
        menuitems = ["Item 1","Item 2","Item 3"]
        menu = self.menubar.addMenu('&Stuff')
        for item in menuitems:
            entry = menu.addAction(item)
            self.connect(entry,QtCore.SIGNAL('triggered()'), lambda: self.doStuff(item))
            menu.addAction(entry)
        print ("init done")

    def doStuff(self, item):
        print(item)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())