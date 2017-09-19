# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Created on 12.09.2017
@author: thephuong.tran
'''
import gtk
import gtk.glade
#import subprocess
#import xlrd

# Temp data to show table
# They would be replaced with function, which automatically pull data from xlsx: use xlrd
columns = ["Input",
           "Beschreibung",
           "Output",
           "Beschreibung"]

# Avoid hard-/handing code the data 
refTabl = [("i201","symbol_i1","o300","symbol_o1"),
           ("i201","symbol_i2","o300","symbol_o2"),
           ("i201","symbol_i3","o300","symbol_o3"),
           ("i201","symbol_i4","o300","symbol_o4"),
           ("i201","symbol_i5","o300","symbol_o5"),
           ("i201","symbol_i6","o300","symbol_o6"),
           ("i201","symbol_i7","o300","symbol_o7"),
           ("i201","symbol_i8","o300","symbol_o8"),
           ("i201","symbol_i9","o300","symbol_o9")]


class aktor_status():
        
    def __init__(self):      
        self.gladeXml = gtk.glade.XML("aktor_status_20170914.glade")
        self.gladeXml.signal_autoconnect(self)
        self.window = self.gladeXml.get_widget("window_main")
        self.window.set_title("aktor_status_20170914")
        
        # Aktor status definieren:
        self.var = 'This is a common status'
        self.window.show_all()       
    #...........................................................................
    #...........................................................................
    #button close / function program stop
    def btnClose(self):                         #beenden befehl zum ausfuehren
        gtk.main_quit()
     
    def on_menuItem_break_activate(self,btn):   #funktion bestaetigt, noch keine beenden befehl
        self.btnClose()
        
    def on_btnClose_clicked(self,*args):        #funktion bestaetigt, noch keine beenden befehl
        self.btnClose()        
    #...........................................................................
    
    #...........................................................................
    #manual_signal_for_aktor
    #button einlesen
    def on_manual_iAktor_clicked (self,btn):    #set manual_signal_for_aktor button              
        self.label = self.gladeXml.get_widget("lblStatus") 
        self.label.set_label(aktor_status.var)      #label name setzen

    #...........................................................................   
    #start ioTable
    def on_fkt_RUN_button_press_event(self,btn):    #io table show
        tblIOtable().main()                                
    
    def on_btnAktorStatus_pressed(self,btn):        
        self.label = self.gladeXml.get_widget("lblStatus")
        self.label1 = self.gladeXml.get_widget("lblAktorStatus")
        self.label1.set_label(aktor_status.var)
        
    #...........................................................................  

class tblIOtable():
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Ref. Window")
        self.window.set_size_request(200, 200)
        self.window.connect("delete_event", self.delete_event)
        
    def main(self):
        gtk.main()
         
aktor_status = aktor_status().main()
