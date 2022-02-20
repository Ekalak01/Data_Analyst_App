import unittest
from manager_object import *
from PyQt5 import QtGui, QtWidgets,QtCore,QtWebEngineWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtChart import *
import pandas as pd

class TestNumber(unittest.TestCase):
    
    def test_insert_data(self):
        direct = "Appfolder/Import"+"/"+"csvtest1.csv"
        dt = data()
        dt.is_dimension(direct)
        dt.is_measurement(direct)
     
if __name__ == '__main__':
   unittest.main()