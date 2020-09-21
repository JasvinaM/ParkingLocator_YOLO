# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:43:12 2020

@author: JM Ealn Davan
"""
'''
Title: Python GUI Login – Graphical Registration And Login System In Python
Website: SIMPLIFIED PYTHON
URL:https://www.simplifiedpython.net/python-gui-login/
Author: Gulsanober Saba
Date Posted: 3 November 2018
Date Referred: 10 May 2020
'''

from tkinter import *
import os
import hashlib, binascii
import pymysql
import re

from field_checking_functions import password_format_checking
from field_checking_functions import field_blank_checking

from tabbed_main_interface import main_interface 

'''
Title: Hashing Passwords in Python
Website: Vitosh Academy
URL:https://www.vitoshacademy.com/hashing-passwords-in-python/
Author: Alessandro Molina
Date Posted: 20 September 2018
Date Referred: 10 May 2020
'''
'''
De-hasing the password to be matched with the login password entered 

@param stored_password: the password stored in the mysql database of the username
@param provided_password: the password from the password input field
@return pwdhash == stored_password: return boolean if both the passwords match
'''
def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


'''
Implementing event on login button  

@param event: getting the left-mouse click event / the 'Enter' key event on the login button 
'''
def login_verify(event):
    usernameFromUser = usernameVerify.get()
    passwordFromUser = passwordVerify.get()
    usernameLoginEntry.delete(0, END)
    passwordLoginEntry.delete(0, END)

    if field_blank_checking(usernameFromUser) == TRUE or field_blank_checking(passwordFromUser) == TRUE:
        messagebox.showinfo('Error', 'Both username and password has to be filled!')
    else:
        
        try:
            con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
            
            cur = con.cursor()
            sql="select password from admin where username='%s'" %usernameFromUser
            cur.execute(sql)
            result = cur.fetchone()
            password_fetched = result[0]

            
            boolean = verify_password(password_fetched, passwordFromUser)
            con.close()

            if boolean:
                login_sucess()
                
            else:
                messagebox.showinfo('Error', 'Invalid password')
        except:
            messagebox.showinfo('Error', 'Username not found')
            
         
# Once successfully logged in, then the tabbed interface will be shown after this window is removed
def login_sucess():
    loginScreen.destroy()
    main_interface(loginScreen)


#display messagebox before exiting the program
def on_closing_login_screen():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        loginScreen.destroy()
        

# Designing window for login 
def login():
    global loginScreen
    loginScreen = Tk()
    loginScreen.title("Parking Locator - Login")

    blankLbl = Label(loginScreen, text="")
    blankLbl.grid(row=2, column=1)
    
    '''
    Title: How can I prevent a window from being resized with tkinter?
    Website: StackOverflow
    URL: https://stackoverflow.com/questions/21958534/how-can-i-prevent-a-window-from-being-resized-with-tkinter
    Author: Alex Thornton
    Date Posted: 22 February 2014
    Date Referred: 29 May 2020
    '''
    loginScreen.resizable(width=False, height=False)
    loginScreen.geometry("1280x720")

    '''
    Title: Centering window python tkinter
    Website: StackOverflow
    URL: https://stackoverflow.com/questions/25636804/centering-window-python-tkinter
    Author: OregonTrail
    Date Posted: 03 September 2014
    Date Referred: 29 May 2020
    '''
    programWidth = 1280
    programHeight = 720
    screenWidth = loginScreen.winfo_screenwidth()
    screenHeight = loginScreen.winfo_screenheight()
    displayLocationX = (screenWidth/2) - (programWidth/2)
    displayLocationY = (screenHeight/2) - (programHeight/2)
    loginScreen.geometry('%dx%d+%d+%d' % (programWidth, programHeight, displayLocationX, displayLocationY))
    
    global usernameVerify
    global passwordVerify

    usernameVerify = StringVar()
    passwordVerify = StringVar()

    global usernameLoginEntry
    global passwordLoginEntry
    
    
    '''
    Title: how to add a png picture to a tinkter python window?
    Website: StackOverflow
    URL: https://stackoverflow.com/questions/41899109/how-to-add-a-png-picture-to-a-tinkter-python-window
    Author: Tom Fuller
    Date Posted: 28 January 2017
    Date Referred: 27 May 2020
    '''
    imageLogo = PhotoImage(master = loginScreen, file = "logo/Parking Locator Logo.png") # your image
    imageLabel = Label(loginScreen, image = imageLogo) # put the image on a label
    imageLabel.grid(row = 2, column = 1, columnspan = 1, padx = 50) # put the label in the grid

    usernameLabel = Label(loginScreen, text="Username * ")
    usernameLabel.grid(row= 7, column=1, padx= 550, pady = 20)
    
    usernameLoginEntry = Entry(loginScreen, textvariable=usernameVerify)
    usernameLoginEntry.grid(row=11, column=1)
    
    blankLbl1 = Label(loginScreen, text="")
    blankLbl1.grid(row=12, column=1)
    
    
    passwordLabel = Label(loginScreen, text="Password * ")
    passwordLabel.grid(row=13, column=1)
    
    passwordLoginEntry = Entry(loginScreen, textvariable=passwordVerify, show= '*')
    passwordLoginEntry.grid(row=14, column=1)
    
    blankLbl2 = Label(loginScreen, text="")
    blankLbl2.grid(row=15, column=1)
 
    
    loginBtn = Button(loginScreen, text="Login", width=10, height=1)
    loginBtn.grid(row=16, column=1)
    
    
    
    '''
    Title: Events and Binds
    Website: Python Tkinter Course
    URL: https://www.python-course.eu/tkinter_events_binds.php
    Author: -
    Date Posted: -
    Date Referred: 29 May 2020
    '''
    loginBtn.bind('<Button-1>', login_verify)
    
    '''
    Title: How do I bind the enter key to a function in tkinter?
    Website: StackOverflow
    URL: https://stackoverflow.com/questions/16996432/how-do-i-bind-the-enter-key-to-a-function-in-tkinter
    Author: 7stud
    Date Posted: 08 June 2013
    Date Referred: 29 May 2020
    '''
    loginBtn.bind('<Return>', login_verify)

    '''
    Title: How do I handle the window close event in Tkinter?
    Website: StackOverflow
    URL: https://stackoverflow.com/questions/111155/how-do-i-handle-the-window-close-event-in-tkinter
    Author: Matt Gregory
    Date Posted: 21 September 2008 
    Date Referred: 26 May 2020
    '''
    loginScreen.protocol("WM_DELETE_WINDOW", on_closing_login_screen)
    
    loginScreen.mainloop()
    

login()