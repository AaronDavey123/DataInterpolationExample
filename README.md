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

![Alt Text](Pictures/Screenshot_2024-11-29_125858.png)

This formula ensures the new value is proportionally spaced between the previous and next values.

- If only one neighbor is found: The function uses that neighbor to fill the missing value (either the previous or next value).
- If no neighbors are found: The missing value remains `None`, which would be unlikely given real-world data.

```python
# Example of calcMissing function for linear interpolation in Python
import numpy as np
















