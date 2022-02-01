import argparse
import pandas as pd
from PyQt5 import QtGui, QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
import pandas as pd
from PyQt5.uic import loadUi
import sys
import matplotlib.pyplot as plt
from datetime import *
import os

class listcol(QtWidgets.QListWidget):
    got_signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(listcol, self).__init__(parent)
        #loadUi('datasheet.ui', self)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setViewMode(QListView.IconMode)
        self.setDefaultDropAction(Qt.MoveAction)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            super(listcol, self).dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            super(listcol, self).dragMoveEvent(event)
    
    def dropEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            """links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.got_signal.emit(("dropped col"), links)"""
        else:
            event.setDropAction(Qt.MoveAction)
            super(listcol, self).dropEvent(event)
            """self.got_signal.emit(("dropped col"))"""

class listrow(QtWidgets.QListWidget):
    got_signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(listrow, self).__init__(parent)
        self.setIconSize(QtCore.QSize(124, 124))
        self.setDragDropMode(QAbstractItemView.DragDrop)
        #self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setViewMode(QListView.IconMode)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            super(listrow, self).dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            super(listrow, self).dragMoveEvent(event)
    
    def dropEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            """links = []
            print("links",links)
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.got_signal.emit(("dropped row"), links)"""
        else:
            event.setDropAction(Qt.MoveAction)
            super(listrow, self).dropEvent(event)
            """self.got_signal.emit(("dropped row"))"""

class listdi(QtWidgets.QListWidget):
    got_signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(listdi, self).__init__(parent)
        self.setIconSize(QtCore.QSize(124, 124))
        self.setDragDropMode(QAbstractItemView.DragDrop)
        #self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)
        self.setDefaultDropAction(Qt.MoveAction)
        #self.setViewMode(QListView.IconMode)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            super(listdi, self).dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            super(listdi, self).dragMoveEvent(event)
    
    def dropEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            """links = []
            print("links",links)
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.got_signal.emit(("dropped row"), links)"""
        else:
            event.setDropAction(Qt.MoveAction)
            super(listdi, self).dropEvent(event)
 
class listmea(QtWidgets.QListWidget):
    got_signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(listmea, self).__init__(parent)
        self.setIconSize(QtCore.QSize(124, 124))
        self.setDragDropMode(QAbstractItemView.DragDrop)
        #self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)
        self.setDefaultDropAction(Qt.MoveAction)
        #self.setViewMode(QListView.IconMode)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            super(listmea, self).dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            super(listmea, self).dragMoveEvent(event)
    
    def dropEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            """links = []
            print("links",links)
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.got_signal.emit(("dropped row"), links)"""
        else:
            event.setDropAction(Qt.MoveAction)
            super(listmea, self).dropEvent(event)
            
