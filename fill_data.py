import math
import os
import random
import re
import sys

import math
import os
import random
import re
import sys

def calcMissing(readings):
    # Number of data rows
    n = len(readings)
    
    # Initialize lists to hold timestamps and mercury levels, including missing entries
    timestamps = []
    mercury_levels = []
    missing_indices = {}
    
    # Process each line of input
    for i in range(n):
        line = readings[i].strip().split("\t")
        timestamps.append(line[0])  # Store timestamp
        
        value = line[1]
        # Check if the line contains a missing value
        if "Missing" in value:
            missing_label = value  # Store the missing label, e.g., "Missing_1"
            mercury_levels.append(None)  # Use None to mark the missing value
            missing_indices[missing_label] = i  # Save index for later
        else:
            mercury_levels.append(float(value))  # Store valid mercury level as float
    
    # Perform linear interpolation to fill in missing values
    for i in range(n):
        if mercury_levels[i] is None:
            # Find the closest previous and next known values for interpolation
            prev_index, next_index = i - 1, i + 1
            
            # Move backwards to find the last known value before the missing entry
            while prev_index >= 0 and mercury_levels[prev_index] is None:
                prev_index -= 1
            
            # Move forwards to find the next known value after the missing entry
            while next_index < n and mercury_levels[next_index] is None:
                next_index += 1
            
            # Calculate interpolated value if both neighbors are found
            if prev_index >= 0 and next_index < n:
                # Linear interpolation formula
                prev_value = mercury_levels[prev_index]
                next_value = mercury_levels[next_index]
                interpolated_value = prev_value + (next_value - prev_value) * ((i - prev_index) / (next_index - prev_index))
                mercury_levels[i] = interpolated_value
            elif prev_index >= 0:
                # Use the last known previous value if no next value is found
                mercury_levels[i] = mercury_levels[prev_index]
            elif next_index < n:
                # Use the next known value if no previous value is found
                mercury_levels[i] = mercury_levels[next_index]
    
    # Print the missing values in the order of "Missing_1" to "Missing_20"
    for label, index in missing_indices.items():
        print(f"{label}: {mercury_levels[index]:.6f}")



sample_data = [
    "2023-01-01 12:00\t26.4",
    "2023-01-02 12:00\tMissing_1",
    "2023-01-03 12:00\t27.0",
    "2023-01-04 12:00\t28.5",
    "2023-01-05 12:00\tMissing_2",
    "2023-01-06 12:00\t30.2",
    "2023-01-07 12:00\t31.4",
    "2023-01-08 12:00\tMissing_3",
    "2023-01-09 12:00\t30.8",
    "2023-01-10 12:00\t29.7",
    "2023-01-11 12:00\tMissing_4",
    "2023-01-12 12:00\t28.1",
    "2023-01-13 12:00\t26.9",
    "2023-01-14 12:00\tMissing_5",
    "2023-01-15 12:00\t25.4"
]

calcMissing(sample_data)




