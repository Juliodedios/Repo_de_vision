import cv2
import numpy as np
import face_recognition as fr
import os
import random
from datetime import datetime
#Accedemos a la carpeta
path = 'Personal'
images = []
clases = []
lista = os.listdir(path)
print("Files and directories in '", path, "' :")
#Imprimimos lista
#Variables a utilizar
comp1=100

#Lectura de Rostros de la base de datos
for lis in lista:
    #Leemos las imagenes de la base
    imgdb=cv2.imread(f'{path}/{lis}')
    #Almacenamos las imagenes
    images.append(imgdb)
    #guardamos los nombres
    clases.append(os.path.splitext(lis)[0])
print(clases)
#Generamos una función para códificar los rostros
def codrostros(images):
    listacod = []

    for img in images:
        #Corrección de color
        img=cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        #cODIFICAMOS LA IMAGEN
        cod=fr.face_encodings(img)[0]
        #Almacenamos la codificación
        listacod.append(cod)
    return listacod


#--------------------------------------------------------------------------
#Definimos hora de ingrso
def horario(nombre):
    #Generamos un archivo modo lectura y escritura
    with open('Horario.csv','r+') as h:
        #Leemos la información
        data=h.readline()
        #Creamos la lista de nombres
        listanombres=[]

        #Iteramos cada linea del documento
        for line in data:
            #Buscamos la entrada y la diferenciamos con una coma
            entrada=line.split(',')
            #almacenamos los nombres
            listanombres.append(entrada[0])
        #Verificamos si ya hemos almacenado el m¿nombre
        if nombre not in listanombres:
            #Estraemps información actual
            info = datetime.now()
            #Extraemos fecha
            fecha=info.strftime('%Y:%m:%d')
            #Extraemos hora
            hora=info.strftime('%H:%M:%S')
            #Guardamos la información
            h.writelines(f'\n{nombre},{fecha},{hora}')
            print(info)
#Llamamos la función

rostroscod = codrostros(images)



#url='http://192.168.0.56/1600x1200.jpg'
#cap = cv2.VideoCapture(url)
cap = cv2.VideoCapture(0)

#winName='IP_CAM'
#cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
while True:
   # cap.open(url)
    #ret,frame=cap.read()
    ret, frame = cap.read()
    #redimensionamos
    frame2=cv2.resize(frame,(0,0),None,0.25,0.25)
    #realizamos la corrección de color
    rgb=cv2.cvtColor(frame2,cv2.COLOR_BGR2RGB)
    #Buscamos los rostros
    faces=fr.face_locations(rgb)
    facescod=fr.face_encodings(rgb,faces)
    #Iteramos
    for facescod,faceloc in zip(facescod,faces):
        #comparamos la base de datos con la imagen de la camara
        comparacion = fr.compare_faces(rostroscod,facescod)
    #Calculamos la similitud
        simi=fr.face_distance(rostroscod,facescod)
    #Buscamos el valor mas bajo
        min=np.argmin(simi)
        if comparacion[min]:
            nombre=clases[min].upper()
            print(nombre)
        #Extraemos las coordenadas
            yi,xf,yf,xi=faceloc
        #Escalamos
            yi, xf, yf, xi=yi*4,xf*4,yf*4,xi*4
            indice=comparacion.index(True)

        #comparamos
            if comp1 != indice:
            #Dibujar los cambios de colores
                r=random.randrange(0,255,50)
                g = random.randrange(0, 255, 50)
                b = random.randrange(0, 255, 50)
                comp1 = indice
            if comp1==indice:
                cv2.rectangle(frame,(xi,yi),(xf,yf),(r,g,b),3)
                cv2.rectangle(frame, (xi, yf-35), (xf, yf), (r, g, b), cv2.FILLED)
                cv2.putText(frame,nombre,(xi+6,yf-6),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2)
                horario(nombre)
    cv2.imshow("Reconocimiento facial", frame)
    t=cv2.waitKey(5)
    if t==27:
        break