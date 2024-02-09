# Importamos librerias
import cv2

# Leemos la imagen
imagen =cv2.imread('RGB_p.jpg')

# Redimensionar de manera general
#cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
#INTER_NEAREST, INTER_LINEAR, INTER_AREA, INTER_CUBIC,INTER_LANCZOS4
img_1 = cv2.resize(imagen, None, fx = 1.5, fy = 1.5)
img_2 = cv2.resize(imagen, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_AREA)
img_3 = cv2.resize(imagen, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

# Redimensionar de manera especifica por dimensiones
ancho = 400
alto = 500
tam = (ancho, alto)
img_4 = cv2.resize(imagen, tam, interpolation = cv2.INTER_CUBIC)


# Mostramos el recorte
cv2.imshow('IMAGEN ORIGINAL', imagen)
cv2.imshow('REDIMENSION 1', img_1)
cv2.imshow('REDIMENSION 2', img_2)
cv2.imshow('REDIMENSION 3', img_3)
cv2.imshow('REDIMENSION 4', img_4)

cv2.waitKey(0)