#importamos librerias
import cv2
import matplotlib.pylab as plt
#Importamos la imagen del drone en escala de grises
dronegray=cv2.imread("descarga.png", 0)#Un solo canal o una sola matriz
#Importamos la imagen del drone en color
dronergb=cv2.imread("descarga.png", 1) #Tres canales o tres matrices
#Importamos la imagen del drone en color
dronecolor=cv2.imread("descarga.png") #Tres canales o tres matrices
#Corrección de color de BGR a rgb
img=cv2.cvtColor(dronecolor,cv2.COLOR_BGR2RGB)
#Corrección de color de BGR a HSV
imgHSV=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

#Extraemos los atributos principales de la imagen en escala de grises
#H = img[: , : , 0]
#S = img[: , : , 1]
#V = img[: , : , 2]
#Los 3 comandos anteriores son identicos a el siguiente comando
H,S,V = cv2.split(imgHSV)
r,g,b = cv2.split(img)
#r[:,:]=150
#img [:,:,0]=r

print(H)
archivo_h=open("Matriz_h","w")
archivo_h.write('hola'%H)
archivo_h.close()

#Ploteamos los canales
fig=plt.figure()
#Canal rojo
ax1=fig.add_subplot(2,2,1)
ax1.imshow(H)
ax1.set_title("Canal h")
#Canal verde
ax2=fig.add_subplot(2,2,2)
ax2.imshow(S)
ax2.set_title("Canal s")
#Canal azul
ax2=fig.add_subplot(2,2,3)
ax2.imshow(V)
ax2.set_title("Canal v")
#Reconstrucción de imagen
imgre=cv2.merge((H,S,V))
imgH=cv2.cvtColor(imgre,cv2.COLOR_HSV2RGB)
#Imagen original

ax4=fig.add_subplot(2,2,4)
ax4.imshow(imgH )
ax4.set_title("Original")

fig_1=plt.figure(3)
#Canal rojo
ax1=fig_1.add_subplot(2,2,1)
ax1.imshow(r)
ax1.set_title("Canal h")
#Canal verde
ax2=fig_1.add_subplot(2,2,2)
ax2.imshow(g)
ax2.set_title("Canal s")
#Canal azul
ax2=fig_1.add_subplot(2,2,3)
ax2.imshow(b)
ax2.set_title("Canal v")
#Reconstrucción de imagen
imgres=cv2.merge((r,g,b))
#Imagen original

ax4=fig_1.add_subplot(2,2,4)
ax4.imshow(imgres)
ax4.set_title("Original")


plt.show()
#Con el teclado pasamos la imagen
cv2.waitKey(0)