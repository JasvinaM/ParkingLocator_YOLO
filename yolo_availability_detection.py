# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:16:23 2020

@author: JM Ealn Davan
"""

'''
Title: YOLO object detection with OpenCV
Website: pyimagesearch
URL: https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/
Author: Adrian Rosebrock 
Date Posted: 12 November 2018
Date Referred: 07 May 2020
'''

import numpy as np
import argparse
import imutils
import time
import cv2
import os

'''
Title: Measure time elapsed in Python
Website: StackOverflow
URL: https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python
Author: NPE
Date Posted: 10 September 2011
Date Referred: 26 March 2020
'''
# to measure the time taken to run the YOLO object detection algorithm
import time

# to name the processed/ output filename with the current datetime
from datetime import datetime

'''
Run the YOLO object detection algorithm on the desired video 

@param video_name: the path name/ directory of the video file to be processed
@param capacity: the total number of cars that the parking lot can accommodate
@return lot_area: to label the output file with the parking lot area ID
'''
def yolo_detection(video_name, capacity, lot_area): 
    
    '''
    Title: Example 3: Get the current date and time
    Website: Programiz
    URL: https://www.programiz.com/python-programming/datetime/current-datetime
    Author: -
    Date Posted: -
    Date Referred: 24 May 2020
    '''

    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y(%H-%M-%S)")
    
    #convert string to int
    capacity = int(capacity) 
    
    #start time of the program
    startTime = time.time()


    # construct the argument parse and parse the arguments  
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detections")
    ap.add_argument("-t", "--threshold", type=float, default=0.3, help="threshold when applying non-maxima suppression")
    args = vars(ap.parse_args())
    
    # load the COCO class labels that the YOLO model was trained on
    labelsPath = os.path.sep.join(["yolo-coco", "coco.names"])
    LABELS = open(labelsPath).read().strip().split("\n")
    
    # initialize a list of colors to represent each possible class label
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
    
    # derive the paths to the YOLO weights and model configuration
    weightsPath = os.path.sep.join(["yolo-coco", "yolov3.weights"])
    configPath = os.path.sep.join(["yolo-coco", "yolov3.cfg"])
    
    # load the YOLO object detector trained on COCO dataset (80 classes)
    # and determine only the *output* layer names that we need from YOLO
    print("[INFO] loading YOLO from disk...")
    
    
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    
    # initialize the video stream, pointer to output video file, and frame dimensions
    vs = cv2.VideoCapture(video_name)
    writer = None
    (W, H) = (None, None)
    
    # try to determine the total number of frames in the video file
    try:
        prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() \
    		else cv2.CAP_PROP_FRAME_COUNT
        total = int(vs.get(prop))
        print("[INFO] {} total frames in video".format(total))
        
    # an error occurred while trying to determine the total number of frames in the video file
    except:
        print("[INFO] could not determine # of frames in video")
        print("[INFO] no approx. completion time can be provided")
        total = -1
        
    
    # loop over frames from the video file stream
    while True:
    	# read the next frame from the file
        (grabbed, frame) = vs.read()
        
    	# if the frame was not grabbed, then we have reached the end of the stream
        if not grabbed:
            break
        
    	# if the frame dimensions are empty, grab them
        if W is None or H is None:
            (H, W) = frame.shape[:2]
            
    	# construct a blob from the input frame and then perform a forward pass of the YOLO object detector,
    	# giving us our bounding boxes and associated probabilities
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        start = time.time()
        layerOutputs = net.forward(ln)
        end = time.time()
        
        # initialize our lists of detected bounding boxes, confidences, and class IDs, respectively
        boxes = []
        confidences = []
        classIDs = []
        
        # loop over each of the layer outputs
        for output in layerOutputs:
            
            # loop over each of the detections
            for detection in output:
                
                # extract the class ID and confidence (i.e., probability) of the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
                
                # filter out weak predictions by ensuring the detected
                # probability is greater than the minimum probability
                if confidence > args["confidence"]:
                    
                    # scale the bounding box coordinates back relative to
                    # the size of the image, keeping in mind that YOLO
                    # actually returns the center (x, y)-coordinates of
                    # the bounding box followed by the boxes' width and height
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
                    
                    # use the center (x, y)-coordinates to derive the top
                    # and and left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    # update our list of bounding box coordinates,
                    # confidences, and class IDs
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)
                    
        # apply non-maxima suppression to suppress weak, overlapping bounding boxes
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"],	args["threshold"])
        
        # ensure at least one detection exists
        if len(idxs) > 0:
            
            #loop over indexes to place the availability of the car and truck in the video
            for i in idxs.flatten():
                #count the number of cars in the frame
                count_cars = 0
                
                # loop over the indexes we are keeping
                for i in idxs.flatten():
                    
                    if LABELS[classIDs[i]] == "car" or LABELS[classIDs[i]] == "truck" :
                        count_cars = count_cars+1
                    
                    #get total parking lots by user
                    total = capacity 
                    
                    #get the number of empty parking spaces
                    available = total - len(idxs)
                
        			# extract the bounding box coordinates
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])
        			# draw a bounding box rectangle and label on the frame
                    color = [int(c) for c in COLORS[classIDs[i]]]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
                    cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                
                
                available = total - count_cars
                
                '''
                Title: Python OpenCV | cv2.rectangle() method
                Website: GeeksforGeeks
                URL: https://www.geeksforgeeks.org/python-opencv-cv2-rectangle-method/
                Author: Rajnis09
                Date Posted: -
                Date Referred: 28 May 2020
                '''
                rectangle_start_point = (30, 50) 
                rectangle_end_point = (270, 150) 
                rectangle_color = (255, 255, 255) 
                rectangle_thickness = -1
                cv2.rectangle(frame, rectangle_start_point, rectangle_end_point, rectangle_color, rectangle_thickness) 
                 
                cv2.putText(frame, "Available: %d spots" %available, (30, 95),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 0, 127), 2)

                cv2.putText(frame, "Total: %d spots" %total, (30, 125),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 0, 127), 2)
                

    	# check if the video writer is None
        if writer is None:
            
    		# initialize our video writer
            #output files are kept as .avi extension to show the difference between input and output video files
            filename = "output/" + "Lot_Area_" + lot_area+ "_" +dt_string + ".avi"        
            fourcc = cv2.VideoWriter_fourcc(*"MJPG")
            writer = cv2.VideoWriter(filename, fourcc, 30, (frame.shape[1], frame.shape[0]), True)
    		
            # some information on processing single frame
            if total > 0:
                elap = (end - start)
                print("[INFO] single frame took {:.4f} seconds".format(elap))
                print("[INFO] estimated total time to finish: {:.4f}".format(
    				elap * total))
    	
        # write the output frame to disk
        writer.write(frame)
    
    # release the file pointers
    print("[INFO] cleaning up...")
    print("[INFO] done! ")
    writer.release()
    vs.release()
    
    #end time of the program
    endTime = time.time()
    
    #get the time taken for the detection process to run in seconds and minutes
    print("Time taken (seconds) = ", endTime - startTime) 
    print("Time taken (minutes) = ", (endTime - startTime) / 60) 

