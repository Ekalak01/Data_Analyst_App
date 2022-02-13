import argparse
import colorsys
from sqlite3 import Row
from tkinter import Y
from PyQt5 import QtGui, QtWidgets,QtCore,QtWebEngineWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtChart import *
import pandas as pd
from PyQt5.uic import loadUi
import sys
from datetime import *
import os
import re
import shutil
import numpy as np
import random
import altair as alt
from io import StringIO
from range_slider import *
"""from test3 import *"""

class WebEngineView(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.page().profile().downloadRequested.connect(self.onDownloadRequested)
        self.windows = []

    @QtCore.pyqtSlot(QtWebEngineWidgets.QWebEngineDownloadItem)
    def onDownloadRequested(self, download):
        if (
            download.state()
            == QtWebEngineWidgets.QWebEngineDownloadItem.DownloadRequested
        ):
            path, _ = QtWidgets.QFileDialog.getSaveFileName(
                self, self.tr("Save as"), download.path()
            )
            if path:
                download.setPath(path)
                download.accept()

    def createWindow(self, type_):
        if type_ == QtWebEngineWidgets.QWebEnginePage.WebBrowserTab:
            window = QtWidgets.QMainWindow(self)
            view = QtWebEngineWidgets.QWebEngineView(window)
            window.resize(640, 480)
            window.setCentralWidget(view)
            window.show()
            return view

    def updateChart(self, chart, **kwargs):
        output = StringIO()
        chart.save(output, "html", **kwargs)
        self.setHtml(output.getvalue())

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
            self.sett.WindowsFilterPopup(source_item.item(0, 0).text())
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
        #self.clearSelection()
        
    def setup(self,sett):
        self.sett = sett 
        
    def dragLeaveEvent(self,event) -> None:
        if self.count():            
            self.takeItem(self.currentRow())
            self.clearSelection()
            self.sett.get_rowcol()
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
            self.clearSelection()
            self.sett.get_rowcol()
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
        #self.clearSelection()  
    
    def setup(self,sett):
        self.sett = sett 
    
    def dragLeaveEvent(self,event) -> None:
        if self.count():            
            self.setDefaultDropAction(QtCore.Qt.MoveAction)
            self.takeItem(self.currentRow())
            self.clearSelection()
            self.sett.get_rowcol()
                          
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
            
            self.sett.get_rowcol() 
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
        #self.setDefaultDropAction(Qt.MoveAction)
        
        
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

    def sort(self, Ncol, order):
        self.layoutAboutToBeChanged.emit()
        header=self.arraydata.columns[Ncol]
        try:
            for j in self._dataframe.iloc[:,Ncol]:
            
                if '-' in str(j):
                    
                    self._dataframe[header]=pd.to_datetime(self._dataframe[header].astype(str), format='%Y-%d-%m')
                    print(self._dataframe[header])
                    self._dataframe[header] = self._dataframe[header].dt.strftime('%d/%m/%Y')
                    print(self._dataframe[header])
                    break
                else:
                    pass
                
        except:
            pass
        
        try:
            for j in self._dataframe.iloc[:,Ncol]:
            
                if '00:00:00' in str(j):
                    
                    self._dataframe[header]=pd.to_datetime(self._dataframe[header].astype(str), dayfirst=True)
                    print(self._dataframe[header])
                    self._dataframe[header] = self._dataframe[header].dt.strftime('%d/%m/%Y')
                    print(self._dataframe[header])
                    break
                else:
                    pass
                
        except:
            pass
            
        for j in self._dataframe.iloc[:,Ncol]:  
            if '/' in str(j):
                try :
                    self._dataframe[header]=pd.to_datetime(self._dataframe[header].astype(str), dayfirst=True)
                    self._dataframe[header] = self._dataframe[header].dt.strftime('%d/%m/%Y')
                except:
                    pass
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
        self.list_filter.setup(self) 


        #self.fil_bt.clicked.connect(self.start_fil)
        self.back_bt.clicked.connect(self.backbt)
        
        self.my_layout=QVBoxLayout(self.chart)
        self.w = WebEngineView()
        self.file_combo.addItem("None")# Error if use call None in App
        #self.combo_box.activated.connect(self.do_something)
        
        self.file_combo.activated.connect(self.selectionChange)
        self.file_combo.activated.connect(self.countheadtype)

        #selected measure
        lstmeasure=['None','min','max','mid','sum','count']
        for i in lstmeasure:
            self.slmeasure_bt.addItem(i)
        self.slmeasure_bt.activated.connect(self.selectMea)
        
        #selected Graph
        self.shgraph_bt.addItem("None")
        self.shgraph_bt.addItem("Pie chart")
        self.shgraph_bt.addItem("Line chart")
        self.shgraph_bt.addItem("Bar chart")
        self.shgraph_bt.activated.connect(self.selectGraph)
        
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

    def selectMea(self):
        try:
            self.groupby(self.dff,self.dtcol,self.dtrow)
            self.createtable(self.dfff)
            self.plot(self.dfff,self.row,self.col)
        except:
            pass

    def selectGraph(self):
        graph = self.shgraph_bt.currentText()
        if self.col != [] and self.row != []:
            if graph == 'Bar chart':
                if self.dcol ==True:
                    self.vbarplot(self.dfff,self.row,self.col)
                else:
                    self.hbarplot(self.dfff,self.row,self.col)
            elif graph == 'Line chart':
                self.lineplot()
            elif graph =='Pie chart':
                self.pieplot()
            else:
                pass
        else:
            pass

    def selectionChange(self, i):
        self.texte = self.file_combo.currentText()
        print(f"Index {i} pour la commune {i}, texte -> {self.texte}")
        return self.texte
    
    def countheadtype(self):
        measurement.clear()
        dimension.clear()
        if self.texte == 'None':
            sheet_pg=Datasheet(self.csvfol)
            widget.addWidget(sheet_pg)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            direct = "Appfolder/Import"+"/"+str(self.texte)
            self.df = pd.read_csv(direct+"/save.csv")
            
            for colname, coltype in self.df.dtypes.iteritems():
                headers.append(colname)
                if coltype == object:
                    dimension.append(colname) 
                elif 'Code' in colname or 'ID' in colname:
                    dimension.append(colname)
                else:
                    measurement.append(colname)
            self.pd=self.df
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
        
    def backbt(self):
        dimension.clear()
        measurement.clear()
        datasource_pg = Mainwindow()
        widget.addWidget(datasource_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
            

    def insertdata(self):
        
        list_dimension = self.list_dimension
        self.list_dimension.clear()
        list_measurement=self.list_measures
        self.list_measures.clear()
        list_dimension.insertItems(0, dimension)
        list_measurement.insertItems(0, measurement)

    def lineplot(self):
        try:
            self.my_layout.removeWidget(self.w)
        except:
            pass
        mesure=[]
        if self.dcol == True:
            for i in self.row:
                mesure.append(i)
            strm='//'.join(str(i) for i in mesure)
            alt.data_transformers.disable_max_rows()
            line=alt.Chart(self.dfff).transform_fold(
                    mesure
                ).mark_line(point=True).encode(
                    x=self.col[0]+':N',
                    y=alt.Y('value:Q',title=strm),
                    color=alt.Color('key:N',legend=alt.Legend(title='Line Color')),
                    tooltip=[self.col[0],'value:Q']
                        ).properties(
                            width=500,
                            height=350)
            self.w.updateChart(line)
        else:
            for i in self.col:
                mesure.append(i)
            strm='//'.join(str(i) for i in mesure)
            alt.data_transformers.disable_max_rows()
            line=alt.Chart(self.dfff).transform_fold(
                mesure
            ).mark_line(point=True).encode(
                y=self.row[0]+':N',
                x=alt.X('value:Q',title=strm),
                color=alt.Color('key:N',legend=alt.Legend(title='Line Color')),
                tooltip=[self.row[0],'value:Q']
                    ).properties(
                        width=500,
                        height=350)
            self.w.updateChart(line)

    def pieplot(self):
        try:
            self.my_layout.removeWidget(self.w)
        except:
            pass
        alt.data_transformers.disable_max_rows()
        if self.dcol == True:
            for i in range(len(self.row)):
                    pie=alt.Chart(self.dfff).mark_arc().encode(
                    theta=self.row[0]+':Q'
                    ,color=self.col[0]+':N'
                    ,tooltip=[str(self.col[0]),self.row[0],self.row[i]])
            self.w.updateChart(pie)
        else:
            for i in range(len(self.row)):
                    pie=alt.Chart(self.dfff).mark_arc().encode(
                    theta=self.col[0]+':Q'
                    ,color=self.row[0]+':N'
                    ,tooltip=[str(self.row[0]),self.col[0],self.col[i]])
            self.w.updateChart(pie)
    

    def hbarplot(self,df,row,col):
        try:
            self.my_layout.removeWidget(self.w)
        except:
            pass
        self.shgraph_bt.setCurrentText('Bar chart')
        alt.data_transformers.disable_max_rows()     
        nchart=[]
        if len(row) >=2:
            for i in range(len(col)):
                ch=alt.Chart(df).mark_bar().encode(
                y=str(row[1])+':N',
                x=self.col[i]+':Q',
                tooltip=[str(row[0]),str(row[1]),col[i]]
                ).facet(
                    row=alt.Row(str(row[0]))
                ).resolve_scale(y='independent').interactive()
                nchart.append(ch)
        else:
            for i in range(len(col)):
                ch=alt.Chart(df).mark_bar().encode(
                    y=str(row[0])+':N',
                    x=col[i]+':Q',
                    tooltip=[str(row[0]),col[i]]
                    ).interactive()
                nchart.append(ch)
                
        charts=alt.hconcat(*nchart)
        self.w.updateChart(charts)
            
        self.my_layout.addWidget(self.w)
          
    def vbarplot(self,df,row,col):
        try:
            self.my_layout.removeWidget(self.w)
        except:
            pass
        self.shgraph_bt.setCurrentText('Bar chart')
        alt.data_transformers.disable_max_rows()     
        nchart=[]
        if len(col) >=2:
            for i in range(len(row)):
                ch=alt.Chart(df).mark_bar().encode(
                x=str(col[1])+':N',
                y=row[i]+':Q',
                tooltip=[str(col[0]),str(col[1]),row[i]]
                ).facet(column=alt.Column(str(col[0]))
                    
                ).resolve_scale(x='independent').interactive()
                nchart.append(ch)
        else:
            for i in range(len(row)):
                ch=alt.Chart(df).mark_bar().encode(
                x=str(col[0])+':N',
                y=row[i]+':Q',
                tooltip=[str(col[0]),row[i]]
                ).interactive()
                nchart.append(ch)

             
        charts=alt.vconcat(*nchart)
        self.w.updateChart(charts)
            
        self.my_layout.addWidget(self.w)  


    def get_rowcol(self):
        try:
            self.slmeasure_bt.setCurrentText('sum')
            self.dff=self.df
            listcol=self.list_col
            listrow=self.list_row
            col=[]
            row=[]
            lst=[]
            dtcol=[]
            dtrow=[]
            for x in range(listcol.count()):
                col.append(listcol.item(x).text())
                dtcol.append(listcol.item(x).text())
            for x in range(listrow.count()):
                row.append(listrow.item(x).text())
                dtrow.append(listrow.item(x).text())
            self.col=col
            self.row=row
            
            for i in col:
                if 'Date' in i :
                    self.dff[i]=pd.to_datetime(self.dff[i], errors='coerce')
                    dateindex=dtcol.index(i)
                    dtcol.remove(i)
                    dtcol.insert(dateindex,self.dff[i].dt.year)
                lst.append(i)
            
            for i in row:
                if 'Date' in i :
                    self.dff[i]=pd.to_datetime(self.dff[i], errors='coerce')
                    dateindex=dtrow.index(i)
                    dtrow.remove(i)
                    dtrow.insert(dateindex,self.dff[i].dt.year)
                lst.append(i)

            if len(lst) == 0:
                self.dfff =pd.DataFrame({'' : []})
                self.createtable(self.dfff)
            
            elif len(lst)==1:
                for i in measurement:
                    lst.append(i)
                self.dff=self.dff.loc[:,lst]

            else:
                self.dff=self.dff.loc[:,lst]
            self.dcol=False

            self.dtcol=dtcol
            self.dtrow=dtrow

            self.groupby(self.dff,dtcol,dtrow)
            self.createtable(self.dfff)
            self.plot(self.dfff,row,col)
        except:
            pass
    
    def barplot1(self,df,row,col):
        try:
            self.my_layout.removeWidget(self.w)
        except:
            pass
        self.shgraph_bt.setCurrentText('Bar chart')
        alt.data_transformers.disable_max_rows()     
        nchart=[]
        if len(col) >=2:
            
            ch=alt.Chart(df).mark_bar().encode(
            x=col[1]+':Q',
            y=row[0]+':N',
            tooltip=[str(col[0]),col[1],row[0]]
            ).facet(column=alt.Column(str(col[0]))
                
            ).resolve_scale(x='independent').interactive()
            nchart.append(ch)
        else:
            for i in range(len(row)):
                ch=alt.Chart(df).mark_bar().encode(
                x=str(col[1])+':Q',
                column=col[0]+':N',
                tooltip=[str(col[0]),col[1]]
                ).interactive()
                nchart.append(ch)

             
        charts=alt.vconcat(*nchart)
        self.w.updateChart(charts)
            
        self.my_layout.addWidget(self.w) 


    def barplot2(self,df,row,col):
        try:
            self.my_layout.removeWidget(self.w)
        except:
            pass
        self.shgraph_bt.setCurrentText('Bar chart')
        alt.data_transformers.disable_max_rows()     
        nchart=[]
        if len(row) >=2:
            for i in range(len(row)):
                ch=alt.Chart(df).mark_bar().encode(
                x=col[0]+':N',
                y=row[1]+':Q',
                tooltip=[str(col[0]),row[0],row[1]]
                ).facet(row=alt.Row(str(row[0]))
                    
                ).resolve_scale(x='independent').interactive()
                nchart.append(ch)
        else:
            for i in range(len(row)):
                ch=alt.Chart(df).mark_bar().encode(
                y=row[1]+':Q',
                row=alt.Row(row[0]+':N'),
                tooltip=[row[0],row[1]]
                ).interactive()
                nchart.append(ch)

             
        charts=alt.vconcat(*nchart)
        self.w.updateChart(charts)
            
        self.my_layout.addWidget(self.w) 


    def checkdimension(self):
        self.dcol=False
        self.mcol=False
        self.mrow=False
        for i in dimension:
            if i in self.col:
                self.dcol=True
        for i in measurement:
            if i in self.col:
                self.mcol=True
            elif i in self.row:
                self.mrow=True


    def plot(self,df:pd.DataFrame,row,col):
        self.checkdimension()

        if self.dcol==True and self.mcol==True:
            self.barplot1(df,row,col)
        elif self.dcol==False and self.mrow==True:
            self.barplot2(df,row,col)
        elif self.dcol==True and self.mcol==False:
            self.vbarplot(df,row,col)
        else:
            self.hbarplot(df,row,col)

    def groupby(self,df:pd.DataFrame,dtcol,dtrow):
        self.checkdimension()
        mea = self.slmeasure_bt.currentText()
        if mea =='sum':
            if self.dcol==True:
                df=df.groupby(dtcol).sum()
                self.dfff=df.reset_index()
            else:
                df=df.groupby(dtrow).sum()
                self.dfff=df.reset_index()
        elif mea == 'min':
            if self.dcol==True:
                df=df.groupby(dtcol).min()
                self.dfff=df.reset_index()
            else:
                df=df.groupby(dtrow).min()
                self.dfff=df.reset_index()
        elif mea == 'max':
            if self.dcol==True:
                df=df.groupby(dtcol).max()
                self.dfff=df.reset_index()
            else:
                df=df.groupby(dtrow).max()
                self.dfff=df.reset_index() 
        elif mea == 'mid':
            if self.dcol==True:
                df=df.groupby(dtcol).mean()
                self.dfff=df.reset_index()
            else:
                df=df.groupby(dtrow).mean()
                self.dfff=df.reset_index() 
        elif mea == 'count':
            if self.dcol==True:
                df=df.groupby(dtcol).count()
                self.dfff=df.reset_index()
            else:
                df=df.groupby(dtrow).count()
                self.dfff=df.reset_index() 


    def createtable(self,df:pd.DataFrame):
        
        self.model = PandasModel(df)
        self.tableView.setModel(self.model)
        self.tableView.setSortingEnabled(True)
        self.tableView.sortByColumn(0, Qt.AscendingOrder)
    
    def WindowsFilterPopup(self, item):
        try:
            self.df=self.pd
            if 'Date' not in item and item in dimension:
                exPopup = FilterPopup(item,self.df)
                exPopup.setGeometry(100, 200, 100, 100)
                
                exPopup.exec()
                self.filter_data(item)
            else:
                exPopup = FilterPopup2(item,self.dfff)
                exPopup.setGeometry(100, 200, 100, 100)
                exPopup.exec()
                self.filterrange(item)
        except:
            pass
        
    

    def lastfilterdata(self,dic,item):
        self.last_fil=[]
        self.lastfilhead=item
        for i in dic:
            self.last_fil.append(i)

    def filterrange(self,item):
        try:
            min=int(rangefilter[0])
            max=int(rangefilter[1])
            self.dfff=self.dfff.loc[(self.dfff[item] >= min) & (self.dfff[item] <= max)] 
            self.df=self.df.loc[(self.df[item] >= min) & (self.df[item] <= max)] 
            print(self.dfff)
            self.createtable(self.dfff)
            if self.col != [] and self.row != []:
                self.plot(self.dfff,self.row,self.col)      

            return self.dfff 
        except:
            pass

    def filter_data(self,item):
        
        try:
            print(self.last_fil)
            self.dfff[self.lastfilhead].unique()
            self.df_data_list=self.last_fil
            self.dfff=self.dfff[self.dfff[self.lastfilhead].isin(self.df_data_list)]
            print(self.dfff)

        except:
            pass
        
        try:
            if item in self.col or item in self.row:
                self.dfff[item].unique()
                self.df_data_list=checked_items
                self.dfff=self.dfff[self.dfff[item].isin(self.df_data_list)]
                dic=self.dfff.set_index(item).T.to_dict('list')
                self.lastfilterdata(dic,item)
                
                
                self.df=self.df[self.df[item].isin(self.df_data_list)]
                self.createtable(self.dfff)
                if self.col != [] and self.row != []:
                    self.plot(self.dfff,self.row,self.col) 
            else:
                pass
        except:
            pass


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
               
                Input = "Union"
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
                        
                        
                    r = open(self.save_list_file,'r',encoding='utf-8')          
                    
                    for i in r:
                        i=i.replace('\n','')
                        
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
    
    def gotosheet(self):
            try:
                sel_item=self.list_sheet.currentItem().text()
                self.csvfol=self.dirr_sheet+'/'+sel_item
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
                        df = pd.read_excel(fname)
                        
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
        if fname[-5:] == '.xlsx':
            self.savefile_excel(df,path)
        else:
            self.savefile(df,path)
        self.write_to_list_file(self.save_list_file)
        #print("save")    

    def savefile(self,df:pd.DataFrame,path):
        try:
            df.to_csv(path+'/save.csv',index=False)
            self.gotofile()
        except:
            pass   

    def savefile_excel(self,df:pd.DataFrame,path):
        try:
            df.to_csv(path+'/save.csv',index=False,encoding='windows-1252')
            self.gotofile()
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

class FilterPopup(QDialog):
    def __init__(self, name,df:pd.DataFrame,parent=None):
    
        super(FilterPopup, self).__init__(parent)
        self.name = name
        self.df=df
        checked_items.clear()
        self.setFixedWidth(380)
        self.setFixedHeight(517)
        loadUi("FileterPop.ui",self)
        df=df.groupby(self.name).sum().reset_index()
        self.dflst = df[self.name].values.tolist()
        self.label_head.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:'OCR A Extended';font-size:25pt;font-weight:600\">"+str(name)+"</span></p></body></html>") 
       
        self.listWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        
        for i in self.dflst:
            item = QListWidgetItem(str(i))
            # could be Qt.Unchecked; setting it makes the check appear
            item.setCheckState(Qt.Checked)
            self.listWidget.addItem(item)
        
        self.check_bt.clicked.connect(self.Checkstate)
        self.okButton.clicked.connect(self.generate_file)
        self.okButton.clicked.connect(self.close)
        self.cancelButton.clicked.connect(self.close)

        
        self.setWindowTitle("Filter Data"+  "["+str(name)+"]")
        self.show()

    def Checkstate(self):
        
        for index in range(self.listWidget.count()):
            if self.listWidget.item(index).checkState() == Qt.Checked:
                self.listWidget.clear()
                for i in  self.dflst:
                    item = QListWidgetItem(str(i))
                    # could be Qt.Unchecked; setting it makes the check appear
                    item.setCheckState(Qt.Unchecked)
                    self.listWidget.addItem(item)
                    
            else:
                self.listWidget.clear()
                for i in  self.dflst:
                    item = QListWidgetItem(str(i))
                    # could be Qt.Unchecked; setting it makes the check appear
                    item.setCheckState(Qt.Checked)
                    self.listWidget.addItem(item)
                    
                
    def generate_file(self):
        
        for index in range(self.listWidget.count()):
            if self.listWidget.item(index).checkState() == Qt.Checked:
                checked_items.append(self.listWidget.item(index).text())
                print("checked_items",checked_items)
        self.close

class FilterPopup2(QDialog):
    def __init__(self, name,df:pd.DataFrame,parent=None):
        super(FilterPopup2, self).__init__(parent)
        self.name = name
        self.df=df
        minimum=self.df[name].min()
        maximum=self.df[name].max()
        rangefilter.clear()
        self.setFixedWidth(480)
        self.setFixedHeight(517)
        loadUi("FileterPop2.ui",self)
        self.label_head.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:'OCR A Extended';font-size:23pt;font-weight:600\">"+str(name)+"</span></p></body></html>")
        
        self.slider.minimumChanged.connect(self.label_minimum.setText)
        self.slider.minimumChanged.connect(self.line_minimum.setText)
        
        self.slider.maximumChanged.connect(self.label_maximum.setText)
        self.slider.maximumChanged.connect(self.line_maximum.setText)
        
        self.slider.setMinimumHeight(30)
        self.slider.setMinimum(int(minimum))
        self.slider.setMaximum(int(maximum))
        self.slider.setLow(int(minimum))
        self.slider.setHigh(int(maximum))
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        
        self.okButton.clicked.connect(self.close)
        self.cancelButton.clicked.connect(self.close)
        self.okButton.clicked.connect(self.echo)

    

 
        self.setWindowTitle("Filter Data"+  "["+str(name)+"]")

        self.raise_()
        self.show()

    def echo(self):
        min=self.label_minimum.text()
        max=self.label_maximum.text()
        rangefilter.append(min)
        rangefilter.append(max)
        

if __name__ == "__main__":

    rangefilter=[]
    checked_items=[]
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

