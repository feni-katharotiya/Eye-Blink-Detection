import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] ='0'


import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import distance

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils


#EAR calculation function
def calculate_EAR(landmarks,eye_indices):

    # step1 : Get the coordinates of eye points
    eye = np.array([(landmarks[pt].x ,landmarks[pt].y) for pt in eye_indices])

    # step2 : Compute vertical and Horizontal distances
    d2 = distance.euclidean(eye[1], eye[5]) # vertical distance
    d3 = distance.euclidean(eye[2], eye[4]) # vertical distance
    d1 = distance.euclidean(eye[0], eye[3]) # HORIZONTAL distance

    # step 3 : calculare EAR
    EAR = (d2 + d3) / (2.0 * d1)
    return EAR

# Eye landmark indices
left_eye_indices = [33,160,158,13,153,144]
right_eye_indices = [362,385,387,263,373,380]


video_path ='VideoFile.mp4'
cap = cv2.VideoCapture(video_path)

# Blink threshold and frame counters
EAR_THRESHOLD = 0.25
BLINK_FRAMES = 3
frame_counter =0
blink_count = 0 # Blink count

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            
            #Convert the landmarks to numpy array
            landmarks = face_landmarks.landmark

            #Calculate EAR for both
            left_EAR = calculate_EAR(landmarks, left_eye_indices)
            right_EAR = calculate_EAR(landmarks, right_eye_indices)
            
            # Avarage EAR for both eyes
            avg_EAR = (left_EAR + right_EAR) / 2.0 

            #check if EAR is below the blink threshold
            if avg_EAR < EAR_THRESHOLD :
                frame_counter += 1
            else:
                if frame_counter >= BLINK_FRAMES :
                    print("Blink Detected !")
                    blink_count += 1
                    #Reset  frame counter After Blink 
                    frame_counter = 0
           
            mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)

    #Display the blink count on the frame
    cv2.putText(frame, f"Blink : {blink_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # Display the resulting frame
    cv2.imshow('Face Mesh with Blink Detection', frame)

     # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()