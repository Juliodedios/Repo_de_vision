import cv2

cap = cv2.VideoCapture(0)

winName='IP_CAM'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
while(1):
    #cap.open(url)
    ret,frame=cap.read()
    #cv2.rectangle(frame,pt1=(20,10),pt2=(100,200),color=(255,255,0),thickness=10)
    print(frame.shape)
    if ret:
        
        #frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
        frame_2=cv2.flip(frame,1)
        cv2.rectangle(frame_2,pt1=(20,10),pt2=(100,200),color=(255,255,0),thickness=10)
        cv2.circle(frame_2,center=(320,240),radius=20,color=(255,120,110),thickness=5)
        cv2.circle(frame_2,center=(50,20),radius=20,color=(255,0,255),thickness=-1)
        cv2.line(frame_2,pt1=(0,0),pt2=(640,480),color=(120,120,120),thickness=5)
        fuente=cv2.FONT_ITALIC
        cv2.putText(frame_2,text="Hola mundo",org=(10,240),fontFace=fuente,fontScale=2,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA)
        gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow(winName,frame)
        rct = frame[250:573, 250:573]
        redimension=cv2.resize(rct, None, fx = 2.5, fy = 3.0)
        cv2.imshow(winName, frame_2)
        #cv2.imshow(winName, rct)
    tecla=cv2.waitKey(1) & 0xFF
    if tecla ==27:
        break
cv2.destroyAllWindows()