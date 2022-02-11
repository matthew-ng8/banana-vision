## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2015-2017 Intel Corporation. All Rights Reserved.

###############################################
##      Open CV and Numpy integration        ##
###############################################

import pyrealsense2 as rs
import numpy as np
import cv2

'''
Displays 6 9x9 submatrices of the RGB and XYZ 
User inputs the central X and Y coordinate for the image
depth_colormap_dim : tuple of (xDimension, yDimension, numLayers)
                        this is assuming the color_image and 
                        depth_image are the same size
color_image        : a numpy array of (xDimension, yDimension, 3) with RGB layers 
depth_image        : a numpy array of (xDimension, yDimension, 3) with XYZ layers 
'''
def display9x9(depth_colormap_dim, color_image, depth_frame):
    # depth_colormap_dim = (500, 500, 3) # was here for testing 
    xMat = np.zeros(shape = depth_colormap_dim)
    yMat = np.zeros(shape = depth_colormap_dim)
    zMat = np.zeros(shape = depth_colormap_dim)
    for i in range (0, depth_colormap_dim[0]):
            for j in range (0, depth_colormap_dim[1]):
                    depth = depth_frame.get_distance(j,i)
                    depth_intrin = depth_frame.profile.as_video_stream_profile().intrinsics
                    depth_point = rs.rs2_deproject_pixel_to_point(depth_intrin, [j, i], depth)
                    xMat[i][j] = depth_point[0]
                    yMat[i][j] = depth_point[1]
                    zMat[i][j] = depth_point[2]


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

    xImage = xMat
    yImage = yMat
    zImage = zMat

    for j in range(yCenterPixel - 4, yCenterPixel +5):
        for i in range(xCenterPixel - 4, xCenterPixel +5):
            print("(" + str(i) + "," + str(j) + ")  ", end = "")
        print("\n")


    print("Red Channel")
    for j in range(yCenterPixel - 4, yCenterPixel +5):
        for i in range(xCenterPixel - 4, xCenterPixel +5):
            print("%3d" % redImage[i][j], end = "")
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
            print("%3.3f " % xImage[i][j][0], end = "")
        print("\n")

    print("Y Depth Channel")
    for j in range(yCenterPixel - 4, yCenterPixel +5):
        for i in range(xCenterPixel - 4, xCenterPixel +5):
            print("%3.3f " % yImage[i][j][0], end = "")
        print("\n")

    print("Z Depth Channel")
    for j in range(yCenterPixel - 4, yCenterPixel +5):
        for i in range(xCenterPixel - 4, xCenterPixel +5):
            print("%3.3f " % zImage[i][j][0], end = "")
        print("\n")

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
align_to = rs.stream.color
align = rs.align(align_to)
test = 0
# Get device product line for setting a supporting resolution
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))

found_rgb = False
for s in device.sensors:
    if s.get_info(rs.camera_info.name) == 'RGB Camera':
        found_rgb = True
        break
if not found_rgb:
    print("The demo requires Depth camera with Color sensor")
    exit(0)

config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

if device_product_line == 'L500':
    config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
else:
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)
thres = 0.55 # Threshold to detect object
classNames= []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
 
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'
 
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
try:
    while True:

        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        aligned_frames = align.process(frames)
        depth_frame = aligned_frames.get_depth_frame()
        color_frame = aligned_frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
        

        depth_colormap_dim = depth_colormap.shape
        color_colormap_dim = color_image.shape

        
        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha = 0.03), cv2.COLORMAP_JET)
        img = color_image
        classIds, confs, bbox = net.detect(img,confThreshold=thres)
        print(classIds,bbox)
        if len(classIds) != 0:
            for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
                cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        # Show images
        
        if test < 2:
            display9x9(depth_colormap_dim,color_image, depth_frame)
            test = test + 1
        images = np.hstack((color_image, depth_colormap))
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
        cv2.waitKey(1)

finally:

    # Stop streaming
    pipeline.stop()
