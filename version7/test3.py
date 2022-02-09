import sys
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QApplication
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QApplication, QDialog


class ExampleWidget(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        listWidget = QListWidget(self)
        listWidget.itemDoubleClicked.connect(self.buildExamplePopup)
        for n in ["Jack", "Chris", "Joey", "Kim", "Duncan"]:
            QListWidgetItem(n, listWidget)
        self.setGeometry(100, 100, 100, 100)
        self.show()

    
    def buildExamplePopup(self, item):
        exPopup = ExamplePopup(item.currentItem().text(), self)
        exPopup.setGeometry(100, 200, 100, 100)
        exPopup.show()


class ExamplePopup(QDialog):

    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.name = name
        self.label = QLabel(self.name, self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ExampleWidget()
    sys.exit(app.exec_())