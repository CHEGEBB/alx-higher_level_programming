#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # try:
    #     for i in range(x):
    #         print(my_list[i], end="")
    #     print()
    #     return i + 1
    # except IndexError:
    #     print()
    #     return i
    count = 0
    for i in range(x):
        try:
            print('{}'.format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print('')
    return count
