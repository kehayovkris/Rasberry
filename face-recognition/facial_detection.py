import cv2

# Carica il classificatore preaddestrato per la rilevazione facciale
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inizializza la webcam
cap = cv2.VideoCapture(1)

while True:
 # Leggi un frame dalla webcam
 ret, frame = cap.read()

 # Converti il frame in scala di grigi (per la rilevazione facciale)
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

 # Esegui la rilevazione facciale
 faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

 # Disegna un rettangolo intorno ai volti rilevati
 for (x, y, w, h) in faces:
     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

 # Mostra il frame con i volti rilevati
 cv2.imshow('Face Detection', frame)

 # Esci se si preme il tasto 'q'
 if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Rilascia la webcam e chiudi la finestra
cap.release()
cv2.destroyAllWindows()