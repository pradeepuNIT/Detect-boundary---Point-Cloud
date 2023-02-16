import cv2
import numpy as np
import json

def detect_boundary(img):
    """Detects the boundary of an image and its line segments.

    Args:
        img_path (str): Path to the input image.

    Returns:
        tuple: A tuple containing the boundary image and line segments image.
    """
    image = cv2.imread(img)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(3,3),0)
    kernel = np.ones((3,3),np.uint8)

    closing = cv2.morphologyEx(blur,cv2.MORPH_CLOSE,kernel)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
    erosion = cv2.erode(closing,kernel,iterations = 1)

    boundary_img = closing - erosion
    # cv2.imshow("Original Image", image)
    # cv2.imshow("boundary_img", boundary_img)

    # Detect line segments using LSD
    lsd = cv2.createLineSegmentDetector(0)
    lines = lsd.detect(gray)[0] 

     # Draw the detected lines
    lines_img = np.zeros_like(image)
    for line in lines:
        x1, y1, x2, y2 = map(int, line[0])  # Convert from float to int
        cv2.line(lines_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Store line segments in a JSON file
    line_list = []
    for line in lines:
        x1, y1, x2, y2 = map(int, line[0])
        line_dict = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
        line_list.append(line_dict)
    
    with open('BIM.json', 'w') as f:
        json.dump(line_list, f)
    
    return boundary_img, lines_img


def draw_lines_from_json(json_file, img):
    """Draws line segments on an image from a JSON file.

    Args:
        json_file (str): Path to the JSON file containing line segments.
        img (numpy.ndarray): Input image on which the line segments will be drawn.

    Returns:
        numpy.ndarray: Image with line segments drawn.
    """
    with open(json_file) as f:
        lines = json.load(f)
    
    lines_img = np.zeros_like(img)
    for item in lines:
        x1 = item['x1']
        y1 = item['y1']
        x2 = item['x2']
        y2 = item['y2']
        cv2.line(lines_img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
    
    return lines_img


if __name__=="__main__":
    image = "BIM.png"
    boundary_img, lines_img = detect_boundary(image)
    img = cv2.imread(image)
    cv2.imshow('Original Image', img)
    cv2.imshow('Boundary Image', boundary_img)
    cv2.imshow('Detected Lines using LSD', lines_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    lines_json = 'BIM.json'
    img = cv2.imread(image)
    lines_img = draw_lines_from_json(lines_json, img)
    cv2.imshow('Original Image', img)
    cv2.imshow('Detected Lines From Json', lines_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

