![Open CV Github Frame](https://github.com/TH-Activities/saturday-hack-night-template/assets/90635335/78554b37-32b2-4488-a10c-5c68098d7776)



# Project Name: Yoshikage
This document scanner project is a Python-based tool that transforms images of documents into high-quality, perspective-corrected, and thresholded scans. The project provides an interactive user interface for selecting document corners, allows users to choose between vertical and horizontal orientations, and outputs both the thresholded image and a PDF version for easy document archiving.
## Team members
1. [Sean Mathen Mathew](https://github.com/mrsean2005/)
2. [Bharath R Padmanabh](https://github.com/MrWonder2/)
## Link to product walkthrough
[link to video](https://www.youtube.com/watch?v=Z7xmvlP1ugk)
## How it Works ?

1. Corner Selection:
     User clicks on four document corners in an image.

2. Orientation Input:
     User chooses document orientation (vertical/horizontal).

3. Perspective Correction:
     Calculates and applies a perspective transformation.

4. Grayscale Conversion:
     Converts the perspective-corrected image to grayscale.

5. Adaptive Thresholding:
     Applies adaptive thresholding for better contrast.

6. Optional Erosion:
     Optional step for further image refinement.

7. Export Results:
     Displays and saves the high-res image and PDF scan.
   
## Libraries used
1. OpenCV
2. Numpy
3. Pillow
4. ReportLab
## How to configure
```pip install opencv-python numpy pillow reportlab```
## How to Run
py app.py
Select 4 points
Choose v/h for oreintation
