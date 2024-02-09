#importamos librerias
import cv2
import matplotlib.pylab as plt
import numpy as np
#Importamos la imagen del drone en color
dronecolor=cv2.imread("descarga.png") #Tres canales o tres matrices
#Corrección de color de BGR a rgb
img=cv2.cvtColor(dronecolor,cv2.COLOR_BGR2RGB)
B,G,R=cv2.split(img)

b_1 = np.savetxt('B.txt', B, delimiter =', ')    
G_1 = np.savetxt('G.txt', G, delimiter =', ')
R_1 = np.savetxt('R.txt', R, delimiter =', ')        

  
cv2.waitKey(0)

