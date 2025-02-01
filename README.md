# Image Templating and Orientation using OpenCV

## Overview
This project demonstrates image templating and orientation detection using OpenCV. The primary objective is to identify a template (e.g., an apple) in a given image and determine its orientation.

## Features
- **Template Matching:** Finds the template object in a larger image.
- **Orientation Detection:** Determines the rotation of the detected object.
- **OpenCV Methods:** Uses `cv2.matchTemplate()`, edge detection, and rotation correction.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install opencv-python numpy
```

## Sample Images
We use sample images such as an apple for demonstration. The template image contains the reference object, and the target image has the object in different positions.

## Implementation
### 1. Load Images
```python
import cv2
import numpy as np

image = cv2.imread('target_image.jpg', 0)  # Load target image in grayscale
template = cv2.imread('template.jpg', 0)  # Load template image in grayscale
```

### 2. Template Matching
```python
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
h, w = template.shape
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)
```

### 3. Orientation Detection
```python
edges = cv2.Canny(template, 50, 200)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)
for rho, theta in lines[:, 0]:
    angle = np.degrees(theta)
    print(f'Object detected at angle: {angle} degrees')
```

## Results
- The template is identified in the target image.
- The orientation angle is detected and displayed.

## Future Enhancements
- Implementing real-time detection.
- Improving accuracy with deep learning-based approaches.

## Contact
For queries or contributions, feel free to reach out!

