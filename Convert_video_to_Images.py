import os
import cv2

# Specify the video path and the folder to save frames
video_path = 'VideoFile.mp4' 
output_folder = 'D:/frames/'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Frame counter
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Construct the file name (e.g., "1.jpg", "2.jpg", ...)
    frame_filename = os.path.join(output_folder, f"{frame_count + 1}.jpg")

    # Save the current frame as an image file
    cv2.imwrite(frame_filename, frame)

    print(f"Saved: {frame_filename}")
    
    frame_count += 1

# Release the video capture object
cap.release()
print("Finished saving frames.")
