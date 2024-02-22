import cv2

url='http://192.168.0.56/1600x1200.jpg'
cap = cv2.VideoCapture(url)

winName='IP_CAM'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
ancho=int(cap.get(3))
alto=int(cap.get(4))
#(Nombre, codificación, frames por segundo, tamaño)
out=cv2.VideoWriter("Primer_video_1.avi",cv2.VideoWriter_fourcc('M','J','P','G'),2,(ancho,alto))
while(1):
    cap.open(url)
    ret,frame=cap.read()
    rgb_1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    hsv_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)

    cv2.imshow("BGR", frame)
    #cv2.imshow("RGB",rgb_1)
    #cv2.imshow("HSV", hsv_1)
    #cv2.imshow("Gray", gray_1)
    tecla = cv2.waitKey(1) & 0xFF
    if tecla ==27:
        break
cv2.destroyAllWindows()