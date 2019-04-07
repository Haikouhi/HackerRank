# you are given a string and you must swap cases
#convert all lowercase to uppercase and vice versa


#version 1
string_input = input()
print(string_input.swapcase())


#verison 2
print(input().swapcase())

#version 3
import sys

for line in sys.stdin:
    #line = line[:-1]
    line = ''.join([c.upper() if c.islower() else c.lower() for c in line])
    print(line)