import sys
import numpy as np
from tkinter import *
del globals()["Image"]
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

inputImageName = sys.argv[1] 
outputImageName = sys.argv[2]
inputArray = np.array(Image.open(inputImageName))

root = Tk()
points = [[0,0], [0,0], [0,0], [0,0]]
count = 0
upperLeftPoint = [0,0]
upperRightPoint = [0,0]
lowerLeftPoint = [0,0]
lowerRightPoint = [0,0]

def callback(event):
    global count
    print(event.x, event.y)
    points[count][0] = event.x
    points[count][1] = event.y
    count += 1
    if(count == 4):
        root.destroy()

def swapPositions(lst, pos1, pos2): 
    first_ele = lst.pop(pos1)    
    second_ele = lst.pop(pos2-1)  
    lst.insert(pos1, second_ele)   
    lst.insert(pos2, first_ele)        
    return lst

def sortPoints(points):
    global upperLeftPoint 
    global upperRightPoint 
    global lowerLeftPoint 
    global lowerRightPoint 
    for i in range(len(points) - 1):
        if(points[i][1] > points[3][1]):
            points = swapPositions(points, i, 3)
    for i in range(len(points) - 2):
        if(points[i][1] > points[2][1]):
            points = swapPositions(points, i, 2)
    if(points[0][0] > points[1][0]):
        points = swapPositions(points, 0, 1)
    if(points[2][0] > points[3][0]):
        points = swapPositions(points, 2, 3)
    upperLeftPoint = points[0]
    upperRightPoint = points[1]
    lowerLeftPoint = points[2]
    lowerRightPoint = points[3]
      
frame = Frame(root, bd=2, relief=SUNKEN)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
xscroll = Scrollbar(frame, orient=HORIZONTAL)
xscroll.grid(row=1, column=0, sticky=E+W)
yscroll = Scrollbar(frame)
yscroll.grid(row=0, column=1, sticky=N+S)
canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
xscroll.config(command=canvas.xview)
yscroll.config(command=canvas.yview)
frame.pack(fill=BOTH,expand=1)
img = ImageTk.PhotoImage(Image.open(inputImageName))
canvas.create_image(0,0,image=img,anchor="nw")
canvas.config(scrollregion=canvas.bbox(ALL))
canvas.bind("<Button-1>", callback)
root.mainloop()

sortPoints(points)
x1 = upperLeftPoint[0]
y1 = upperLeftPoint[1]
x2 = upperRightPoint[0]
y2 = upperRightPoint[1]
x3 = lowerLeftPoint[0]
y3 = lowerLeftPoint[1]
x4 = lowerRightPoint[0]
y4 = lowerRightPoint[1]
print(x1, y1, x2, y2, x3, y3, x4, y4)
x1after = 0
y1after = 0
x2after = 999
y2after = 0
x3after = 0
y3after = 999
x4after = 999
y4after = 999

A = np.array([[x1,y1,1,0,0,0,0,0],
    [0,0,0,x1,y1,1,0,0],
    [0,0,0,0,0,0,x1,y1],
    [x2,y2,1,0,0,0,0,0],
    [0,0,0,x2,y2,1,0,0],
    [0,0,0,0,0,0,x2,y2],
    [x3,y3,1,0,0,0,0,0],
    [0,0,0,x3,y3,1,0,0],
    [0,0,0,0,0,0,x3,y3],
    [x3,y3,1,0,0,0,0,0],
    [0,0,0,x3,y3,1,0,0],
    [0,0,0,0,0,0,x3,y3]], dtype = float)

B = np.array([[x1after],
              [y1after],
              [0],
              [x2after],
              [y2after],
              [0],
              [x3after],
              [y3after],
              [0],
              [x4after],
              [y4after],
              [0]], dtype = float)

x = np.linalg.lstsq(A, B, rcond = None)
a1 , a2, a3, a4, a5, a6, a7, a8 = x[0][0][0], x[0][1], x[0][2], x[0][3], x[0][4], x[0][5],  x[0][6], x[0][7]
T = [[a1,a2,a3],
     [a4,a5,a6],
     [a7,a8,1]]    

print("",a1,a2)    

