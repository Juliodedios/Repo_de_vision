#importamos librerias
import cv2
import numpy as np
import matplotlib.pylab as plt
#Crear imagen negra
img = np.zeros((10,10,1), np.uint8)
#modificar algunos pixeles
img[0,0]=30
img[1,1]=50
img[2,2]=200
img[3,3]=140 
img[4,4]=250
img[5,5]=255

#Se muestran los valores numericos
print(img)
#Se muestra la imagen
plt.imshow(img, cmap='gray')
plt.show()