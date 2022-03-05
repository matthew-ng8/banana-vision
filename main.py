from ast import List
from pickle import NONE
import cv2
import pyrealsense2 as rs
import numpy as np
import time

from frame_data import frame_data


#dictionary to hold objects
objectDictionary = {}
creationTime= time.time()
lifeSpan = 30
MAX_FRAMES = 5
DEPTH_TOLERANCE = .20
CENTER_TOLERANCE = 3

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
count = 0
try:
    while True:
        time1 = time.time_ns()
        
        # if count%5 ==0:
        #     print(time1)
        count = count+1
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

        if len(classIds) != 0:
            for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
                cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                x = (int) ((box[2] + (box[0])) /2)
                y = (int) ((box[3] + (box[1])) /2)
                depth = depth_frame.get_distance(x,y)
                if (lifeSpan <= (time.time() - creationTime)):
                    objectDictionary.clear()
                    creationTime = time.time()
                if (objectDictionary.get(classNames[classId-1]) == None):
                    objectDictionary.update({classNames[classId-1]: [] })
                    dataList = objectDictionary.get(classNames[classId-1])
                    dataList.append(frame_data((x,y), DEPTH_TOLERANCE, MAX_FRAMES))
                else:
                    dataList = objectDictionary.get(classNames[classId-1])
                    isAdded = False
                    for index in dataList:
                        if (index.similarCenter((x,y))):
                            if (index.addFrame(depth)): #addFrame returns true if at max frames
                                if (index.checkDepths()):
                                    print(classNames[classId-1])    
                                dataList.remove(index)    
                            else:
                                index.setCenter((x,y))
                                isAdded = True
                            break
                    if (not isAdded):
                        dataList.append(frame_data((x,y), DEPTH_TOLERANCE, MAX_FRAMES))
                            

                
                
        
        # if test < 2:
        #     display9x9(depth_colormap_dim,color_image, depth_frame)
        #     test = test + 1
        images = np.hstack((color_image, depth_colormap))
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
        cv2.waitKey(1)

finally:

    # Stop streaming
    pipeline.stop()