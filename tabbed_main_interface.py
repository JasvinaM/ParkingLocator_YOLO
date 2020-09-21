# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:02:46 2020

@author: JM Ealn Davan
"""

'''
Title: Creating Tabbed Widget With Python-Tkinter
Website: GeeksforGeeks
URL: https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/
Author: Shreyasi_Chakraborty
Date Posted: -
Date Referred: 24 May 2020
'''

import tkinter as tk                     
from tkinter import ttk 
from tkinter import messagebox
from tkinter import *

from parking_lot_availability_detection import tab1_function 
from scanned_parking_lot_history import tab2_function 
from resident_configuration import tab3_function 
from parking_lot_detail_configuration import tab4_function 
from admin_registration import tab5_function 


'''
Add the main interface to the login screen

@param window: the window of the 5th tab from the 'tabbed_main_interface' file
'''
def main_interface(root):
        
    #display messagebox before exiting the program
    def on_closing_screen():
        if messagebox.askokcancel("Quit", "Do you want to logout?"):
            root.destroy()
    
    
    '''
    Title: Python - Tkinter Menu
    Website: tutorialspoint
    URL: https://www.tutorialspoint.com/python/tk_menu.htm
    Author: -
    Date Posted: -
    Date Referred: 29 May 2020
    '''
    #display help & documentation for the features in each tab 
    def help_for_users():
       helpWindow = Toplevel(root)
       helpWindow.geometry("1280x720")
       
       canvas = tk.Canvas(helpWindow, width=1248, height = 710)
    
       scrolly = tk.Scrollbar(helpWindow, orient='vertical', command=canvas.yview)
       
       
       '''
       Title: Make a Label Bold Tkinter Ask Question
       Website: StackOverflow
       URL: https://stackoverflow.com/questions/46495160/make-a-label-bold-tkinter
       Author: adder
       Date Posted: 29 September 2017
       Date Referred: 29 May 2020
       '''
       descSystem = Label(canvas, text="This system is created to detect parking spaces in parking lots for residential area that do not have parking spaces specifically allocated for residents. ")
       descSystem.grid(row = 0, column=0, sticky='w')
       canvas.create_window(0, 1*50, anchor='nw', window=descSystem)
       
       
       help1Title = Label(canvas, text="Parking Lot Availability Detection", font='Helvetica 18 bold')
       help1Title.grid(row = 1, column=0, sticky='w')
       canvas.create_window(0, 2*50, anchor='nw', window=help1Title)
       
       '''
       Title: How do I use Tkinter in Python to create line-wrapped text that fills the width of the window?
       Website: StackOverflow
       URL: https://stackoverflow.com/questions/11949391/how-do-i-use-tkinter-in-python-to-create-line-wrapped-text-that-fills-the-width
       Author: Jim Denney
       Date Posted: 14 August 2012
       Date Referred: 29 May 2020
       '''
       help1 = Label(canvas, text="Here you can select video files (.mp4 extension) by clicking the “Browse” button and navigating to that particular file. After the file is selected, select a parking lot from the options/ drop down list that is shown in the video. \n\nOnce that is done, click the “Run Detection” to allow the detection process to begin. Please note that this process will take some time depending on the length of the video. \n\nWhen the video is processing, an indicator “Scanning the Video …” will appear under the “Run Detection” button. If the processing is done, a “Done” will be displayed under the “Run Detection” button. \n\nThe processed video with the availability detection will be shown in the following tab, “Scanned Parking Lot History” , once the program has been restarted (Please close and open the program once again).", wraplength=1250, justify="left")
       help1.grid(row = 2, column=0)
       canvas.create_window(0, 3*50, anchor='nw', window=help1)
       
       
       help2Title = Label(canvas, text="Scanned Parking Lot History", font='Helvetica 18 bold')
       help2Title.grid(row = 4, column=0, sticky='w')
       canvas.create_window(0, 4*115, anchor='nw', window=help2Title)
       
       help2 = Label(canvas, text="You can click on the file name to view the video where previous parking availability were scanned. \n\nThe video will display the number of available spaces as well as the total spaces that is in the parking lot. \n\nTo exit the video, press the ‘q’ key.", wraplength=1250, justify="left")
       help2.grid(row = 5, column=0)
       canvas.create_window(0, 5*102, anchor='nw', window=help2)
       
       
       help3Title = Label(canvas, text="Resident Group Settings", font='Helvetica 18 bold')
       help3Title.grid(row = 4, column=0, sticky='w')
       canvas.create_window(0, 6*112, anchor='nw', window=help3Title)
        
       help3 = Label(canvas, text="House Number: The resident’s house number \n\nChat ID: Any messaging platform that might be used in the future to contact residents, or inform them on the availability of the parking spaces with future improvement. \n\nName: The resident’s name\n\nPhone Number: The resident’s mobile phone number\n\nLot Area: The parking lot area where the resident parks (or on their house level/ floor) \n\nA “Search” button is placed to allow the search of a resident’s record based on their House Number. This feature is provided to display the details of a single record in the input fields. By entering the House Number and clicking the search button, the remaining fields will be searched and displayed in the entry for fast reference as well as ease modification process. \n\nThe “Add”, “Update” and “Delete” buttons allows the insertion of a new resident, modification of the details of an existing resident as well as removing an existing resident respectively. \n\nThe “Clear” button is used to clear the input fields if a new record needs to be added. \n\nThe table shown displays all the resident records. You can view all the resident data by scrolling through the table if there are more than 10 records. \n\nIf you want to display a certain group of residents based on the lot area, you can do so by selecting a lot are from the option/ drop down list on top of the table and click “Filter”. To show all the records after filtering, select “Clear Filter”.", wraplength=1250, justify="left")
       help3.grid(row = 5, column=0)
       canvas.create_window(0, 7*104, anchor='nw', window=help3)
        
    
       help4Title = Label(canvas, text="Parking Lot Detail Configuration", font='Helvetica 18 bold')
       help4Title.grid(row = 4, column=0, sticky='w')
       canvas.create_window(0, 8*172, anchor='nw', window=help4Title)
        
       help4 = Label(canvas, text="Lot Area ID: The unique identifier of a parking lot location \n\nDescription: The description for the parking lot \n\nCapacity: The total number of vehicles that can be accommodated in the parking lot \n\nA “Search” button is placed to allow the search of a parking lot’s record based on its Lot Area ID. This feature is provided to display the details of a single record in the input fields. By entering the Lot Area ID and clicking the search button, the remaining fields will be searched and displayed in the entry for fast reference as well as ease modification process. \n\nThe “Add”, “Update” and “Delete” buttons allows the insertion of a new parking lot, modification of the details of an existing parking lot as well as removing an existing parking lot respectively.  \n\nThe “Clear” button is used to clear the input fields if a new record needs to be added.  \n\nThe table shown displays all the parking lot records. You can view all the parking lot data by scrolling through the table if there are more than 10 records. ", wraplength=1250, justify="left")
       help4.grid(row = 5, column=0)
       canvas.create_window(0, 9*160, anchor='nw', window=help4)
    
        
       help5Title = Label(canvas, text="Admin Registration", font='Helvetica 18 bold')
       help5Title.grid(row = 4, column=0, sticky='w')
       canvas.create_window(0, 10*189, anchor='nw', window=help5Title)
        
       help5 = Label(canvas, text="A valid username and password are required to be entered for the new administrator. \n\nThe password must be between 6 to 12 characters that contains a uppercase letter (Example: A), lowercase letter (Example: a), digits (Example: 0) as well as symbols (Example: !). \n\n Once the form is filled, the “Register” button can be clicked to add the new administrator in the system. \n\n", wraplength=1250, justify="left")
       help5.grid(row = 5, column=0)
       canvas.create_window(0, 11*178, anchor='nw', window=help5)
    
       
       canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set)
       
       
       canvas.grid(sticky="nsew")
       scrolly.grid(sticky="nse",row=0, column=10)
       
    
    
    root = tk.Tk() 
    root.title("Parking Locator - Detect spaces for you") 
    
    '''
    Title: How can I prevent a window from being resized with tkinter?
    Website: StackOverflow
    URL: https://stackoverflow.com/questions/21958534/how-can-i-prevent-a-window-from-being-resized-with-tkinter
    Author: Alex Thornton
    Date Posted: 22 February 2014
    Date Referred: 29 May 2020
    '''
    root.resizable(width=False, height=False)
    root.geometry("1390x720")
    
    
    '''
    Title: Centering window python tkinter
    Website: StackOverflow
    URL: https://stackoverflow.com/questions/25636804/centering-window-python-tkinter
    Author: OregonTrail
    Date Posted: 03 September 2014
    Date Referred: 29 May 2020
    '''
    #centering the window screen
    w = 1390
    h = 720
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    
    #creating the menu to keep the logout option under the file menu
    #and about option under the heklp menu
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=on_closing_screen)
    menubar.add_cascade(label="File", menu=filemenu)
    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About...", command=help_for_users)
    menubar.add_cascade(label="Help", menu=helpmenu)
    
    root.config(menu=menubar)
    
    
    #title for the interface
    titleLabel = tk.Label(root, text="Parking Locator", font='Helvetica 18 bold italic')
    titleLabel.grid(row = 0, column = 0)
    
    
    logoutBtn = tk.Button(root, text="Logout", command = on_closing_screen)
    logoutBtn.grid(row = 0, column = 59)
    
    
    #tab widget to move accross different screens
    tabControl = ttk.Notebook(root) 
    
    tab1 = ttk.Frame(tabControl) 
    tab2 = ttk.Frame(tabControl) 
    tab3 = ttk.Frame(tabControl) 
    tab4 = ttk.Frame(tabControl) 
    tab5 = ttk.Frame(tabControl) 
    
    tabControl.add(tab1, text ='Parking Lot Availability Detection') 
    tabControl.add(tab2, text ='Scanned Parking Lot History') 
    tabControl.add(tab3, text ='Resident Configuration') 
    tabControl.add(tab4, text ='Parking Lot Detail Configuration') 
    tabControl.add(tab5, text ='Admin Registration') 
    
    
    '''
    Title: How to create a self resizing grid of buttons in tkinter?
    Website: StackOverflow
    URL: https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
    Author: Vaughn Cato
    Date Posted: 29 September 2011
    Date Referred: 24 May 2020
    
    Title: tkinter sticky=N+W Error: global name 'N' is not defined
    Website: StackOverflow
    URL: https://stackoverflow.com/questions/37643258/tkinter-sticky-nw-error-global-name-n-is-not-defined
    Author: Bryan Oakley 
    Date Posted: 05 June 2016
    Date Referred: 24 May 2020
    '''
    tabControl.grid(row=1, column=0, columnspan = 60, rowspan = 60, sticky=tk.N+tk.S+tk.E+tk.W) 
    
    #added other files to the tabs
    tab1_function(tab1)
    tab2_function(tab2)
    tab3_function(tab3)
    tab4_function(tab4)
    tab5_function(tab5)
    
    
    '''
    Title: Change text size and color of ttk notebook
    Website: StackOverflow
    URL: https://stackoverflow.com/questions/55761436/change-text-size-and-color-of-ttk-notebook
    Author: Cloud-Chaser
    Date Posted: 24 January 2020
    Date Referred: 27 May 2020
    '''
    style = ttk.Style()
    style.configure('TNotebook.Tab', foreground='black', padding = 10)
    
    root.protocol("WM_DELETE_WINDOW", on_closing_screen)
                                                                  
                                                                   
    root.mainloop()   