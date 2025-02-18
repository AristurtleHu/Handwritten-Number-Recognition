# Handwritten Digit Recognition using KNN Algorithm on Raspberry Pi

This project demonstrates the recognition of handwritten digits using the **K-Nearest Neighbors (KNN)** algorithm on a **Raspberry Pi**. It processes images of handwritten digits, applies necessary image preprocessing, and displays the recognition results on a digital display.

## Project Overview

The goal of this project is to build a system capable of recognizing handwritten digits, process the images using image processing techniques, and display the recognized digits on a screen. The steps include:

- **Image Preprocessing** (Convert image to two colors, segmentation, resizing, and erosion)
- **Model Training** using KNN Algorithm for handwritten digit recognition
- **Digital Display** integration to show the recognition result

## Components

### 1. Model Training (KNN Algorithm)
We use the **K-Nearest Neighbors (KNN)** algorithm to classify handwritten digits. The KNN classifier works by comparing the feature vectors of the input image to a training set of labeled digit images. The label of the most similar training examples is chosen as the predicted digit.

### 2. Image Processing
Several preprocessing steps are applied to convert raw image data into a suitable format for classification:

- **Convert to Two Colors (Binarization)**:
  Convert the grayscale image to a binary (black and white) image, which simplifies the digit recognition process.
  
- **Segmentation**:
  If multiple digits are detected in the image, they are segmented to ensure each digit is processed individually.
  
- **Resize to Square**:
  Resize the digit image to a fixed size (e.g., 28x28 pixels), which is compatible with the KNN classifier’s input requirement.
  
- **Erosion**:
  Apply an erosion operation to remove noise and improve the clarity of the digit, making it easier for the classifier to recognize.

### 3. Digital Display Integration
Once the digit is recognized by the KNN model, the result is displayed on a **LCD/LED display** connected to the Raspberry Pi. The system provides real-time digit recognition feedback on the display.

## How It Works

1. **Image Capture**:
   The system uses a camera module connected to the Raspberry Pi to capture an image of a handwritten digit.

2. **Preprocessing**:
   The captured image undergoes various preprocessing techniques (binarization, segmentation, resizing, erosion) to prepare it for digit classification.

3. **Recognition**:
   The processed image is fed into the pre-trained KNN classifier to predict the digit.

4. **Display the Result**:
   After classification, the recognized digit is shown on a digital display connected to the Raspberry Pi.

## Requirements

- Raspberry Pi (any model with camera support)
- Camera Module (for capturing handwritten digits)
- LCD/LED Display (to show the recognition result)
- Python with OpenCV and scikit-learn libraries for image processing and machine learning

## How to Use

1. Connect the Raspberry Pi to the camera module and LCD/LED display.
2. Run the code on the Raspberry Pi to capture an image of a handwritten digit.
3. The system processes the image, recognizes the digit, and displays the result on the screen.

## Conclusion

This project is an application of basic image processing and machine learning techniques to recognize handwritten digits in real-time on a Raspberry Pi. It highlights the use of the KNN algorithm for classification and demonstrates how image preprocessing can improve recognition accuracy.

## Future Enhancements

- Integrating other machine learning algorithms (e.g., SVM, CNN) for improved accuracy.
- Adding support for recognizing more complex handwritten text.
- Optimizing the system for faster recognition on the Raspberry Pi.

