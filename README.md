# Mercury Level Interpolation for Missing Data

## Overview

This Python script processes time-series data that includes mercury levels measured at various times. Some of the readings may be missing, denoted by labels like `Missing_1`, `Missing_2`, etc. The goal of this script is to detect these missing values and fill them in using linear interpolation based on the known values surrounding the missing data points. The final output prints the interpolated mercury levels for the missing entries, ordered by the labels such as "Missing_1", "Missing_2", etc.

## Features

- **Detects Missing Values:** It identifies missing readings from the input data marked with labels like `Missing_1`, `Missing_2`, etc.
- **Linear Interpolation:** For each missing value, the script uses linear interpolation to estimate the value based on the previous and next valid readings.
- **Output in Order:** The missing values are output in a specific order, from "Missing_1" to "Missing_20", depending on the data.

## Code Explanation

### 1. Importing Required Libraries
The script uses the following libraries:
```python
import math
import os
import random
import re
import sys
```


These libraries are imported at the beginning of the script. Although some are not used in this version
(e.g., math, os), they can be useful for future extensions.

### 2. calcMissing Function: Detecting Missing Data

The calcMissing function processes the input data, checking for missing values (indicated by labels like Missing_1, Missing_2, etc.) and storing them accordingly. It also stores the timestamps and mercury levels.

- Input: The function takes a list of readings, where each reading is a string representing a timestamp and a mercury level. Missing values are marked with labels like Missing_1, Missing_2, etc.

- Outputs: The function identifies the missing values and stores the indices of those missing entries for later processing. It also stores the timestamps and mercury levels in two separate lists (timestamps and mercury_levels).

```python
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
```
#### What Happens Here:
- Iterating through the readings: The function loops through each reading and splits the data into timestamp and value. If the value contains a missing label (like Missing_1), it appends None to the mercury_levels list and records the index in missing_indices.
- Handling valid readings: If the value is valid, it converts it to a float and appends it to the mercury_levels list.

### 3. Interpolation: Filling Missing Values

Once the missing values are detected, the next step is interpolation. This is done by using linear interpolation to estimate the missing values based on the known readings before and after the missing entry. The `calcMissing` function performs this interpolation.

Here’s how the interpolation works:

For each missing entry:
- The function looks at the previous and next valid values (i.e., values that are not `None`).

If both previous and next valid values are found, it calculates the interpolated value using the formula:

![Interpolation](Pictures/pic)

This formula ensures the new value is proportionally spaced between the previous and next values.

- If only one neighbor is found: The function uses that neighbor to fill the missing value (either the previous or next value).
- If no neighbors are found: The missing value remains `None`, which would be unlikely given real-world data.

```python
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
```
### 4. Printing Missing Values

After filling the missing values using interpolation, the function prints the interpolated values in the order of the labels Missing_1, Missing_2, etc. This ensures that the user can see which missing values were filled and what the interpolated values are.

```python
    # Print the missing values in the order of "Missing_1" to "Missing_20"
    for label, index in missing_indices.items():
        print(f"{label}: {mercury_levels[index]:.6f}")
```

### 5. Sample Data and Function Call

Finally, the script defines a sample dataset that includes timestamps and mercury levels, some of which are marked as missing. The calcMissing function is called on this sample data to demonstrate how it handles missing values.

```python
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
```

## Understanding Linear Interpolation

**Linear interpolation** is a method used to estimate unknown values that fall between two known data points. It assumes that the rate of change between the two points is constant, meaning that the values change at a steady rate. This assumption allows us to estimate intermediate values by drawing a straight line between the known points and using the equation of that line to find the unknown value.

### Why Use Linear Interpolation?

Linear interpolation is commonly used when data is missing or sparse, especially in time-series data, such as environmental readings (temperature, humidity, mercury levels) where measurements are expected to change smoothly. It provides a simple yet effective way to estimate missing values without introducing too much computational complexity.

For example, in the case of mercury levels, if some readings are missing at certain timestamps, we can estimate these values by using the known readings before and after the missing data points.

### The Interpolation Formula

The linear interpolation formula calculates the value of a point between two known points on a straight line. The formula is as follows:

![Interpolation](Pictures/pic)

Where:
- \(x_1\) and \(x_2\) are the known x-values (e.g., timestamps or indices).
- \(y_1\) and \(y_2\) are the corresponding y-values (e.g., mercury levels) at \(x_1\) and \(x_2\).
- \(x\) is the x-value at which we want to estimate the corresponding y-value (this is where the interpolation occurs).
- The term \(\frac{{y_2 - y_1}}{{x_2 - x_1}}\) is the **slope** of the line between the two known points.

### Step-by-Step Breakdown of the Formula

1. **Determine the known values**: First, we identify the two known points (x₁, y₁) and (x₂, y₂), where we have the data, and the unknown point where we want to estimate the value.
   
2. **Find the slope**: The slope of the line between the two known points is calculated as the difference in y-values (\(y_2 - y_1\)) divided by the difference in x-values (\(x_2 - x_1\)).

3. **Apply the formula**: Once we have the slope, we calculate how far the missing x-value \(x\) is from \(x_1\) and use this to scale the difference in y-values. The result is the interpolated y-value at \(x\).

### Conclusion

Linear interpolation is an essential technique in data processing, particularly in scenarios where you need to fill in missing values in a time-series dataset. By assuming that the change between known data points is linear, it allows you to estimate intermediate values in a simple yet effective way. In this script, linear interpolation is used to fill in missing mercury levels by estimating values based on the available surrounding data. This ensures that the dataset remains continuous and ready for further analysis.

















