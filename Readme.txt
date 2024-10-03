Eye Blink Detection Project

Overview : This This project implements a real-time Eye Blink Detection system using MediaPipe Face Mesh and OpenCV. It calculates the Eye Aspect Ratio (EAR) to detect blinks, providing a valuable tool for applications in user interaction, health monitoring, and safety.

Features
- Real-time Eye Blink Detection: Utilizes MediaPipe Face Mesh for accurate landmark detection.
- EAR Calculation: Computes the Eye Aspect Ratio for precise blink detection.
- Customizable Blink Threshold: Easily adjustable parameters to fine-tune blink detection.
- Results Logging: Records blink detection results, including EAR values and thresholds, in a text file.
- Visual Feedback: Displays detected blinks on the processed images.


Requirements
- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- SciPy


Usage
Place your images in the D:/frames/person11 directory. Ensure the images are named numerically (e.g., 1.jpg, 2.jpg, etc.).

Run the script:

bash
Copy code
python <script-name>.py
The processed results, including blink counts and EAR values, will be saved in blink_results_p11.txt.

Press q to exit the display window while processing.
