
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

img = cv2.imread('dic1.jpg', 0)
#cv2.imshow('dic.jpg', img)
#img1 = img[:, 0:(int)(img.shape[1]/2)]
#img2 = img[:, -(int)(img.shape[1]/2):, : ]
#cv2.imwrite('dic1.jpg', img1)
#cv2.imshow('dic.jpg', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
print(img.shape)
x = []
for i in img:
    x.append(i.sum())
    print(i.shape)
print(len(x))
x = np.array(x)
#x = np.random.random_integers(1, 100, 5)
plt.plot(x)
plt.show()
plt.plot(x)
plt.ylabel('No of times')
plt.show()
top=100
#print(np.argwhere(x > 80000))
ind = np.argpartition(x, -top)[-top:]
print(ind[np.argsort(x[ind])])
ind = sorted(ind)
print(ind)

from numpy import diff
dx = 0.1
dy = diff(x)/dx
plt.plot(dy)
plt.show()




