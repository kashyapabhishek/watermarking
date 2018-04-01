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
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(LL1,'fsajlfja',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)


fig = plt.figure()
for i, a in enumerate([LL1, LH1, HL1, HH1]):
    ax = fig.add_subplot(2, 2, i + 1)
    ax.imshow(a, origin='image', interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=12)


fig.suptitle("dwt2 coefficients", fontsize=14)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(LL1 ,'fsajlfjkhkhja',(10,100), font, 4,(255,255,255),2,cv2.LINE_AA)

fig = plt.figure()
plt.imshow(LL1, interpolation="nearest", cmap=plt.cm.gray)
fig.suptitle("dwt2 coefficients", fontsize=14)
# # Now reconstruct and plot the original image
reconstructed = pywt.idwt2(coeffs2, 'bior1.3')
fig = plt.figure()
plt.imshow(reconstructed, interpolation="nearest", cmap=plt.cm.gray)
# # imArray_H=pywt.idwt2(coeffs2, 'bior1.3')

# cv2.imshow('image',imArray_H)
# cv2.waitKey(0)

# coeffs3 = pywt.dwt2(LL1, 'bior1.3')
# LL2, (LH2, HL2, HH2) = coeffs3

# coeffs4 = pywt.dwt2(LL2, 'bior1.3')
# LL3, (LH3, HL3, HH3) = coeffs4





# fig = plt.figure()
# for i, a in enumerate([LL3, LH3, HL3, HH3]):
#     ax = fig.add_subplot(2, 2, i + 1)
#     ax.imshow(a, origin='image', interpolation="nearest", cmap=plt.cm.gray)
#     ax.set_title(titles[i], fontsize=12)


# fig.suptitle("dwt2 ll coefficients", fontsize=14)







# imArray_H=pywt.idwt2(coeffs2, 'bior1.3')
# fig = plt.figure()
# ax = fig.add_subplot(2, 2,3)
# ax.imshow(imArray_H, origin='image', interpolation="nearest", cmap=plt.cm.gray)
# fig.suptitle("hi", fontsize=12)

# cv2.imwrite('pen.jpg',imArray_H)



















# # Now reconstruct and plot the original image
# reconstructed = pywt.idwt2(coeffs2, 'bior1.3')
# fig = plt.figure()
# plt.imshow(reconstructed, interpolation="nearest", cmap=plt.cm.gray)
# # Check that reconstructed image is close to the original
# np.testing.assert_allclose(original, reconstructed, atol=1e-13, rtol=1e-13)

# # Now do the same with dwtn/idwtn, to show the difference in their signatures

# coeffsn = pywt.dwtn(original, 'bior1.3')
# fig = plt.figure()
# for i, key in enumerate(['aa', 'ad', 'da', 'dd']):
#     ax = fig.add_subplot(2, 2, i + 1)
#     ax.imshow(coeffsn[key], origin='image', interpolation="nearest",
#     cmap=plt.cm.gray)
#     ax.set_title(titles[i], fontsize=12)

# fig.suptitle("dwtn coefficients", fontsize=14)

# # Now reconstruct and plot the original image
# reconstructed = pywt.idwtn(coeffsn, 'bior1.3')
# fig = plt.figure()
# plt.imshow(reconstructed, interpolation="nearest", cmap=plt.cm.gray)

# # Check that reconstructed image is close to the original
# np.testing.assert_allclose(original, reconstructed, atol=1e-13, rtol=1e-13)

plt.show()
