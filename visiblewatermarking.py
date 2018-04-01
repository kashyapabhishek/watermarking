import numpy as np
import cv2

img = cv2.VideoCapture(0)


while True:
    ret, frame = img.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'watermark',(10,400), font, 4,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('hh',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
img.release()
cv2.destroyAllWindows()
