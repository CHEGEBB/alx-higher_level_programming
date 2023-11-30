#!/usr/bin/python3
import dis
from magic_calculation_102 import magic_calculation

# Example usage and print the result
result = magic_calculation(10, 5)
print("Result:", result)

# Print disassembled bytecode
dis.dis(magic_calculation)

