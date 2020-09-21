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
from field_checking_functions import alphabet_format_checking  
from field_checking_functions import number_format_checking  
from field_checking_functions import phone_number_format_checking   

'''
Add the resident configuration interface to the tabbed widget 

@param window: the window of the 3rd tab from the 'tabbed_main_interface' file
'''
def tab3_function(window):
    
    lot_area_selected = ""
    
    style = ttk.Style(window)
    style.configure('Treeview', rowheight=40)
    
    # Using treeview widget 
    treev = ttk.Treeview(window, selectmode ="browse") 
    
    # Create a Tkinter variable for the drop down list 
    # for the records and the table filter
    tkvar_table = StringVar(window)
    tkvar_lot_area_resident = StringVar(window)
    
    #display the table that contains the records of the residents
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
        treev.grid(row=4,  column = 4, rowspan = 8, columnspan = 5) 
        
        # Defining number of columns 
        treev["columns"] = ("1", "2", "3", "4", "5") 
          
        # Defining heading 
        treev['show'] = 'headings'
          
        # Assigning the width and anchor to the respective columns 
        #c = centre
        treev.column("1", width = 150, anchor ='c') 
        treev.column("2", width = 150, anchor ='c') 
        treev.column("3", width = 180, anchor ='c') 
        treev.column("4", width = 180, anchor ='c') 
        treev.column("5", width = 150, anchor ='c') 
          
        # Assigning the heading names to the respective columns 
        treev.heading("1", text ="House Number") 
        treev.heading("2", text ="Chat ID") 
        treev.heading("3", text ="Name") 
        treev.heading("4", text ="Phone Number") 
        treev.heading("5", text ="Lot Area") 
    
          
        # Inserting the items and their features to the columns built 
        con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
        cur = con.cursor()
        sql="select * from resident"
        cur.execute(sql)
        result = cur.fetchall()
        counter = 0
        for data in result:
            treev.insert("", 'end', text =("L",counter),  values =(data[0], data[1], data[2], data[3], data[4])) 
            counter = counter + 1
        con.close()
        
        #place the selected row of record to the entry fields in the form
        treev.bind('<ButtonRelease-1>', select_item)
        
        
    #display the table that contains the records of the filtered lot area of the residents
    def displayFilteredList():
        
        treev.delete(*treev.get_children())
        
        style = ttk.Style(window)
        style.configure('Treeview', rowheight=40)
        
        # Calling grid method to treeview 
        treev.grid(row=4,  column = 4, rowspan = 8, columnspan = 5) 
        
        # Defining number of columns 
        treev["columns"] = ("1", "2", "3", "4", "5") 
          
        # Defining heading 
        treev['show'] = 'headings'
          
        # Assigning the width and anchor to  the respective columns 
        #c = centre
        treev.column("1", width = 150, anchor ='c') 
        treev.column("2", width = 150, anchor ='c') 
        treev.column("3", width = 180, anchor ='c') 
        treev.column("4", width = 180, anchor ='c') 
        treev.column("5", width = 150, anchor ='c') 
          
        # Assigning the heading names to the respective columns 
        treev.heading("1", text ="House Number") 
        treev.heading("2", text ="Chat ID") 
        treev.heading("3", text ="Name") 
        treev.heading("4", text ="Phone Number") 
        treev.heading("5", text ="Lot Area") 
          
        # Inserting the items and their features to the columns built 
        con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
        
        lot_area_selected = tkvar_table.get()
        
        cur = con.cursor()
        sql="select * from resident where lot_area='%s'" %lot_area_selected
        cur.execute(sql)
        result = cur.fetchall()
        counter = 0
        for data in result:
            treev.insert("", 'end', text =("L",counter),  values =(data[0], data[1], data[2], data[3], data[4])) 
            counter = counter + 1
        con.close()
        
        #place the selected row of record to the entry fields in the form
        treev.bind('<ButtonRelease-1>', select_item)
        
        
    # Store the parking lot area ID in the array
    choices = list()
    
    
    #display the parking lot ID drop down list in the form
    def dropdown_field_resident():
        '''
        Title: Tk dropdown example
        Website: Python Tutorials
        URL:https://pythonspot.com/tk-dropdown-example/
        Author: -
        Date Posted: -
        Date Referred: 10 May 2020
        '''

        con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
        cur = con.cursor()
        sql="select distinct lot_area_id from parking_lot_details order by lot_area_id asc" 
        cur.execute(sql)
        result = cur.fetchall()
        counter = 0
        for data in result:
            choices.append(data[0])
            counter = counter + 1
        con.close()
        
        # set the default option
        tkvar_lot_area_resident.set(choices[0]) 
        
        #creating the drop down list
        popupMenu = OptionMenu(window, tkvar_lot_area_resident, *choices)
        popupMenu.grid(row = 6, column =1)
        
        # on change dropdown value
        def change_dropdown(*args):
            tkvar_lot_area_resident.get()
        
        # link function to change dropdown
        tkvar_lot_area_resident.trace('w', change_dropdown)
        
    
    #display the parking lot ID drop down list for the table filter
    def dropdown():
         # set the default option
        tkvar_table.set(choices[0]) 
        
        #creating the drop down list
        popupMenu = OptionMenu(window, tkvar_table, *choices)
        Label(window, text="Choose a parking lot:").grid(row = 2, column = 4)
        popupMenu.grid(row = 2, column =5)
        
        # on change dropdown value
        def change_dropdown(*args):
            tkvar_table.get() 
        
        # link function to change dropdown
        tkvar_table.trace('w', change_dropdown)
        
    
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
        house_no.set(treev.item(curItem)['values'][0])
        chat_id.set(treev.item(curItem)['values'][1])
        name.set(treev.item(curItem)['values'][2])
        phone_num.set(treev.item(curItem)['values'][3])
        tkvar_lot_area_resident.set(treev.item(curItem)['values'][4])
        
        
    #search the resident records based on the house number
    def search():
        
        if field_blank_checking(house_no.get()) == TRUE:
            messagebox.showinfo('Error', 'Please enter the house number to search!')
        elif number_format_checking(house_no.get()) == TRUE:
            messagebox.showinfo('Error', 'House number cannot contain alphabet, symbols and whitespaces!')
        else:
            
            try:
                con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
                cur = con.cursor()
                sql="select * from resident where house_no='%s'" %house_no.get()
                cur.execute(sql)
                result = cur.fetchone()
                chat_id.set(result[1])
                name.set(result[2])
                phone_num.set(result[3])            
                tkvar_lot_area_resident.set(result[4])
                
                houseNumberEntry.configure(state='disabled')
                con.close()
            except:
                messagebox.showinfo('No Data', 'No such resident available.')
                clear()
                
                
    #remove any data on the entry fields
    def clear():
        house_no.set('')
        chat_id.set('')
        name.set('')
        phone_num.set('')
        tkvar_lot_area_resident.set(choices[0])
        houseNumberEntry.configure(state='normal')
        
        
    #add a new resident record
    def add():
        
        if field_blank_checking(house_no.get()) == TRUE or field_blank_checking(chat_id.get()) == TRUE or field_blank_checking(name.get()) == TRUE or field_blank_checking(phone_num.get()) == TRUE :
            messagebox.showinfo('Error', 'Please enter all the fields!')
        elif number_format_checking(house_no.get()) == TRUE:
            messagebox.showinfo('Error', 'House number cannot contain alphabet, symbols and whitespaces!')
        elif alphabet_format_checking(name.get()) == TRUE:
            messagebox.showinfo('Error', 'Name cannot contain number, symbols and whitespaces!')
        elif phone_number_format_checking(phone_num.get()) == TRUE:
            messagebox.showinfo('Error', 'Phone number must have the format 0123333444 or +601233334444!')
        else:
            
            try:
                con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
                cur = con.cursor()
                sql="insert into resident values ('%s','%s','%s','%s', '%s')" %(house_no.get(), chat_id.get(), name.get(), phone_num.get(), tkvar_lot_area_resident.get())
                cur.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Record Saved')
                displayList()
            except:
                messagebox.showinfo('Error', 'House number exists')
            finally:
                clear()
    
    #update an existing resident's records
    def update():
        
        if field_blank_checking(house_no.get()) == TRUE or field_blank_checking(chat_id.get()) == TRUE or field_blank_checking(name.get()) == TRUE or field_blank_checking(phone_num.get()) == TRUE :
            messagebox.showinfo('Error', 'Please enter all the fields!')
        elif number_format_checking(house_no.get()) == TRUE:
            messagebox.showinfo('Error', 'House number cannot contain alphabet, symbols and whitespaces!')
        elif alphabet_format_checking(name.get()) == TRUE:
            messagebox.showinfo('Error', 'Name cannot contain number, symbols and whitespaces!')
        elif phone_number_format_checking(phone_num.get()) == TRUE:
            messagebox.showinfo('Error', 'Phone number must have the format 0123333444 or +601233334444!')
        else:
                
            try:
                con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
                cur = con.cursor()
                sql="update resident set chat_id = '%s', name = '%s', phone_number = '%s', lot_area = '%s' where house_no = '%s'" %(chat_id.get(), name.get(), phone_num.get(), tkvar_lot_area_resident.get(), house_no.get())
                cur.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Record Modified')
                displayList()
            except:
                messagebox.showinfo('Error', 'Error in data changes')
            finally:
                clear()
           
            
    #removing an existing resident
    def delete():
        
        if field_blank_checking(house_no.get()) == TRUE :
            messagebox.showinfo('Error', 'Please enter the house number to remove it!')
        elif number_format_checking(house_no.get()) == TRUE:
            messagebox.showinfo('Error', 'House number cannot contain alphabet, symbols and whitespaces!')
        else:
            try:
                con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
                cur = con.cursor()
                sql="delete from resident where house_no = '%s'" %(house_no.get())
                cur.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Record Deleted')
                displayList()
            except:
                messagebox.showinfo('Error', 'Error in data deletion')
            finally:
                clear()
    
    
    ptitle = Label(window, text='''Manage Resident Details''', font='Helvetica 12 bold')
    ptitle.grid(row=0, column=0, columnspan=10)
    
    blankLbl = Label(window, text=" ", height=1)
    blankLbl.grid(row=1, column=0)
    
    house_no = StringVar()
    chat_id = StringVar()
    name = StringVar()
    phone_num = StringVar()
    
    houseNumberLabel = Label(window, text='House Number ')
    houseNumberEntry = Entry(window, textvariable=house_no)
    chatIdLabel = Label(window, text='Chat ID ')
    chatIdEntry = Entry(window, textvariable=chat_id)
    nameLabel = Label(window, text='Name ')
    nameEntry = Entry(window, textvariable=name)
    phoneNumberLabel = Label(window, text='Phone Number ')
    phoneNumberEntry = Entry(window, textvariable=phone_num)
    lotAreaLabel = Label(window, text='Lot Area ')
    dropdown_field_resident()
    
    searchBtn = Button(window, text="Search", command=search)
    addBtn = Button(window, text="Add", command=add, width=30)
    updateBtn = Button(window, text="Update", command=update, width=30)
    deleteBtn = Button(window, text="Delete", command=delete, width=30)
    clearBtn = Button(window, text="Clear", command=clear, width=30)
    filterBtn = Button(window, text="Filter", command=displayFilteredList)
    clearFilterBtn = Button(window, text="Clear Filter", command=displayList)
    
    blankLbl1 = Label(window, text=" ", width=5)
    
    houseNumberLabel.grid(row=2, column=0)
    houseNumberEntry.grid(row=2, column=1)
    searchBtn.grid(row=2, column=2)
    
    chatIdLabel.grid(row=3, column=0)
    chatIdEntry.grid(row=3, column=1)
    nameLabel.grid(row=4, column=0)
    nameEntry.grid(row=4, column=1)
    phoneNumberLabel.grid(row=5, column=0)
    phoneNumberEntry.grid(row=5, column=1)
    lotAreaLabel.grid(row=6, column=0)
    
    blankLbl1.grid(row=2, column=3)
    
    addBtn.grid(row=8, column=1)
    updateBtn.grid(row=9, column=1)
    deleteBtn.grid(row=10, column=1)
    clearBtn.grid(row=11, column=1)
    
    filterBtn.grid(row=2, column=6)
    clearFilterBtn.grid(row=2, column=7)

    
    displayList()
    dropdown()



