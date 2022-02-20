import argparse
import colorsys
from genericpath import exists
from sqlite3 import Row
#from this import d
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
import json

class importclass :
    def __init__(self):
        ####
            parent_dir=QtCore.QDir.currentPath()
            print("parent_dir",parent_dir)
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
        ####   
    def opensheet (self):
        """
        Created Folder Sheet 
        
        """
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
        self.save(self.dirr_sheet)
        #self.read_from_file(self.save_file)  
        #self.dirrsheet(self.dirr_sheet)
        
        return self.dirr_sheet
    
    def save(self,dirr_sheet):
        self.filename = "Sheetname"
        self.save_file = dirr_sheet+"/"+self.filename+'.txt'
        return self.save_file
    
    def openx(self):
        
        parent_dir=QtCore.QDir.currentPath()
        #print("parent_dir",parent_dir)
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
        print ( self.save_list_file )
        return self.save_list_file
    
    def dirr(self):
        return self.dirr_Import
          
    def Importfile_class (self,path):
        filename = []
        #print("Path Import 2",path)
        fname = QFileInfo(path).fileName()
        #print(fname,"import_file 2")
        if fname not in filename:    
            filename.append(path)
            
            if fname[-4:] == '.csv':
                df = pd.read_csv(path,encoding='utf-8-sig')
            elif fname[-5:] == '.xlsx':
                df = pd.read_excel(path)
            try:
                self.save_filename(df,fname)
                return fname
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
        #self.write_to_list_file(self.save_list_file)
        return True   
    
    def savefile(self,df:pd.DataFrame,path):
        return df.to_csv(path+'/save.csv',index=False)
           
    def savefile_excel(self,df:pd.DataFrame,path):
        return df.to_csv(path+'/save.csv',index=False,encoding='windows-1252')
    
    def union_file(self,list_csv):
        """
            Union File ( list_csv ) 
        """
        xo = []
        for i in range(len(list_csv)):
            print("infor")
            if len(list_csv) >= 2:
                print("if len = 2")
                Input = "Union"
                co=[]
                fname = []
                check =[]
                with open(self.save_list_file,'a',encoding='utf-8') as a:
                    read = open(self.save_list_file,'r',encoding='utf-8')   
                    Lines = read.readlines()
                    for j in Lines:
                        check.append(j.replace('\n',''))
                    for x in range(len(list_csv)):
                        #pathbuf = os.path.join(list_csv[i])
                        #df = pd.read_csv(self.gofile(list_csv[x]))
                        xo.append(self.gofile(list_csv[x]))
                        #print("xo",xo)
                    
                    if "Union0" in check: 
    
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
                                break       
                        
                    else:
                        print("else")
                        a.write("\n"+Input+'0')
                        x = Input+'0'
                        fname.append(x)
                    frame = pd.concat(xo,axis=0,ignore_index=True)
                    frame.drop_duplicates(inplace=True)
                    print("frame",frame)
                    print("fname",fname)
                    print("x",x)
                    return self.save_union(frame,fname) 
                    #return frame
            else:
                print("Error")
                pass
            
    def save_union(self,df,fname):
        """
            save file name is Union
        """
        print("save_union")
        r = open(self.save_list_file,'r',encoding='utf-8')          
                    
        for i in r:
            i=i.replace('\n','')
        
        r.close()
        
        path = os.path.join(self.dirr_Import,fname[0])
        print(path,"path")
        
        if not os.path.exists(path):
            os.mkdir(path)
            #df.to_csv(os.path.join(path,str(x) +".csv"),index = False, encoding='utf-8-sig')
        self.savefile(df,path) 
    
    def gofile(self,sel_item):
        
        op = importclass()
        sv = op.dirr()
        self.csvfol= sv+'/'+sel_item+'/save.csv'
        print("sel",sel_item)
        print("Path in Import Folder",self.csvfol)
        try:
            df = pd.read_csv(self.csvfol,encoding='windows-1252')
        except:
            df = pd.read_csv(self.csvfol,encoding='utf-8-sig')
          
        return df
    
    def rm_sh(self,sel_item):
    
        dr = self.opensheet()
        nt = self.save(dr)
        shutil.rmtree(dr+'/'+str(sel_item))### del folder
        return nt
    
    def rm_file(self,sel_item):
        
        dr = self.dirr()
        sv = self.openx()
        shutil.rmtree(dr+'/'+str(sel_item))### del folder
        return sv
    
