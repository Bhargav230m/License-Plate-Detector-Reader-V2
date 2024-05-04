# License Plate Detector and Reader V2

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<p><strong>Click this button to get the V1 of this system - </strong> <button onclick="window.location.href='https://github.com/Bhargav230m/License-Plate-Reader/tree/main'" style="padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer;"><strong>License Plate Detector</strong></button> </p> 
</body>
</html>

---

**An advanced license plate detection system made by Bhargav Raj, It utilizes yolov8 models and easyocr to detect and read license plates**

## How does it work
**There a few steps involved before we actually read and detect license plate, below those are mentioned.**
- Loading of models (Model 1: This is to read the license plates-Model 3: EasyOcr)
- Opening the camera (can utilize images and videos)
- Detecting license plates then preprocessin it
- Feeding the preprocessed cropped license plate to the ocr model
- Output

**This are just the basic steps in making a license plate detection and reader system, You can make this more advanced and accurate</br>However, this gives us the basic overview on how to make a license plate detection and reader system.**

## What has improved
**The setup remains unchanged, but the model has improved significantly, with many noticeable changes in the code itself.**

## Why not update the previous repositry
**I chose to create a separate repository for v2 to keep it distinct from v1.**