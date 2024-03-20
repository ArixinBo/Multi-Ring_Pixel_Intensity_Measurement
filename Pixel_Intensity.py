from ij import IJ, WindowManager
from ij.gui import GenericDialog, OvalRoi, ShapeRoi
from ij.measure import ResultsTable
import os

def getRadiusInput():
    gd = GenericDialog("Radius Input")
    gd.addNumericField("Outer radius (px):", 40, 0)  # Default value 40, 0 decimal places
    gd.addNumericField("Inner radius (px):", 15, 0)  # Default value 15, 0 decimal places
    gd.showDialog()
    if gd.wasCanceled():
        print("User canceled dialog!")
        return None, None
    # User input values
    outer_radius = gd.getNextNumber()
    inner_radius = gd.getNextNumber()
    return outer_radius, inner_radius

def measureRingAtCoordinates(center_x, center_y, outer_radius, inner_radius, imp):
    imp.killRoi()  # Clear any existing ROI
    
    # Define the ring-shaped ROI
    outer_oval = OvalRoi(center_x - outer_radius, center_y - outer_radius, outer_radius * 2, outer_radius * 2)
    inner_oval = OvalRoi(center_x - inner_radius, center_y - inner_radius, inner_radius * 2, inner_radius * 2)
    ring_shape = ShapeRoi(outer_oval).not(ShapeRoi(inner_oval))
    imp.setRoi(ring_shape)

    # Ensure the global ResultsTable is reset before measurement
    ResultsTable.getResultsTable().reset()

    # Perform the measurement
    IJ.run("Measure")

    # Retrieve the measurement result
    rt = ResultsTable.getResultsTable()
    if rt.getCounter() > 0:
        area = rt.getValueAsDouble(rt.getColumnIndex("Area"), 0)
        mean_intensity = rt.getValueAsDouble(rt.getColumnIndex("Mean"), 0)
        return area, mean_intensity
    else:
        return "No measurement", "No measurement"

# Set measurement settings
IJ.run("Set Measurements...", "area mean redirect=None decimal=3")

# Load the image
imp = WindowManager.getCurrentImage()
if imp is None:
    print("No image open")
    exit()

# Manually get radius input from user
outer_radius, inner_radius = getRadiusInput()
if outer_radius is None or inner_radius is None:
    exit()

# Run this if the the radii are fixed and the program requires full automation
#outer_radius = 40 # unit in pixel 
#inner_radius = 15 # unit in pixel


# Define file paths (kept unchanged as per your request)
input_file_path = 'C:/Users/'  # update this directory with your file containing pixel coordinates of the sample of interest.
output_file_path = os.path.splitext(input_file_path)[0] + '_measurements.txt'

# Read the coordinates
coordinates = []
with open(input_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) >= 4:
            coordinates.append((int(parts[2]), int(parts[3])))    # ImageJ generate X, and Y pixel coordinates at column 2 , 3. Adjust these numbers accordingly. 

for cor in coordinates:
	print(cor)

# Iterate, measure, and store results
measurements = []
for x, y in coordinates:
    area, mean_intensity = measureRingAtCoordinates(x, y, outer_radius, inner_radius, imp)
    measurements.append((x, y, area, mean_intensity))

# Write measurements to file
with open(output_file_path, 'w') as outfile:
    outfile.write("X_coord\tY_coord\tArea\tMean_Intensity\n")
    for x, y, area, mean_intensity in measurements:
        outfile.write("{}\t{}\t{}\t{}\n".format(x, y, area, mean_intensity))

print("Mean Intensity Measurements saved to: {}".format(output_file_path))
IJ.selectWindow("Results")
IJ.run("Close")