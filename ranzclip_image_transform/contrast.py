import cv2
import numpy as np
import os

def nothing(x):
    pass

img = cv2.imread('image\\'+os.listdir('image')[0])
img = cv2.resize(img,dsize=(600,600))

cv2.namedWindow('image')

cv2.createTrackbar('alpha', 'image', 0, 500, nothing)
switch = '0:OFF\n1:On'
cv2.createTrackbar(switch, 'image', 1, 1, nothing)

out = img.copy()

while(1):
    cv2.imshow('image', out)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

    alpha = cv2.getTrackbarPos('alpha','image')/100
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        out = img.copy()
    else:
        out = np.clip(((1 + alpha) * img - 128 * alpha), 0, 255).astype(np.uint8)
