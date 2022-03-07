import unittest
from manager_object import *
from PyQt5 import QtGui, QtWidgets,QtCore,QtWebEngineWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtChart import *
import pandas as pd

class TestNumber3(unittest.TestCase):
    
    def setUp(self):
        self.op = importclass()
        
    def test_RemoveSheet(self):
        op = importclass()
        op.opensheet()
        #op.save(dr)
        op.rm_sh("Sheet0")
            
    def test_RemoveFile(self):
        op = importclass()
        op.rm_file("sp.csv")
        
    def test_clear(self):
        self.op.clearall()
"""if __name__ == '__main__':
   unittest.main()"""