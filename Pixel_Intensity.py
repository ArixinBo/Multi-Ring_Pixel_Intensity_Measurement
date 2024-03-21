from ij import IJ, WindowManager
from ij.gui import OvalRoi, ShapeRoi
from ij.measure import ResultsTable
import os

def getRadiusInput():
    """Prompt user for outer and inner radii of the ring."""
    from ij.gui import GenericDialog
    gd = GenericDialog("Radius Input")
    gd.addNumericField("Outer radius (px):", 40, 0)
    gd.addNumericField("Inner radius (px):", 20, 0)
    gd.showDialog()
    if gd.wasCanceled():
        return None, None
    outer_radius = gd.getNextNumber()
    inner_radius = gd.getNextNumber()
    return outer_radius, inner_radius

def measureIntensityInRing(imp, x, y, outer_radius, inner_radius):
    """Measure mean intensity within a specified ring for the given image and return results."""
    imp.killRoi()  # Clear any existing ROI
    
    # Create the ring ROI
    outer_oval = OvalRoi(x - outer_radius, y - outer_radius, 2 * outer_radius, 2 * outer_radius)
    inner_oval = OvalRoi(x - inner_radius, y - inner_radius, 2 * inner_radius, 2 * inner_radius)
    ring_roi = ShapeRoi(outer_oval).not(ShapeRoi(inner_oval))
    
    imp.setRoi(ring_roi, False)
    IJ.run(imp, "Measure", "")
    rt = ResultsTable.getResultsTable()

    mean_intensity = rt.getValue("Mean", rt.getCounter()-1)
    area = rt.getValue("Area", rt.getCounter()-1)
    
    return area, mean_intensity

# Define file paths
input_file_path = r'C:\Users\'  # Update this with the actual path to your coordinates file
output_file_path = os.path.splitext(input_file_path)[0] + '_measurements.txt'

# Read the coordinates from the file
coordinates = []
with open(input_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) >= 2:  # Adjust according to your file
            coordinates.append((int(parts[2]), int(parts[3])))  # # ImageJ generate X, and Y pixel coordinates at column 2 , 3. Adjust these numbers accordingly.

# Load the image or movie
imp = WindowManager.getCurrentImage()
if imp is None:
    print("No image open.")
    exit()

# Get user input for radii
outer_radius, inner_radius = getRadiusInput()
if outer_radius is None or inner_radius is None:
    exit()

# Run this if the radii are fixed and the program requires full automation
#outer_radius = 40 # unit in pixel 
#inner_radius = 15 # unit in pixel

# Prepare to write measurements
with open(output_file_path, 'w') as outfile:
    outfile.write("Slice\tSample_Position\tX_coord\tY_coord\tArea\tMean_Intensity\n")

    slices = imp.getNSlices()
    for slice in range(1, slices + 1):
        imp.setSlice(slice)
        for index, (x, y) in enumerate(coordinates, start=1):
            area, mean_intensity = measureIntensityInRing(imp, x, y, outer_radius, inner_radius)
            outfile.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(slice, index, x, y, area, mean_intensity))

print("Measurements saved to: {}".format(output_file_path))
