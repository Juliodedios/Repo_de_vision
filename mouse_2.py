import cv2
import numpy as np
#####Función_Inicio#######
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),50,(0,255,0),-1)
    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
    pass
cv2.namedWindow(winname='Imagen_gris')
cv2.setMouseCallback('Imagen_gris',draw_circle)
#####Función_Fin##########

####Mostrar_Imagenes_Inicio####
img = np.zeros((1080,1080,3),np.int8)
while True:
    cv2.imshow('Imagen_gris',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
####Mostrar_Imagenes_Fin####
