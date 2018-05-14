# Folder: Images/1/ and Images/2
#

from PIL import Image, ImageTk
import os
import glob
import ImageChops
import math, operator

print 'Remove Duplicate Images'

# initialize global variable
imageDir1 = ''
imageList1 = []
imageDir2=''
imageList2= []
removeList=[]
count=0
    
# load file
imageDir1 = os.path.join(r'./Images/1/')
imageList1 = glob.glob(os.path.join(imageDir1, '*.*'))
print 'Load %d images from 1' % (len(imageList1))
imageDir2 = os.path.join(r'./Images/2/')
imageList2 = glob.glob(os.path.join(imageDir2, '*.*'))
print 'Load %d images from 2' % (len(imageList2))
if (len(imageList1) == 0) or (len(imageList2) == 0):
    print 'No images found in the specified dir!'
    exit()


for imagepath1 in imageList1:
	img1 = Image.open(imagepath1)
	print 'Image 1: %s' %(imagepath1)

	for imagepath2 in imageList2:
		count=0
		img2 = Image.open(imagepath2)
		print '\tImage 2: %s' %(imagepath2)
		h = ImageChops.difference(img1, img2).histogram()
		for element in h:
			if element != 0:
				count+=1
		diff = (count/len(h))*100
		print '\t\tDifference: %f' %diff
		if diff < 10:
			removeList.append(imagepath2)

# remove
print 'Remove list:'
print removeList
for rm in removeList:
	os.remove(rm)
print 'Removed Duplicate Image!'