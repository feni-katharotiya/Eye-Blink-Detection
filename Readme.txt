# Eye Blink Detection Project

## Overview
This This project implements a real-time Eye Blink Detection system using MediaPipe Face Mesh and OpenCV. It calculates the Eye Aspect Ratio (EAR) to detect blinks, providing a valuable tool for applications in user interaction, health monitoring, and safety.

### Main Logic
Here the main logic is derived using Eye Aspect Ration .
EAR = (d1 + d2 + d3) / (3 * d4 )
; d1 = Vertivcal Distance between landmarks from face landmark model
, d2 = Vertical distance  between landmarks from face landmark model
, d3 = Vertical distance  between landmarks from face landmark model
, d4 = Horizontal distance  between landmarks from face landmark model

SO ,The numerator measures the vertical distances between the top and bottom eyelid.The denominator measures the horizontal distance between the corners of the eye.
​Open Eye: The vertical distances (numerator) are relatively larger compared to the horizontal distance, resulting in a higher EAR value.
Closed Eye: The vertical distances become smaller as the eyelids come closer, reducing the EAR value.
A typical threshold for detecting a blink is when the EAR falls below 0.25, but this can vary based on the individual's eye shape and facial features. If the EAR goes below this threshold for several consecutive frames, a blink is detected !

## Features
- Real-time Eye Blink Detection: Utilizes MediaPipe Face Mesh for accurate landmark detection.
- EAR Calculation: Computes the Eye Aspect Ratio for precise blink detection.
- Customizable Blink Threshold: Easily adjustable parameters to fine-tune blink detection.
- Results Logging: Records blink detection results, including EAR values and thresholds, in a text file.
- Visual Feedback: Displays detected blinks on the processed images.


## Requirements
- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- SciPy


## Usage
1.Place your images in the D:/frames/person11 directory. Ensure the images are named numerically (e.g., 1.jpg, 2.jpg, etc.).

2.Run the script:
```bash
   python <script-name>.py

The processed results, including blink counts and EAR values, will be saved in blink_results_p11.txt.

Press q to exit the display window while processing.
