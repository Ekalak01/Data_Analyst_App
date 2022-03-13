import argparse
import colorsys
from genericpath import exists
from sqlite3 import Row
#from this import d
from tkinter import Y
from typing import Dict
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
import hashlib

class importclass :
    def __init__(self):
        ####
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
        #print("self.dirr_sheet",self.dirr_sheet)
        return self.dirr_sheet ## Appfolder\\Sheet/Sheet0'
    
    def keep_parent_dir(self,parent_dir,dirr_sheet):
        
        self.keep_dir = parent_dir+"/"+dirr_sheet
        #print(self.keep_dir)
        return self.keep_dir
        
    def save(self,dirr_sheet):
        """
            Save Sheetname .txt 
        """
        self.filename = "Sheetname"
        self.save_file = dirr_sheet+"/"+self.filename+'.txt'
        return self.save_file
    
    def Add_sheet(self):
        """
            Add_sheet And Created Folder Sheet 
        """
        Input = "Sheet"
        co=[]
        fname=[]
        op = importclass()
        sv = op.opensheet()
        nt = op.save(sv)
        with open(nt,'a',encoding='utf-8') as a:
            read = open(nt,'r',encoding='utf-8')   
            Lines = read.readlines()
            
            try:
                r=open(nt,'r',encoding='utf-8')   
                for j in r:
                    co.append(j.replace('\n',''))
                r.close()
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
            read.close()
        r = open(nt,'r',encoding='utf-8')          
        for i in r:
            i=i.replace('\n','')
        r.close()
        dr = op.opensheet()
        path = os.path.join(dr,fname[0])

        if not os.path.exists(path):
            os.mkdir(path)
            return False
        
        return True

    def openx(self):
        """
            Open FileName.txt 
            [Return PARTH File this Use save filename . txt]
        """
        
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
        #print ("Keep it Save_list_file",self.save_list_file )
        return self.save_list_file
    
    def dirr_save(self):
        """
            Return dirr_Import
        """
        return self.dirr_Import
          
    def Importfile_class (self,path):
        """
            Import Fuc Use Path file 
        """
        filename = []
        fname = QFileInfo(path).fileName()
        if fname not in filename:    
            filename.append(path)
            if fname[-4:] == '.csv':
                df = pd.read_csv(path,encoding='utf-8-sig')
            elif fname[-5:] == '.xlsx':
                df = pd.read_excel(path)
            
            if fname != "":
                self.save_filename(df,fname)
                return fname
            else:
                return False
       
    def save_filename(self,df,fname):
        """
            Save AND Create File if havent File In path 
        """   
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
        """
            Convert Csv to Save.csv File
        """
        return df.to_csv(path+'/save.csv',index=False)
           
    def savefile_excel(self,df:pd.DataFrame,path):
        """
            Convert Xlsx to Save.csv File
        """
        return df.to_csv(path+'/save.csv',index=False,encoding='windows-1252')
    
    def union_file(self,list_csv):
        """
            Union File usr list name File to Union 
        """
        xo = []
        for i in range(len(list_csv)):
            if len(list_csv) >= 2:
                Input = "Union"
                co=[]
                fname = []
                check =[]
                with open(self.save_list_file,'a',encoding='utf-8') as a:
                    read = open(self.save_list_file,'r',encoding='utf-8')   
                    Lines = read.readlines()
                    read.close()
                    for j in Lines:
                        check.append(j.replace('\n',''))
                    for x in range(len(list_csv)):
                        xo.append(self.gofile(list_csv[x]))
                    
                    if "Union0" in check: 
    
                        r=open(self.save_list_file,'r',encoding='utf-8')   
                        
                        for j in r:
                            co.append(j.replace('\n',''))
                        r.close()
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
                        a.write("\n"+Input+'0')
                        x = Input+'0'
                        fname.append(x)
                    frame = pd.concat(xo,axis=0,ignore_index=True)
                    frame.drop_duplicates(inplace=True)
                    #print("frame",frame)
                    #print("fname",fname)
                    return self.save_union(frame,fname) 
                    #return frame
                
            else:
                print("Error")
                pass
            
    def save_union(self,df,fname):
        """
            Save file name is Union
        """
        #print("save_union")
        r = open(self.save_list_file,'r',encoding='utf-8')          
                    
        for i in r:
            i=i.replace('\n','')
        
        r.close()
        
        path = os.path.join(self.dirr_Import,fname[0])
        #print(path,"path")
        
        if not os.path.exists(path):
            os.mkdir(path)
        self.savefile(df,path) 
    
    def gofile(self,sel_item):
        """
            Read Csv File And Return DataFrame --> df 
        """
        op = importclass()
        sv = op.dirr_save()
        self.csvfol= sv+'/'+sel_item+'/save.csv'
        #print("sel",sel_item)
        #print("Path in Import Folder",self.csvfol)
        try:
            df = pd.read_csv(self.csvfol,encoding='windows-1252')
        except:
            df = pd.read_csv(self.csvfol,encoding='utf-8-sig')
          
        return df
    
    def rm_sh(self,sel_item):
        """
            Remove SheetName in PATH File 
        """
    
        dr = self.opensheet()   
        x = dr+'/'+str(sel_item)
        for path in x :
            if os.path.exists(path) and os.path.isdir(path):
                shutil.rmtree(x)
                nt = self.save(dr)
                return nt
        
    def rm_file(self,sel_item):
        """
            Remove Folder FileName in PATH File 
        """
        dr = self.dirr_save()
        sv = self.openx()
        shutil.rmtree(dr+'/'+str(sel_item))### del folder
        return sv
    
    def clearall(self):
        """
            Remove AppFolder
        """
        parent_dir=QtCore.QDir.currentPath()
        directory= "Appfolder"
        path = os.path.join(parent_dir, directory)
        shutil.rmtree(path)
        return True


