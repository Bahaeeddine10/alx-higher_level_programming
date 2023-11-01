#!/usr/bin/python3
for tebahpla in range(25, -1, -1):
    c = tebahpla + ord('A')
    if tebahpla % 2 == 1:
        c+= 32
    print("{:c}".format(c), end="")
