#importamos librerias
import cv2
import matplotlib.pylab as plt
#Importamos la imagen del drone en color
dronecolor=cv2.imread("descarga.png") #Tres canales o tres matrices
#Corrección de color de BGR a rgb
img=cv2.cvtColor(dronecolor,cv2.COLOR_BGR2RGB)

#Ploteamos 
print(img.shape)
#Resize por dimensión
imagen_r1=cv2.resize(img,(100,200))
#Resize por radio
ancho=2
alto=2
imagen_r2=cv2.resize(img,(0,0),img,ancho,alto)
imagen_r3=cv2.flip(img,1)
print(img.shape)
print(imagen_r2.shape)
fig=plt.figure()
#Canal rojo
ax1=fig.add_subplot(2,2,1)
ax1.imshow(imagen_r1)
ax1.set_title("Canal h")
#Canal verde
ax2=fig.add_subplot(2,2,2)
ax2.imshow(imagen_r2)
ax2.set_title("Canal s")
#Canal azul
ax3=fig.add_subplot(2,2,3)
ax3.imshow(imagen_r3)
ax3.set_title("Canal v")
#Reconstrucción de imagen

ax4=fig.add_subplot(2,2,4)
ax4.imshow(img )
ax4.set_title("Original")


plt.show()
#Con el teclado pasamos la imagen
cv2.waitKey(0)