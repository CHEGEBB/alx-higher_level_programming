#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i != ord('q') and i != ord('e'):
        print('{}'.format(chr(i)), end='')
        continue