class data:
    def __init__(self):
        self.dic_head_data = {"Datalize":[]}
    
    def openjsoninsheet(self,directory):
        """
            Return dirr_sheet 
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
        self.dirr_sheet=path
        self.filename = "data"
        self.save_json_file = self.dirr_sheet+"/"+self.filename+'.json'
        self.wirtedata(self.dirr_sheet)
        return self.dirr_sheet

    def todatetime(self,df:pd.DataFrame):
        headers=[]
        datetime=[]
        for colname, coltype in df.dtypes.iteritems():
            headers.append(colname)
            if 'Date' in colname or 'date' in colname:
                df[colname]=pd.to_datetime(df[colname],dayfirst=True)
                dindex=headers.index(colname)
                dfy=df[colname].dt.year
                dfq=df[colname].dt.to_period('Q').dt.strftime('Q%q')
                dfm=df[colname].dt.month
                dfd=df[colname].dt.day
                df.insert(dindex,colname+'(Day)',dfd)
                df.insert(dindex,colname+'(Month)',dfm)
                df.insert(dindex,colname+'(Quarter)',dfq)
                df.insert(dindex,colname+'(Year)',dfy)
                

    def is_dimension(self,df:pd.DataFrame):
        dimension = []
        headers=[]
        for colname, coltype in df.dtypes.iteritems():
            headers.append(colname)
            if 'Date' in colname or 'date' in colname:
                dt=['(Year)','(Quarter)','(Month)','(Day)']
                for i in dt:
                    dimension.append(colname+i)
            if coltype == object and 'Date' not in colname and 'date' not in colname:
                dimension.append(colname) 
            elif 'Code' in colname or 'ID' in colname:
                dimension.append(colname)
                
        return dimension
    
    def check_dimension(self,txtdia,dimension):
        if txtdia in dimension:
            #print("Dimension True")
            return True
        else:
            #print("Dimension False")
            return False
        
    def check_measurement(self,txtdia,measurement):
        if txtdia in measurement:
            #print("Measurement True")
            return True
        else:
            #print("Measurement False")
            return False
    
    def is_measurement(self,df:pd.DataFrame):
        measurement = []
        for colname, coltype in df.dtypes.iteritems():
            if 'Code' in colname or 'ID' in colname :
                pass
            elif coltype != object and 'Date' not in colname:
                    measurement.append(colname)  
        return measurement
           
    def wirtedata (self,csvfol):
        data = csvfol+"/"+"data.json"
        with open (data,"w") as file:
            json.dump(self.dic_head_data,file,indent = 4)
    
    def readdata (self,csvfol):
        data = csvfol+"/"+"data.json"
        if os.path.exists(data) == False:
            self.wirtedata(csvfol)
        with open (data,"r") as file:
            self.dic_head_data = json.load(file)
        return self.dic_head_data
    
    def selction_Change(self,texte):
        self.texte = texte
        return self.texte
    
    def checkdrilldown(self,item:str):
        if '+' in item:
            j=item.split('+')
            item=j[0]
        return item

    def getgroupby(self,df:pd.DataFrame,lstgrp:list,agg:dict):
        if agg == {}:
            dfff=df.groupby(lstgrp).sum().reset_index()
        else:
            df=df.groupby(lstgrp).agg(agg)
            dfff=df.reset_index()
        return dfff

    def get_datarowcol(self,row:list,col:list):
        lst=[]
        for i in col:
            lst.append(i)
        for i in row:
            lst.append(i)
        return lst
 
    def MD5_main(self,dic):
        """
            Use md5 encode file dia & mea 
        """
    
        md5_hash = hashlib.md5()
        content = json.dumps(dic, sort_keys=False).encode()
        md5_hash.update(content)
        digest = md5_hash.hexdigest()
        return digest
    
    def MD5(self,dirr):
        """
            Use md5 encode file dia & mea 
        """
    
        md5_hash = hashlib.md5()
        a_file = open(dirr, "rb")
        content = a_file.read()
        md5_hash.update(content)
        digest = md5_hash.hexdigest()
        return digest
    
    def backupHeaderinJson(self,di,mea,csvfol,texte):
        dt = data()
        headBackUp = dt.readdata(csvfol)
        
        im = importclass()
        self.dirr_Import = im.dirr_save()
        self.dirr_sheet = self.dirr_Import+"/"+texte+"/save.csv"
        md5_hash = hashlib.md5()

        a_file = open(self.dirr_sheet, "rb")
        content = a_file.read()
        md5_hash.update(content)
        digest = md5_hash.hexdigest()
        
        for i in headBackUp['Datalize']:
            if i["Path"] == texte and i["md5"] == digest:
                i["Dimension"] = di
                i["Measurement"] = mea
                #print(headBackUp)
                self.dic_head_data = headBackUp
                self.wirtedata(csvfol)
                return True
        headBackUp['Datalize'].append(
            {
                "Path": texte,
                "md5": digest,
                "Dimension": di,
                "Measurement": mea
            }
            )
        self.dic_head_data = headBackUp
        #print(headBackUp)
        self.wirtedata(csvfol)
        a_file.close()
    
    def backupHeaderinJson2(self,di,mea,csvfol,texte):
        """
            Back Up Json File In Data Base 
                filename :  
                Satus : 
                Dimension : 
                Measurement : 
                MD5 : 
        """
        dt = data()
        headBackUp = dt.readdata(csvfol)
    
        if  headBackUp == {}:
            headBackUp[texte]= {"Status ":["Not Change"],"Dimension":[],"Measurement":[],"MD5":[]}
            self.dic_head_data = headBackUp
            self.wirtedata(csvfol)
        try:
            if  headBackUp[texte] == {}:
                headBackUp[texte]= {"Status ":["Not Change"],"Dimension":[],"Measurement":[],"MD5":[]}
                self.dic_head_data = headBackUp
                self.wirtedata(csvfol) 
        except:
            headBackUp[texte]= {"Status ":["Not Change"],"Dimension":[],"Measurement":[],"MD5":[]}
            self.dic_head_data = headBackUp
            self.wirtedata(csvfol)

        headBackUp2 = {}
        headBackUp2[texte] = {"Dimension":[],"Measurement":[]}
        for i in headBackUp[texte]["Dimension"]:
            headBackUp2[texte]["Dimension"].append(str(i))
        for m in headBackUp[texte]["Measurement"]:
            headBackUp2[texte]["Measurement"].append(str(m))
        print("headBackUp2_2",headBackUp2)    
            
        dic = headBackUp2[texte] 
        md = dt.MD5_main(dic)
        self.digest2 = md
        #print("digest2",self.digest2)
        
        headBackUp[texte] = {"Status":["Not Change"],"Dimension":[],"Measurement":[],"MD5":[]}
        for i in di:
            headBackUp[texte]["Dimension"].append(str(i))
        for m in mea:
            headBackUp[texte]["Measurement"].append(str(m))
        headBackUp[texte]["MD5"].append(str(self.digest2))
        self.dic_head_data = headBackUp
        self.wirtedata(csvfol)
        
        headBackUp3 = {}
        headBackUp3[texte] = {"Dimension":[],"Measurement":[]}
        for i in headBackUp[texte]["Dimension"]:
            headBackUp3[texte]["Dimension"].append(str(i))
        for m in headBackUp[texte]["Measurement"]:
            headBackUp3[texte]["Measurement"].append(str(m))
        #print("headBackUp3",headBackUp3) 
        
        dic2 = headBackUp3[texte] 
        md2 = dt.MD5_main(dic2)
        self.digest3 = md2
        headBackUp = dt.readdata(csvfol)
        #print("digest3",self.digest3)
        
        if self.digest3 == self.digest2:
            return True
        else:
            print("Mai JER Last ")
            headBackUp[texte]= {"Status":["Change"],"Dimension":[],"Measurement":[],"MD5":[]}
            for i in di:
                headBackUp[texte]["Dimension"].append(str(i))
            for m in mea:
                headBackUp[texte]["Measurement"].append(str(m))
            headBackUp[texte]["MD5"].append(str(self.digest3))
            self.dic_head_data = headBackUp
            self.wirtedata(csvfol)
        #print(headBackUp)   
    
    def isJson_dilist(self,csvfol,texte):
        di_list_json = []
        dt = data()
        headBackUp = dt.readdata(csvfol)
    
        for i in range(len(headBackUp['Datalize'])):
            if headBackUp['Datalize'][i]["Path"] == texte :
                #print(headBackUp['Datalize'][i]["Path"])
                di_list_json = headBackUp['Datalize'][i]["Dimension"]
                #print("di_list_json",di_list_json)
                return di_list_json
    
    def isJson_mealist(self,csvfol,texte):
        mea_list_json = []
        dt = data()
        headBackUp = dt.readdata(csvfol)
        for i in range(len(headBackUp['Datalize'])):
            if headBackUp['Datalize'][i]["Path"] == texte :
                #print(headBackUp['Datalize'][i]["Path"])
                mea_list_json = headBackUp['Datalize'][i]["Measurement"]
                #print("mea_list_json",mea_list_json)
                return mea_list_json

class filter:
    def filter_data(self,df:pd.DataFrame,item:str,checkitem:dict):
        """ Filter data fuction for filter dimension"""
        try:
            df_data_list=checkitem[item]
            df=df[df[item].isin(df_data_list)]
            return df
        except:
            pass
    def filterrange(self,df:pd.DataFrame,item:str,checkitem:dict):
        """ Filter range fuction for filter measurement"""
        try:
            min=float(checkitem[item][0])
            max=float(checkitem[item][1])
            df=df.loc[(df[item] >= min) & (df[item] <= max)] 
            return df
        except:
            pass
    
class graphmanage:
    def barplot1(self,df,row,col):
        alt.data_transformers.disable_max_rows()     
        nchart=[]
        if len(col) >=2:
            
            ch=alt.Chart(df).mark_bar().encode(
            x=col[1]+':Q',
            y=row[0]+':N',
            tooltip=[str(col[0]),col[1],row[0]]
            ).facet(column=alt.Column(str(col[0]))
                
            ).resolve_scale(x='independent',y = 'independent').interactive()
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

    def barplot2(self,df,row,col):
        alt.data_transformers.disable_max_rows()     
        nchart=[]
        if len(row) >=2:
            for i in range(len(row)):
                ch=alt.Chart(df).mark_bar().encode(
                x=col[0]+':N',
                y=row[1]+':Q',
                tooltip=[str(col[0]),row[0],row[1]]
                ).facet(row=alt.Row(str(row[0]))
                    
                ).resolve_scale(x='independent',y = 'independent').interactive()
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
    
    def lineplot(self,df,dcol,row,col):
        mesure=[]
        alt.data_transformers.disable_max_rows()
        if dcol == True:
            for i in row:
                mesure.append(i)
            if len(col) ==2:
                strm='//'.join(str(i) for i in mesure)
                line=alt.Chart(df).transform_fold(
                        mesure
                    ).mark_line(point=True).encode(
                        x=col[1]+':N',
                        y=alt.Y('value:Q',title=strm),
                        column=col[0]+':N',
                        color=alt.Color('key:N',legend=alt.Legend(title='Line Color')),
                        tooltip=[col[0],col[1],'value:N']
                            ).properties(
                                width=500,
                                height=350)
            else:
                strm='//'.join(str(i) for i in mesure)
                line=alt.Chart(df).transform_fold(
                        mesure
                    ).mark_line(point=True).encode(
                        x=col[0]+':N',
                        y=alt.Y('value:Q',title=strm),
                        color=alt.Color('key:N',legend=alt.Legend(title='Line Color')),
                        tooltip=[col[0],'value:Q']
                            ).properties(
                                width=500,
                                height=350)
        else:
            for i in col:
                mesure.append(i)
            if len(row)==2:
                strm='//'.join(str(i) for i in mesure)
                line=alt.Chart(df).transform_fold(
                    mesure
                ).mark_line(point=True).encode(
                    y=row[1]+':N',
                    x=alt.X('value:Q',title=strm),
                    row=row[0]+':N',
                    color=alt.Color('key:N',legend=alt.Legend(title='Line Color')),
                    tooltip=[row[0],'value:Q',row[0]]
                        ).properties(
                            width=500,
                            height=350)
            else:    
                strm='//'.join(str(i) for i in mesure)
                line=alt.Chart(df).transform_fold(
                    mesure
                ).mark_line(point=True).encode(
                    y=row[0]+':N',
                    x=alt.X('value:Q',title=strm),
                    color=alt.Color('key:N',legend=alt.Legend(title='Line Color')),
                    tooltip=[row[0],'value:Q']
                        ).properties(
                            width=500,
                            height=350)
        charts=line
        return charts

    def pieplot(self,df,dcol,row,col):
        """ plot pie chart"""
        nchart=[]
        alt.data_transformers.disable_max_rows()
        if dcol == True:
            if len(col) >1:
                for i in range(len(row)):
                    pie=alt.Chart(df).mark_arc(stroke="#fff").encode(
                    theta=alt.Theta(row[i]+':Q')
                    ,color=alt.Color(col[1]+':N')
                    ,column=alt.Column(col[0])
                    ,tooltip=[str(col[0]),row[i],col[1]]
                    ).resolve_scale(theta="independent",color="independent")
                    nchart.append(pie)
                charts=alt.vconcat(*nchart)
            else:
                for i in range(len(row)):
                        pie=alt.Chart(df).mark_arc(stroke="#fff").encode(
                        theta=row[i]+':Q'
                        ,color=col[0]+':N'
                        ,tooltip=[str(col[0]),row[i]]
                        ).resolve_scale(theta="independent",color="independent")
                        nchart.append(pie)
                charts=alt.vconcat(*nchart).resolve_scale(theta="independent",color="independent")
        else:
            if len(row) >1:
                for i in range(len(col)):
                    pie=alt.Chart(df).mark_arc(stroke="#fff").encode(
                    theta=alt.Theta(col[i]+':Q')
                    ,color=alt.Color(row[1]+':N')
                    ,row=alt.Row(row[0])
                    ,tooltip=[str(row[0]),row[1],col[i]]
                    ).resolve_scale(theta="independent",color="independent")
                    nchart.append(pie)
                charts=alt.hconcat(*nchart)
            else:
                for i in range(len(col)):
                        pie=alt.Chart(df).mark_arc(stroke="#fff").encode(
                        theta=col[0]+':Q'
                        ,color=row[0]+':N'
                        ,tooltip=[str(row[0]),col[0]]
                        ).resolve_scale(theta="independent",color="independent")
                        nchart.append(pie)
                charts=alt.hconcat(*nchart).resolve_scale(theta="independent",color="independent")
        return charts
    
    def hbarplot(self,df,row,col):
        alt.data_transformers.disable_max_rows()     
        nchart=[]
        if len(row) ==3:
            for i in range(len(col)):
                ch=alt.Chart(df).mark_bar().encode(
                y=alt.Y(row[1],sort=alt.SortField(field=row[0],order ='ascending')),
                x=alt.X(col[i]),
                row=alt.Row(str(row[0])),
                color=alt.Color(row[2]),
                tooltip=[str(row[0]),str(row[1]),str(row[2]),col[i]]
                ).resolve_scale(y = 'independent').properties(title="bar chart").interactive()
                nchart.append(ch)
        elif len(row) ==2:
            for i in range(len(col)):
                ch=alt.Chart(df).mark_bar().encode(
                y=alt.Y(str(row[1])+':N',sort=alt.SortField(field=row[0],order ='ascending')),
                x=col[i]+':Q',
                tooltip=[str(row[0]),str(row[1]),col[i]]
                ).facet(
                    row=alt.Row(str(row[0]))
                ).resolve_scale(y = 'independent').properties(title="bar chart").interactive()
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
        return charts
          
    def vbarplot(self,df,row,col):
        alt.data_transformers.disable_max_rows()     
        nchart=[]
        if len(col) ==3:
            for i in range(len(row)):
                ch=alt.Chart(df).mark_bar().encode(
                x=alt.X(str(col[1])+':N',sort=alt.SortField(field=col[0],order ='ascending')),
                y=row[i]+':Q',
                color=str(col[2]),
                tooltip=[str(col[0]),str(col[1]),str(col[2]),row[i]]
                ).facet(column=alt.Column(str(col[0]))
                ).resolve_scale(x='independent').properties(title="bar chart")
                nchart.append(ch)
        elif len(col) ==2:
            for i in range(len(row)):
                ch=alt.Chart(df).mark_bar().encode(
                x=alt.X(str(col[1])+':N',sort=alt.SortField(field=col[0],order ='ascending')),
                y=row[i]+':Q',
                tooltip=[str(col[0]),str(col[1]),row[i]]
                ).facet(column=alt.Column(str(col[0]))
                ).resolve_scale(x='independent').properties(title="bar chart").interactive()
                nchart.append(ch)
        else:
            for i in range(len(row)):
                ch=alt.Chart(df).mark_bar().encode(
                x=col[0]+':N',
                y=row[i]+':Q',
                tooltip=[col[0],row[i]]
                ).interactive()
                nchart.append(ch)

             
        charts=alt.vconcat(*nchart).resolve_scale(x='shared')
        return charts