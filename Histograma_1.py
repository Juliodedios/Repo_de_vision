import cv2
import numpy as np
import matplotlib.pylab as plt
img_bgr=cv2.imread('drone.jpg')
img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
hist_values=cv2.calcHist([img_bgr], channels=[1], mask=None,histSize=[256],ranges=[0,256]) #Calcula el histograma par la matriz verde 
print(hist_values.shape)
tamaño=(512,512)
img_resize=cv2.resize(img_bgr,tamaño,interpolation=cv2.INTER_CUBIC)
hist_values_resize=cv2.calcHist([img_resize], channels=[1], mask=None,histSize=[256],ranges=[0,256]) #Calcula el histograma par la matriz azul 
#plt.plot(hist_values)
print(img_bgr.shape)
min=0
max=0
for x in hist_values:
    for z in x:
        if z > max:
             max = z
        if z < min:
            min = z
print(max)
print(min)
   
fig_1 = plt.figure()
# imagen original
ax1 = fig_1.add_subplot(1,2,1)
ax1.plot(hist_values)
ax1.set_title("IMAGEN")

# recorte
ax2 = fig_1.add_subplot(1,2,2)
ax2.plot(hist_values_resize)
ax2.set_title("Histograma azul")

plt.show()