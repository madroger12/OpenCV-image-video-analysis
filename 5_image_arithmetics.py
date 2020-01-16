# simple addition

'''
import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('5img.png')
img2 = cv2.imread('5img2.png')

add = img1+img2

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# add images, and have each carry a different "weight"

'''
import cv2
import numpy as np

img1 = cv2.imread('5img.png')
img2 = cv2.imread('5img2.png')

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

################################################

import cv2
import numpy as np

# Load two images
img1 = cv2.imread('5img.png')
img2 = cv2.imread('python.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()