import unittest
from manager_object import *
import pandas as pd

class TestGroupby5(unittest.TestCase):
    def setUp(self) -> None:
        self.dt=data()
        self.df=pd.read_csv('test.csv')
        self.dimension=self.dt.is_dimension(self.df)
        self.measurement=self.dt.is_measurement(self.df)
        return super().setUp()  

    def test_getdimension(self):
        self.assertIsInstance(self.dt.is_dimension(self.df),list)    
    
    def test_getmeasurement(self):
        self.assertIsInstance(self.dt.is_measurement(self.df),list)

    def test_isdimension(self):
        self.assertTrue(self.dt.check_dimension('Name',self.dimension))    
        self.assertFalse(self.dt.check_dimension('Sales',self.dimension))

    def test_ismeasurement(self):
        self.assertTrue(self.dt.check_measurement('Sales',self.measurement))    
        self.assertFalse(self.dt.check_measurement('Names',self.measurement))

    
    def test_getmin(self):
        col=['Name']
        agg={'Sales':'min'}
        group=self.dt.getgroupby(self.df,col,agg)
        Ice=group.loc[group['Name']=='Ice','Sales'].values[0]
        Pooh=group.loc[group['Name']=='Pooh','Sales'].values[0]
        self.assertEqual(Ice,3)
        self.assertEqual(Pooh,5)

    def test_getmax(self):
        col=['Name']
        agg={'Sales':'max'}
        group=self.dt.getgroupby(self.df,col,agg)
        Ice=group.loc[group['Name']=='Ice','Sales'].values[0]
        Pooh=group.loc[group['Name']=='Pooh','Sales'].values[0]
        self.assertEqual(Ice,11)
        self.assertEqual(Pooh,12)
    
    def test_getsum(self):
        col=['Name']
        agg={'Sales':'sum'}
        group=self.dt.getgroupby(self.df,col,agg)
        Ice=group.loc[group['Name']=='Ice','Sales'].values[0]
        Pooh=group.loc[group['Name']=='Pooh','Sales'].values[0]
        self.assertEqual(Ice,25)
        self.assertEqual(Pooh,50)

    def test_getmean(self):
        col=['Name']
        agg={'Sales':'mean'}
        group=self.dt.getgroupby(self.df,col,agg)
        Ice=group.loc[group['Name']=='Ice','Sales'].values[0]
        Pooh=group.loc[group['Name']=='Pooh','Sales'].values[0]
        self.assertEqual(Ice,6.25)
        self.assertEqual(Pooh,8.333333333333334)

    def test_getcount(self):
        col=['Name']
        agg={'Sales':'count'}
        group=self.dt.getgroupby(self.df,col,agg)
        Ice=group.loc[group['Name']=='Ice','Sales'].values[0]
        Pooh=group.loc[group['Name']=='Pooh','Sales'].values[0]
        self.assertEqual(Ice,4)
        self.assertEqual(Pooh,6)

    def test_getmedian(self):
        col=['Name']
        agg={'Sales':'median'}
        group=self.dt.getgroupby(self.df,col,agg)
        Ice=group.loc[group['Name']=='Ice','Sales'].values[0]
        Pooh=group.loc[group['Name']=='Pooh','Sales'].values[0]
        self.assertEqual(Ice,5.5)
        self.assertEqual(Pooh,8.5)

