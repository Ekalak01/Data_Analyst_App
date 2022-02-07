import argparse
from sqlite3 import Row
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

class listfilter(QtWidgets.QListWidget):
    #got_signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(listfilter, self).__init__(parent)
        
        self.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setAcceptDrops(True)
        self.setViewMode(QListView.IconMode)
        
    def setup(self,sett):
        self.sett = sett 
        
    def dragLeaveEvent(self,event) -> None:
        if self.count():            
            self.takeItem(self.currentRow())
            #super().dragLeaveEvent(e)"""
            
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
        else:
            super(listfilter, self).dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
        else:
            super(listfilter, self).dragMoveEvent(event)
    
    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
            data = event.mimeData()
            source_item = QStandardItemModel()
            source_item.dropMimeData(data, Qt.CopyAction, 0,0, QModelIndex())
            print(source_item.item(0, 0).text())
            #self.addItem(source_item.item(0, 0).text())
            #self.sett.addtotable()
        else:
            super(listfilter, self).dropEvent(event) 

class listcol(QtWidgets.QListWidget):
    #got_signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(listcol, self).__init__(parent)
        
        self.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setAcceptDrops(True)
        self.setViewMode(QListView.IconMode)
        
    def setup(self,sett):
        self.sett = sett 
        
    def dragLeaveEvent(self,event) -> None:
        if self.count():            
            self.takeItem(self.currentRow())
            #super().dragLeaveEvent(e)"""
            
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
        else:
            super(listcol, self).dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
        else:
            super(listcol, self).dragMoveEvent(event)
    
    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
            data = event.mimeData()
            source_item = QStandardItemModel()
            source_item.dropMimeData(data, Qt.CopyAction, 0,0, QModelIndex())
            print(source_item.item(0, 0).text())
            self.addItem(source_item.item(0, 0).text())
            self.sett.addtotable()
        else:
            super(listcol, self).dropEvent(event)      
   
class listrow(QtWidgets.QListWidget):
    #got_signal = pyqtSignal(str)
    def __init__(self,parent=None):
        
        super(listrow, self).__init__(parent)
        self.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setAcceptDrops(True)
        self.setViewMode(QListView.IconMode)    
    
    def setup(self,sett):
        self.sett = sett 
    
    def dragLeaveEvent(self,event) -> None:
        if self.count():            
            self.setDefaultDropAction(QtCore.Qt.MoveAction)
            self.takeItem(self.currentRow())
                          
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
        else:
            print("error")
            super(listrow, self).dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
        else:
            print("error")
            super(listrow, self).dragMoveEvent(event)
    
    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
            data = event.mimeData()
            source_item = QStandardItemModel()
            source_item.dropMimeData(data, Qt.CopyAction, 0,0, QModelIndex())
            print(source_item.item(0, 0).text())
            self.addItem(source_item.item(0, 0).text())  
            self.sett.addtotable() 
        else:
            print("error")
            super(listrow, self).dropEvent(event)          

class listdi(QtWidgets.QListWidget):
    got_signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(listdi, self).__init__(parent)
        self.setIconSize(QtCore.QSize(124, 124))
        self.setDragDropMode(QAbstractItemView.DragDrop)
        #self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        #self.setAcceptDrops(True)
        #self.setDefaultDropAction(Qt.MoveAction)
        #self.setViewMode(QListView.IconMode)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
        else:
            super(listdi, self).dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
        else:
            super(listdi, self).dragMoveEvent(event)
    
    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            #event.accept()
            """data = event.mimeData()
            source_item = QStandardItemModel()
            source_item.dropMimeData(data, Qt.CopyAction, 0,0, QModelIndex())
            print(source_item.item(0, 0).text())
            self.addItem(source_item.item(0, 0).text())"""
        else:
            super(listdi, self).dropEvent(event)

class listmea(QtWidgets.QListWidget):
    got_signal = pyqtSignal(str)
    def __init__(self, parent=None):
        super(listmea, self).__init__(parent)
        
        self.setIconSize(QtCore.QSize(124, 124))
        self.setDragDropMode(QAbstractItemView.DragDrop)
        #self.setAcceptDrops(True)
        self.setDefaultDropAction(Qt.MoveAction)
        
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
        else:
            super(listdi, self).dragEnterEvent(event)
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            event.accept()
        else:
            super(listdi, self).dragMoveEvent(event)
    
    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            """event.accept()
            data = event.mimeData()
            source_item = QStandardItemModel()
            source_item.dropMimeData(data, Qt.CopyAction, 0,0, QModelIndex())
            print(source_item.item(0, 0).text())
            self.addItem(source_item.item(0, 0).text())"""
        else:
            super(listdi, self).dropEvent(event)
            
