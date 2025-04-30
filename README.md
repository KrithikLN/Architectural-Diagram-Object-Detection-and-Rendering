Architectural Diagram Object Detection and Rendering
====================================================

This project focuses on detecting and rendering architectural elements from diagram images

## __Repository Structure:__

* ArchTrain.pt: trained YOLOv7 model weight used for object detection.

* ObjectCropping.ipynb: Notebook for cropping detected objects from Architectural Diagrams.

* WallCoordinatesAndRendering.ipynb: Notebook for extracting wall coordinates and rendering layouts.
 
* WallCoordinatesRenderingInteractive.ipynb: Interactive notebook for interactive visualization 

* WallCoordinatesRenderingInteractive.py: Python script version of the interactive rendering tool.

* WallsWithObjects.ipynb: Notebook combining wall structures with overlayed objects.

* wall_coordinates.json: JSON file containing extracted wall coordinates.

* wall_coordinates_without_doors.json: JSON file with wall coordinates excluding doors.

* cropped_images/: Directory containing cropped images of detected objects.

* images/test/: Test images used for detection and rendering.

We have used the [ROBIN](https://github.com/gesstalt/ROBIN) Dataset for the images

## __Getting Started__
__Requirements:__
* Python 3.x
* opencv-python
* matplotlib
* numpy
* json
* Install the required packages using pip:
 ```
 pip install torch opencv-python matplotlib numpy
 ```
## __Usage:__
1. Clone the Repository:
 ```
 git clone https://github.com/KrithikLN/Architectural-Diagram-Object-Detection-and-Rendering.git
 ```
2. Run the ObjectCropping.ipynb notebook to detect architectural elements in images and crop them for further processing.
3. Use the WallCoordinatesAndRendering.ipynb notebook to extract wall coordinates from diagrams and render the architectural layout.
4. Execute the WallCoordinatesRenderingInteractive.py script to visualize and interact with the renderings.

## __LICENSE:__
This project is licensed under the GNU General Public License

