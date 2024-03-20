Automated analysis of protein mass loss through intensity changes in movies collected from STEM – a Jython approach (20240314)

1.	Use the multi-point tool in ImageJ to select the center of protein particles. Try to center at high magnification and position it as correctly as possible.

2.	Create the pixel coordination list – under Analyze menu, select Set Measurements. Click Center of mass, and set Decimal places (0-9) to 0. In Result options, deselect Save row/column headers; click OK. This will generate a list of X,Y coordinates of the selected pixels (column 1(X) and 2(Y)).  

3.	Save as .txt file to the directory where is image is located. The Jython script will use this file directory.

4. Select 'Language' in ImageJ scripts and chose Jython. Run the script 'Pixel_Intensity.py', and add outer radius and inner radius of the protein ring (in pixels). If the protein is circular, put inner raidus value '0'.

5. To mark the selected positions, run script 'Marking_Sample_Location.py' which plots the selected sample positions.     