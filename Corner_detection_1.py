#Harris Algorithm
import cv2
import numpy as np
import matplotlib.pylab as plt
 

def carga_imagen(x):
    tab_BGR = cv2.imread(x)
    tab_gray = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2GRAY)
    tab_RGB = cv2.cvtColor(tab_BGR,cv2.COLOR_BGR2RGB)
    return tab_gray,tab_RGB,tab_BGR


imgray,imbgr,imgrgb=carga_imagen("tablero.jpg")
#print(imrgb.shape)
dst=cv2.cornerHarris(src=imgray,blockSize=3,ksize=3,k=0.04)
#Imagen fuente, tamaño considerado para la deteción,Parámetro de apertura de la derivada de Sobel utilizada, parametro del detector de harrys(presición)
#Imagen fuente,tamaño del eelemnto,definición de la esquina, definición de forma del elemento
dst_txt = np.savetxt('dst.txt', dst, delimiter =', ')
dst=cv2.dilate(dst,None)
#Operaciones morfológicas sirven para modificar la estructura de la imágen 
imgrgb[dst>0.01*dst.max()]=[0,255,0]
print
#Si el resultado del algoritmo es mayor que 0.01 veces que el valor máximo, debe ser igual a color verde
cv2.imshow("Chess",imgrgb)
cv2.waitKey(0)