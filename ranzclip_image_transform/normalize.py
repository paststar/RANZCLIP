#-*- coding: utf-8 -*-
import cv2
import numpy as np
import os

def nothing(x):
    pass

img = cv2.imread('image\\'+os.listdir('image')[0])
img = cv2.resize(img,dsize=(600,600))

cv2.namedWindow('image')


cv2.createTrackbar('mean', 'image', 0, 1000, nothing)
cv2.createTrackbar('std', 'image', 0, 100, nothing)

switch = '0:OFF\n1:On'
cv2.createTrackbar(switch, 'image', 1, 1, nothing)

out = img.copy()
while(1):
    cv2.imshow('image', out)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    mean = cv2.getTrackbarPos('mean','image')
    std = cv2.getTrackbarPos('std', 'image')
    s = cv2.getTrackbarPos(switch, 'image')


    if s == 0:
        out = img.copy()
    else:
        for i in range(3):
            out[:,:,i] = (((img[:,:,i] - mean/10)/(std/10))).astype(np.uint8)


        out=out.astype(np.uint8)

cv2.destroyAllWindows()
