import argparse
import pandas as pd
from PyQt5 import QtGui, QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtChart import *
import pandas as pd
from PyQt5.uic import loadUi
import sys
from matplotlib import *
from matplotlib import style
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
style.use('ggplot')
import matplotlib.pyplot as plt
from datetime import *
import os
import re
import shutil

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
    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._dataframe.columns[section])

            if orientation == Qt.Vertical:
                return str(self._dataframe.index[section])

        return None

    def countheadtype(self,df):
        for colname, coltype in df.dtypes.iteritems():
            self.dimension=[]
            self.measurement=[]
            if coltype == object:
                dimension.append(colname) 
            elif colname =='Postal Code' or colname=='Row ID':
                dimension.append(colname) 
            else:
                measurement.append(colname)

    def sort(self, Ncol, order):
        self.layoutAboutToBeChanged.emit()
        header=self.arraydata.columns[Ncol]
        for j in self._dataframe.iloc[:,Ncol]:
            if '/' in str(j):
                self._dataframe[header]=pd.to_datetime(self._dataframe[header].astype(str), format='%d/%m/%Y')
                if order == 0:
                    self._dataframe=self._dataframe.sort_values(by=header,ascending=True)
                    self._dataframe[header] = self._dataframe[header].dt.strftime('%d/%m/%Y')
                elif order == 1:
                    self._dataframe=self._dataframe.sort_values(by=header,ascending=False)
                    self._dataframe[header] = self._dataframe[header].dt.strftime('%d/%m/%Y')
                break

            elif type(j) == int :
                self._dataframe[header]=self._dataframe[header].astype(int)
                if order == 0:
                    self._dataframe=self._dataframe.sort_values(by=header,ascending=True)
                elif order == 1:
                    self._dataframe=self._dataframe.sort_values(by=header,ascending=False)
                break
            else:

                if order == 0:
                    self._dataframe=self._dataframe.sort_values(by=header,ascending=True)
                elif order == 1:
                    self._dataframe=self._dataframe.sort_values(by=header,ascending=False)
                break

        self.layoutChanged.emit()

