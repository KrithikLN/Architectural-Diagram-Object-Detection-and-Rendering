This project focuses on detecting and rendering architectural elements from diagram images

__File Structure:__

⋅⋅* ArchTrain.pt: trained YOLOv7 model weight used for object detection.

⋅⋅* ObjectCropping.ipynb: Notebook for cropping detected objects from Architectural Diagrams.

⋅⋅* WallCoordinatesAndRendering.ipynb: Notebook for extracting wall coordinates and rendering layouts.
 
⋅⋅* WallCoordinatesRenderingInteractive.ipynb: Interactive notebook for interactive visualization 

⋅⋅* WallCoordinatesRenderingInteractive.py: Python script version of the interactive rendering tool.

⋅⋅* WallsWithObjects.ipynb: Notebook combining wall structures with overlayed objects.

⋅⋅* wall_coordinates.json: JSON file containing extracted wall coordinates.

⋅⋅* wall_coordinates_without_doors.json: JSON file with wall coordinates excluding doors.

⋅⋅* cropped_images/: Directory containing cropped images of detected objects.

⋅⋅* images/test/: Test images used for detection and rendering.

We have used the ROBIN Dataset for the images
