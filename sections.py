import numpy as np

def getSection6(x,y) :
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

def getSection4(x,y) :
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

def getSection3(x) :
    #determine x coordinate quadrant
    if(x <= 213 and x >= 0) :
        x_dir = "left"
    elif(x > 213 and x <= 426) :
        x_dir = "middle"
    elif(x > 426 and x <= 640) :
        x_dir = "right"

    return x_dir
