import cv2
import numpy as np
import os

def onChange(k):
    #t = (k*5,k*5,k*5)
    #array=np.full(img.shape,t,dtype=np.uint8)
    #dst=cv2.add(img,array)
    #cv2.imshow('after',dst)

    dst = img.copy()
    dst=dst.astype(np.float)
    dst = ((dst/255)**(k/100))*255
    dst=dst.astype(np.uint8)

    cv2.imshow('after',dst)

    
 
img = cv2.imread('image\\'+os.listdir('image')[0])
img = cv2.resize(img,dsize=(600,600))
cv2.imshow('before',img)

cv2.createTrackbar('level','before',0,1000,onChange)

cv2.waitKey()
cv2.destroyAllWindows()
