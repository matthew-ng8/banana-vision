'''
ESE 440 
Property of Banana Vision 
Last edited 2/26/2022
'''

from time import struct_time


class frame_data:
	'''
	center is passed in as a tuple of (x, y)
	percentError is for checking the depths of frames within Tolerance level
	maxFrames is the maximum amount of frames frame_data can hold onto
	centerTolerance is the tolerance level to match the center value to the previous center
	'''
	def __init__(self, center, percentError, maxFrames, centerTolerance=10):
		self.frames=[]
		self.center = center
		self.percentError = percentError
		self.maxFrames = maxFrames
		self.centerTolerance = centerTolerance


	def getCenter(self):
		return self.center
	def setCenter(self, newCenter):
		self.center = newCenter
	# def timeCheck(self):
	# 	return lifeSpan <= (struct_time - self.creationTime)
	'''
	Compares the center tuple we have to the new center. 
	returns true if simlar(with in threshold) false if not
	'''
	def similarCenter(self, newCenter):
		newX = newCenter[0]
		newY = newCenter[1]
		x = self.center[0]
		y = self.center[1]
		if newX <= x+self.centerTolerance and newX >= x-self.centerTolerance:
			if newY <= y+self.centerTolerance and newY >= y-self.centerTolerance:
				return True
		return False

		return sameObject
	def hasMaxFrames(self):
		return len(self.frames) == self.maxFrames
	def getFrames(self): 
		return self.frames
	'''
	addds a new depth for a frame at the end
	returns true or false depending on if adding a new depth has put us at max frames
	'''
	def addFrame(self, depth):
		if not self.hasMaxFrames():
			self.frames.append(depth)
		else:
			print("Unable to add another frame as there are max frames")
			#should we throw an exception or smth here? 
		return self.hasMaxFrames()
	def printFrames(self):
		print(self.frames)
	'''
	Checks through all the frames to make sure that the depths of the last frames are 
	all within the tolerance of the first frame received. 
	if there is one that is not within the tolerancec, return False
	TODO: is the percent error better vs a static set tolerance level?
	'''
	def checkDepths(self):
		if len(self.frames) == 0:
			return False
		tolerance = self.percentError*self.frames[0]
		initialDepth = self.frames[0]
		sameObject = True
		for depth in self.frames:
			if depth >= tolerance+initialDepth or depth <= initialDepth-tolerance:
				sameObject = False
				break

		return sameObject