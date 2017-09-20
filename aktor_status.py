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

##############################################################################
# Define temp. global variable

##############################################################################
# define Window, each in its own class.

class aktorStatus:
	"""Main window: show aktor_status of multiple actuators"""
        
        def __init__(self):
            
        # Set the Glade file
            self.gladefile = "aktor_status.glade"
            self.wTree = gtk.glade.XML(self.gladefile) 
                
        # Create our dictionay and connect it
            dic = { "on_btn1_clicked" : self.btn1_clicked,
                    "on_MainWindow_destroy" : gtk.main_quit }
            self.wTree.signal_autoconnect(dic)
            
            self.wTree.signal_connect("on_tempbtn1_clicked", self.tempbtn_clicked, "1")
#            self.wTree.signal_connect("on_tempbtn2_clicked", self.tempbtn_clicked)
#            self.wTree.signal_connect("on_tempbtn3_clicked", self.tempbtn_clicked)
           
#####
# define events (defined and connect through the dictionary, dic)
        def btn1_clicked(self, widget):
            pass
        
        def tempbtn_clicked(self, widget, data):
            self.label = self.wTree.get_widget("activeAktor") 
            self.label.set_label(data)

##############################################################################
if __name__ == "__main__":
	aktor = aktorStatus()
	gtk.main()

