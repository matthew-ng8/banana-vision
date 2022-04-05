import numpy as np

def testSurface(depth_frame) :

    #middle section of the depth image
    arraySurface = 0
    #parsing through the data to create the histogram
    for i in range (0, 3):
        for j in range (0, 3):
            depth = depth_frame.get_distance(i*64,j*48)
            if (depth >= 0 and depth <= 1):
                arraySurface = arraySurface + 1
                
    MiddleSurface = 0
    if(arraySurface>=9):
        MiddleSurface = 1
    
    Output = "NONE"
    if(MiddleSurface == 1):
        Output = "wall"
    return Output    
        #there is a surface (centered in front) 
    
    #print statement for right/left/center surface
    #if(rightSurface):
        #TTS print right surface
    #elif(leftSurface):
        #TTS print left surface
    #elif(centerSurface):
        #TTS print center surface