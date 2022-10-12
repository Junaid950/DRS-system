import tkinter
from tkinter import *
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading#for multli threading in python coding
import imutils
import time
def play(speed):
    print(f"You clicked on play.Speed is{speed}")
def pending(decision):
    # 1.Displaying the decesion panding image 
    frame = cv2.cvtColor(cv2.imread("C:/Users/dell/Desktop/home/project/Decesion pending.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame 
    canvas.create_image (0,0,image = frame,anchor = tkinter.NW)
    time.sleep(1)#wait for 1 second
    #For sponsered image
    frame = cv2.cvtColor(cv2.imread("C:/Users/dell/Desktop/home/project/MRF.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame 
    canvas.create_image (0,0,image = frame,anchor = tkinter.NW)
    time.sleep(1.5)
    frame = cv2.cvtColor(cv2.imread("C:/Users/dell/Desktop/home/project/MRF.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame 
    canvas.create_image (0,0,image = frame,anchor = tkinter.NW)
    #for out/not out
    if decesion == "out":
        frame = cv2.cvtColor(cv2.imread("C:/Users/dell/Desktop/home/project/out.jpg"),cv2.COLOR_BGR2RGB)

        #DecesionImg= "C:/User/dell/Desktop/home/project/out.jpg"
    else:
        #DecesionImg = "C:/Users/dell/Desktop/home/project/Not out.jpg"
        frame = cv2.cvtColor(cv2.imread("C:/Users/dell/Desktop/home/project/Not out.jpg"),cv2.COLOR_BGR2RGB)

    frame = cv2.cvtColor(cv2.imread(DecesionImg),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame 
    canvas.create_image (0,0,image = frame,anchor = tkinter.NW)
    
def out():
    thread = threading.Thread(target= pending,args= ("out",))
    thread.daemon = 1
    thread.start()
    print("player is out")
def not_out():
    thread = threading.Thread(target= pending,args= ("not out",))
    thread.daemon = 1
    thread.start()
    print("player is not out")
#Tk.canvas
#width and height of the main screen
SET_WIDTH = 650
SET_HEIGHT = 368 
#thinkter GUI starts from here
window = tkinter.Tk()
window.title("code with JOJO the thired umpire Decesion reveiw kit")
cv_img = cv2.cvtColor(cv2.imread('C:/Users/dell/Desktop/home/project/junaid.jpg'),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width = SET_WIDTH,height = SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho = tkinter.NW,image=photo)
canvas.pack()
#Buttons to control playback
btn = tkinter.Button(window,text="<<Previous (Fast)",width = 50,command = partial(play, -25))
btn.pack()
btn = tkinter.Button(window,text="<<Previous (Slow)",width = 50,command = partial(play, -2))
btn.pack()
btn = tkinter.Button(window,text="Next (slow)>>",width = 50,command = partial(play, 2))
btn.pack()
btn = tkinter.Button(window,text="Next (Fast)>>",width = 50,command = partial(play, 25))
btn.pack()
btn = tkinter.Button(window,text="Give out",width = 50,command = out)
btn.pack()
btn = tkinter.Button(window,text="Give not out",width = 50,command = not_out)
btn.pack()
window.mainloop()