class data:
    def __init__(self):
        
        self.dic_head_data = {}
        
        """parent_dir=QtCore.QDir.currentPath()
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
        #self.read_from_list_file(self.save_list_file)"""
    
    def openjsoninsheet(self):
        
        parent_dir=QtCore.QDir.currentPath()
        #print("parent_dir",parent_dir)
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
        self.filename = "data"
        self.save_json_file = self.dirr_sheet+"/"+self.filename+'.json'
        self.wirtedata(self.dirr_sheet)
        print ( "self.dirr_sheet",self.dirr_sheet)
        
    def is_dimension(self,direct):
        dimension = []
        self.df = pd.read_csv(direct+"/save.csv")
        for colname, coltype in self.df.dtypes.iteritems():
                if coltype == object:
                    dimension.append(colname) 
                elif 'Code' in colname or 'ID' in colname:
                    dimension.append(colname)
        return dimension
    
    def is_measurement(self,direct):
        measurement = []
        self.df = pd.read_csv(direct+"/save.csv")
        for colname, coltype in self.df.dtypes.iteritems():
            if 'Code' not in colname or 'ID' not in colname :
                if coltype == int or coltype == float:
                    measurement.append(colname) 
        return measurement
    
    """
        # print(dt.check_dimension(direct))
        def check_dimension(self,direct):
        x = self.is_dimension(direct)
        if  "Order ID" in  x:
            print("True")
        else:
            print("pass") """
           
    def wirtedata (self,csvfol):
        x = csvfol+"/"+"data.json"
        print("x",x)
        with open (x,"w") as file:
            json.dump(self.dic_head_data,file)
    
    def readdata (self,csvfol):
        print("readfilx",csvfol)
        x = csvfol+"/"+"data.json"
        if os.path.exists(x) == False:
            self.wirtedata(csvfol)
        with open (x,"r") as file:
            self.dic_head_data = json.load(file)
        print("self.dic_head_data",self.dic_head_data)
        return self.dic_head_data
    
    def selction_Change(self,texte):
        self.texte = texte
        return self.texte
    
    def keepsheet(self,csvfol):
        self.csvfol = csvfol
        return self.csvfol
    
    def created(self,csvfol,texte):
        dt = data()
        headBackUp = dt.readdata(csvfol)
        headBackUp[texte] = {"Dimension":[],"Measurement":[]}
        self.dic_head_data = headBackUp
        self.wirtedata(csvfol) 
        print("------Created Key--------")
    
    def backupHeaderinJson(self,di,mea,csvfol,texte):
        dt = data()
        headBackUp = dt.readdata(csvfol)
        print("csvfol",csvfol)
        try:
            del headBackUp[texte]["Dimension"][:]
            del headBackUp[texte]["Measurement"][:]
        except:
            pass
        #dt.created(csvfol,texte)
        headBackUp = dt.readdata(csvfol)
        headBackUp[texte] = {"Dimension":[],"Measurement":[]}
        self.dic_head_data = headBackUp
        print(self.dic_head_data)
        for i in di:
            headBackUp[texte]["Dimension"].append(str(i))
        for m in mea:
            headBackUp[texte]["Measurement"].append(str(m))
        self.dic_head_data = headBackUp
        self.wirtedata(csvfol)   
    
    def isJson_dilist(self,csvfol,texte):
        di_list_json = []
        dt = data()
        headBackUp = dt.readdata(csvfol)
        for i in headBackUp[texte]["Dimension"]:
            di_list_json.append(i)
        return di_list_json
    
    def isJson_mealist(self,csvfol,texte):
        mea_list_json = []
        dt = data()
        headBackUp = dt.readdata(csvfol)
        for i in headBackUp[texte]["Measurement"]:
            mea_list_json.append(i)
        return mea_list_json

        