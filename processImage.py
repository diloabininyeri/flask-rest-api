import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('https://cdn.muzlu.com/users/muhammetsrc/441_1e2e5d455536616c66f328ce988e11481523826808.jpg',0)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()