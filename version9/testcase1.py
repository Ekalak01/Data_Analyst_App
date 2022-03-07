import unittest
from manager_object import *
from PyQt5 import QtGui, QtWidgets,QtCore,QtWebEngineWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtChart import *
import pandas as pd

class TestNumber2(unittest.TestCase):
    
    def setUp(self):
        self.dt = data()
        self.csvfol = "Appfolder/Sheet/Sheet0"
        self.texte = "csvtest1.csv" ##File name this u read add Save Data (Head Type)
        self.direct = "Appfolder/Import"+"/"+str(self.texte)
        self.df = pd.read_csv(self.direct+"/save.csv")
        
    def test_Insert_data(self):
        Im = importclass()
        Im.Add_sheet()
        di = self.dt.is_dimension(self.df)
        mea = self.dt.is_measurement(self.df)
        self.dt.backupHeaderinJson(di,mea,self.csvfol,self.texte)##Back Up In data.json
    
    def test_CheckHeader(self):
        di = self.dt.is_dimension(self.df)
        mea = self.dt.is_measurement(self.df)
        self.dt.check_dimension("Customer Name",di)
        self.dt.check_measurement("Sales",mea)
        
    def test_Wirte_Read_Json(self):
        self.dt.wirtedata(self.csvfol)## Replace {} Data
        self.dt.readdata(self.csvfol)
        
    
if __name__ == '__main__':
   unittest.main()