#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stats(size, status_codes, count):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
        count (int): The number of lines processed.
    """
    print("Lines processed: {}".format(count))
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    count = 0

    try:
        for line in sys.stdin:
            count += 1

            if count % 10 == 0:
                print_stats(size, status_codes, count)

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if len(line) > 2 and line[-2] in valid_codes:
                    status_codes[line[-2]] = status_codes.get(line[-2], 0) + 1
            except IndexError:
                pass

        print_stats(size, status_codes, count)

    except KeyboardInterrupt:
        print_stats(size, status_codes, count)
        raise
