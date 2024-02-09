import cv2
import numpy as np
def nada (x):
    pass

cv2.namedWindow('Parametros')
cv2.createTrackbar('T_min','Parametros',0,179,nada)
cv2.createTrackbar('T_max','Parametros',0,179,nada)
cv2.createTrackbar('P_min','Parametros',0,255,nada)
cv2.createTrackbar('P_max','Parametros',0,255,nada)
cv2.createTrackbar('L_min','Parametros',0,255,nada)
cv2.createTrackbar('L_max','Parametros',0,255,nada)
cv2.createTrackbar('Kernel_x','Parametros',1,30,nada)
cv2.createTrackbar('Kernel_y','Parametros',1,30,nada)


cap=cv2.VideoCapture(2)
while(1):
    ret,frame=cap.read()
    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        Tmin= cv2.getTrackbarPos('T_min','Parametros')
        Tmax = cv2.getTrackbarPos('T_max', 'Parametros')
        Pmin = cv2.getTrackbarPos('P_min', 'Parametros')
        Pmax = cv2.getTrackbarPos('P_max', 'Parametros')
        Lmin = cv2.getTrackbarPos('L_min', 'Parametros')
        Lmax = cv2.getTrackbarPos('L_max', 'Parametros')
        kernelx = cv2.getTrackbarPos('Kernel_x', 'Parametros')
        kernely = cv2.getTrackbarPos('Kernel_y', 'Parametros')
        color_oscuro=np.array([Tmin,Pmin,Lmin])
        color_claro = np.array([Tmax, Pmax, Lmax])
        mascara= cv2.inRange(hsv,color_oscuro,color_claro)
        kernel=np.ones((kernelx,kernely),np.uint8)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
        mascara=cv2.morphologyEx(mascara, cv2.MORPH_OPEN,kernel)
        contornos,_=cv2.findContours(mascara, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contornos,-1,(0,0,0),2)
        cv2.imshow("Camara", frame)
        cv2.imshow("Mascara", mascara)
        tecla = cv2.waitKey(1) & 0xFF
    if tecla == 27:
        break
cv2.destroyAllWindows()

