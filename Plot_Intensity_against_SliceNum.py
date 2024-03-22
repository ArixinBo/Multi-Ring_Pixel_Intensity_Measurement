import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Loading the coordinate file
file_path = ''  

# Read the data
data = pd.read_csv(file_path, sep='\t')

# Pivot the table to have slice numbers as rows and sample positions as columns with mean intensities as values
pivoted_data = data.pivot(index='Slice', columns='Sample_Position', values='Mean_Intensity')

# Plot each sample position as a separate line
plt.figure(figsize=(12, 8))
for column in pivoted_data.columns:
    plt.plot(pivoted_data.index, pivoted_data[column], marker='o', linestyle='-', label=f'Sample {column}')

plt.xlabel('Slice Number')
plt.ylabel('Mean Intensity')
plt.title('Mean Intensity Change Across Slices for Each Sample Position')
plt.legend(title='Sample Position', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()

