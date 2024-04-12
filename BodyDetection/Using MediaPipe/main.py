import cv2
import mediapipe as mp  

mp_hands = mp.solutions.hands
drawing = mp.solutions.drawing_utils
mpFacemesh = mp.solutions.face_mesh

hands = mp_hands.Hands(max_num_hands=2)
faceMesh = mpFacemesh.FaceMesh(max_num_faces=2)
cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()        
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hands_detected = hands.process(imgRGB)
    faces_detected = faceMesh.process(imgRGB)
    
    if hands_detected.multi_hand_landmarks:
        for hand_landmark in hands_detected.multi_hand_landmarks:
            drawing.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS)
    
    if faces_detected.multi_face_landmarks:
        for face_landmark in faces_detected.multi_face_landmarks:
            # Draw face landmarks with modified drawing specifications
            drawing.draw_landmarks(img, face_landmark, mpFacemesh.FACEMESH_CONTOURS,
                                   landmark_drawing_spec=drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
                                   connection_drawing_spec=drawing.DrawingSpec(color=(0,0,255), thickness=1, circle_radius=1))
    
    cv2.imshow("Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cap.release()

