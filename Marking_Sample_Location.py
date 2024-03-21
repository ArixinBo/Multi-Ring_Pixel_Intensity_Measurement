# This script is designed to use together with the `Pixel_Intensity.py` script in ImageJ to mark the position of the sample of interest.

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load an image
image_path = r'C:\Users\'  # Make sure to update this path
image = Image.open(image_path)

# Convert the image to a numpy array for plotting
image_array = np.array(image)

# Plot the image
plt.figure(figsize=(6, 6))  # You can adjust the figure size as needed
plt.imshow(image_array, cmap='gray')  # Adjust 'cmap' based on your image
plt.axis('on')  
plt.show()


# Define file paths 
input_file_path = 'C:/Users/'   #This is the file path for the saved coordinates.


# Read the coordinates
coordinates = []
with open(input_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) >= 4:
            coordinates.append((int(parts[2]), int(parts[3])))
            
print("The saved pixel positions in the coordinate files are as follows:")
for item in coordinates:
    print(item)

from PIL import Image

from PIL import Image, ImageDraw

# Load your image, and make sure to update the path.
image_path = r'C:\Users\'              #This is path for the image, on which the coordinates would be drawn. 



def draw_rings_with_cross(image, centers, outer_diameter, inner_diameter, ring_color=(255, 0, 0), cross_color=(0, 255, 0), cross_size=5):
    """
    Draws rings (only outlines) on the image at specified center coordinates and adds a green cross marker at each center.

    Parameters:
    - image: PIL.Image object.
    - centers: List of tuples, each representing the (x, y) coordinates of the ring center.
    - outer_diameter: Diameter of the outer circle of the ring.
    - inner_diameter: Diameter of the inner circle of the ring.
    - ring_color: Color of the ring. Default is red (255, 0, 0).
    - cross_color: Color of the cross marker. Default is green (0, 255, 0).
    - cross_size: Length of each arm of the cross in pixels.
    """
    draw = ImageDraw.Draw(image)

    for center in centers:
        x, y = center
        outer_radius = outer_diameter / 2
        inner_radius = inner_diameter / 2

        # Draw the outer circle (ring's outer boundary)
        draw.ellipse([x - outer_radius, y - outer_radius, x + outer_radius, y + outer_radius], outline=ring_color)
        
        # Draw the inner circle (ring's inner boundary). Note: We're only drawing the outline, so there's no fill between the rings.
        draw.ellipse([x - inner_radius, y - inner_radius, x + inner_radius, y + inner_radius], outline=ring_color)
        
        # Draw a green cross at the center
        draw.line([x - cross_size, y, x + cross_size, y], fill=cross_color, width=1)  # Horizontal line
        draw.line([x, y - cross_size, x, y + cross_size], fill=cross_color, width=1)  # Vertical line

    return image

# Load your image, and make sure to update the path.
image_path = r'C:\Users\' 
>>>>>>> 8d6468d1a2690d8f18a057678cec0c5656dd1932
image = Image.open(image_path)

# As above, coordinates is a list of tuples, each representing the (x, y) coordinates of the ring center
centers = coordinates # coordinates from the saved result file. 

#Put this numbers accordingly, to match your actual measurement. 
outer_diameter = 30 # unit is in pixel
inner_diameter = 15 # unit is in pixel

# Draw the rings with green crosses on the image
# Note: Using the updated function name 'draw_rings_with_cross'
modified_image = draw_rings_with_cross(
    image, centers, outer_diameter, inner_diameter, 
    ring_color=(0, 255, 0), cross_color=(255, 0, 0), cross_size=5
)

# Display or save the modified image
#modified_image.show()  

# Convert the modified image to a NumPy array for plotting
modified_image_array = np.array(modified_image)

# Plot the modified image
plt.figure(figsize=(12, 12))  # Adjust figure size as needed
plt.imshow(modified_image_array)
plt.axis('on')  
plt.show()
