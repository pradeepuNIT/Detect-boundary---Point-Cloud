
## Boundary Detection On Construction Site Image

## Description

This task is an implementation of finding the boundaries of each column and beams in the construction site image and store boundaries into json.

## Requirements

Necessary packages to install

    Python=3.8.10
    cv2==4.5.4
    numpy==1.21.6
    json==2.0.9


## Usage

```sh
python boundary.py
```
 It detect the boundary of a construction site image from the file path and generate output boundary image and json file contains boundaries. 

 Load the exported json and draw the extracted boundaries on the respective image.

## Approach followed

Steps:

    1. Read the input image and convert it to grayscale.

    2. Apply a Gaussian blur to the image to remove any noise.

    3. Apply morphological closing operation to fill any gaps in the image.

    4. Apply morphological erosion to the image to separate the connected lines.

    5. Find the line segments in the image using the LSD(Line Segment Detector) algorithm.

    6. Store the line segments in a JSON file.

## Results

![BIM_detected_boundaries](https://user-images.githubusercontent.com/122999996/219460618-c357f4ef-515c-418d-a673-dc279bef9854.png)
![Camera_detected_boundaries](https://user-images.githubusercontent.com/122999996/219460612-a3dfef24-e7c6-4bc9-a638-81cd06274377.png)

