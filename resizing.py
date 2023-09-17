import cv2
# print(cv2.__version__)
import easyocr

# Load the image
# image = cv2.imread('image_to_latex/test2.png') # 1024 x 192
image = cv2.imread('latex_to_response/result_image.png') # 200 x 100



# Define the ROI containing the objects
# x, y, width, height = 0, 0, 1024, 192  # Adjust these values accordingly
x, y, width, height = 0, 0, 200, 100  # Adjust these values accordingly

# Crop the ROI from the image
roi = image[y:y+height, x:x+width]
for row in roi:
    print(row)

# Convert the ROI to grayscale (if needed)
gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
for row in gray_roi:
    print(row)

# Threshold the grayscale image to segment objects
_, binary_roi = cv2.threshold(gray_roi, 128, 255, cv2.THRESH_BINARY)
# cv2.imwrite('roi_image.jpg', binary_roi)
binary_roi = cv2.bitwise_not(binary_roi)
# Find contours of objects in the binary image
contours, _ = cv2.findContours(binary_roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Measure the size of each detected object in pixels
for contour in contours:
    object_area = cv2.contourArea(contour)
    object_width = cv2.boundingRect(contour)[2]
    object_height = cv2.boundingRect(contour)[3]
    
    # Print the size of the object in pixels
    print(f"Object Area: {object_area} pixels^2")
    print(f"Object Width: {object_width} pixels")
    print(f"Object Height: {object_height} pixels")
    print()

# reader = easyocr.Reader(['en'])  # Replace 'en' with the language you're working with
# results = reader.readtext(image)
# top = 0
# bottom = 0
# for (bbox, text, prob) in results:
#     (top_left, top_right, bottom_right, bottom_left) = bbox
#     top = max(top, top_left)
#     bottom = min(bottom, bottom_left)
#     top_left = tuple(map(int, top_left))
#     bottom_right = tuple(map(int, bottom_right))

#     # Draw a bounding box around the character using OpenCV
#     cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
# print(top, bottom)
# cv2.imwrite('image.jpg', image)
# cv2.imshow('Handwritten Character with Bounding Boxes', image)
