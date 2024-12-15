import threading
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # find camera

#dimension of camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

counter = 0

face_match = False

reference_image = cv2.imread('image_reference.jpg')

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame,reference_image.copy())['verified']:
            face_match = True
    except ValueError:
        face_match = False



while True:
    ret, frame = cap.read()

    if ret:
        frame = cv2.flip(frame, 1)
        if counter %30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError: # not recognizing face
                pass
        counter += 1 

        if face_match:
            cv2.putText(frame, "MATCH!", (24,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),3)
        else:
            cv2.putText(frame, "NOT MATCH!", (24,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),3)
        
        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows
