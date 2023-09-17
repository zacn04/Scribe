import cv2
from PIL import Image
from PIL.Image import fromarray
import numpy as np
<<<<<<< HEAD
from handwriting import main 
=======
>>>>>>> 9125d73 (tys first commit)


def find_four_edges_of_text(image, highlighted_coords, notepad_coords):
    """find the 4 edges of text within text box corners
    """    
    h_top, h_bottom, h_left, h_right = highlighted_coords
    n_top, n_bottom, n_left, n_right = notepad_coords
    

    # Define the ROI containing the objects
    # x, y, width, height = 0, 0, 1024, 192  # Adjust these values accordingly

    # Crop the ROI from the image
    roi = image[h_top:h_bottom, h_left:h_right]

<<<<<<< HEAD
    # Convert the ROI to grayscale (if needed)
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
=======
    print(highlighted_coords)
    # Convert the ROI to grayscale (if needed)
    # print("shape",roi.shape)
    gray_roi = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
>>>>>>> 9125d73 (tys first commit)

    # Threshold the grayscale image to segment objects
    _, binary_roi = cv2.threshold(gray_roi, 128, 255, cv2.THRESH_BINARY)

    binary_roi = cv2.bitwise_not(binary_roi)
    # Find contours of objects in the binary image
    contours, _ = cv2.findContours(binary_roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Measure the size of each detected object in pixels
<<<<<<< HEAD
    top, bottom, left, right = n_bottom, n_top, n_right, n_left
=======
    top, bottom, left, right = n_bottom, -69, n_right, n_left
>>>>>>> 9125d73 (tys first commit)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        t = y
        b = y + h
        l = x
        r = x + w

        top = min(top, t)
        bottom = max(bottom, b)
        left = min(left, l)
        right = max(right, r)
<<<<<<< HEAD
=======

        # object_area = cv2.contourArea(contour)
        # object_width = cv2.boundingRect(contour)[2]
        # object_height = cv2.boundingRect(contour)[3]
        
        # # Print the size of the object in pixels
        # print(f"Object Area: {object_area} pixels^2")
        # print(f"Object Width: {object_width} pixels")
        # print(f"Object Height: {object_height} pixels")
>>>>>>> 9125d73 (tys first commit)
    return (top, bottom, left, right)

def resize_image(object_coords, image):
    height, width = image.shape[:2]
    aspect_ratio = width / height
    desired_height = object_coords[1] - object_coords[0]
    desired_width = int(desired_height*aspect_ratio)
    output_image = cv2.resize(image, (desired_width, desired_height))
    return output_image

def find_open_spot(notepad_coords, object_coords, image):
    # image_dim = l x r
    o_top, o_bottom, o_left, o_right = object_coords
    n_top, n_bottom, n_left, n_right = notepad_coords
    height, width = image.shape[:2]
<<<<<<< HEAD
    print(height, width)
    if n_right - o_right >= width:
        return (o_top, o_bottom, o_left, width)
    return (o_top+height, o_bottom+height, o_left, o_left+width)

def cv_to_pil(cv_image):
    numpy_array = cv2.cvtColor(cv_image, cv2.COLOR_BGRA2RGBA)
    pil_image = Image.fromarray(numpy_array)
    return pil_image

def pil_to_cv(pil_image):
    pil_image_array = np.array(pil_image)
    cv2_image = cv2.cvtColor(pil_image_array, cv2.COLOR_RGBA2BGRA)
    return cv2_image

def insert_image(pil_image, highlighted_coords, notepad_coords):
    """Call me

    Args:
        pil_image (_type_): _description_
        highlighted_coords (_type_): _description_
        notepad_coords (_type_): _description_

    Returns:
        _type_: _description_
    """    
    cv2_image = pil_to_cv(pil_image)
    object_coords = find_four_edges_of_text(cv2_image, highlighted_coords, notepad_coords)
=======
    if n_right - o_right >= width:
        return (o_top, o_bottom, o_left, width)
    return (o_top-height, o_bottom-height, o_left, o_left+width)

def cv_to_pil(cv_image):
    numpy_array = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGBA)
    pil_image = Image.fromarray(numpy_array)
    return pil_image

def get_new_size(object_coords, image):
    print("coords",object_coords)
    height, width = image.shape[:2]
    aspect_ratio = width / height
    desired_height = object_coords[1] - object_coords[0]
    desired_width = int(desired_height*aspect_ratio)
    return desired_width, desired_height 

def insert_image(pil_image, highlighted_coords, notepad_coords):
    pil_image = pil_image.convert('RGB') 
    pil_image_array = np.array(pil_image)

    cv2_image = cv2.cvtColor(pil_image_array, cv2.COLOR_RGB2BGR)
    object_coords = find_four_edges_of_text(cv2_image, highlighted_coords, notepad_coords)
    print("new size",get_new_size(object_coords, cv2_image))
>>>>>>> 9125d73 (tys first commit)
    resized_image = resize_image(object_coords, cv2_image)
    open_coords = find_open_spot(notepad_coords, object_coords, resized_image)
    pil_image = cv_to_pil(resized_image)
    return (open_coords, pil_image)
<<<<<<< HEAD

if __name__ == "__main__":
    pil_image1 = main.process_text_to_image("1+1")
    print(pil_image1)
    pil_image2 = main.process_text_to_image("2+2")
    cv_image1 = pil_to_cv(pil_image1)
    cv_image2 = pil_to_cv(pil_image2)

    resized_cv_image2 = resize_image((0, 10, 0, 0), cv_image2)
    four_edges = find_four_edges_of_text(cv_image1, (20, 40, 0, 50), (0, 93, 0, 56))
    print(four_edges)
    openspot = find_open_spot((0, 93, 0, 56), four_edges, resized_cv_image2)
    print(openspot)
    # print(resized_cv_image2)
=======
>>>>>>> 9125d73 (tys first commit)
    