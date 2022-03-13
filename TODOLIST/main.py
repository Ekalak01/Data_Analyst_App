from asyncio import all_tasks
from binascii import Incomplete
from re import S
import sys
from tkinter import Widget
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
import os
from PyQt5 import QtCore,QtWidgets,QtGui
import json
from PyQt5.QtWidgets import QDialog, QApplication,QVBoxLayout
from PyQt5.uic import loadUi
import shutil

from PyQt5.QtChart import QValueAxis,QChart, QChartView,QPieSeries,QBarSet, QPercentBarSeries, QBarCategoryAxis,QHorizontalStackedBarSeries
from PyQt5.QtCore import QPoint , pyqtSignal
from PyQt5.QtGui import QColor, QBrush, QLinearGradient, QGradient, QPainter 

################
import time
import datetime
from dateutil.parser import parse

###############

class colck:
    
    def __init__(self,time_val):
        self.time_val = time_val
        #print("x",self.time_val)
        
def singleton(cls):
    """ decorator function to implement singleton design pattern. See PEP318."""
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class MySignal(QObject):
    
    #Signal Class which includes a signal as class attribute.
    
    object_signal = pyqtSignal(colck)
    

class MyThread(QThread):
    
    """
    This class contains a signal and run method.
    An object of the signal is activated by .start() method
    and sends the results using MySignal Class instance.
    """
    def __init__(self, val):
        super().__init__()
        
        self.object_signal = MySignal().object_signal
        #print(type( self.object_signal))
        self.val = val
        
        #self.run()
        
    def run(self):
        
        """
        Function is called when Thread is .strat().
        """
        while(1):
            
            #my_id = MyObject().send_id()
            time_val = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            #print(time_val)
            self.object_signal.emit(colck(time_val))
            # Defining a ranodm sleep time (0-10) seconds.
            sleep_time = 1
            time.sleep(sleep_time)
        
###############

class Mainwindow(QDialog):
    def __init__(self):
        
        super(Mainwindow,self).__init__()
        loadUi("ui2/login.ui",self)
        self.Pass_ed.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_bt.clicked.connect(self.login)
        self.Ex_bt.clicked.connect(self.close_x)
        self.register_bt.clicked.connect(self.reg)
        
        self.my_signal = MySignal()
        self.object_signal = self.my_signal.object_signal
        self.object_signal.connect(self.show_it)


    def show_it(self, nval=None):
        
        my_text = f"{nval.time_val}"
        self.time.setText(my_text)
        
    def error(self,texte):
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        #msg.setText("Error")
        msg.setText(str(texte))
        msg.setWindowTitle("Error")
        msg.exec_()
        
    def login(self):
        data=json.load(open('login.json','r'))
        user=self.User_ed.text()
        pw=self.Pass_ed.text()
        
        try:
            us=False
            
            if user == "" and pw == "" :
                error1 = "Please Enter User and Password"
                self.error(error1)
                return  
            
            for i in range(len(data)):      
                if user == data[i]["user"] and pw == data[i]["password"]: 
                    us=True
                    userid.append(user)
                    break
            
            if us == False:
                error2 = "User or PassWord Incorrect"
                self.error(error2)
            
            if us == True:
                print("login success")
                try:
                    r=open(str(userid[0])+'/'+'Titlename.txt','r',encoding='utf-8')
                    for i in r:
                        if '/' not in i:
                            y.append(i)
                        else:
                            pass
                    r.close()
                    
                except:
                    pass
                
                maintitle_pg = maintitle()
                widget.addWidget(maintitle_pg)
                widget.setCurrentIndex(widget.currentIndex()+1)
                

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
        
    def reg(self):
        creat = creatac()
        widget.addWidget(creat)
        widget.setCurrentIndex(widget.currentIndex()+1)

