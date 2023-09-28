import cv2
import serial

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0) 
ser = serial.Serial('/dev/ttyUSB0', 9600)

def larghezza_a_distanza(larghezza):
    return (0.9 / larghezza) *100

while True:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        center_x = x + w // 2
        center_y = y + h // 2

        distanza = larghezza_a_distanza(w)

        if distanza > 0 and distanza <0.5:

            distanzam = 1

        elif distanza > 0.5 and distanza<1:

            distanzam = 2

        elif distanza > 1 and distanza < 1.5:

            distanzam = 3

        elif distanza>1.5 and distanza <2:
            
            distanzam = 4
        else:
            distanzam = 5

        # Calcola le coordinate nel piano cartesiano
        coord_x = center_x - (frame.shape[1] // 2)
        coord_y = (frame.shape[0] // 2) - center_y
    
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    ser.write(f'{center_x} {center_y} {distanzam}\n'.encode())
    print(f"Inviata posizione del volto nel piano cartesiano: ({coord_x}, {coord_y}), distanza: {distanza} cm, valori: {distanzam}")

    # Disegna le linee verticali ed orizzontali per creare il piano cartesiano
    cv2.line(frame, (frame.shape[1] // 2, 0), (frame.shape[1] // 2, frame.shape[0]), (0, 255, 0), 2)
    cv2.line(frame, (0, frame.shape[0] // 2), (frame.shape[1], frame.shape[0] // 2), (0, 255, 0), 2)

    cv2.imshow('Rilevamento volti in tempo reale', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
