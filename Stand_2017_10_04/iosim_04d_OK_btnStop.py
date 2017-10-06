# -*- coding: utf-8 -*-
#!/usr/bin/env python

#......................
#version OK
#gui ok, loop on work

#..............................
#gui
import pygtk
import gtk.glade
pygtk.require("2.0")

#..............................
#IOsim dll
import inspect, time
from ctypes import *

#..............................
import csv
#import runSIM
import simTable
import startSIM

#..............................
#import csv created
import ioTable
import readXlsx

#...........................................................................
#OK
#iosim = cdll.LoadLibrary(r"C:\Program Files\HEIDENHAIN\TNCvbBase\control\JHIOsim.dll")  #iosim = "self" ??
iosim = cdll.LoadLibrary(r"C:\tools\HEIDENHAIN\TNCvbBase\control\JHIOsim.dll")  #iosim = "self" ??

#SIM_ID = 111        #fix ID def

#...........................................................................
#define GLOBAL var for control
varStop = 0
varStart = 0

#...........................................................................
#OK
class IOsim():
    def __init__(self):
    # Set local var:
        # Set the Glade file
        self.gladefile = "iosim_04a.glade"
        self.wTree = gtk.glade.XML(self.gladefile) 
    # Create our dictionay and connect it (for buttons, which don't need to sent or receive data)
        dic = { "on_btnExit_clicked"            : self.btnExit_clicked,             #exit button
                "on_imagemenuitem1_activate"    : self.imagemenuitem1_activate,     #quit button, menu
                "on_btnStop_clicked"            : self.btnStop_clicked,             #stop button
                "on_btnStart_clicked"           : self.btnStart_clicked,            #start button
                #"on_btnReadSIM_ID_clicked"      : self.btnReadSIM_ID_clicked, 
                "on_btnFilechooser_file_set"    : self.btnFilechooser_file_set,     #file select                  
                "on_MainWindow_destroy"         : gtk.main_quit }
        self.wTree.signal_autoconnect(dic)   
      
    #................................................................
    #button def
    def closeProgram(self):                 
        gtk.main_quit()
    
    def btnExit_clicked(self, widget):
        self.btnExit = self.wTree.get_widget('btnExit')
        self.closeProgram()
        
    def imagemenuitem1_activate(self, widget):
        self.btnQuit = self.wTree.get_widget('imagemenuitem1')
        self.closeProgram()
    
    '''def btnReadSIM_ID_clicked(self, widget):
        self.entry = self.wTree.get_widget('entrySIM_ID')      
        entrySIM_ID = self.entry.get_text()
        self.label = self.wTree.get_widget('statusSIM_ID')
        self.label.set_label(entrySIM_ID) 
        #....................................................
        SIM_ID = entrySIM_ID
        #print SIM_ID
        #....................................................
    '''              
    def btnFilechooser_file_set(self, widget):
        print'filechooser test OK'
        self.entry = self.wTree.get_widget('btnFilechooser')
        Filename = self.entry.get_filename()
        self.label = self.wTree.get_widget('lblFilename')
        self.label.set_label(Filename)    
    
    def btnStop_clicked(self, widget):
        print'stop btn test OK'
        print varStop
        if varStop != 0:                #break programm
            readXlsx.readXlsx()
            ioTable.IOTable()
        else: 
            self.closeProgram()          
    
    def btnStart_clicked(self, widget):                     #entry value for SIM_ID, no entry --> nothing
        print'start btn test OK'
        self.entry = self.wTree.get_widget('entrySIM_ID')
        entrySIM_ID = self.entry.get_text()     
        SIM_ID = entrySIM_ID
        print SIM_ID
        
        startSIM.startSIM()
#????????
        #global SIM_ID
              
#...........................................................................
#OK
#SIM = (
#	('O10','I10'),
#	('O11','I11'),
#	('O12','I12'),
#	('O13','I13'),
#	('O14','I14'),
#	('O15','I15'),
#)

#...........................................................................
# Access SIM_ID as following:     IDIn = getSIM()[0];    IDOut = getSIM()[1]
#start/stop

#...........................................................................
#SIM_ID = 111
    '''def getSIM_ID():
        id = 0
        while id == 0:
            id = input('Enter SIM_ID here: ')       #sim_id = 0: nicht aktiviert
        return id
    '''
#...........................................................................
if __name__ == "__main__":
    IOsim = IOsim()
    gtk.main()
    
#    getSIM()
#    IDIn = getSIM()[0]
#    IDOut = getSIM()[1]  
#    sim_ID = getSIM_ID()
#    runSim(sim_ID)