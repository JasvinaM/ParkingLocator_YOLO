# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:42:26 2020

@author: JM Ealn Davan
"""
'''
Title: Python Program - Add Delete Modify
Website: Youtube
URL: https://www.youtube.com/watch?v=otd3vL9byJw
Author: MicroNG
Date Posted: 18 October 2017
Date Referred: 10 May 2020
'''

import pymysql
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 

from field_checking_functions import field_blank_checking
from field_checking_functions import number_format_checking  

'''
Add the parking lot detail configuration interface to the tabbed widget 

@param window: the window of the 4th tab from the 'tabbed_main_interface' file
'''
def tab4_function(window):

    style = ttk.Style(window)
    style.configure('Treeview', rowheight=40)
    
    # Using treeview widget 
    treev = ttk.Treeview(window, selectmode ="browse") 
    
    # Create a Tkinter variable for the records 
    tkvar = StringVar(window)
    
    
    #display the table that contains the records of the parking lot 
    def displayList():
        '''
        Title: ttk.Treeview - Can't change row height
        Website: StackOverflow
        URL: https://stackoverflow.com/questions/26957845/ttk-treeview-cant-change-row-height
        Author: Terry Jan Reedy
        Date Posted: 16 November 2014
        Date Referred: 10 May 2020
        
        
        Title: How to clear an entire Treeview with Tkinter
        Website: StackOverflow
        URL: https://stackoverflow.com/questions/22812134/how-to-clear-an-entire-treeview-with-tkinter
        Author: James Adam
        Date Posted: 21 November 2014
        Date Referred: 11 May 2020
        '''
        
        treev.delete(*treev.get_children())
        
        style = ttk.Style(window)
        style.configure('Treeview', rowheight=40)
        
        # Calling grid method to treeview 
        treev.grid(row=2,  column = 5, rowspan = 8)
    
        # Defining number of columns 
        treev["columns"] = ("1", "2", "3") 
          
        # Defining heading 
        treev['show'] = 'headings'
          
        # Assigning the width and anchor to  the respective columns 
        #c = centre
        treev.column("1", width = 150, anchor ='c') 
        treev.column("2", width = 180, anchor ='c') 
        treev.column("3", width = 150, anchor ='c') 
    
          
        # Assigning the heading names to the respective columns 
        treev.heading("1", text ="Lot Area ID") 
        treev.heading("2", text ="Description") 
        treev.heading("3", text ="Capacity") 
    
          
        # Inserting the items and their features to the columns built 
        con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
        cur = con.cursor()
        sql="select * from parking_lot_details"
        cur.execute(sql)
        result = cur.fetchall()
        counter = 0
        for data in result:
            treev.insert("", 'end', text =("L",counter),  values =(data[0], data[1], data[2])) 
            counter = counter + 1
        con.close()
        
        #place the selected row of record to the entry fields in the form
        treev.bind('<ButtonRelease-1>', select_item)
        

    '''
    Place the details of the selected row from the table to the entry fields
    
    @param a: the row selected from the table
    '''
    def select_item(a):
        '''
        Title: python tkinter tree get selected item values
        Website: StackOverflow
        URL: https://stackoverflow.com/questions/30614279/python-tkinter-tree-get-selected-item-values/30615520
        Author: tobias_k
        Date Posted: 03 June 2015
        Date Referred: 11 May 2020
        '''
        curItem = treev.focus()
        lot_area_id.set(treev.item(curItem)['values'][0])
        desc.set(treev.item(curItem)['values'][1])
        capacity.set(treev.item(curItem)['values'][2])
    
        
    #search the parking lot records based on the lot area ID
    def search():
        
        if field_blank_checking(lot_area_id.get()) == TRUE:
            messagebox.showinfo('Error', 'Please enter the Lot Area ID to search!')
        else:
            
            try:
                con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
                cur = con.cursor()
                sql="select * from parking_lot_details where lot_area_id='%s'" %lot_area_id.get()
                cur.execute(sql)
                result = cur.fetchone()
                desc.set(result[1])
                capacity.set(result[2])
                lotAreaIdEntry.configure(state='disabled')
                con.close()
            except:
                messagebox.showinfo('No Data', 'No such parking lot details available.')
                clear()
            
            
    #remove any data on the entry fields
    def clear():
        lot_area_id.set('')
        desc.set('')
        capacity.set('')
        lotAreaIdEntry.configure(state='normal')
    
        
    #add a new parking lot 
    def add():
        
        if field_blank_checking(lot_area_id.get()) == TRUE or field_blank_checking(desc.get()) == TRUE or field_blank_checking(capacity.get()) == TRUE :
            messagebox.showinfo('Error', 'Please enter all the fields!')
        elif number_format_checking(capacity.get()) == TRUE:
            messagebox.showinfo('Error', 'Capacity cannot contain alphabet, symbols and whitespaces!')
        else:
            
            try:
                con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
                cur = con.cursor()
                sql="insert into parking_lot_details values ('%s','%s','%s')" %(lot_area_id.get(), desc.get(), capacity.get())
                cur.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Record Saved')
                displayList()
            except:
                messagebox.showinfo('Error', 'Lot Area exists')
            finally:
                clear()
    
    
    #update an existing parking lot's records
    def update():
        
        if field_blank_checking(lot_area_id.get()) == TRUE or field_blank_checking(desc.get()) == TRUE or field_blank_checking(capacity.get()) == TRUE :
            messagebox.showinfo('Error', 'Please enter all the fields!')
        elif number_format_checking(capacity.get()) == TRUE:
            messagebox.showinfo('Error', 'Capacity cannot contain alphabet, symbols and whitespaces!')
        else:
                
            try:
                con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
                cur = con.cursor()
                sql="update parking_lot_details set description = '%s', capacity = '%s' where lot_area_id = '%s'" %(desc.get(), capacity.get(), lot_area_id.get())
                cur.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Record Modified')
                displayList()
            except:
                messagebox.showinfo('Error', 'Error in data changes')
            finally:
                clear()
           
           
    #removing an existing parking lot
    def delete():
        if field_blank_checking(lot_area_id.get()) == TRUE :
            messagebox.showinfo('Error', 'Please enter the Lot Area ID to remove it!')
        else:
            try:
                con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
                cur = con.cursor()
                sql="delete from parking_lot_details where lot_area_id = '%s'" %(lot_area_id.get())
                cur.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Record Deleted')
                displayList()
            except:
                messagebox.showinfo('Error', 'Error in data deletion')
            finally:
                clear()

    
    ptitle = Label(window, text='''Manage Parking Lot Details''', font='Helvetica 12 bold')
    ptitle.grid(row=0, column=1, columnspan=10)
    
    blankLbl = Label(window, text=" ", height=1)
    blankLbl.grid(row=1, column=0)
    
    lot_area_id = StringVar()
    desc = StringVar()
    capacity = StringVar()
    
    
    lotAreaIdLabel = Label(window, text='Lot Area ID ')
    lotAreaIdEntry = Entry(window, textvariable=lot_area_id)
    descLabel = Label(window, text='Description ')
    descEntry = Entry(window, textvariable=desc)
    capacityLabel = Label(window, text='Capacity ')
    capacityEntry = Entry(window, textvariable=capacity)
    
    searchBtn = Button(window, text="Search", command=search)
    addBtn = Button(window, text="Add", command=add, width=30)
    updateBtn = Button(window, text="Update", command=update, width=30)
    deleteBtn = Button(window, text="Delete", command=delete, width=30)
    clearBtn = Button(window, text="Clear", command=clear, width=30)
    
    blankLbl1 = Label(window, text=" ", width=5)
    blankLbl2 = Label(window, text=" ", width=15)
    
    lotAreaIdLabel.grid(row=2, column=1)
    lotAreaIdEntry.grid(row=2, column=2)
    searchBtn.grid(row=2, column=3)
    
    descLabel.grid(row=3, column=1)
    descEntry.grid(row=3, column=2)
    capacityLabel.grid(row=4, column=1)
    capacityEntry.grid(row=4, column=2)
    
    blankLbl1.grid(row=2, column=4)
    
    addBtn.grid(row=6, column=2)
    updateBtn.grid(row=7, column=2)
    deleteBtn.grid(row=8, column=2)
    clearBtn.grid(row=9, column=2)
    
    blankLbl2.grid(row=3, column=0)
    
    
    displayList()



