#!/usr/bin/env python
'''
Created on 22.08.2017
@author: thephuong.tran
'''
# example treeviewcolumn.py

import pygtk
pygtk.require('2.0')
import gtk
import csv

class IOTable:

    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("IO Table")
        self.window.connect("delete_event", self.delete_event)

        # create a liststore with one string column to use as the model
        self.liststore = gtk.ListStore(str, str, str, str, str, str)

        # create the TreeView using liststore
        self.treeview = gtk.TreeView(self.liststore)

        # create the TreeViewColumns to display the data
        self.tvcolumn = gtk.TreeViewColumn('Input | ')
        self.tvcolumn1 = gtk.TreeViewColumn('Description | ')
        self.tvcolumn2 = gtk.TreeViewColumn('State | ')
        self.tvcolumn3 = gtk.TreeViewColumn('Output | ')
        self.tvcolumn4 = gtk.TreeViewColumn('Description | ')
        self.tvcolumn5 = gtk.TreeViewColumn('State')

        # add columns to treeview
        self.treeview.append_column(self.tvcolumn)  #input column 0..
        self.treeview.append_column(self.tvcolumn1)
        self.treeview.append_column(self.tvcolumn2)
        self.treeview.append_column(self.tvcolumn3)        
        self.treeview.append_column(self.tvcolumn4)
        self.treeview.append_column(self.tvcolumn5)

        # create a CellRenderers to render the data
        self.cell = gtk.CellRendererText()
        self.cell1 = gtk.CellRendererText()
        self.cell2 = gtk.CellRendererText()
        self.cell3 = gtk.CellRendererText()
        self.cell4 = gtk.CellRendererText()
        self.cell5 = gtk.CellRendererText()

        # add the cells to the columns - 2 in the first
        self.tvcolumn.pack_start(self.cell, True)   #input column ..
        self.tvcolumn1.pack_start(self.cell1, True)
        self.tvcolumn2.pack_start(self.cell2, True)
        self.tvcolumn3.pack_start(self.cell3, True)
        self.tvcolumn4.pack_start(self.cell4, True)
        self.tvcolumn5.pack_start(self.cell5, True)
        
        # set the cell attributes to the appropriate liststore column
        # GTK+ 2.0 doesn't support the "stock_id" property
        self.tvcolumn.set_attributes(self.cell, text=0)
        self.tvcolumn1.set_attributes(self.cell1, text=1)
        self.tvcolumn2.set_attributes(self.cell2, text=2)
        self.tvcolumn3.set_attributes(self.cell3, text=3)
        self.tvcolumn4.set_attributes(self.cell4, text=4)
        self.tvcolumn5.set_attributes(self.cell5, text=5)

        data = csv.reader(open('IOTable.csv'))
        for row in data:
            self.liststore.append(row)
        self.window.add(self.treeview)
        self.window.show_all()
        return

def main():
    gtk.main()

if __name__ == "__main__":
    IOTable = IOTable()
    main()