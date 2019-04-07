#you are given a string, you must split it on a " "(space) delimiter and join using a - (hyphen)


#verison 1 
print('-'.join(input().split(' ')))

#version 2
line = input()
words = line.split(' ')
print('-'.join(words))