from PyQt5 import QtGui, QtCore,QtWidgets
import sys, random

def clear(listwidget):
    #for i in range(listwidget.count()):
        #item = listwidget.item(i)
        listwidget.clearSelection()

app = QtWidgets.QApplication([])
top = QtWidgets.QWidget()

# list widget
myListWidget = QtWidgets.QListWidget(top)
myListWidget.setSelectionMode(1)
myListWidget.resize(200,300)
for i in range(10):
    item = QtWidgets.QListWidgetItem("item %i" % i, myListWidget)
    myListWidget.addItem(item)
    if random.random() > 0.5: 
        # randomly select half of the items in the list
        item.setSelected(True)

# clear button
myButton = QtWidgets.QPushButton("Clear", top)
myButton.resize(60,30)
myButton.move(70,300)
myButton.clicked.connect(lambda: clear(myListWidget))
top.show()

sys.exit(app.exec_())