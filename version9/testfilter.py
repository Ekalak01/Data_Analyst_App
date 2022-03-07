import unittest
from manager_object import *
import pandas as pd
from pandas.util.testing import *

class TestFilter4(unittest.TestCase):
    def setUp(self) -> None:
        self.ft=filter()
        self.df=pd.read_csv('sp.csv')
        return super().setUp()

    def test_filterdata(self):
        df1=self.ft.filter_data(self.df,'Region',{'Region':['West','East']})
        df2=self.df[self.df['Region'].isin(['West','East'])]
        assert_frame_equal(df1,df2)

    def test_filterrange(self):
        df1=self.ft.filterrange(self.df,'Profit',{'Profit':[1000,6000]})  
        df2=self.df.loc[(self.df['Profit'] >= 1000) & (self.df['Profit'] <= 6000)]
        assert_frame_equal(df1,df2)
    
    def test_filterdatetime(self):
        self.df['Order Date']=pd.to_datetime(self.df['Order Date'],dayfirst=True).dt.year
        df1=self.ft.filter_data(self.df,'Order Date',{'Order Date':[2018,2019]})
        df2=self.df[self.df['Order Date'].isin([2018,2019])]
        assert_frame_equal(df1,df2)
