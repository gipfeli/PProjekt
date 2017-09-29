#!/usr/bin/env python

import sys
try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
except:
	sys.exit(1)
    
import readxlsx
import csv
from time import sleep

import logging # Debugging
logging.basicConfig(level=logging.DEBUG)

##############################################################################
# Define temp. global variable

##############################################################################
# define Window, each in its own class.

class aktorStatus:
	"""Main window: show aktor_status of multiple actuators"""
        
        def __init__(self):
        # Set temp. local var:
            self.aktor_realStatus = ["1", "0", "0"] # 1 = On; 0 = Off            
        # Set the Glade file
            self.gladefile = "aktor_status.glade"
            self.wTree = gtk.glade.XML(self.gladefile) 
                
        # Create our dictionay and connect it (for buttons, which don't need to sent or receive data)
            dic = { "on_btn1_clicked" : self.btn1_clicked,
                    "on_refDBio_clicked" : self.refDBio_clicked,
                    "on_MainWindow_destroy" : gtk.main_quit }
            self.wTree.signal_autoconnect(dic)
            
        # Button events define:
            # Choose actuators:
            self.btn1 = self.wTree.get_widget("tempbtn1")
            self.btn1.connect("clicked", self.on_tempbtn1_clicked, "1", self.aktor_realStatus[0])
            self.btn2 = self.wTree.get_widget("tempbtn2")
            self.btn2.connect("clicked", self.on_tempbtn2_clicked, "2", self.aktor_realStatus[1])
            self.btn3 = self.wTree.get_widget("tempbtn3")
            self.btn3.connect("clicked", self.on_tempbtn3_clicked, "3", self.aktor_realStatus[2])
            # Get/Retrieve status of actuators
            self.getStatus = self.wTree.get_widget("getStatusBtn")
            self.getStatus.connect("clicked", self.getStatusBtn_clicked)
            # Show IO Table

            
#####
# define events (defined and connect through the dictionary, dic)
        def btn1_clicked(self, widget):
            self.entry = self.wTree.get_widget('entry1')
            port = self.entry.get_text()
            self.label = self.wTree.get_widget('status1')
            self.label.set_label(port)
        
        def status(self, var):
            self.label = self.wTree.get_widget("status1") 
            if var == "1":
                self.label.set_label("On")                
            else:
                self.label.set_label("Off")                
        
        def on_tempbtn1_clicked(self, widget, data, onoff):
            self.label = self.wTree.get_widget("activeAktor") 
            self.label.set_label(data)
            self.status(onoff)
        
        def on_tempbtn2_clicked(self, widget, data, onoff):
            self.label = self.wTree.get_widget("activeAktor") 
            self.label.set_label(data)
            self.status(onoff)
            
        def on_tempbtn3_clicked(self, widget, data, onoff):
            self.label = self.wTree.get_widget("activeAktor") 
            self.label.set_label(data)
            self.status(onoff)
            
        def getStatusBtn_clicked(self, widget):
            self.label = self.wTree.get_widget('status1')
            status = self.label.get_label()
            self.label = self.wTree.get_widget('status1.5')
            self.label.set_label(status)

        def refDBio_clicked(self, widget):
            readxlsx.readData()
            self.label = self.wTree.get_widget('status1')
#            status = self.label.get_label()
            data = csv.reader(open('IOTable.csv'))
            for row in data:
#                if status == row[3]:
#                    print row[3], row[4]
#                    outputstatus = row[4]
                outputstatus = row[4]
                self.label = self.wTree.get_widget('status2')
                self.label.set_label(outputstatus)
                sleep(1)
            
            
            
##############################################################################
if __name__ == "__main__":
	aktor = aktorStatus()
	gtk.main()

