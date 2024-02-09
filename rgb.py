#importamos librerias
import cv2
import numpy as np
import matplotlib.pylab as plt
#Crear imagen negra
img = 255*np.ones((10,10,3), np.uint8)
#Extraemos los canales
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
#modificamos loa canales
R[:,:]=0
G[:,:]=50
B[:,:]=120
#Se muestran los valores numericos
img [:,:,0]=R
img [:,:,1]=G
img [:,:,2]=B
print(img)
#Se muestra la imagen
plt.imshow(img)
plt.show()

cv2.waitKey(0)