# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:30:02 2020

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

'''
Add the admin registration interface to the tabbed widget 

@param window: the window of the 5th tab from the 'tabbed_main_interface' file
'''
def tab5_function(window):

    '''
    Implementing event on register button 
    
    @param event: getting the left-mouse click event / the 'Enter' key event on the register button 
    '''
    def register_user(event):
        username_info = username.get()
        password_info = password.get()
        
        if field_blank_checking(username_info) == TRUE or field_blank_checking(password_info) == TRUE:
            messagebox.showinfo('Error', 'Both username and password has to be filled!')
        else:
            
            try:
                con=pymysql.connect(user='root', password='', host='localhost', database='parking_locator')
                cur = con.cursor()

                '''
                Title: A check if username exist in database with Python
                Website: StackOverflow
                URL: https://stackoverflow.com/questions/57578420/a-check-if-username-exist-in-database-with-python
                Author: stahamtan
                Date Posted: 20 August 2019
                Date Referred: 18 May 2020
                '''
                check_username_exist = cur.execute("select username from admin where username = '%s'" %(username_info))
        
                if check_username_exist > 0 :
                    messagebox.showinfo('Error', 'Username already taken')
                elif password_format_checking(password_info): 
                    messagebox.showinfo('Error', 'Invalid password! A password must be between 6 to 12 characters that contains a uppercase letter, lowercase letter, digits as well as symbols.')
                else:
                    password_info = hash_password(password_info)
                    sql="insert into admin (username, password) values ('%s','%s')" %(username_info, password_info)
                    cur.execute(sql)
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success', 'Registration Success')
            except:
                messagebox.showinfo('Error', 'Registration Failed')
            finally:
                usernameEntry.delete(0, END)
                passwordEntry.delete(0, END)


    '''
    Title: Hashing Passwords in Python
    Website: Vitosh Academy
    URL:https://www.vitoshacademy.com/hashing-passwords-in-python/
    Author: Alessandro Molina
    Date Posted: 20 September 2018
    Date Referred: 10 May 2020
    '''
    '''
    Hasing the password to be stored in the mysql database
    
    @param password: pass the password from the input field to be hashed
    @return (salt + pwdhash).decode('ascii'): hashed password
    '''
    def hash_password(password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    
    #Designing interface for registration   
    def register():
        global username
        global password
        global usernameEntry
        global passwordEntry
        username = StringVar()
        password = StringVar()
    
        ptitle = Label(window, text='''Register New Administrator''', font='Helvetica 12 bold')
        ptitle.grid(row=0, column=1, columnspan=8)
        
        blankLbl = Label(window, text=" ", height=1)
        blankLbl.grid(row=1, column=1)
        
        fillLabel = Label(window, text="Please enter details below:")
        fillLabel.grid(row=2, column=3)
        
        blankLbl1 = Label(window, text="")
        blankLbl1.grid(row=3, column=3)
        
        usernameLabel = Label(window, text="Username * ")
        usernameLabel.grid(row=4, column=3)
        
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=5, column=3)
        
        passwordLabel = Label(window, text="Password * ")
        passwordLabel.grid(row=6, column=3)
        
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=7, column=3)
        
        blankLbl2 = Label(window, text="", height=1)
        blankLbl2.grid(row=8, column=1)
        
        registrationBtn = Button(window, text="Register", width=11, height=1)
        registrationBtn.grid(row=9, column=3)
        
        '''
        Title: Events and Binds
        Website: Python Tkinter Course
        URL: https://www.python-course.eu/tkinter_events_binds.php
        Author: -
        Date Posted: -
        Date Referred: 29 May 2020
        '''
        registrationBtn.bind('<Button-1>', register_user)
        
        '''
        Title: How do I bind the enter key to a function in tkinter?
        Website: StackOverflow
        URL: https://stackoverflow.com/questions/16996432/how-do-i-bind-the-enter-key-to-a-function-in-tkinter
        Author: 7stud
        Date Posted: 08 June 2013
        Date Referred: 29 May 2020
        '''
        registrationBtn.bind('<Return>', register_user)
        
        
        blankLbl3 = Label(window, text=" ", width=50)
        blankLbl3.grid(row=0, column=0)
        
        
    register()
