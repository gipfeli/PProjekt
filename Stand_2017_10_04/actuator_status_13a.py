# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Created on 22.08.2017
@author: thephuong.tran
'''
import pygtk
import gtk.glade
from _csv import reader
pygtk.require("2.0")

import readXlsx_11
import ioTable_11

import csv


#.............................................................................
# define Window, each in its own class.

class actuator_status:        
    def __init__(self):
    # Set local var:
        # Set the Glade file
        self.gladefile = "actuator_status_11.glade"
        self.wTree = gtk.glade.XML(self.gladefile) 
            
    # Create our dictionay and connect it (for buttons, which don't need to sent or receive data)
        dic = { "on_btn1_clicked" : self.btn1_clicked,                          #send to actuator button
                "on_btnExit_clicked" : self.btnExit_clicked,                    #exit button
                "on_imagemenuitem1_activate" : self.imagemenuitem1_activate,    #quit button, menu
                "on_btnIOTable_clicked" : self.btnIOTable_clicked,              #ioTable button
                "on_btnStop_clicked" : self.btnStop_clicked,                    #stop button
                "on_btnStart_clicked" : self.btnStart_clicked,                  #start button                    
                "on_MainWindow_destroy" : gtk.main_quit }
        self.wTree.signal_autoconnect(dic)
        
    # Button events define:           
        # Get/Retrieve status of actuators
        self.getStatus = self.wTree.get_widget("getStatusBtn")
        self.getStatus.connect("clicked", self.getStatusBtn_clicked)
         
        # Count IO Table instances:
        self.numberWindow = 0
        
    #................................................................           
    # define events (defined and connect through the dictionary, dic)
    #send to actuator button
    def btn1_clicked(self, widget):
        self.entry = self.wTree.get_widget('entry1')
        port = self.entry.get_text()
        self.label = self.wTree.get_widget('status1')
        self.label.set_label(port)
    
    #entry value, read status
    def getStatusBtn_clicked(self, widget):
        self.label = self.wTree.get_widget('status1')
        status = self.label.get_label()
        self.label = self.wTree.get_widget('status2')
        self.label.set_label(status)
    
    #................................................................
    #start/stop button for loop
    def btnStop_clicked(self, widget):
        self.label = self.wTree.get_widget('btnStop')
    
    def btnStart_clicked(self, widget):
        self.label = self.wTree.get_widget('btnStart')    
        try:
            while True:
                readXlsx_11.readXlsx() 
        except KeyboardInterrupt:
            print ('break up!')  
      
    #.....................................................
    #close program
    def closeProgram(self):                 #close program
        gtk.main_quit()
    
    def btnExit_clicked(self, widget):
        self.btnExit = self.wTree.get_widget('btnExit')
        self.closeProgram()
        
    def imagemenuitem1_activate(self, widget):
        self.btnQuit = self.wTree.get_widget('imagemenuitem1')
        self.closeProgram()
    
    #.....................................................
    #ioTable button
    
    def btnIOTable_clicked(self, widget):                                 
        self.btnIOTable = self.wTree.get_widget('btnIOTable')   #show the actuator status
        self.label = self.wTree.get_widget('status1')
        status = self.label.get_label()
        self.label = self.wTree.get_widget('status2')
        self.label.set_label(status)       
        
        #try:    
        data = csv.reader(open('IOTable.csv'))
        readXlsx_11.readXlsx()              #create a ioTable.csv file, ioTable.xlsx must be available
        
        for row in data:
                if status == row[3]:
                    #print row[3], row[4]
                    outputstatus = row[4]                       #show output status
                                  
        self.label = self.wTree.get_widget('lblActuatorStatus')
        self.label.set_label(outputstatus)            
        
        if self.numberWindow == 1:                              #show ioTable only one 
            #ioTable_11().quit()
            def _close(self):
                self.quit()
        else:
            self.numberWindow = 1
            ioTable_11.IOTable()
                                
        #except:
        #    outputstatus = 'new entry!'
        #    self.label.set_label(outputstatus) 
    
                
#.............................................................................
if __name__ == "__main__":
	actuator_status = actuator_status()
	gtk.main()