class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """
    
    def __init__(self, dataframe: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe
        self.arraydata = self._dataframe
        print(dataframe)
        self.countheadtype(dataframe)
        

    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return str(self._dataframe.iloc[index.row(), index.column()])

        return None
    
    def countheadtype(self,df):
        for colname, coltype in df.dtypes.iteritems():
            headers.append(colname)
            if coltype == object:
                dimension.append(colname) 
            elif colname =='Postal Code' or colname=='Row ID':
                dimension.append(colname)
                
            else:
                measurement.append(colname)

class Datasheet(QtWidgets.QMainWindow):
    def __init__(self,df: pd.DataFrame):
        self.dataframe=df
        super(Datasheet,self).__init__()
        loadUi("datasheet.ui",self)

        self.insertdata()
    
    def insertdata(self):   
        list_dimension = self.list_dimension
        list_measurement=self.list_measures
        list_dimension.insertItems(0, dimension)
        list_measurement.insertItems(0, measurement)

    def addtotable(self):
            df=self.dataframe
            listcol=self.list_col
            listrow=self.list_row
            col=[]
            row=[]
            lst=[]
            for x in range(listcol.count()):
                col.append(listcol.item(x).text())
            for x in range(listrow.count()):
                row.append(listrow.item(x).text())
            for i in col:
                lst.append(i)
            for i in row:
                lst.append(i)
            df=df.loc[:,lst]
            df=df.groupby(col).sum()

            
            self.model = PandasModel(df)
            self.tableView.setModel(self.model)
            self.tableView.setSortingEnabled(True)
            self.tableView.sortByColumn(0, Qt.AscendingOrder)



    def close_x(self):
        should_save = QMessageBox.question(self, "Exit", 
                                                     "Do you want to Exit ?",
                                                     defaultButton = QMessageBox.Yes)
        if should_save == QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            pass   
          
class Mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        loadUi("data.ui",self)
        
        ###created folder by user 
        
        parent_dir=QtCore.QDir.currentPath()
        directory= "Sheetname"
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        self.dirr=path
        self.filename = "Sheetname"
        self.save_file = self.dirr+"/"+self.filename+'.txt'
        self.read_from_file(self.save_file)
        
        ####
        
        self.Import_bt.clicked.connect(self.Importfiles)
        self.listWidget.itemDoubleClicked.connect(self.gotosheet)
        self.add_bt.clicked.connect(self.addsheet)
        self.del_bt.clicked.connect(self.remove)
        self.Ex_bt.clicked.connect(self.close_x)
        
        ####
        
    def gotosheet(self):
        fname=''
        for i in filename:
            fname=i
        df = pd.read_csv(fname,encoding='windows-1252')
        sel_item = self.listWidget.currentItem().text()
        titlelist.append(sel_item)
        print("titlelist",titlelist)
        sheet_pg=Datasheet(df)
        widget.addWidget(sheet_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def addsheet(self):
        j = 0  
        
        #print("start",j)
        Input = "Sheet"
        read = open(self.save_file,'r',encoding='utf-8')
        with open(self.save_file,'a',encoding='utf-8') as a:
                 
            Lines = read.readlines()
                
            for i in Lines:
                j += 1
            print(j) 
                
            if Lines == []:
                a.write(Input+str(j+1))
                x = Input+str(j+1)
                #y.append(Input)
            elif (Input+str(j+1)) in Lines:
                #print("true")
                a.write("\n"+Input+str(j+2))
                x = Input+str(j+2)
            else:
                a.write("\n"+Input+str(j+1))
                x = Input+str(j+1)
                #y.append(Input)          
            
        path = os.path.join(self.dirr,x)
                
        if not os.path.exists(path):
            os.mkdir(path)
            #titlelist.append(Input) 
        
        f=open(self.dirr+'/'+x+'/col.txt','w',encoding='utf-8')
        f.close
        f=open(self.dirr+'/'+x+'/row.txt','w',encoding='utf-8')
        f.close       
        
        ###
        maintitle_pg = Mainwindow()
        widget.addWidget(maintitle_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
        ###
        
    def addtotable(self,df):
        try:
            self.model = PandasModel(df)
            self.tableView.setModel(self.model)
            self.tableView.setSortingEnabled(True)
            self.tableView.sortByColumn(0, Qt.AscendingOrder)
        except:
            pass
    
    def remove(self):
        row = self.listWidget.currentRow()
    
        item = self.listWidget.item(row)
        
        if item is None:
            return
        else:
            item = self.listWidget.takeItem(row)
            del item
        
        self.write_to_file(self.save_file)

    def write_to_file(self, file):
        try:
            list_widget = self.listWidget
            entries = '\n'.join(list_widget.item(ii).text() for ii in range(list_widget.count()))
            with open(file, 'w',encoding='utf-8') as fout:
                fout.write(entries)
        except OSError as err:
            print(f"file {file} could not be written")

    def read_from_file(self, file):
        try:
            list_widget = self.listWidget
            with open(file, 'r',encoding='utf-8') as fin:
                    entries = [e.strip() for e in fin.readlines()]
            list_widget.insertItems(0, entries)
        except OSError as err:
            with open(file, 'w',encoding='utf-8'):
                #print("pass")
                pass
    
    def Importfiles(self):
        try:
            path,_= QFileDialog.getOpenFileName(self,"Import file",'',"Csv files (*.csv);;Excel files(*.xlsx)","Csv (*.csv);;Xlsx (*.xlsx)")
            fname = QFileInfo(path).fileName()
            filename.append(path)
            df = pd.read_csv(fname,encoding='windows-1252')
            self.addtotable(df)
        except:
            pass
        
    def close_x(self):
        should_save = QMessageBox.question(self, "Save data", 
                                                     "Should the data be saved?",
                                                     defaultButton = QMessageBox.Yes)
        if should_save == QMessageBox.Yes:
            self.write_to_file(self.save_file)
            sys.exit(app.exec_())
        else:
            pass

filename=[]
measurement=[]
dimension=[]
headers=[]
titlelist=[]

if __name__ == "__main__":
    
    app  = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    main = Mainwindow()
    widget.addWidget(main)
    widget.resize(1171, 747)
    widget.show()
    sys.exit(app.exec_())
