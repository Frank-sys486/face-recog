# Face Verification System 🧑‍💻

This project is a **real-time face verification system** built using **OpenCV**, **DeepFace**, and Python. It uses your webcam to capture live video frames and compares them with a reference image to determine if there's a match.

## Features
- **Real-Time Face Verification**: Captures live video and compares it to a reference image.
- **DeepFace Integration**: Uses the DeepFace library for face recognition and verification.
- **Threaded Processing**: Verifies faces asynchronously to maintain smooth video capture.
- **Visual Feedback**: Displays "MATCH!" or "NOT MATCH!" on the screen to indicate the verification status.

## Demo
![Demo Screenshot](https://github.com/Frank-sys486/face-recog/blob/main/screenshot.png)  

## How It Works
1. Captures video frames from the webcam.
2. Every 30 frames, the system verifies the face in the frame against a reference image (`image_reference.jpg`).
3. Displays the verification status ("MATCH!" or "NOT MATCH!") on the video feed.
4. Press **Q** to quit the application.

## Installation

### Prerequisites
1. Python 3.x installed on your system.
2. The following Python libraries:
   - `opencv-python`
   - `deepface`
   - `threading`

You can install the required libraries using `pip`:
```bash
pip install opencv-python deepface
```

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/face-verification.git
   ```
2. Navigate to the project directory:
   ```bash
   cd face-verification
   ```
3. Place your reference image in the project directory and name it `image_reference.jpg`.
4. Run the application:
   ```bash
   python main.py
   ```

## How to Use
1. Ensure your webcam is properly connected.
2. Place your reference image (`image_reference.jpg`) in the project directory.
3. Start the application:
   ```bash
   python main.py
   ```
4. Look into the camera. If the system detects a match with the reference image, "MATCH!" will appear on the screen. Otherwise, "NOT MATCH!" will be displayed.
5. Press **Q** to exit the application.

## Customization
- **Reference Image**: Replace `image_reference.jpg` with another image for verification.
- **Frame Check Frequency**: Adjust the frame interval for verification by modifying this line in the code:
  ```python
  if counter % 30 == 0:
  ```
- **Camera Resolution**: Change the camera resolution by modifying these lines:
  ```python
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  ```

## Code Overview
- **Face Verification**: Uses `DeepFace.verify()` to compare the live frame with the reference image.
- **Threading**: Offloads the verification task to a separate thread for smoother performance.
- **Real-Time Feedback**: Displays live feedback on the video feed using OpenCV's `putText`.

## Dependencies
- [OpenCV](https://opencv.org/): For capturing and displaying video frames.
- [DeepFace](https://github.com/serengil/deepface): For face recognition and verification.
- Python's built-in `threading` module for asynchronous processing.

## Contribution
Contributions are welcome! Feel free to fork this repository and submit a pull request if you have ideas for improvements or new features.

### Future Enhancements
- Add support for multiple reference images.
- Improve face detection accuracy.
- Display confidence scores for matches.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
This project uses the [DeepFace library](https://github.com/serengil/deepface) for face verification and [OpenCV](https://opencv.org/) for video processing.
