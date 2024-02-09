import cv2
import numpy as np
import matplotlib.pylab as plt
 #Ahora con imagenes

imagen =cv2.imread('RGB_p.jpg')

# Visualizar en paint los pixeles
rct = imagen[250:573, 250:573]

# Mostramos el recorte
cv2.imshow('IMAGEN ORIGINAL', imagen)
cv2.imshow('RECORTE', rct)

cv2.waitKey(0)
#