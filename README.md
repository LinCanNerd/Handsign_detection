# Hand Gesture Recognition using Computer Vision

## Introduction

This repository contains a Python-based project that utilizes computer vision techniques and popular libraries such as OpenCV, Scikit-learn, and Mediapipe to analyze hand gestures in real-time using a webcam. The goal of this project is to create a system capable of recognizing and classifying different hand gestures, allowing users to interact with technology in a more intuitive and natural way, ultimately making it more accessible.

## Features

- Real-time hand gesture recognition using a webcam.
- Execution of various commands on a PC based on recognized gestures.
- Utilizes computer vision algorithms for background subtraction, hand segmentation, feature extraction, and classification.
- Supports a wide range of hand gestures for controlling devices or software.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following dependencies installed:

- Python (3.6 or higher)
- OpenCV
- Scikit-learn
- Mediapipe
- Webcam or camera device

You can install the required Python packages using `pip`:

```bash
pip install opencv-python scikit-learn mediapipe
```

### Usage

1. Clone this repository:

```bash
git clone https://github.com/yourusername/hand-gesture-recognition.git
cd hand-gesture-recognition
```

2. Run the main script:

```bash
python main.py
```

3. Use your webcam to interact with the system by performing various hand gestures. The system will recognize the gestures and trigger corresponding actions.

## Technical Details

Throughout the project, we employ various methodologies and algorithms to process video frames and extract meaningful hand gesture information. Some of the key technical aspects include:

- Background subtraction: Removing the background to isolate the hand.
- Hand segmentation: Identifying and isolating the hand within the frame.
- Feature extraction: Extracting relevant features from the hand gesture.
- Classification techniques: Using machine learning to classify the recognized gesture.

For more detailed technical information, refer to the project's documentation and code.

## Challenges

While developing this project, we encountered several challenges in achieving accurate gesture recognition. Some of the common challenges include:

- Accurate background subtraction to isolate the hand.
- Robust hand segmentation techniques, especially in varying lighting conditions.
- Effective feature extraction to capture the essence of each gesture.
- Training and fine-tuning classification models for high accuracy.

## Contributing

We welcome contributions from the community. If you have ideas, bug fixes, or improvements, feel free to open an issue or submit a pull request.
\n Biziura Olha,
\n Lin Can,
\n Srymova Aruta.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We would like to express our gratitude to the open-source community and the developers of the libraries and tools that made this project possible.

---

By contributing to this project, you are helping to advance the field of computer vision and gesture-based control, making technology more accessible and intuitive for everyone. Enjoy experimenting with hand gestures and exploring the possibilities of this project!
