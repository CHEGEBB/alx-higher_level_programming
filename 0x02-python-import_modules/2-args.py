#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1  # subtract 1 to exclude the script name
args = sys.argv[1:]

print("{} argument{}:".format(num_args, 's' if num_args != 1 else '') + ('.' if num_args == 0 else ''))
for i, arg in enumerate(args, start=1):
    print("{}: {}".format(i, arg))
    
