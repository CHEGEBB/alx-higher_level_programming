#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz ", end='')
            else:
                print("Fizz ", end='')
        elif i % 5 == 0:
            print("Buzz ", end='')
        else:
            print(f'{i}', end=' ')
