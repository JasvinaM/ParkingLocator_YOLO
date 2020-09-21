# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:42:26 2020

@author: JM Ealn Davan
"""

import pymysql
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 

'''
Title: Tkinter tkFileDialog module
Website: Python Tutorials
URL: https://pythonspot.com/tk-file-dialogs/
Author: -
Date Posted: -
Date Referred: 24 May 2020
'''
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

from yolo_availability_detection import yolo_detection 

'''
Add the parking lot avaialbility detection interface to the tabbed widget 

@param window: the window of the 1st tab from the 'tabbed_main_interface' file
'''
def tab1_function(window):
    # Create a Tkinter variable for the dropdown of the parking lot drop down list
    tkvar = StringVar(window)

    parking_lot_capacity = 0
    
    #indicator text to inform the user on the status of the detection process
    loadingLabel = Label(window, text="")
    loadingLabel.grid(row = 6, column =3)
        
    #create the parking lot drop down list
    def dropdown():
        '''
        Title: Tk dropdown example
        Website: Python Tutorials
        URL:https://pythonspot.com/tk-dropdown-example/
        Author: -
        Date Posted: -
        Date Referred: 10 May 2020
        '''
        
        # Store the parking lot area ID in the array
        choices = list()
        con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                
        cur = con.cursor()
        
        #get the ID by ascending order
        sql="select lot_area_id from parking_lot_details order by lot_area_id asc" 
        cur.execute(sql)
        result = cur.fetchall()
        counter = 0
        for data in result:
            choices.append(data[0])
            counter = counter + 1
        con.close()
        
        # set the default option
        tkvar.set(choices[0]) 
        
        #creating the drop down list
        popupMenu = OptionMenu(window, tkvar, *choices)
        Label(window, text="Choose a parking lot").grid(row = 3, column = 2)
        popupMenu.grid(row = 3, column =3)
        
        # on change dropdown value, get the selected value
        def change_dropdown(*args):
            tkvar.get() 
        
        # link function to change dropdown
        tkvar.trace('w', change_dropdown)
        
    
    #run the detection process on the video selected
    def run():
        try:
            
            con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
            
            cur = con.cursor()
            sql="select capacity from parking_lot_details where lot_area_id ='%s'" %tkvar.get()
            cur.execute(sql)
            result = cur.fetchone()
            parking_lot_capacity = result[0]
            con.close()
            
            '''
            Title: Tkinter Label not appearing
            Website: Stack Overflow
            URL: https://stackoverflow.com/questions/44768319/tkinter-label-not-appearing
            Author: AlphaMycelium
            Date Posted: 09 August 2017
            Date Referred: 28 May 2020
            '''
            #inform the user that the detection process has started
            loadingLabel['text']="Scanning the Video ..."
            window.update()

            #call the YOLO detection function
            start_program(video_dir.get(), parking_lot_capacity, tkvar.get())
            
            '''
            Title: Changing the text on a label
            Website: Stack Overflow
            URL: https://stackoverflow.com/questions/17125842/changing-the-text-on-a-label
            Author: falsetru 
            Date Posted: 15 June 2013
            Date Referred: 27 May 2020
            '''
            #inform the user that the detection process has ended
            loadingLabel['text']="Done! Please re-open the program to view it in the 'Scanned Parking Lot History' tab."

        except:
           messagebox.showinfo('Error', 'Program unable to run. Please contact the technition!')
        finally:
            clear()
    
        
    #clear the video input field
    def clear():
        video_dir.set('')
        

    #call the YOLO object detection algorithm from the 'yolo_availability_detection' file
    def start_program(video_name, capacity, lot_area): 
        yolo_detection(video_name, capacity, lot_area)


    #display a dialog to allow user select the video file (.mp4) that they wish to scan
    #and put that video file path in the entry field
    def file():
        '''
        Title: Python 3 - Open file dialog window in tkinter with filedialog
        Website: Github
        URL: https://gist.github.com/Yagisanatode/0d1baad4e3a871587ab1
        Author: Yagisanatode
        Date Posted: -
        Date Referred: 27 May 2020
        '''
        name = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp4 files","*.mp4"),("all files","*.*")))
        video_dir.set(name)

        
    ptitle = Label(window, text='''Select Video File & Corresponding Parking Lot for Availability Detection''', font='Helvetica 12 bold')
    ptitle.grid(row=0, column=1, columnspan=10)
    
    blankLbl = Label(window, text=" ", height=5)
    blankLbl.grid(row=1, column=1)
    
    blankLbl1 = Label(window, text=" ", height=3)
    
    blankLbl2 = Label(window, text=" ", width=25)
    blankLbl2.grid(row=0, column=0)
    
    blankLbl3 = Label(window, text=" ", height=1)
    
    video_dir = StringVar()
    
    dropdown()
    
    label1 = Label(window, text='Video File ')
    entry1 = Entry(window, textvariable=video_dir)
    entry1.configure(state='disabled')

    
    browseBtn = Button(window, text="Browse", command=file)
    detectionBtn = Button(window, text="Run Detection", command= run, width=30)
    
    label1.grid(row=1, column=2)
    entry1.grid(row=1, column=3)
    browseBtn.grid(row=1, column =4)
    
    blankLbl1.grid(row=4, column=2)
    
    detectionBtn.grid(row=5, column=3)
    
    blankLbl1.grid(row=5, column=1)
    
