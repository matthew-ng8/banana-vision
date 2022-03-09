import numpy as np

def getQuadrant6(x,y) :
    #determine x coordinate quadrant
    if(x <= 213 and x >= 0) :
        x_dir = "left"
    elif(x > 213 and x <= 426) :
        x_dir = "middle"
    elif(x > 426 and x <= 640) :
        x_dir = "right"

    #determing y coordinate quadrant
    if(y <= 240 and y >= 0) :
        y_dir = "top"
    elif(x > 240 and x <= 480) :
        y_dir = "bottom"

    return x_dir, y_dir

def getQuadrant4(x,y) :
    #determine x coordinate quadrant
    if(x <= 320 and x >= 0) :
        x_dir = "left"
    elif(x > 320 and x <= 640) :
        x_dir = "right"

    #determing y coordinate quadrant
    if(y <= 240 and y >= 0) :
        y_dir = "top"
    elif(x > 240 and x <= 480) :
        y_dir = "bottom"

    return x_dir, y_dir

def getQuadrant3(x) :
    #determine x coordinate quadrant
    if(x <= 213 and x >= 0) :
        x_dir = "left"
    elif(x > 213 and x <= 426) :
        x_dir = "middle"
    elif(x > 426 and x <= 640) :
        x_dir = "right"

    return x_dir

def testSurface(depth_frame) :
    arraySurface = np.zeros(10)
    for i in range (0,320):
        for j in range (0, 480):
            depth = depth_frame.get_distance(j,i)
            if (depth >= 0 and depth <= 0.1):
                arraySurface[0]+=1
            if (depth >= 0.11 and depth <= 0.20):
                arraySurface[1]+=1
            if (depth >= 0.21 and depth <= 0.3):
                arraySurface[2]+=1
            if (depth >= 0.31 and depth <= 0.4):
                arraySurface[3]+=1
            if (depth >= 0.41 and depth <= 0.5):
                arraySurface[4]+=1
            if (depth >= 0.51 and depth <= 0.6):
                arraySurface[5]+=1
            if (depth >= 0.61 and depth <= 0.7):
                arraySurface[6]+=1
            if (depth >= 0.71 and depth <= 0.8):
                arraySurface[7]+=1
            if (depth >= 0.81 and depth <= 0.9):
                arraySurface[8]+=1
            if (depth >= 0.91 and depth <= 1):
                arraySurface[9]+=1
    leftSurface = 0
    for i in range (0, 10):
        if(arraySurface[i]>=38400):
            leftSurface = 1
            #there is a surface (left side wall) 
            break

    arraySurface = np.zeros(10)
    for i in range (320,640):
        for j in range (0, 480):
            depth = depth_frame.get_distance(j,i)
            if (depth >= 0 and depth <= 0.1):
                arraySurface[0]+=1
            if (depth >= 0.11 and depth <= 0.20):
                arraySurface[1]+=1
            if (depth >= 0.21 and depth <= 0.3):
                arraySurface[2]+=1
            if (depth >= 0.31 and depth <= 0.4):
                arraySurface[3]+=1
            if (depth >= 0.41 and depth <= 0.5):
                arraySurface[4]+=1
            if (depth >= 0.51 and depth <= 0.6):
                arraySurface[5]+=1
            if (depth >= 0.61 and depth <= 0.7):
                arraySurface[6]+=1
            if (depth >= 0.71 and depth <= 0.8):
                arraySurface[7]+=1
            if (depth >= 0.81 and depth <= 0.9):
                arraySurface[8]+=1
            if (depth >= 0.91 and depth <= 1):
                arraySurface[9]+=1

    rightSurface = 0
    for i in range (0, 10):
        if(arraySurface[i]>=38400):
            rightSurface = 1
            #there is a surface (right side wall) 
            break
    centerSurface = 0
    if(rightSurface and leftSurface):
        centerSurface = 1
        rightSurface = 0
        leftSurface = 0
        #there is a surface (centered in front) 

    #print statement for right/left/center surface
    #if(rightSurface):
        #TTS print right surface
    #elif(leftSurface):
        #TTS print left surface
    #elif(centerSurface):
        #TTS print center surface