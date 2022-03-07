import unittest
from manager_object import *
from PyQt5 import QtGui, QtWidgets,QtCore,QtWebEngineWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtChart import *
import pandas as pd
from pandas.util.testing import *
from testcase1 import *
from testcase2 import *
from testfilter import *
from testgroupby import * 

class TestNumber(unittest.TestCase):
    
    def setUp(self):
        self.op = importclass()
        self.parent_dir=QtCore.QDir.currentPath()
        self.filename = "/"+"csvtest1.csv"
        self.path = self.parent_dir + self.filename
        self.filename = "/"+"sp.csv"
        self.path2 = self.parent_dir + self.filename
        self.list_csv = ["csvtest1.csv","sp.csv"]
        
    def test_Sheet(self):
        
        self.op.Add_sheet()
        nt = self.op.opensheet()
        self.op.Add_sheet()
        self.op.save(nt)
        
    def test_Import_File(self):
       
        Im =  self.op.Importfile_class(self.path)
        Im2 = self.op.Importfile_class(self.path2)
        df =  self.op.gofile("csvtest1.csv")
        df2 = self.op.gofile("sp.csv")
        self.op.save_filename(df,Im)
        self.op.save_filename(df2,Im2)
    
    def test_Union(self):
        
        self.op.union_file(self.list_csv)
        self.op.gofile("Union0")
     
    
        
if __name__ == '__main__':
   unittest.main()