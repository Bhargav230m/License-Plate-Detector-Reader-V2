# License Plate Detector and Reader V2

**An Advanced License Plate Detection System**

This system leverages YOLOv8 models and EasyOCR to detect and read license plates with high accuracy.

## How It Works

The process involves several key steps:

1. **Loading the Models**  
   Initialize the YOLOv8 model for license plate detection and EasyOCR for optical character recognition (OCR).

2. **Opening the Camera**  
   You can utilize both images and videos as input sources for license plate detection.

3. **Detecting License Plates**  
   The system identifies license plates in the input, then preprocesses the detected plates for better OCR performance.

4. **Preprocessing**  
   Prepare the cropped license plate images to enhance the accuracy of the OCR model.

5. **Feeding to OCR Model**  
   Input the preprocessed license plate images into the EasyOCR model to extract the text.

6. **Output**  
   Display the detected license plate text.

**This overview provides a basic understanding of a license plate detection and reading system. For enhanced performance and accuracy, consider incorporating additional advanced techniques and refinements.**
