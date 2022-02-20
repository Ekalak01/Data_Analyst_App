import unittest
from manager_object import *
from PyQt5 import QtGui, QtWidgets,QtCore,QtWebEngineWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtChart import *
import pandas as pd

class TestNumber(unittest.TestCase):
    
    def test_sheet(self):
        op = importclass()
        nt = op.opensheet()
        op.save(nt)
        
    def test_file(self):
        path = "C:/Users/s6301012620103/Documents/Softdev2/Assigment_3/testcsv/version7.2/csvtest1.csv"
        op = importclass()
        op.openx()
        Im = op.Importfile_class(path)
        df =  op.gofile("csvtest1.csv")
        op.save_filename(df,Im)
    
    def test_union(self):
        list_csv = ["csvtest1.csv","sp.csv"]
        op = importclass()
        op.union_file(list_csv)
        op.gofile("Union0")
        
if __name__ == '__main__':
   unittest.main()