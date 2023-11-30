#!/usr/bin/python3
import sys

# Extract command-line arguments (excluding script name)
args = sys.argv[1:]

# Initialize a variable to store the sum
result_sum = 0

# Iterate through arguments, convert to integers, and add to the sum
for arg in args:
    result_sum += int(arg)

# Print the sum
print(result_sum)

