import cv2
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np

drawing = False
ix = -1
iy = -1



def draw_circle(event, x, y, flags, param):

    global drawing, ix , iy 
q
    if event == cv2.EVENT_LBUTTONDOWN:
        
        drawing = True
        ix,iy = x, y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)

        
cv2.namedWindow (winname='my_drawing') 
cv2.setMouseCallback('my_drawing', draw_circle)

img = np.zeros((512,512,3))

while True:

    cv2.imshow('mydrawing',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
