#This script will generat gui with 4 buttons :
# Take new photo , Open exisit photo , Track face and Close
# It will process the images to detect eyes and faces also track face movment. 
#Adapted and moodified from https://github.com/opencv/opencv/tree/master/samples/python 
#Sami 

import tkinter as tk # import tkinter instance
from tkinter import *
import numpy as np
import cv2
import os 
from tkinter.filedialog import askopenfilename



#######
#This is importing the face tracking script 
def t():
	import t.py
	f.App()

########

    #These datasets are crucial to detect eyes and faces 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def close(): #This function to exit when Close button pressed
	exit()

def file(): #This function to choose an image from computer files.

	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
	return filename
    


######################
def open(): # This function for opening an image from the computer 

	img=cv2.imread(file())

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	    eyes = eye_cascade.detectMultiScale(roi_gray)
	    for (ex,ey,ew,eh) in eyes:
	        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imshow('img',img)
	cv2.waitKey(5000)
	cv2.destroyAllWindows()
######################
def newshot(): #This function for capturing new photo using the webcam 


	img = cv2.VideoCapture(0)

	video_capture = cv2.VideoCapture(0)
	# Check success
	cv2.waitKey(1000)
	if not video_capture.isOpened():
	    raise Exception("Could not open video device")
	# Read picture. ret === True on success
	ret, frame = video_capture.read()
	print(frame)
	cv2.imwrite('./anImage.jpg',frame) #The photo will be saved in the project directory named anImage.jpg
	# Close device
	video_capture.release()
	# We need this photo to go bellow 
	img=cv2.imread('anImage.jpg') 

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	    eyes = eye_cascade.detectMultiScale(roi_gray)
	    for (ex,ey,ew,eh) in eyes:
	        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imshow('img',img)
	cv2.waitKey(5000)
	cv2.destroyAllWindows()
    
 
######################
#GUI 
window = tk.Tk() # create tkinter window frame

window.title("Face Detection")# write window title

# configure frame size
window.rowconfigure(1, minsize=350, weight=1)
window.columnconfigure(1, minsize=400, weight=1)

# create buttons
fr_buttons = tk.Frame(window, relief=tk.RAISED , bd=1)
# fr_buttonsC = tk.Frame(window, relief=tk.RAISED , bd=1)
# fr_buttonsT = tk.Frame(window, relief=tk.RAISED , bd=1)

btn1 = tk.Button(fr_buttons, text="Take New Photo", command=newshot)
btn2 = tk.Button(fr_buttons, text="Open Photo", command=open)
btn3 = tk.Button(fr_buttons, text="Track face", command=t)
btn4 = tk.Button(fr_buttons, text="Close", command=close)





# Append widgets into frame
btn1.grid(row=2, column=1)
btn2.grid(row=2, column=2)
btn3.grid(row=2, column=3)
btn4.grid(row=2, column=4)

fr_buttons.grid(row=1, column=1)



#Keep the window
window.mainloop()
