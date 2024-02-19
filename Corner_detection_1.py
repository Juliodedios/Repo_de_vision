import cv2
import numpy as np
import matplotlib.pylab as plt
 

def carga_imagen(x):
    tab_BGR = cv2.imread(x)
    tab_gray = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2GRAY)
    tab_RGB = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2RGB)
    return tab_gray,tab_RGB,tab_BGR
imgray,imbgr,imgrgb=carga_imagen("tablero_base.jpg")
#print(imrgb.shape)
dst=cv2.cornerHarris(src=imgray,blockSize=2,ksize=3,k=0.04)

dst=cv2.dilate(dst,None)
imgrgb[dst>0.01*dst.max()]=[255,0,0]
cv2.imshow("Chess",imgrgb)
cv2.waitKey(0)