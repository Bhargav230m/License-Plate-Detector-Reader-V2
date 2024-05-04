import easyocr
import json
import cv2 as cv

# Function to preprocess the frame
def preprocess(image):
    """
    Preprocess the image

    Args:
    image (numpy.ndarray): An image

    Returns:
    numpy.ndarray: The preprocessed image
    """

    img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # Converts the image to grayscale
    _, thresholded_image = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)  # Getting the threshold of the image
    img = cv.bitwise_not(thresholded_image)
    img = cv.erode(img, (9, 9), 8)  # Eroding to get a better and ligthen up image
    
    return img

def read_license_plate(cropped_image):
    """
    Reads the license plate information from a cropped image.

    Args:
    cropped_image (numpy.ndarray): A cropped image containing a license plate.

    Returns:
    dictionary: The read data
    Example: { "plate_1": "Example Plate" ...etc }
    """
    license_counter = 1
    license_dict = {}

    for image in cropped_image:
        if image is not None:
            reader = easyocr.Reader(['en'])  # Initializes the readerimg = preprocess(cropped_image)  # Preprocess the crop
            result = reader.readtext(image)  # Read the license plate text
            number = [item[1] for item in result] # Get the license number

            license_dict[f"plate_{license_counter}"] = number
            license_counter += 1

    return license_dict

def get_license_plate(frame, prediction):
    """
    Extracts license plates or car crops from a frame.

    Args:
    - frame: Input frame/image.
    - license_plate_model: Model for license plate detection.s.

    Returns:
    - Cropped image of the detected object (license plate).
    - None if nothing is detected
    """

    cropped_images = []

    for dec_results in prediction:
        if dec_results:
            result = json.loads(dec_results.tojson())[0]["box"] # Results to json
            cropped_img = frame[int(result["y1"]):int(result["y2"]), int(result["x1"]):int(result["x2"])] # Cropped image
            cropped_images.append(cropped_img)
        else: 
            cropped_images.append(None)
    read_number = read_license_plate(cropped_images)
    return read_number