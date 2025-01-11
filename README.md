# OpenCV Image Processing Assignment

## Overview
This project demonstrates basic image processing techniques using OpenCV, including text overlay, drawing shapes, and saving modified images.

## Features
- **Read an image**: Load an image from a file using `cv2.imread`.
- **Add text to the image**: Overlay custom text at a specified location using `cv2.putText`.
- **Draw shapes on the image**: Create rectangles or other shapes using `cv2.rectangle`.
- **Display the image**: Show the processed image in a window using `cv2.imshow`.
- **Save the result**: Save the modified image to a file using `cv2.imwrite`.

## Requirements
- Python 3.x
- OpenCV library (`cv2`)

Install OpenCV using pip:
```bash
pip install opencv-python
```

## How to Run the Code
1. Clone this repository:
   ```bash
   git clone https://github.com/CeliaIneza/OpenCV-ImageProcessing.git
   ```
2. Navigate to the project directory:
   ```bash
   cd OpenCV-ImageProcessingAssign
   ```
3. Run the Python script:
   ```bash
   python assignment.py
   ```

## Example Workflow
The code performs the following steps:
1. Loads the image `assignment-001-given.jpg`.
2. Adds the text `RAH972U` to the image at a specific position.
3. Draws a green rectangle on the image to highlight a region.
4. Displays the processed image in a resizable window.
5. Saves the result as `my-result.jpg`.