class creatac(QDialog):
    def __init__(self):
        super(creatac,self).__init__()
        loadUi("ui2/register.ui",self)
        self.Confirm_bt.clicked.connect(self.add)
        self.Cancel_bt.clicked.connect(self.cancel)

    def add(self):
        user=self.User_ed.text()
        Passw=self.Pass_ed.text()
        Repass=self.Repass_ed.text()

        listObj = []
        filename = 'login.json'
        with open(filename) as fp:
            listObj = json.load(fp)
        
        if Passw == Repass and user != "" and Passw != "" and Repass != "":
            listObj.append({
            "user": str(user),
            "password":str(Passw),})
            with open(filename, 'w') as json_file:
                json.dump(listObj, json_file, 
                                    indent=4,  
                                    separators=(',',': '))
            self.cancel()
            
        elif Passw != Repass:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            #msg.setText("Error")
            msg.setText("Password doesn't match")
            msg.setWindowTitle("Error")
            msg.exec_()
        
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            #msg.setText("Error")
            msg.setText('Please Enter Information Before Confirm')
            msg.setWindowTitle("Error")
            msg.exec_()
        

    def close_x(self):
        should_save = QMessageBox.question(self, "Exit", 
                                                     "Do you want to Exit ?",
                                                     defaultButton = QMessageBox.Yes)
        if should_save == QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            pass
    
    def cancel(self):
        login_pg = Mainwindow()
        widget.addWidget(login_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
class maintitle(QDialog):
    def __init__(self):
        super(maintitle,self).__init__()
        loadUi("ui2/maintitleui2.ui",self)
        
        ###created folder by user 
        parent_dir=QtCore.QDir.currentPath()
        directory= userid[0]
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        self.dirr=path
        self.filename = "Titlename"
        self.save_file = self.dirr+"/"+self.filename+'.txt'
        self.read_from_file(self.save_file)
        ####
        
        self.listWidget.itemDoubleClicked.connect(self.gototask)
        self.back_bt.clicked.connect(self.backtologin)
        self.exit_bt.clicked.connect(self.close_x)
        self.new_bt.clicked.connect(self.addtitle)
        self.remove_bt.clicked.connect(self.remove)
        self.export_bt.clicked.connect(self.export_)
        self.import_bt.clicked.connect(self.import_)
        self.titlechart.clicked.connect(self.titlechart_show)
        self.barchart_c.clicked.connect(self.barchart)
        
        
        try:
            rep=[]
            for i in y:
                rep.append(i.replace("\n",""))
            y.clear()
            for i in rep:
                y.append(i)
        except:
            pass
        
        
    def export_(self):
        
        shutil.make_archive('syncfolder'+'/'+userid[0], 'zip', userid[0]) 
        z = "Export your user Complete" 
        self.noti(z)
        
    def import_(self):
        try:
            path,_= QFileDialog.getOpenFileName(self,"Import file",'syncfolder',"Zip files (*.zip)","Zip (*.zip)")
            filename = QFileInfo(path).fileName()
            filename=filename[:-4]
            
            if filename == userid[0]:
                shutil.rmtree(self.dirr)
                shutil.unpack_archive(path,filename, 'zip')
                f=open(filename+'/'+'Titlename.txt')
                titlechart.clear()
                title_x.clear()
                titlelist.clear()
                barchar.clear()
                y.clear()
                for i in f:
                    y.append(i)
                z = "Import Complete" 
                self.noti(z)
            elif filename =='':
                return
            
            elif filename != userid[0]:
                self.dialogerror("Cannot sync another user!")
                pass    
            elif filename in s:
                self.dialogerror("Title already exist")
                pass
            else:
                pass
                
        except:
            pass 
        
        
        maintitle_pg = maintitle()
        widget.addWidget(maintitle_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def noti (self,z):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        #msg.setText("Error")
        msg.setText(str(z))
        msg.setWindowTitle("Noti")
        msg.exec_()
        
    def dialogerror(self,x):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        #msg.setText("Error")
        msg.setText(str(x))
        msg.setWindowTitle("Error")
        msg.exec_()
        
    def addtitle(self):
        

        Input = self.textEdit.text()
        r=open(self.save_file,'r',encoding='utf-8')
        
        if Input == "":
            x = "More information"
            self.dialogerror(x)
            return
        
        if Input in y:
            x = "Title already exist \n please Enter new title "
            self.dialogerror(x)     
            return
        else:
            r= open(self.save_file,'r',encoding='utf-8')
            with open(self.save_file,'a',encoding='utf-8') as a:
              
                Lines=r.readlines()
                
                if Lines == []:
                    a.write(Input)
                    y.append(Input)  
                else:
                    a.write("\n"+Input)
                    y.append(Input)
               
            path = os.path.join(self.dirr,Input)
                
            if not os.path.exists(path):
                os.mkdir(path)
                #titlelist.append(Input) 
            f=open(self.dirr+'/'+Input+'/taskname.txt','w',encoding='utf-8')
            f.close        
            ###
            maintitle_pg = maintitle()
            widget.addWidget(maintitle_pg)
            widget.setCurrentIndex(widget.currentIndex()+1)
            ###
    
    def remove(self):
        row = self.listWidget.currentRow()
    
        item = self.listWidget.item(row)
        
        try:
            sel_item = self.listWidget.currentItem().text()
        except:
            pass
        
        if item is None:
            return
        else:
            item = self.listWidget.takeItem(row)
            del item
            y.remove(sel_item)
            
        shutil.rmtree(self.dirr+'/'+str(sel_item))### del folder
        self.write_to_file(self.save_file)
            
        try:
            del titlechart[sel_item]
            y.remove(sel_item)
        except:
            pass
        
    def titlechart_show(self):
        title_x.clear()
        r=open(self.save_file,'r',encoding='utf-8')
        #title_x=[]
        for i in r:
            title_x.append(i.replace('\n',''))
        r.close()
        for k in title_x:
            f=open(self.dirr+'/'+k+'/taskname.txt','r',encoding='utf-8')
            n=0
            for j in f:
                if '/' not in j:
                    n+=1
                else:
                    pass
        
            titlechart[str(k)]=n
        title_x.clear()
        self.chart = TitleChart()
        self.chart.show()
        r.close()
                
    def barchart(self):
        title_x.clear()
        barchar.clear()
        r=open(self.save_file,'r',encoding='utf-8')
        #title=[]
        for i in r:
            title_x.append(i.replace('\n',''))
        r.close()
        for k in title_x:
            f=open(self.dirr+'/'+k+'/taskname.txt','r',encoding='utf-8')
            complete=0
            incomplete=0
            for j in f:
                if '/' in j:
                    pass
                if '✓' in j:
                    complete+=1     
                if '✓' not in j and '/' not in j:
                    incomplete+=1
            barchar[str(k)]=[complete]
            barchar[str(k)]+=[incomplete]
            
        title_x.clear()   
        self.chart = BarChart()
        self.chart.show()
        r.close()
    
    def gototask(self):
        sel_item = self.listWidget.currentItem().text()
        try:    
            with open(str(userid[0])+'/'+sel_item+'/'+'bactask.json','r+') as fp:
                dic=json.load(fp)
            dt.update(dic)
        except:
            with open(str(userid[0])+'/'+sel_item+'/'+'bactask.json','w') as fp:
                pass
        try:
            r=open(str(userid[0])+'/'+sel_item+'/'+'taskname.txt','r',encoding='utf-8')
            for i in r:
                if '/' not in i:
                    s.append(i)
                else:

                    pass
            r.close()
                    
        except:
            pass
                
        titlelist.append(sel_item)
        print("titlelist",titlelist)
        task_pg=task()
        widget.addWidget(task_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
              
    def backtologin(self):
        self.write_to_file(self.save_file)
        userid.remove(userid[0])
        titlechart.clear()
        barchar.clear()
        y.clear()
        login_pg = Mainwindow()
        widget.addWidget(login_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
            
    def write_to_file(self, file):
        try:
            list_widget = self.listWidget
            entries = '\n'.join(list_widget.item(ii).text() for ii in range(list_widget.count()))
            with open(file, 'w',encoding='utf-8') as fout:
                fout.write(entries)
        except OSError as err:
            print(f"file {file} could not be written")

    def read_from_file(self, file):
        try:
            list_widget = self.listWidget
            with open(file, 'r',encoding='utf-8') as fin:
                    entries = [e.strip() for e in fin.readlines()]
            list_widget.insertItems(0, entries)
        except OSError as err:
            with open(file, 'w',encoding='utf-8'):
                print("pass")
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


class task(QDialog):
    def __init__(self):
        super(task,self).__init__()
        loadUi("ui2/taskui.ui",self)
        ###created folder by user 
        parent_dir=QtCore.QDir.currentPath()
        directory= str(userid[0])
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        self.dirr=path+'/'+titlelist[0]
        self.filename = "taskname"
        self.save_file = self.dirr+"/"+self.filename+'.txt'
        self.read_from_file(self.save_file)
        ####
        
        self.new_bt.clicked.connect(self.nextpgadd)
        self.remove_bt.clicked.connect(self.remove)
        self.exit_bt.clicked.connect(self.close_x)
        self.back.clicked.connect(self.backtotitle)
        self.listWidget.itemDoubleClicked.connect(self.detail)
        self.done_bt.clicked.connect(self.done)
        self.report_bt.clicked.connect(self.report)
        
        
        ######
        self.countday()
        self.updatejson()
        
        try:
            rep=[]
            for i in s:
                rep.append(i.replace("✓","").replace("\n",""))
            s.clear()
            for i in rep:
                s.append(i)
        except:
            pass
        
    def report(self):
        
        report_pg=report()
        widget.addWidget(report_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
       
    def countday(self):
        try:
            current_time = datetime.datetime.now()
            date = current_time.strftime("%Y/%#m/%#d") 
            count_today=0  
            count_athday=0
            for i in dt.keys():
                if i == date:
                    count_today=len(dt[date])
                    for i in dt[date]:
                        if '✓' in i:
                            count_today-=1      
                else:
                    for j in dt[i]:
                        count_athday+=1
                        if '✓' in j:
                            count_athday-=1
                            
                
            self.Today.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">"+str(count_today)+"</span></p></body></html>") 
            self.Ath_today.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">"+str(count_athday)+"</span></p></body></html>")
        except:
            pass
 
    def updatejson(self):
        try:
            with open(self.dirr+'/'+'bactask.json', 'w') as json_file:
                json.dump(dt,json_file)
        except:
            pass
        
    def error(self,text):
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        #msg.setText("Error")
        msg.setText(str(text))
        msg.setWindowTitle("Error")
        msg.exec_()
        
    def detail(self):
        item = self.listWidget.currentItem().text()
        if '/' in item:
            return
        if '✓' in item:
            item=item[1:]
        taskname.insert(0,item)
        self.write_to_file(self.save_file)
        
        detail_pg=detail()
        widget.addWidget(detail_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    
    def backtotitle(self):
        self.write_to_file(self.save_file)
        s.clear()
        static_task.clear()
        dt.clear()
        titlelist.clear()
        login_pg = maintitle()
        widget.addWidget(login_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def checkdatetitle(self):
        try:
            for i in list(dt):
                if len(dt[i])==0:
                    del dt[i]
                    self.countday()
            new_d = (sorted(dt.items(), key=lambda x: parse(x[0])))
            t2=[]
            for i in range(len(new_d)):
                dstr='\n'.join(str(e)for e in new_d[i])     
                t2.append(dstr.replace("[","").replace("]","").replace("'","").replace(",","\n").replace("",""))
            
            with open(self.save_file,'w',encoding='utf-8') as f:
                for i in t2:
                    f.write(i+'\n')
        except:
            pass
        
    def remove(self):
        row = self.listWidget.currentRow()
    
        item = self.listWidget.item(row)
        try:
            sel_item = self.listWidget.currentItem().text()
        except:
            pass
        
        if '/' in sel_item:
            return
        
        if item is None:
            return
        else:
            item = self.listWidget.takeItem(row)
            del item
            
            d2 = {k:[i for i in v if i not in sel_item] for k, v in dt.items()}
            dt.update(d2)
            
            if '✓' in sel_item:
                sel_item=sel_item[1:]
                
            shutil.rmtree(self.dirr+'/'+str(sel_item))### del folder
            self.write_to_file(self.save_file)
            
            try:
                s.remove(sel_item)

            except:
                pass
            
            self.checkdatetitle()
            task_ob = task()
            widget.addWidget(task_ob)
            widget.setCurrentIndex(widget.currentIndex()+1)  
    
    def done(self):
        try:
            item = self.listWidget.currentItem().text()
            sel_items =self.listWidget.selectedItems()
            row = self.listWidget.currentRow()
            
            if '/' in item:
                return
            if item is None:
                return
            elif '✓' in item:
                for i in sel_items:
                    i.setText(str(item).replace('✓',''))
                    for i in dt.values():
                        if item in i:
                            index = i.index(item)
                            i.remove(item)
                            i.insert(index,str(item).replace('✓',''))
                            
            else:
                for i in sel_items:
                    i.setText('✓'+str(item))
                    for i in dt.values():
                        if item in i:
                            index = i.index(item)
                            i.remove(item)
                            i.insert(index,'✓'+item)
                        
                            
                        
            self.countday()
            self.updatejson()
            self.write_to_file(self.save_file)
        except:
            pass
    
    def nextpgadd(self):
        add_pg = addto()
        widget.addWidget(add_pg)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def close_x(self):
        should_save = QMessageBox.question(self, "Save data", 
                                                     "Should the data be saved?",
                                                     defaultButton = QMessageBox.Yes)
        if should_save == QMessageBox.Yes:
            self.write_to_file(self.save_file)
            sys.exit(app.exec_())
        else:
            pass
    
    def write_to_file(self, file):
        try:
            list_widget = self.listWidget
            entries = '\n'.join(list_widget.item(ii).text() for ii in range(list_widget.count()))
            with open(file, 'w',encoding='utf-8') as fout:
                fout.write(entries)
        except OSError as err:
            print(f"file {file} could not be written")

    def read_from_file(self, file):
        try:
            list_widget = self.listWidget
            with open(file, 'r',encoding='utf-8') as fin:
                entries = [e.strip() for e in fin.readlines()]
            list_widget.insertItems(0, entries)
        except OSError as err:
            with open(file, 'w',encoding='utf-8'):
                pass
    
    def refreshpage(self):
        task_ob = task()
        widget.addWidget(task_ob)
        widget.setCurrentIndex(widget.currentIndex()+1) 
                
class addto(QDialog):   
    
    def __init__(self):
        super(addto,self).__init__()
        loadUi("ui2/addtaskui.ui",self)
        ########
        parent_dir=QtCore.QDir.currentPath()
        directory= str(userid[0])
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        self.dirr=path+'/'+titlelist[0]
        self.filename = "taskname"
        self.save_file = self.dirr+"/"+self.filename+'.txt'
        
        #########
        
        self.add_bt.clicked.connect(self.newtask)
        self.cancel.clicked.connect(self.backpg)
        self.dateEdit.setDate(QDate.currentDate())
        
        ####
        self.my_signal = MySignal()
        self.object_signal = self.my_signal.object_signal
        self.object_signal.connect(self.show_it)
        
    def show_it(self, nval=None):
        
        my_text = f"{nval.time_val}"
        self.time.setText(my_text)
        
    def write_to_file(self, file):
        try:
            text=self.detail_text.toPlainText()
            with open(self.dirr+'/'+file+'.txt', 'w',encoding='utf-8') as fout:
                fout.write(text)
        except OSError as err:
            print(f"file {file} could not be written")
            
    def backpg(self): 
          
        task_ob = task()
        widget.addWidget(task_ob)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        
        
    def newtask(self):
        setdate=self.dateEdit.date().getDate()
        setdate=list(setdate)
        setdatestr='/'.join(str(e)for e in setdate)
        """settime=self.timeEdit.time().toString()
        settime=settime[:-3]"""
        Input = self.textEdit.text()
        
        
        if Input == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!!!!!!")
            msg.setInformativeText('More information')
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        
        if Input in s:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error!!!!!!")
            msg.setInformativeText("Title already exist \n please Enter new title ")
            msg.setWindowTitle("Error")
            msg.exec_()  
            return  
        else:
            try:
                path = os.path.join(self.dirr,Input)
                if not os.path.exists(path):
                    os.mkdir(path)
                taskname.append(Input)
                s.append(str(Input))
                if setdatestr not in dt:
                    dt[setdatestr]=[Input]
                else:
                    dt[setdatestr]+=[Input]
                    

                new_d = (sorted(dt.items(), key=lambda x: parse(x[0])))
                t2=[]
                for i in range(len(new_d)):
                    dstr='\n'.join(str(e)for e in new_d[i])
                        
                    t2.append(dstr.replace("[","").replace("]","").replace("'","").replace(",","\n"))
                
                with open(self.save_file,'w',encoding='utf-8') as f:
                    for i in t2:
                        f.write(i+'\n')
                
                        
                with open(self.dirr+'/'+'bactask.json', 'w') as json_file:
                    json.dump(dt,json_file)   
                self.write_to_file(Input+'/'+'savefile')
            except:
                pass
    
        task_ob = task()
        widget.addWidget(task_ob)
        widget.setCurrentIndex(widget.currentIndex()+1) 
          
class detail(QDialog):
    def __init__(self):
        super(detail,self).__init__()
        loadUi("ui2/detailui.ui",self)
        self.back.clicked.connect(self.backbt)
        parent_dir=QtCore.QDir.currentPath()+'/'+str(userid[0])
        directory= str(titlelist[0])
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        self.dirr=path+'/'+taskname[0]
        self.filename = "savefile"
        self.save_file = self.dirr+"/"+self.filename+'.txt'
        self.read_from_file(self.save_file)
        
    def backbt(self):
        self.write_to_file(self.save_file)
        task_ob = task()
        taskname.clear()
        widget.addWidget(task_ob)
        widget.setCurrentIndex(widget.currentIndex()+1) 
    
    def write_to_file(self, file):
        try:
            text=self.textEdit_todo.toPlainText()
            with open(file, 'w',encoding='utf-8') as fout:
                fout.write(text)
        except OSError as err:
            print(f"file {file} could not be written")
    
    def read_from_file(self, file):
        try:
            
            with open(file, 'r',encoding='utf-8') as fin:
                entries = [e.strip() for e in fin.readlines()]
                entriesstr=''.join(str(e)for e in entries)
            self.textEdit_todo.setPlainText(entriesstr)
        except OSError as err:
            with open(file, 'w'):
                pass
                       
class report(QDialog):
    def __init__(self):
        super(report,self).__init__()
        loadUi("ui2/reportui.ui",self)
        self.back.clicked.connect(self.backbt)
        self.exit_bt.clicked.connect(self.close_x)
        parent_dir=QtCore.QDir.currentPath()+'/'+str(userid[0])
        directory= str(titlelist[0])
        path = os.path.join(parent_dir, directory)
        self.dirr=path
        self.static()
        self.Daychart()
        self.chart_bt.clicked.connect(self.piechart)
        self.daychart_bt.clicked.connect(self.bardaychart)

        
    def backbt(self):
        task_ob = task()
        daychart.clear()
        static_task.clear()
        widget.addWidget(task_ob)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def close_x(self):
        should_save = QMessageBox.question(self, "Exit", 
                                                     "Do you want to Exit ?",
                                                     defaultButton = QMessageBox.Yes)
        if should_save == QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            pass
        
    def Daychart(self):
        for i in dt.keys():
            complete=0
            incomplete=0
            for j in dt[i]:
                if '✓' in j:
                    complete+=1
                if '✓' not in j:
                    incomplete+=1
                daychart[i]=[complete]
                daychart[i]+=[incomplete]
        k=[]
        l=[]
        day_chart = (sorted(daychart.items(), key=lambda x: parse(x[0])))
        for i in day_chart:
            for j in i:
                if '/' in j:
                    k.append(j)
                else:
                    l.append(j)
        daychart.clear()
        for i in range(len(k)):
            daychart[k[i]]=l[i]
    
                
    def static(self):
        complete=0
        incomplete=0
        f=open(self.dirr+'/'+'taskname.txt','r',encoding='utf-8')
        for i in f:
            if '/' in i:
                pass
            
            if '✓' in i:
                complete+=1
                
            if '✓' not in i and '/' not in i:
                incomplete+=1
        alltask=complete+incomplete        
        static_task['complete'] = complete
        static_task['incomplete'] = incomplete
        static_task['All task'] = alltask
        self.c_c.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">"+str(complete)+"</span></p></body></html>") 
        self.c_inc.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">"+str(incomplete)+"</span></p></body></html>")
        self.c_all.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">"+str(alltask)+"</span></p></body></html>")
        
        
    def piechart(self):
        self.chartDemo = Chart()
        self.chartDemo.show()
        
    def bardaychart(self):
        self.chartDemo = DayChart()
        self.chartDemo.show()

class Chart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chart Formatting Demo')
        self.resize(600, 400)

        self.initChart()

        self.setCentralWidget(self.chartview)
        
        
    def initChart(self):

        series = QPieSeries()
        series.setHoleSize(0.40)

        complete_task=static_task['complete']
        incomplete_task=static_task['incomplete']

        self.complete = series.append("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Complete task "+str(complete_task)+"</span></p></body></html>", complete_task)
        self.complete.setExploded(False)
        self.complete.setLabelVisible(True)
        self.complete.setBrush(QtGui.QColor("#58ff8f"))
        
        self.incomplete=series.append("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Incomplete task "+str(incomplete_task)+"</span></p></body></html>", incomplete_task)
        self.incomplete.setExploded(False)
        self.incomplete.setLabelVisible(True)
        self.incomplete.setBrush(QtGui.QColor("#ff5861"))

        


        self.chart = QChart()
        self.chart.addSeries(series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Task Chart")

        self.chartview = QChartView(self.chart)
        
class BarChart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chart Formatting Demo')
        self.resize(600, 400)

        self.BarChart()

        
    def BarChart(self):
        set0 = QBarSet("complete")
        set1 = QBarSet("incomplete")
        
        cate=[]
        comp=[]
        incomp=[]
        for categories,(compe,incompe) in barchar.items():
            cate.append(categories)
            comp.append(compe)
            incomp.append(incompe)
            
        set0.append(comp)
        set1.append(incomp)
        set0.setBrush(QtGui.QColor("#48c872"))
        set1.setBrush(QtGui.QColor("#d7484f"))
        
        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.setLabelsVisible(True)

 
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Percent Example")
        chart.setAnimationOptions(QChart.SeriesAnimations)
 
        axis = QBarCategoryAxis()
        axis.append(cate)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        
        axis_y=QValueAxis()
        axis_y.setTitleText('Percentage (%)')
        chart.setAxisY(axis_y, series)
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
 
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
 
        self.setCentralWidget(chartView)
        
class DayChart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chart Formatting Demo')
        self.resize(600, 400)

        self.BarChart()

        
    def BarChart(self):
        set0 = QBarSet("complete")
        set1 = QBarSet("incomplete")
        
        cate=[]
        comp=[]
        incomp=[]
        for categories,(compe,incompe) in daychart.items():
            cate.append(categories)
            comp.append(compe)
            incomp.append(incompe)
            
        set0.append(comp)
        set1.append(incomp)
        set0.setBrush(QtGui.QColor("#48c872"))
        set1.setBrush(QtGui.QColor("#d7484f"))
        
        series = QHorizontalStackedBarSeries()
        series.append(set0)
        series.append(set1)
        series.setLabelsVisible(True)
 
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("DayTaskChart")
        chart.setAnimationOptions(QChart.SeriesAnimations)
 
        axis = QBarCategoryAxis()
        axis.append(cate)
        chart.createDefaultAxes()
        axis.setTitleText('Day')
        chart.setAxisY(axis, series)

        axis_x=QValueAxis()
        axis_x.setTitleText('Task')
        chart.setAxisX(axis_x, series)
        
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
 
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
 
        self.setCentralWidget(chartView)
         
         
        
class TitleChart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chart Formatting Demo')
        self.resize(600, 400)

        self.initChart()

        self.setCentralWidget(self.chartview)
        
        
    def initChart(self):

        series = QPieSeries()
        series.setHoleSize(0.40)

        for name,value in titlechart.items():
            self._slice = series.append("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">"+name+" : "+' '+str(value)+"</span></p></body></html>", value)
            self._slice.setExploded(False)
            self._slice.setLabelVisible(True)
        
        self.chart = QChart()
        self.chart.addSeries(series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Title Chart")
        self.chart.setTheme(QChart.ChartThemeLight)

        self.chartview = QChartView(self.chart)
        
 
 
daychart={}
title_x=[] 
barchar={}
titlechart={}       
static_task={}       
y = []
s = []
taskname=[]
titlelist=[]          
userid =[]
dt={}
if __name__ == '__main__':
    mythread = MyThread(1)
    mythread.start()

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    w = Mainwindow()
    #w = maintodo()
    #w=maintitle()
    widget.addWidget(w)
    widget.setFixedWidth(460)
    widget.setFixedHeight(640)
    widget.show()
    
    sys.exit(app.exec_())
    