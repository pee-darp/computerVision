#! /usr/bin/python3
import numpy as np
import cv2
import os
import sys
from matplotlib import pyplot as plt

img_dir = "/home/spradeep/pradeep/computerVision/images"
img_name = "rainbow.jpeg"
img_path = os.path.join(img_dir, img_name)

img = cv2.imread(img_path)

img = img.astype('float32') / 255.
img_r = img[:,:,0]
img_g = img[:,:,1]
img_b = img[:,:,2]
(r,g,b) = (0.9,1,1.5)
img[:,:,0] = np.multiply(img_r, (img_r))
img[:,:,1] = np.multiply(img_g, (img_g))
img[:,:,2] = np.multiply(img_b, (img_b))
print(f"type: {img.dtype} \nsize: {img.shape}")
print(f"max: {np.min(img)}")

cv2.imshow('rainbow', img)

color = ('r','g','b')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,1])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

key_pressed = cv2.waitKey(0)
try:
    if key_pressed == ord('q'):
        cv2.destroyAllWindows()
        sys.exit()
except KeyboardInterrupt:
    cv2.destroyAllWindows()
    sys.exit()