class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """
    
    def __init__(self, dataframe: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe
        self.arraydata = self._dataframe
        #print(dataframe)
        #self.countheadtype(dataframe)
        
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
    
class Datasheet(QtWidgets.QMainWindow):
    def __init__(self,csvfol):
        #self.dataframe=df
        self.csvfol = csvfol #location Sheet 
        print(self.csvfol) 
        
        """writex = open(self.csvfol+"/text.txt",'w',encoding='utf-8')  
        writex.write("a")"""
        
        super(Datasheet,self).__init__()
        loadUi("datasheet1.ui",self)
        
        self.list_col.setup(self)
        self.list_row.setup(self)
        
        #self.figure = plt.figure(figsize=(15,5))    
        #self.canvas = FigureCanvas(self.figure)  

        
        #self.addtable_bt.clicked.connect(self.addtotable)
        #self.addtable_bt.clicked.connect(self.plot)
        #self.addtable_bt.clicked.connect(self.Horizontalbarchart)
        self.back_bt.clicked.connect(self.backbt)
        #self.addtable_bt.clicked.connect(self.charts)
        
        self.my_layout=QVBoxLayout(self.chart)
        
        self.file_combo.addItem("None")# Error if use call None in App
        #self.combo_box.activated.connect(self.do_something)
        self.file_combo.activated.connect(self.selectionChange)
        self.file_combo.activated.connect(self.countheadtype)
        ###created folder by user 
        
        parent_dir=QtCore.QDir.currentPath()
        directory= "Appfolder"
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        directory2= "Import"
        path = os.path.join(directory, directory2)
        if not os.path.exists(path):
            os.mkdir(path)
            #os.mkdir(path2)
        self.dirr_Import=path
        self.filename = "filename"
        self.save_list_file = self.dirr_Import+"/"+self.filename+'.txt'
        self.read_from_list_file(self.save_list_file)
        
        ####
    
    def selectionChange(self, i):
        
        self.texte = self.file_combo.currentText()
        print(f"Index {i} pour la commune {i}, texte -> {self.texte}")
        return self.texte
    
    def countheadtype(self):
        
        direct = "Appfolder/Import"+"/"+str(self.texte)
        self.df = pd.read_csv(direct+"/save.csv")
        for colname, coltype in self.df.dtypes.iteritems():
            headers.append(colname)
            if coltype == object:
                dimension.append(colname) 
            elif colname =='Postal Code' or colname=='Row ID':
                dimension.append(colname)
            else:
                measurement.append(colname)
        self.insertdata()
        
    def write_to_list_file(self, file):
        try:
            combo_widget = self.file_combo
            entries = '\n'.join(combo_widget.item(ii).text() for ii in range(combo_widget.count()))
            with open(file, 'w',encoding='utf-8') as fout:
                fout.write(entries)
                #print("fout",fout)
        except OSError as err:
            print(f"file {file} could not be written")
    
    def read_from_list_file(self, file):
        try:
            combo_widget = self.file_combo
            with open(file, 'r',encoding='utf-8') as fin:
                    entries = [e.strip() for e in fin.readlines()]
            combo_widget.insertItems(0, entries)
        except OSError as err:
            with open(file, 'w',encoding='utf-8'):
                #print("pass")
                pass    
        
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
        self.list_dimension.clear()
        list_measurement=self.list_measures
        self.list_measures.clear()
        list_dimension.insertItems(0, dimension)
        list_measurement.insertItems(0, measurement)
        
        dimension.clear()
        measurement.clear()
        print("dimension",dimension)
        
    def addtotable(self):
            self.dff=self.df
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
        
        self.list_file.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        
        ###created Super Folder
        
        parent_dir=QtCore.QDir.currentPath()
        directory= "Appfolder"
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        directory2= "Sheet"
        path = os.path.join(directory, directory2)
        if not os.path.exists(path):
            os.mkdir(path)
            #os.mkdir(path2)
        self.dirr_sheet=path
        self.filename = "Sheetname"
        self.save_file = self.dirr_sheet+"/"+self.filename+'.txt'
        self.read_from_file(self.save_file)
            
        ###created folder by user 
        
        parent_dir=QtCore.QDir.currentPath()
        directory= "Appfolder"
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        directory2= "Import"
        path = os.path.join(directory, directory2)
        if not os.path.exists(path):
            os.mkdir(path)
            #os.mkdir(path2)
        self.dirr_Import=path
        self.filename = "filename"
        self.save_list_file = self.dirr_Import+"/"+self.filename+'.txt'
        self.read_from_list_file(self.save_list_file)
        
        ####
        
        self.Import_bt.clicked.connect(self.Importfiles)
        self.list_sheet.itemDoubleClicked.connect(self.gotosheet)
        self.list_file.clicked.connect(self.gotofile)
        self.list_union.clicked.connect(self.gotofile_union)
        self.add_bt.clicked.connect(self.addsheet)
        self.del_bt.clicked.connect(self.remove)
        self.del_file_bt.clicked.connect(self.remove_filename)
        self.del_union_bt.clicked.connect(self.remove_unionfile)
        self.Ex_bt.clicked.connect(self.close_x)
        self.list_sheet.setViewMode(QListWidget.IconMode)
        self.union_bt.clicked.connect(self.union_file)
        self.list_sheet.setAcceptDrops(False)
        
        ####

    def union_file(self,df:pd.DataFrame):
        
        items = self.list_file.selectedItems()
        list_csv = []
        for i in range(len(items)):
            list_csv.append(str(self.list_file.selectedItems()[i].text()))

        print (list_csv)
        
        for i in range(len(items)):
            print(len(items))
            #print(i)
            if len(items) >= 2:
                #print("if")
                Input = "Union"
                #Input2 = ".csv"
                co=[]
                fname =[]
                check =[]
                with open(self.save_list_file,'a',encoding='utf-8') as a:
                    read = open(self.save_list_file,'r',encoding='utf-8')   
                    Lines = read.readlines()
                    for j in Lines:
                        check.append(j.replace('\n',''))
                    
                    data1 = pd.read_csv(str(list_csv[0]))
                    data2 = pd.read_csv(str(list_csv[1]))
                    df = pd.merge(data1, data2,how='outer')
                    if "Union0" in check: 
                        try:
                            r=open(self.save_list_file,'r',encoding='utf-8')   
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
                                    print("if",fname)
                                    break       
                        except:
                            pass
                    else:
                        a.write("\n"+Input+'0')
                        x = Input+'0'
                        fname.append(x)
                        print("else",fname)
                        #
                        #print("pass")
                        
                    r = open(self.save_list_file,'r',encoding='utf-8')          
                    #print("r",r)
                    for i in r:
                        i=i.replace('\n','')
                        #print("i",i)
                    print("fname",fname)
                    path = os.path.join(self.dirr_Import,fname[0])
                    
                    if not os.path.exists(path):
                        os.mkdir(path)
                        #df.to_csv(os.path.join(path,str(x) +".csv"),index = False, encoding='utf-8-sig')
                    self.savefile(df,path)
                    break
            else:
                pass 
           
        ###
        maintitle_pg = Mainwindow()
        widget.addWidget(maintitle_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
        ###      
    def gotofile(self):
        sel_item=self.list_file.currentItem().text()
        self.csvfol=self.dirr_Import+'/'+sel_item+'/save.csv'
        try:
            df = pd.read_csv(self.csvfol,encoding='windows-1252')
            self.addtotable(df)
        except:
            df =pd.DataFrame({'Dont have csv file' : []})
            self.addtotable(df)
            pass
        
    def gotofile_union(self):
        sel_item=self.list_union.currentItem().text()
        self.csvfol=self.dirr_Import+'/'+sel_item+'/save.csv'
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
                sel_item=self.list_sheet.currentItem().text()
                self.csvfol=self.dirr_sheet+'/'+sel_item
                """df = pd.read_csv(self.csvfol,encoding='windows-1252')
                dimension.clear()
                measurement.clear()
                for colname, coltype in df.dtypes.iteritems():
                    if coltype == object:
                        dimension.append(colname) 
                    elif colname =='Postal Code' or colname=='Row ID':
                        dimension.append(colname) 
                    else:
                        measurement.append(colname)
            
                sel_item = self.list_sheet.currentItem().text()
                titlelist.append(sel_item)"""
                sheet_pg=Datasheet(self.csvfol)
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
        path = os.path.join(self.dirr_sheet,fname[0])
                
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
        file_list =[]
        Linex = []
        try:
            path,_= QFileDialog.getOpenFileName(self,"Import file",'',"Csv files (*.csv);;Excel files(*.xlsx)","Csv (*.csv);;Xlsx (*.xlsx)")
            fname = QFileInfo(path).fileName()
            
            with open(self.save_list_file,'a',encoding='utf-8') as a:
                read = open(self.save_list_file,'r',encoding='utf-8')   
                Lines = read.readlines()
                
                for i in Lines:
                    Linex.append(i.replace('\n',''))
                filenamex = path.split("/")[-1]
                
                #print("file_list",filenamex)
                #print("Lines",Linex)
                
                if filenamex not in Linex:    
                    filename.append(path)

                    if fname[-4:] == '.csv':
                        df = pd.read_csv(fname,encoding='utf-8-sig')
                    elif fname[-5:] == '.xlsx':
                        df = pd.read_excel(fname,encoding='utf-8-sig')
                        
                    file_list.append(filenamex)
                    self.list_file.addItems(file_list)
                    self.list_file.addItems(filenamex)
                    
                    maintitle_pg = Mainwindow()
                    widget.addWidget(maintitle_pg)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                
                #self.addsheet(df)
                #self.addtotable(df) 
            #file_list.clear()
                else:
                    print("pass")
                    pass
        except:
            pass
        try:
            self.save_filename(df,fname)
        except:
            pass
        
    def save_filename(self,df,fname):   
        path = os.path.join(self.dirr_Import,fname) 
        if not os.path.exists(path):
            os.mkdir(path)      
        self.savefile(df,path)
        self.write_to_list_file(self.save_list_file)
        #print("save")    
    def addtotable(self,df):
        try:
            self.model = PandasModel(df)
            self.tableView.setModel(self.model)
            self.tableView.setSortingEnabled(True)
            self.tableView.sortByColumn(0, Qt.AscendingOrder)
        except:
            pass
    
    def remove(self):
        row = self.list_sheet.currentRow()

        item = self.list_sheet.item(row)
        try:
            sel_item = self.list_sheet.currentItem().text()
        except:
            pass 
        if item is None:
            return
        else:
            item = self.list_sheet.takeItem(row)
            del item
            df = pd.DataFrame({'Dont have csv file' : []})
            self.addtotable(df)

            shutil.rmtree(self.dirr_sheet+'/'+str(sel_item))### del folder
        self.write_to_file(self.save_file)

    def remove_filename(self):
        print("Remove_Filename")
        row = self.list_file.currentRow()

        item = self.list_file.item(row)
        try:
            sel_item = self.list_file.currentItem().text()
        except:
            pass 
        if item is None:
            return
        else:
            item = self.list_file.takeItem(row)
            del item
            df = pd.DataFrame({'Dont have csv file' : []})
            #self.addtotable(df)

            shutil.rmtree(self.dirr_Import+'/'+str(sel_item))### del folder
        self.write_to_list_file(self.save_list_file)
        
    def remove_unionfile(self):
        print("Remove_Union")
        row = self.list_union.currentRow()

        item = self.list_union.item(row)
        try:
            sel_item = self.list_union.currentItem().text()
        except:
            pass 
        if item is None:
            return
        else:
            item = self.list_union.takeItem(row)
            del item
            df = pd.DataFrame({'Dont have csv file' : []})
            self.addtotable(df)

            shutil.rmtree(self.dirr_Import+'/'+str(sel_item))### del folder
        self.write_to_list_file(self.save_list_file)

    def write_to_file(self, file):
        try:
            list_widget = self.list_sheet
            entries = '\n'.join(list_widget.item(ii).text() for ii in range(list_widget.count()))
            with open(file, 'w',encoding='utf-8') as fout:
                fout.write(entries)
                print( "entries", entries)  
        except OSError as err:
            print(f"file {file} could not be written")

    def read_from_file(self, file):
        try:
            list_widget = self.list_sheet
            with open(file, 'r',encoding='utf-8') as fin:
                    entries = [e.strip() for e in fin.readlines()]
            list_widget.insertItems(0, entries)
        except OSError as err:
            with open(file, 'w',encoding='utf-8'):
                pass
    
    def write_to_list_file(self, file):
        try:
            list_widget = self.list_file
            entries = '\n'.join(list_widget.item(ii).text() for ii in range(list_widget.count()))
            with open(file, 'w',encoding='utf-8') as fout:
                fout.write(entries)
        except OSError as err:
            print(f"file {file} could not be written")
    
    def read_from_list_file(self, file):
        entries = []
        union_en =[]
        try:
            list_widget = self.list_file
            union_widget = self.list_union
            with open(file, 'r',encoding='utf-8') as fin:
                    for e in fin.readlines():
                         if "Union" in e :
                            union_en.append(e.strip())
                         else:
                            entries.append(e.strip())
                         print(union_en)   
                         print(entries)
            list_widget.insertItems(0, entries)
            union_widget.insertItems(0, union_en)
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

if __name__ == "__main__":
    
    union_list = []
    count = []
    filename=[]
    measurement=[]
    dimension=[]
    headers=[]
    titlelist=[]
    
    app  = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    app.setStyle("Fusion")
    main = Mainwindow()
    widget.addWidget(main)
    widget.setFixedWidth(1445)
    widget.setFixedHeight(770)
    widget.show()
    sys.exit(app.exec_())

