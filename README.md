# Eye Blink Detection Project

## Overview
This project implements a real-time Eye Blink Detection system using MediaPipe Face Mesh and OpenCV. It calculates the **Eye Aspect Ratio (EAR)** to detect blinks, providing a valuable tool for applications in user interaction, health monitoring, and safety.

## Key Concept: Eye Aspect Ratio (EAR)

The **Eye Aspect Ratio (EAR)** is used to determine whether the eyes are open or closed in real-time.The **Eye Aspect Ratio (EAR)** is a ratio of distances between specific facial landmarks around the eyes. It is used to determine whether the eyes are open or closed.The formula is:

### EAR Formula:

EAR = (d1 + d2) / (2 * d3)
Where:
- d1 = Vertical distance between landmarks p2 and p6 (top and bottom of the left side of the eye)
- d2 = Vertical distance between landmarks p3 and p5 (top and bottom of the right side of the eye)
- d3 = Horizontal distance between landmarks p1 and p4 (outer corners of the eye)


### Explanation of the Formula:

1. **d1 and d2**: These are the **vertical distances** between the landmarks on the upper and lower eyelids of the eye. They measure how open or closed the eye is.
   - As the eye closes, these distances decrease.
2. **d3**: This is the **horizontal distance** between the outer corners of the eye, which provides a stable reference point that remains relatively constant regardless of head orientation, distance from the camera, or face size.


- **Numerator**: The vertical distances between the upper and lower eyelid landmarks (p2-p6 and p3-p5). This measures how "open" the eye is.
- **Denominator**: The horizontal distance between the outer corners of the eye (p1-p4). This serves as a stable reference point, which remains relatively constant despite head tilt, distance from the camera, or face size.

### Why Use Horizontal Distance (d3)?

The **horizontal distance** between the outer eye corners is used to ensure the EAR calculation is **consistent** across various scenarios:

- **Stability**: The horizontal distance (d3) provides a consistent baseline that does not change significantly with different head poses, tilts, or face sizes.
- **Scale Invariance**: Whether the person is close to or far from the camera, this horizontal distance helps maintain consistency in the EAR calculation.
- **Pose Robustness**: Slight head rotations or tilts have minimal impact on this horizontal distance, making the EAR more reliable in real-world scenarios.
- **Consistency Across Individuals**: The horizontal distance provides a normalized reference, making the EAR applicable to different face shapes and sizes.
- **Scale Invariance**: Whether the face is near or far from the camera, the EAR remains proportional because the horizontal distance is stable.

  
### Blink Detection Logic:

- **Open Eye**: The vertical distances (numerator) are relatively larger compared to the horizontal distance, resulting in a higher EAR value.
- **Closed Eye**: As the eyelids close, the vertical distances reduce, and the EAR value decreases.
  
A typical threshold for detecting a blink is when the EAR falls below 0.25. If the EAR stays below this threshold for several consecutive frames, a blink is detected.

## Features
- **Real-time Eye Blink Detection**: Utilizes MediaPipe Face Mesh for accurate facial landmark detection.
- **EAR Calculation**: Computes the Eye Aspect Ratio to detect blinks.
- **Customizable Blink Threshold**: Parameters can be adjusted to fine-tune blink detection.
- **Results Logging**: Records blink detection results, including EAR values and thresholds, in a text file.
- **Visual Feedback**: Displays detected blinks on the processed images.

## Requirements
- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- SciPy

## Usage
1. Place your images in the `D:/frames/person11` directory. Ensure the images are named numerically (e.g., 1.jpg, 2.jpg, etc.).
2. Run the script:
   ```bash
   python <script-name>.py

The processed results, including blink counts and EAR values, will be saved in blink_results_p11.txt.
Press q to exit the display window while processing.