class Datasheet(QtWidgets.QMainWindow):
    def __init__(self,df: pd.DataFrame):
        self.dataframe=df
        super(Datasheet,self).__init__()
        loadUi("datasheet.ui",self)

        
        self.figure = plt.figure(figsize=(15,5))    
        self.canvas = FigureCanvas(self.figure)  

        self.insertdata()
    
        self.addtable_bt.clicked.connect(self.addtotable)
        #self.addtable_bt.clicked.connect(self.plot)
        #self.addtable_bt.clicked.connect(self.Horizontalbarchart)
        self.back_bt.clicked.connect(self.backbt)
        #self.addtable_bt.clicked.connect(self.charts)
        self.my_layout=QVBoxLayout(self.chart)

    def plot(self):
        self.figure.clear()
        ax =  self.figure.add_subplot(111) 
        self.dff.plot.barh(ax=ax)
        self.canvas.draw()
        my_layout=QVBoxLayout(self.chart)
        my_layout.addWidget(self.canvas)

    def backbt(self):
        dimension.clear()
        measurement.clear()
        datasource_pg = Mainwindow()
        widget.addWidget(datasource_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
            
    def Horizontalbarchart(self):
        try:
            self.my_layout.removeWidget(self.chartView)
        except:
            pass
        series=QHorizontalBarSeries()
        row=[]
        for i in self.dfff[str(self.row[-1])]:
            row.append(i)
        ncol=[]
        col=self.col
        for j in col:
            i=0
            ncol.append('col'+str(i))
            globals()['col'+str(i)]=[]
            for k in self.dfff[j]:
                globals()['col'+str(i)].append(k)
            globals()['set'+str(i)]=QBarSet(j)
            globals()['set'+str(i)].append(globals()['col'+str(i)])
            series.append(globals()['set'+str(i)])
            i+=1
       
                            
        series.setLabelsVisible(True)
 
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Chart")
        chart.setAnimationOptions(QChart.SeriesAnimations)
 
        axis = QBarCategoryAxis()
        axis.append(row)
        chart.createDefaultAxes()
        axis.setTitleText(str(self.row[-1]))
        chart.setAxisY(axis, series)
        
        axis_x=QValueAxis()
        if len(col) >1:
            colstr='/'.join(str(e)for e in row)
            axis_x.setTitleText(colstr)
        else:
            axis_x.setTitleText(str(self.col[0]))

        chart.setAxisX(axis_x, series)
        
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView = QChartView(chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        
        
        self.my_layout.addWidget(self.chartView) 
        
    def barchart(self):
        try:
            self.my_layout.removeWidget(self.chartView)
        except:
            pass    
        series = QBarSeries()
        col=[]
        for i in self.dfff[str(self.col[-1])]:
            col.append(i)
        nrow=[]
        row=self.row
        for j in row:
            i=0
            nrow.append('row'+str(i))
            globals()['row'+str(i)]=[]
            for k in self.dfff[j]:
                globals()['row'+str(i)].append(k)
            globals()['set'+str(i)]=QBarSet(j)
            globals()['set'+str(i)].append(globals()['row'+str(i)])
            series.append(globals()['set'+str(i)])
            i+=1
        series.setLabelsVisible(True)

 
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Percent Example")
        chart.setAnimationOptions(QChart.SeriesAnimations)
 
        axis = QBarCategoryAxis()
        axis.append(col)
        axis.setTitleText(str(self.col[-1]))
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        axis_y=QValueAxis()
        if len(row) >1:
            rowstr='/'.join(str(e)for e in row)
            print(rowstr)
            axis_y.setTitleText(rowstr)
        else:
            axis_y.setTitleText(str(self.row[0]))
        chart.setAxisY(axis_y, series)
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
 
        self.chartView = QChartView(chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)
 
        self.my_layout.addWidget(self.chartView) 

    def insertdata(self):   
        list_dimension = self.list_dimension
        list_measurement=self.list_measures
        list_dimension.insertItems(0, dimension)
        list_measurement.insertItems(0, measurement)

    def addtotable(self):
            self.dff=self.dataframe
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
            self.col=col
            self.row=row
            self.dff=self.dff.loc[:,lst]
            mcol=False
            for i in measurement:
                if i in col:
                    mcol=True

            if mcol==True:
                self.dff=self.dff.groupby(row).sum()
                self.dfff=self.dff.reset_index()
                self.Horizontalbarchart()
            else:
                self.dff=self.dff.groupby(col).sum()
                self.dfff=self.dff.reset_index()
                self.barchart()
            
            self.model = PandasModel(self.dfff)
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
        self.listWidget.clicked.connect(self.gotofile)
        self.add_bt.clicked.connect(self.addsheet)
        self.del_bt.clicked.connect(self.remove)
        self.Ex_bt.clicked.connect(self.close_x)
        ####
    
    def gotofile(self):
        sel_item=self.listWidget.currentItem().text()
        self.csvfol=self.dirr+'/'+sel_item+'/save.csv'
        try:
            df = pd.read_csv(self.csvfol,encoding='windows-1252')
            self.addtotable(df)
        except:
            df =pd.DataFrame({'Dont have csv file' : []})
            self.addtotable(df)
            pass

    def savefile(self,df:pd.DataFrame,path):
        try:
            df.to_csv(path+'/save.csv',index=False)
            self.gotofile()

        except:
            pass

    def gotosheet(self):
            try:
                sel_item=self.listWidget.currentItem().text()
                self.csvfol=self.dirr+'/'+sel_item+'/save.csv'
                df = pd.read_csv(self.csvfol,encoding='windows-1252')
                dimension.clear()
                measurement.clear()
                for colname, coltype in df.dtypes.iteritems():
                    if coltype == object:
                        dimension.append(colname) 
                    elif colname =='Postal Code' or colname=='Row ID':
                        dimension.append(colname) 
                    else:
                        measurement.append(colname)
            
                sel_item = self.listWidget.currentItem().text()
                titlelist.append(sel_item)
                sheet_pg=Datasheet(df)
                widget.addWidget(sheet_pg)
                widget.setCurrentIndex(widget.currentIndex()+1)
            except:
                pass
        
    def addsheet(self,df:pd.DataFrame):
        Input = "Sheet"
        co=[]
        fname=[]
        with open(self.save_file,'a',encoding='utf-8') as a:
            read = open(self.save_file,'r',encoding='utf-8')   
            Lines = read.readlines()
            try:
                r=open(self.save_file,'r',encoding='utf-8')   
                for j in r:
                    co.append(j.replace('\n',''))
                c=co[-1]
                c=int(re.search(r'\d+', c).group())
                for i in Lines:
                    i=i.replace('\n','')
                    if i in co:
                        a.write('\n'+Input+str(c+1))
                        x = Input+str(c+1)
                        fname.append(x)
                        break       
            except:
                if Lines == []:
                    a.write(Input+'0')
                    x = Input+'0'
                    fname.append(x)
        
        r = open(self.save_file,'r',encoding='utf-8')          
        for i in r:
            i=i.replace('\n','')
        path = os.path.join(self.dirr,fname[0])
                
        if not os.path.exists(path):
            os.mkdir(path)
            #titlelist.append(Input)       
        self.savefile(df,path)
        ###
        maintitle_pg = Mainwindow()
        widget.addWidget(maintitle_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
        ###

    def Importfiles(self):
        try:
            path,_= QFileDialog.getOpenFileName(self,"Import file",'',"Csv files (*.csv);;Excel files(*.xlsx)","Csv (*.csv);;Xlsx (*.xlsx)")
            fname = QFileInfo(path).fileName()
            filename.append(path)
            if fname[-4:] == '.csv':
                df = pd.read_csv(fname,encoding='windows-1252')
            elif fname[-5:] == '.xlsx':
                df = pd.read_excel(fname,encoding='windows-1252')
            self.addsheet(df)
            self.addtotable(df)
        except:
            pass    
        
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
        try:
            sel_item = self.listWidget.currentItem().text()
        except:
            pass 
        if item is None:
            return
        else:
            item = self.listWidget.takeItem(row)
            del item
            df =pd.DataFrame({'Dont have csv file' : []})
            self.addtotable(df)

            shutil.rmtree(self.dirr+'/'+str(sel_item))### del folder
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
count=[]  
if __name__ == "__main__":
    
    app  = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    main = Mainwindow()
    widget.addWidget(main)
    widget.resize(1171, 747)
    widget.show()
    sys.exit(app.exec_())
