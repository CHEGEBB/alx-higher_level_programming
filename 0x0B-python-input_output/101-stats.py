#!/usr/bin/python3

"""
Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

import sys
import signal

def print_stats(total_size, status_code_counts):
    """Print accumulated metrics.

    Args:
        total_size (int): The accumulated file size.
        status_code_counts (dict): The accumulated count of status codes.
    """
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

def handle_interrupt(signum, frame):
    """Handle interrupt signal (CTRL + C)."""
    print("\nKeyboardInterrupt detected. Printing statistics...")
    print_stats(total_file_size, status_code_counts)
    sys.exit(0)

# Set up the interrupt handler
signal.signal(signal.SIGINT, handle_interrupt)

# Initialize variables
total_file_size = 0
status_code_counts = {}
line_count = 0

try:
    # Read input line by line
    for line in sys.stdin:
        # Extract relevant information from the log entry
        parts = line.split()
        if len(parts) >= 9:
            status_code = parts[-2]
            file_size = int(parts[-1])
            
            # Update total file size
            total_file_size += file_size
            
            # Update status code counts
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

            # Print statistics every 10 lines
            line_count += 1
            if line_count == 10:
                print_stats(total_file_size, status_code_counts)
                line_count = 0

except KeyboardInterrupt:
    # Handle keyboard interrupt separately
    handle_interrupt(signal.SIGINT, None)
