import sys 
from main import Mainwindow 

from main import * 
import argparse
import colorsys
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

from sqlalchemy import true
from urllib3 import Retry
from range_slider import *
"""from test3 import *"""
a = Mainwindow(QtWidgets)
parent_dir = "C:/Users/s6301012620103/Documents/Softdev2/Assigment_3/testcsv/version7.2"
list_csv = ['csvtest1.csv', 'csvtest2.csv']
fname = []
if a.openImportfolder(parent_dir):
    """print ("Can Open File path")
    """
    print (a.openImportfolder(parent_dir))
else: 
    ("Error")