import cv2
import pywt

img = cv2.imread('peen.jpg',-1)
coffi =  pywt.wavedec2(img, 'haar', 1 )

for i in img:
	print(i)
	break

print("...........................")
for i in coffi:
	print(i)
	break

print("----------------------------")

# cv2.imshow('img1',LL)

img1 =pywt.waverec2(coffi, 'haar');

for i in img1:
	print(i)
	break

cv2.imshow('in',img1)
cv2.waitKey(0)