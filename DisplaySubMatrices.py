'''
Displays 6 9x9 submatrices of the RGB and XYZ 
User inputs the central X and Y coordinate for the image

depth_colormap_dim : tuple of (xDimension, yDimension, numLayers)
                        this is assuming the color_image and 
                        depth_image are the same size
color_image        : a numpy array of (xDimension, yDimension, 3) with RGB layers 
depth_image        : a numpy array of (xDimension, yDimension, 3) with XYZ layers 
'''
def display9x9(depth_colormap_dim, color_image, depth_image):
    # depth_colormap_dim = (500, 500, 3) # was here for testing 
    xLength = depth_colormap_dim[0]
    yLength = depth_colormap_dim[1]

    print("Frame Dimensions are: (" + str(xLength) + ", " + str(yLength) + ")")

    xCenterPixel = int(input("Please enter center X-Coord: "))
    yCenterPixel = int(input("Please enter center Y-Coord: "))
    print(str(xCenterPixel))
    print(str(yCenterPixel))

    # xCenterPixel = 100                  #also for testing
    # yCenterPixel = 200
    # color_image = numpy.full((xLength, yLength, 3), 100)
    # depth_image = numpy.full((xLength, yLength, 3), 100)

    redImage = color_image[:,:,0]
    greenImage = color_image[:,:,1]
    blueImage = color_image[:,:,2]

    xImage = depth_image[:,:,0]
    yImage = depth_image[:,:,1]
    zImage = depth_image[:,:,2]

    for j in range(yCenterPixel - 4, yCenterPixel +5):
        for i in range(xCenterPixel - 4, xCenterPixel +5):
            print("(" + str(i) + "," + str(j) + ")  ", end = "")
        print("\n")


    print("Red Channel")
    for j in range(yCenterPixel - 4, yCenterPixel +5):
        for i in range(xCenterPixel - 4, xCenterPixel +5):
            print("%3d " % redImage[i][j], end = "")
        print("\n")

    print("Green Channel")
    for j in range(yCenterPixel - 4, yCenterPixel +5):
        for i in range(xCenterPixel - 4, xCenterPixel +5):
            print("%3d " % greenImage[i][j], end = "")
        print("\n")

    print("Blue Channel")
    for j in range(yCenterPixel - 4, yCenterPixel +5):
        for i in range(xCenterPixel - 4, xCenterPixel +5):
            print("%3d " % redImage[i][j], end = "")
        print("\n")

    print("X Depth Channel")
    for j in range(yCenterPixel - 4, yCenterPixel +5):
        for i in range(xCenterPixel - 4, xCenterPixel +5):
            print("%3d " % xImage[i][j], end = "")
        print("\n")

    print("Y Depth Channel")
    for j in range(yCenterPixel - 4, yCenterPixel +5):
        for i in range(xCenterPixel - 4, xCenterPixel +5):
            print("%3d " % yImage[i][j], end = "")
        print("\n")

    print("Z Depth Channel")
    for j in range(yCenterPixel - 4, yCenterPixel +5):
        for i in range(xCenterPixel - 4, xCenterPixel +5):
            print("%3d " % zImage[i][j], end = "")
        print("\n")
