from ultralytics import YOLO
import json
import cv2 as cv
from utils import get_license_plate

# Reading configurations
config = json.load(open("config.json", "r", encoding="utf-8"))

# Loading the models
license_plate_detection = YOLO(config["model_paths"]["license_plate_detection"])

# Source
source = {}
for item in config["source"]:
    if item != None:
        source = { "source": item, "value": config["source"][item] }

# Opening the cap this will work for images, videos, camera, url
cap = cv.VideoCapture(source["value"])

while True:
    ret, frame = cap.read() # Read the cap and unpack frame and ret

    if not ret: break

    # Extract results
    prediction = license_plate_detection.predict(source=frame, stream=True, imgsz=640)
    license_number = get_license_plate(frame, prediction)
    
    print(license_number) # All the license number in an dict !!!!