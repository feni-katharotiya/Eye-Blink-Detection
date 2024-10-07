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

# Eye landmark indices with organized points
left_eye_indices = [33, 133, 160, 144, 159, 145, 158, 153]  # Left eye points
right_eye_indices = [362, 263, 385, 380, 386, 374, 387, 373]  # Right eye points

#------------------------------------------------------------------------------------------------
# (By normalizing 3 vertical distances (with weighted sum) with horizontal distance)
# EAR calculation function 

def calculate_EAR(landmarks,eye_indices):

    # step 1 :  Get the coordinates of eye points
    eye = np.array([(landmarks[pt].x, landmarks[pt].y) for pt in eye_indices])

    # step 2 : Compute vertical and Horizontal distances
    d1 = distance.euclidean(eye[0], eye[1])  # Horizontal distance
    d2 = distance.euclidean(eye[2], eye[3])  # Vertical distance (side to side)
    d3 = distance.euclidean(eye[4], eye[5])  # Center vertical distance
    d4 = distance.euclidean(eye[6], eye[7])  # vertical distance (side to side)

    # step 3 : calcilate weighted sum
    weighted_sum = (1 * d2) + (1 * d3) + (0.9 * d4) 

    # step 4 : Normalize the weighted sum by the horizontal distance
    EAR = weighted_sum / ( 3 * d1)
    return EAR

#------------------------------------------------------------------------------------------------
# Create a directory for storing face crops

image_folder = 'D:/frames/person1'


# Get a sorted list of image files numerically
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg')], key=lambda x: int(x.split('.')[0]))

# Blink threshold and frame counters
BLINK_THRESHOLD = 0.2475
BLINK_FRAMES = 2
frame_counter = 0
blink_count = 0 # Blink count

# Open a text file in append mode.
with open('blink_results_p2.txt', 'a') as file:
    # Write the header
    file.write(f"{'IMAGE_NAME':<19}   {'EAR_THRESHOLD':<11}   {'EAR':<19}   {'CALCULATION':<11}   {'VISULIZATION':<11}   {'RESULT'}\n")

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        frame = cv2.imread(image_path)
        if frame is None:
            print(f"Could not read {image_file}")
            continue

        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                
                #Convert the landmarks to numpy array
                landmarks = face_landmarks.landmark

                # #Save the face crop
                # save_face_crop(frame,landmarks,face_crops_folder,image_file)

                #Calculate EAR for both
                left_EAR = calculate_EAR(landmarks, left_eye_indices)
                right_EAR = calculate_EAR(landmarks, right_eye_indices)
                
                # Avarage EAR for both eyes
                avg_EAR = (left_EAR + right_EAR) / 2.0 

                # Dynamically adjust EAR threshold
                # dynamic_threshold = dynamic_EAR_threshold(landmarks, left_eye_indices, right_eye_indices)

                right_EAR = calculate_EAR(landmarks, right_eye_indices)
                print(f"Processing {image_file} - left EAR : {left_EAR} , right EAR: {right_EAR} Avg EAR: {avg_EAR} , frame-counter ; {frame_counter}")

                # store required information in files
                threshold = BLINK_THRESHOLD
                EAR_value = avg_EAR
                blink_status = 1 if (EAR_value < threshold) else 0 # Determine practical blink status (1 if threshold < 0.25, else 0) 
                visualization_status = ''  # Blank for manual entry

                # Compare and determine RESULT
                result = "SUCCESS" #if (blink_status == visualization_status) else "FAILED"

                # Write the results with fixed width for alignment
                file.write(f"{image_file:<19}   {threshold:<11.4f}   {EAR_value:<25}   {blink_status:<11}   {visualization_status:<8}   {result}\n")

                #check if EAR is below the blink threshold
                if avg_EAR < BLINK_THRESHOLD :
                    frame_counter += 1
                else:
                    if frame_counter >= BLINK_FRAMES :
                        print(f"Blink Detected in {image_file}!")
                        blink_count += 1
                    #Reset  frame counterAfter Blink 
                    frame_counter = 0
            
                for idx in left_eye_indices + right_eye_indices : 
                    x,y = int(landmarks[idx].x * frame.shape[1]) , int(landmarks[idx].y * frame.shape[0])
                    cv2.circle(frame ,(x,y) ,2,(0,255,0),-1)

        #  # Scale the image for display purposes only (e.g., 50% of original size)
        # display_scale_factor = 0.5 
        # display_frame = cv2.resize(frame, (int(frame.shape[1] * display_scale_factor), int(frame.shape[0] * display_scale_factor)))

        #Display the blink count on the frame
        cv2.putText(frame, f"Blink Count : {blink_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Show the frame (optional)
        cv2.imshow('Eye Blink Detection', frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):  # Display each frame for 100 ms
            break
   

# Release resources
file.close()
cv2.destroyAllWindows()
print("Finished processing images.")
 
 