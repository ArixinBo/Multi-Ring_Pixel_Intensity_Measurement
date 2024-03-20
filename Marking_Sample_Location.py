# This script is design to use together with the `APIM_Jython.txt` script in ImageJ to mark the position of the sample of interest.


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


# Define file paths (kept unchanged as per your request)
input_file_path = 'C:/Users/'


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

# Assuming you've already defined the 'draw_rings_with_cross' function as given in the previous response

# Load your image,  # Make sure to update the path.
image_path = r'C:\Users\' 
image = Image.open(image_path)

# As above, coordinates is a list of tuples, each representing the (x, y) coordinates of the ring center
centers = coordinates # coordinates from the saved result file. 

#Put this numbers accordingly
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