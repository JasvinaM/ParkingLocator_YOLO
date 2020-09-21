# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:18:46 2020

@author: JM Ealn Davan
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk

#to get video directory
import glob 

import cv2
import tkinter as tk
import os
import tkinter.ttk


'''
Add the scanned parking lot history interface to the tabbed widget 

@param window: the window of the 2nd tab from the 'tabbed_main_interface' file
'''
def tab2_function(window):

    ptitle = Label(window, text='''Video Files to Display Parking Lots with Availability''', font='Helvetica 12 bold')
    ptitle.grid(row=0, column=0, columnspan=10)
    
    blankLbl = Label(window, text=" ", height=1)
    blankLbl.grid(row=1, column=0)
    
    tips = Label(window, text="Press 'q' to close video.")
    tips.grid(row=2, column=0)
    
    '''
    Title: Python - How Scrollbar does work with Labels, radiobuttons, Buttons?
    Website: Stack Overflow
    URL: https://stackoverflow.com/questions/44243693/python-how-scrollbar-does-work-with-labels-radiobuttons-buttons
    Author: j_4321
    Date Posted: 30 May 2017
    Date Referred: 25 May 2020
    '''
    #canvas to store all the button components/ widgets 
    canvas = tk.Canvas(window, width=1350, height=510)
    
    #scrollbar for the canvas
    scrolly = tk.Scrollbar(window, orient='vertical', command=canvas.yview)

    
    '''
    Display the scanned video files clicked by user in another windows
    
    @param filename: the name of the video file
    '''
    def openVideo(filename):
        '''
        Title: How do I open an MP4 video file with python?
        Website: Stack Overflow
        URL: https://stackoverflow.com/questions/36634807/how-do-i-open-an-mp4-video-file-with-python
        Author: Arun Sooraj
        Date Posted: 27 October 2016
        Date Referred: 25 May 2020
        
        Title: OpenCV & Python - Image too big to display
        Website: Stack Overflow
        URL: https://stackoverflow.com/questions/35180764/opencv-python-image-too-big-to-display
        Author: Zynk
        Date Posted: 3 February 2016
        Date Referred: 25 May 2020
        '''
        cap = cv2.VideoCapture(filename)
        ret, frame = cap.read()
        while(1):
           ret, frame = cap.read()
           imS = cv2.resize(frame, (1920, 1080))
           cv2.imshow('frame',imS)
           if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
               cap.release()
               cv2.destroyAllWindows()
               break
           cv2.imshow('frame',imS)

    
    '''
    Get the filename displayed on the button and attach it to the path for the full directory
    & call the openVideo function to display the video
    
    @param buttonVideo: the name of the video file
    '''
    def passName(buttonVideo):
        openVideo("../Parking Locator/output/" + buttonVideo["text"])


    #number of videos in that path
    total_videos = len(glob.glob("../Parking Locator/output/*.avi"))
    
    #array to store all the videos
    video_arr = list()
    for x in range(total_videos):
        video_arr.append(glob.glob("../Parking Locator/output/*.avi")[x])
    
    
    '''
    Title: Python GUI Programming With Tkinter
    Website: Real Python
    URL: create.arduino.cc/projecthub/igorF2/arduino-uno-mini-weather-station-31b555?ref=tag&ref_id=iot&offset=11
    Author: David Amos
    Date Posted: 22 January 2020 
    Date Referred: 11 May 2020
    '''
    for i in range(total_videos):
        
        '''
        Title: Python - How to get the filename in tkinter file dialog [duplicate]
        Website: Stack Overflow
        URL: https://stackoverflow.com/questions/35483700/python-how-to-get-the-filename-in-tkinter-file-dialog
        Author: Kevin
        Date Posted: 18 February 2016
        Date Referred: 27 May 2020
        '''
        #get the name of the video file (without the path), and use as the button label
        buttonName = os.path.basename(video_arr[i])

        #create the button
        buttonVideo = tk.Button(canvas, text=buttonName)

        '''
        Title: Python tkinter find which button is clicked
        Website: Stack Overflow
        URL: https://stackoverflow.com/questions/47295740/python-tkinter-find-which-button-is-clicked
        Author: Bryan Oakley
        Date Posted: 14 November 2017
        Date Referred: 11 May 2020
        '''
        #call the passName button once the button is clicked
        buttonVideo.configure(command=lambda button=buttonVideo: passName(button))
        
        #add the buttons to the canvas
        canvas.create_window(0, i*50, anchor='nw', window=buttonVideo, height=50, width=1350)
    

    # display buttons in the canvas
    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set)
    
    
    '''
    Title: Does grid() has a fill attribute like pack() in tkinter?
    Website: Stack Overflow
    URL: https://stackoverflow.com/questions/52472105/does-grid-has-a-fill-attribute-like-pack-in-tkinter
    Author: Bryan Oakley
    Date Posted: 24 September 2018
    Date Referred: 26 May 2020
    '''
    canvas.grid(sticky="nsew")
    scrolly.grid(sticky="nse",row=3, column=2)


