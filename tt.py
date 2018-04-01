import numpy as np
import matplotlib.pyplot as plt
import pywt
import pywt.data
import cv2

# Load image
#original = pywt.data.aero()

original = cv2.imread('pan.jpg',0)

# Wavelet transform of image, and plot approximation and details
titles = ['Approximation', ' Horizontal detail','Vertical detail', 'Diagonal detail']
coeffs2 = pywt.dwt2(original, 'bior1.3')

LL1, (LH1, HL1, HH1) = coeffs2
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(LL1,'fsajlfja',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)


fig = plt.figure()
for i, a in enumerate([LL1, LH1, HL1, HH1]):
    ax = fig.add_subplot(2, 2, i + 1)
    ax.imshow(a, origin='image', interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=12)


fig.suptitle("dwt2 coefficients", fontsize=14)


# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(LL1 ,'fsajlfjkhkhja',(10,100), font, 4,(255,255,255),2,cv2.LINE_AA)

# fig = plt.figure()
# plt.imshow(LL1, interpolation="nearest", cmap=plt.cm.gray)
# fig.suptitle("dwt2 coefficients", fontsize=14)
# # # Now reconstruct and plot the original image
# reconstructed = pywt.idwt2(coeffs2, 'bior1.3')
# fig = plt.figure()
# plt.imshow(reconstructed, interpolation="nearest", cmap=plt.cm.gray)


plt.show()
