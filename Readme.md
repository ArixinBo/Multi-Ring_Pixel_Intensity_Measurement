
Streamlined Analysis of Sample Mass Loss via Intensity Changes Using Jython

Align and Save Image Stacks: First, to align image stacks, install and learn about the cvTemplate_Matching/stack alignment by following the instructions at this ([link](https://sites.google.com/site/qingzongtseng/template-matching-ij-plugin))

Selecting Samples of Interest: Use ImageJ's multi-point tool to accurately identify the centers of protein particles.

Generating Pixel Coordinates: Under the Analyze menu, select Set Measurements, click on Center of mass, and set Decimal places to 0. Uncheck Save row/column headers in the Result options. This action produces a list of X,Y coordinates for the selected pixels.

Saving Coordinates: Export the coordinates list as a .txt file to the same directory as the image. The Jython script will reference this directory.

Running Jython Scripts: In ImageJ, set the scripting language to Jython. Execute the 'Pixel_Intensity.py' script, inputting the outer and inner radii (in pixels) of the ring-shaped sample; use '0' inner radius for the circular sample. To visually mark selected positions, run the 'Marking_Sample_Location.py' script, which displays the chosen sample locations.   
 
