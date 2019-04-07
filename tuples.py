#given an integer, n , and n space-separated integers as input
#create a tuple t of those n integers
#then compute and print the result of hash(t)
    #hash() is one of the funtions built-in the __builtins__ ;odule, so it need not be imported 


#verison 1
input()
l = map(int, input().strip().split(" "))
print(hash(tuple(l)))

#version 2
N = int(input())
T = tuple(int(x) for x in input().split())
print(hash(T))

#verison 3
n = int(input())
print(hash(tuple([int(x) for x in input().split()])))