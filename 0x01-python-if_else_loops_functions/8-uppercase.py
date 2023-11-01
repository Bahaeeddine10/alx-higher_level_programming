#!/usr/bin/python3

def islower(c):
    return 'a' <= c <= 'z'

def uppercase(s):
    result = ""
    for char in s:
        if islower(char):
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

input_string = "Example String"
output_string = uppercase(input_string)
print(output_string)
