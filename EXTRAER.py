#importamos librerias
import cv2
import numpy as np
import matplotlib.pylab as plt
#Importamos la imagen del drone en escala de grises
dronegray=cv2.imread("Drone.jpg", 0)#Un solo canal o una sola matriz
#Importamos la imagen del drone en color
dronergb=cv2.imread("Drone.jpg", 1) #Tres canales o tres matrices
#Importamos la imagen del drone en color
dronecolor=cv2.imread("Drone.jpg") #Tres canales o tres matrices
#Corrección de color
img=cv2.cvtColor(dronecolor,cv2.COLOR_BGR2RGB)
#Extraemos los atributos principales de la imagen en escala de grises
R = img[: , : , 0]
G = img[: , : , 1]
B = img[: , : , 2]
#Los 3 comandos anteriores son identicos a el siguiente comando
#R,G,B = cv2.split(dronecolor)
print(img)

#Ploteamos los canales
fig=plt.figure()
#Canal rojo
ax1=fig.add_subplot(2,2,1)
ax1.imshow(R, cmap="gray")
ax1.set_title("Canal rojo")
#Canal verde
ax2=fig.add_subplot(2,2,2)
ax2.imshow(G, cmap="gray")
ax2.set_title("Canal verde")
#Canal azul
ax2=fig.add_subplot(2,2,3)
ax2.imshow(B, cmap="gray")
ax2.set_title("Canal azul")
#Reconstrucción de imagen
imgre=cv2.merge((R,G,B))
#Imagen original

ax4=fig.add_subplot(2,2,4)
ax4.imshow(imgre)
ax4.set_title("Original")

plt.show()
#Con el teclado pasamos la imagen
cv2.waitKey(0)