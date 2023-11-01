#!/usr/bin/python3
def fizzbuzz():
    for fz in range(1, 101):
        if fz % 15 == 0:
            print("FizzBuzz", end=" ")
        elif fz % 5 == 0:
            print("Buzz", end=" ")
        elif fz % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{:d}".format(fz), end=" ")
