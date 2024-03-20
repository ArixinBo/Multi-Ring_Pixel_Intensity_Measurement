Automated analysis of protein mass loss through intensity changes in movies collected from STEM – a Jython approach

1. 	Perform stack alignment and save it to .tiff.
a.	To install and learn about cvTemplate_Matching/stack alignment, strictly follow instructions here: https://sites.google.com/site/qingzongtseng/template-matching-ij-plugin 
Align slices in stack – chose matching method: Normalized correlation coefficient. Search area is set at 0. 
b.	Plugin – registration – Linear stack alignment with SIFT (Scale-Invariant Feature Transform)


2.	Use the multi-point tool in ImageJ to select the center of protein particles. Try to center at high magnification and position it as correctly as possible.

3.	Create the pixel coordination list – under Analyze menu, select Set Measurements. Click Center of mass, and set Decimal places (0-9) to 0. In Result options, deselect Save row/column headers; click OK. This will generate a list of X,Y coordinates of the selected pixels (column 1(X) and 2(Y)).  

4.	Save as .txt file to the directory where is image is located. The Jython script will use this file directory.

5. Select 'Language' in ImageJ scripts and chose Jython. Run the script 'Pixel_Intensity.py', and add outer radius and inner radius of the protein ring (in pixels). If the protein is circular, put inner raidus value '0'.

6. To mark the selected positions, run script 'Marking_Sample_Location.py' which plots the selected sample positions.     