import cv2
import numpy as np
import matplotlib.pylab as plt

##Funcion_cargar_i8magenes##
def carga_imagen():
    img = cv2.imread('descarga.png').astype(np.float32) / 255
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img
###########################

##Funcion_ploteo###########
def despliega(img_3):
    fig=plt.figure(figsize=(12,10))
    ax=fig.add_subplot(111)
    ax.imshow(img_3)
    plt.show()
###########################
# Distorsion
imagen=carga_imagen()
gamma=1/50
eleva_un_cuarto=np.power(imagen,gamma)
###despliega(eleva_un_cuarto)
# Distorsión Filtro por kernel
kernel = np.ones(shape = (10,10),dtype = np.float32 )/25
distorsion = cv2.filter2D(imagen, -1,kernel)
###despliega(distorsion)
# Distorsión por blur 
blur_distorsion=cv2.blur(imagen, ksize=(10,10))
###despliega(blur_distorsion) 
blur_gausiano=cv2.GaussianBlur(imagen,(5,5),50)
#despliega(blur_gausiano)
blur_median=cv2.medianBlur(imagen,5)#Se usa sobre todo en imagenes con pixeles extra o puntos 
#despliega(blur_median)
blur_bilateral=cv2.bilateralFilter(imagen,9,75,75)
despliega(blur_bilateral)

cv2.waitKey(0)
