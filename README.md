# Finger Counting using Hand Tracking

This project demonstrates the use of hand tracking to count the number of raised fingers using Mediapipe. The goal is to detect hand landmarks and determine the number of fingers raised.

## Project Structure

The project consists of the following files and directories:

* `FingerCounter.py`: A script for counting the number of raised fingers using hand tracking.
* `HandTrackingModule.py`: A custom module using Mediapipe for hand tracking.
* `requirements.txt`: A file listing the required Python packages.
* `fingers_images`: A directory containing images used for displaying the number of raised fingers.

## Using the Project

To utilize this project, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Elkholtihm/Finger-Counting-using-Hand-Tracking.git
    ```

2. Ensure you have all the necessary dependencies installed. You can install them using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Finger Counter

To run the finger counting script, execute the `FingerCounter.py` file:

```bash
python FingerCounter.py
```

## Hand Tracking Module
The HandTrackingModule.py file contains the HandDetector class, which includes methods to:

Track hand landmarks
Provide the coordinates of the hand landmarks

## Finger Counter Script
The FingerCounter.py script uses the HandDetector module to count the number of raised fingers. The script performs the following steps:

* Capture video from a webcam.
* Track hand landmarks.
* Count the number of raised fingers based on the positions of specific landmarks.
* Display the video with the number of raised fingers.

## Connect with me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hamza-kholti-075288209/)

## Acknowledgments
[![Mediapipe Documentation](https://img.shields.io/badge/Mediapipe-Documentation-0A66C2?style=for-the-badge&logo=mediapipe&logoColor=white)](https://ai.google.dev/edge/mediapipe/solutions/guide) 
[![OpenCV Documentation](https://img.shields.io/badge/OpenCV-Documentation-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
