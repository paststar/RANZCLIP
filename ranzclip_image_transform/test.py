import cv2
import numpy as np
import os

img = cv2.imread('image\\'+os.listdir('image')[0])
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img,dsize=(600,600))

mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]

max_pixel_value=255
mean = np.array(mean, dtype=np.float32)
mean *= max_pixel_value

std = np.array(std, dtype=np.float32)
std *= max_pixel_value

denominator = np.reciprocal(std, dtype=np.float32)

dst = img.copy()
dst = dst.astype(np.float32)
dst -= mean
dst *= denominator

'''
for i in range(3):
    dst[:,:,i] = (((img[:,:,i] - mean[i]*255)/std[i]*255)*255).astype(np.uint8)
'''

cv2.imshow('before',img)
cv2.imshow('after', dst)

cv2.waitKey()
cv2.destroyAllWindows()
