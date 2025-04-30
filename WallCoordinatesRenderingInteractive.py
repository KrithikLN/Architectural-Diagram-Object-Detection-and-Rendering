import json
import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import time

# Load wall coordinates from the JSON file
with open('wall_coordinates.json', 'r') as file:
    wall_coordinates = json.load(file)

# Parameters for wall height
wall_height = 10  # Uniform wall height

# Create a 3D figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Initialize elevation and azimuth
elev = 45
azim = 10

# Function to create wall polygons in 3D
def create_wall_polygon(coords, height):
    top_polygon = [[x, y, height] for x, y in coords]
    bottom_polygon = [[x, y, 0] for x, y in coords]
    wall_sides = []
    for i in range(len(coords)):
        next_index = (i + 1) % len(coords)
        wall_side = [
            [coords[i][0], coords[i][1], 0],
            [coords[next_index][0], coords[next_index][1], 0],
            [coords[next_index][0], coords[next_index][1], height],
            [coords[i][0], coords[i][1], height]
        ]
        wall_sides.append(wall_side)
    return top_polygon, bottom_polygon, wall_sides

# Plot walls in the scene
def plot_scene():
    ax.cla()  # Clear previous plots
    for wall in wall_coordinates:
        top_polygon, bottom_polygon, wall_sides = create_wall_polygon(wall, wall_height)

        ax.add_collection3d(Poly3DCollection([top_polygon], color='gray', alpha=0.5))
        ax.add_collection3d(Poly3DCollection([bottom_polygon], color='gray', alpha=0.5))
        for side in wall_sides:
            ax.add_collection3d(Poly3DCollection([side], color='gray', alpha=0.5))

    # Set axis limits
    all_x = [x for wall in wall_coordinates for x, _ in wall]
    all_y = [y for wall in wall_coordinates for _, y in wall]
    ax.set_xlim(min(all_x), max(all_x))
    ax.set_ylim(min(all_y), max(all_y))
    ax.set_zlim(0, wall_height)

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Height')
    ax.set_title('3D Rendering of Floor Plan')

    # Set the desired viewing angle
    ax.view_init(elev=elev, azim=azim)

# Function to update elevation and azimuth on key press
def on_key(event):
    global elev, azim
    if event.key == 'q':
        plt.close()  # Close the plot when 'q' is pressed
    elif event.key == 'up':
        elev += 5  # Increase elevation
    elif event.key == 'down':
        elev -= 5  # Decrease elevation
    elif event.key == 'left':
        azim -= 5  # Decrease azimuth
    elif event.key == 'right':
        azim += 5  # Increase azimuth

    plot_scene()  # Update the plot with the new view

# Initial plot
plot_scene()

# Connect the key press event to the on_key function
fig.canvas.mpl_connect('key_press_event', on_key)

# Show the plot and enter the main loop
plt.ion()  # Turn on interactive mode
plt.show(block=True)

# Keep the script running until 'q' is pressed
try:
    while plt.fignum_exists(fig.number):  # Check if the figure is still open
        time.sleep(0.1)  # Sleep for a short period to avoid high CPU usage
except KeyboardInterrupt:
    plt.close()  # Close the plot if interrupted
