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
refTabl = [["i201","symbol_i1","o300","symbol_o1"],
           ["i201","symbol_i2","o300","symbol_o2"],
           ["i201","symbol_i3","o300","symbol_o3"],
           ["i201","symbol_i4","o300","symbol_o4"],
           ["i201","symbol_i5","o300","symbol_o5"],
           ["i201","symbol_i6","o300","symbol_o6"],
           ["i201","symbol_i7","o300","symbol_o7"],
           ["i201","symbol_i8","o300","symbol_o8"],
           ["i201","symbol_i9","o300","symbol_o9"]]


class aktor_status():    
    # Aktor status definieren:
    var = 'This is a common status'
    
    def __init__(self):      
        self.gladeXml = gtk.glade.XML("aktor_status_20170914.glade")
        self.gladeXml.signal_autoconnect(self)
        self.window = self.gladeXml.get_widget("window_main")
        self.window.set_title("aktor_status_20170918")
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
    # 

    #...........................................................................   
    #start ioTable
    def on_fkt_RUN_button_press_event(self,btn):    #io table show
        tblIOtable.main()                                
    
    def on_btnAktorStatus_pressed(self,btn):        
        self.label = self.gladeXml.get_widget("lblStatus")
        self.label1 = self.gladeXml.get_widget("lblAktorStatus")
        self.label1.set_label(aktor_status.var)
    
    #...........................................................................  
    # All PyGTK applications must have a gtk.main(). Control ends here
    # and waits for an event to occur (like a key press or mouse event).
    def main(self):
        gtk.main()
    
class tblIOtable():
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Ref. Window")
        self.window.set_size_request(200, 200)
        self.window.connect("delete_event", self.delete_event)
#        
#        # the data in the model (four strings for each row, one for each column)
#        treestore = gtk.ListStore(str, str, str, str)
#        # append the values in the model
#        for i in range(len(refTabl)):
#            treestore.append(refTabl[i])
#        
#        # a treeview to see the data stored in the model
#        view = gtk.TreeView(model=treestore)
#        # for each column
#        for i, column in enumerate(columns):
#            # cellrenderer to render the text
#            cell = gtk.CellRendererText()
#            # the column is created
#            col = gtk.TreeViewColumn(column, cell, text=i)
#            # and it is appended to the treeview
#            view.append_column(col)
#            
#        # a grid to attach the widgets
#        grid = gtk.Grid()
#        grid.attach(view, 0, 0, 1, 1)
#        grid.attach(self.label, 0, 1, 1, 1)
#
#        # attach the grid to the window
#        self.add(grid)
##..................................................................
#    def open_file():
#        '''
#        open and read an excel xlsx file
#        '''
#        
#        file_location = "ioTable.xlsx"
#        table = xlrd.open_workbook(file_location)
#        
#        #sheet 1
#        sheet1 = table.sheet_by_index(0)
#        sheet2 = table.sheet_by_index(0)
#        
#        #read a row
#        print sheet1.row_values(0)
#    
#        #read column 0 = colx=0
#        cell = sheet1.col_slice(colx=0, 
#                                start_rowx=0, end_rowx=10)
#        for cell in cell:
#            print cell.value
#        
#        #read row 0 = rowx=0
#        cell = sheet1.row_slice(rowx=0, 
#                                start_colx=0, end_colx=10)
#        for cell in cell:
#            print cell.value
#        print "ok"
#        #open_file()           
#..................................................................    

    #...........................................................................
    #button restart 
    #...........................................................................    
         
if __name__ == "__main__":
    app = aktor_status()
