#Canny algorithm
import cv2
import numpy as np
import matplotlib.pylab as plt
 
def despliega(img_3):
    fig=plt.figure(figsize=(12,10))
    ax=fig.add_subplot(111)
    ax.imshow(img_3)
    plt.show()
def despliega_doble(img_4,x1,img_5,x2,img_6,x3,img_7,x4):
    fig_1 = plt.figure()
    ax1 = fig_1.add_subplot(2,2,1)
    ax1.imshow(img_4)
    ax1.set_title(x1)
    ax2 = fig_1.add_subplot(2,2,2)
    ax2.imshow(img_5)
    ax2.set_title(x2)
    ax3 = fig_1.add_subplot(2,2,3)
    ax3.imshow(img_6)
    ax3.set_title(x3)
    ax4 = fig_1.add_subplot(2,2,4)
    ax4.imshow(img_7)
    ax4.set_title(x4)
    plt.show()

def carga_imagen(x):
    tab_BGR = cv2.imread(x)
    tab_gray = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2GRAY)
    tab_RGB = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2RGB)
    return tab_gray,tab_RGB,tab_BGR
imgray,imbgr,imgrgb=carga_imagen("tablero_base.jpg")
#imgray,imbgr,imgrgb=carga_imagen("doggy.jpg")
img_dist=cv2.medianBlur(imgrgb,9)
bordes=cv2.Canny(imgrgb,threshold1=0,threshold2=120)
bordes_1=cv2.Canny(img_dist,threshold1=200,threshold2=120)
med_valor=np.median(imgrgb)
lower=int(max(0,0.7*med_valor))
upper=int(max(255,1.3*med_valor))
bordes_2=cv2.Canny(img_dist,threshold1=lower,threshold2=upper)
bordes_3=cv2.Canny(imgrgb,threshold1=lower,threshold2=upper)
countours_b,jerarqui_b=cv2.findContours(bordes_1,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
#print(countours_b)
cv2.drawContours(imgrgb,countours_b,-1,(0,255,0),3)
cv2.imshow("Imagen",imgrgb)
#count_txt = np.savetxt('count.txt', countours_b, delimiter =', ')
despliega_doble(bordes,"Borde sin blur",bordes_1,"Borde blur_1",bordes_2,"Borde blur_2",bordes_3,"Borde sin blur max min")
cv2.waitKey(0)