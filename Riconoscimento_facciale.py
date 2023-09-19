import cv2 as cv  #Importa la libreria OpenCV

capture = cv.VideoCapture(0)  #Apre il dispositivo per l'acquisizione video ovvero la camera

pretrained_model = cv.CascadeClassifier('haarcascade_frontalface_default.xml')  
#Carica un modello xml preaddestrato per il rilevamento dei volti

while True:  # Loop infinito per l'acquisizione video continua
    boolean, frame = capture.read()  #Legge un frame dalla camera
    
    if boolean == True:  #Se la lettura del frame è avvenuta con successo
        
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  
        #Il frame viene convertito in scala di grigi per il rilevamento dei volti
        
        coordinate_list = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)  
        #Rileva i volti nel frame
        
        #Disegna un rettangolo intorno ai volti rilevati nel frame
        for (x,y,w,h) in coordinate_list:
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            
        #Mostra il frame con i volti rilevati
        cv.imshow("Live Face Detection", frame)
        
        #Se vero esce dal ciclo while
        if cv.waitKey(20) == ord('x'):  # Premi il tasto 'x' per uscire
            break
        
capture.release()  #Rilascia il dispositivo di acquisizione video
cv.destroyAllWindows()  #Chiude tutte le finestre di visualizzazione