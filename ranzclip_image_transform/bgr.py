import cv2
import numpy as np
import os

def nothing(x):
    pass
img = cv2.imread('image\\'+os.listdir('image')[0])
img = cv2.resize(img,dsize=(600,600))
cv2.namedWindow('image')

cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

switch = '0:OFF\n1:On'
cv2.createTrackbar(switch, 'image', 1, 1, nothing)

out = img.copy()
while(1):
    cv2.imshow('image', out)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        out = img.copy()
    else:
        out = img.copy()
        out[:,:,0] = img[:,:,0] * (b/255)
        out[:,:,1] = img[:,:,1] * (g/255)
        out[:,:,2] = img[:,:,2] * (r/255)

        out=out.astype(np.uint8)
cv2.destroyAllWindows()