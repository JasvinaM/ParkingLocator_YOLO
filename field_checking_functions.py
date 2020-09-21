# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:42:04 2020

@author: JM Ealn Davan
"""

'''
Title: Call a function from another file in Python
Website: StackOverflow
URL: https://stackoverflow.com/questions/20309456/call-a-function-from-another-file-in-python
Author: Salvador Dali
Date Posted: 01 December 2013
Date Referred: 18 May 2020
'''
import re

'''
Title: Python Exercise: Check the validity of a password
Website: w3resource
URL: https://www.w3resource.com/python-exercises/python-conditional-exercise-15.php
Author: -
Date Posted: 26 February 2020
Date Referred: 18 May 2020
'''
'''
Check if the password for new admin registration matches the required format (require at least a uppercase letter, lowercase letter, digit as well as special character)

@param password: password entered during registration
@return password_invalid_format: boolean value to show if the password is invalid or not
'''
def password_format_checking(password):
    password_invalid_format = True
    while password_invalid_format:  
        if (len(password)<6 or len(password)>12):
            break
        elif not re.search("[a-z]",password):
            break
        elif not re.search("[0-9]",password):
            break
        elif not re.search("[A-Z]",password):
            break
        elif not re.search("[!@#$%^&*()~?<>]",password):
            break
        else:
            password_invalid_format=False
            break
        
    return password_invalid_format


'''
Check if the input contains only alphabets 

@param userinput: input inserted in the entry field
@return userinput_invalid_format: boolean value to show if the userinput is valid or not
'''
def alphabet_format_checking(userinput):
    userinput_invalid_format = True
    while userinput_invalid_format:  
        if not re.search("[a-zA-Z]",userinput):
            break
        if re.search("[0-9]",userinput):
            break
        if re.search("[$#@]",userinput):
            break
        else:
            userinput_invalid_format=False
            break
        
    return userinput_invalid_format


'''
Check if the input contains only numbers 

@param userinput: input inserted in the entry field
@return userinput_invalid_format: boolean value to show if the userinput is valid or not
'''
def number_format_checking(userinput):
    userinput_invalid_format = True
    while userinput_invalid_format:  
        if not re.search("[0-9]",userinput):
            break
        if re.search("[a-z]",userinput):
            break
        if re.search("[A-Z]",userinput):
            break
        if re.search("[$#@]",userinput):
            break
        else:
            userinput_invalid_format=False
            break
        
    return userinput_invalid_format


'''
Title: Regex pattern for Malaysian mobile phone Number
Website: StackOverflow
URL: https://stackoverflow.com/questions/45406613/regex-pattern-for-malaysian-mobile-phone-number
Author: Truong Cong Hau
Date Posted: 31 July 2017
Date Referred: 18 May 2020


Title: -
Website: RegEx Testing
URL: https://www.regextester.com/109940
Author: -
Date Posted: -
Date Referred: 18 May 2020
'''
'''
Check if the input contains valid phone number 
Examples:
    0129456782
    +60127232543
    60127232543

@param userinput: input inserted in the entry field
@return userinput_invalid_format: boolean value to show if the userinput is valid or not
'''
def phone_number_format_checking(userinput):
    userinput_invalid_format = True
    while userinput_invalid_format:  
        if not re.search("^(\+?6?01)[0-9]{7,8}$",userinput):
            break
        else:
            userinput_invalid_format=False
            break
        
    return userinput_invalid_format


'''
Check if the input contains blanks

@param userinput: input inserted in the entry field
@return blank: boolean value to show if the userinput contains blank or not
'''
def field_blank_checking(userinput):
    blank = True
    if (len(userinput) == 0):
        return blank
    else:
        blank=False
        return blank
        
    