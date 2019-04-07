#given an integer, n, perform the following conditional actions:
    #if n is odd, print "weird"
    #if n is even and in the inclusive range of 2 to 5, print "not weird"
    #if n is even and in the inclusive range of 6 to 20, print "weird"
    #if n is even and greater than 20, print "not zeird"


#version 1

N = input("enter number here :")
N = int(N)

if((N%2)==1) : 
    print("Weird")
elif ((N%2)==0 and N>=2 and N<=5):
    print ("Not Weird")
elif ((N%2)==0 and N>=6 and N<=20):
    print ("Weird")
elif ((N%2)==0 and N>20):
    print ("Not Weird")


#Version 2
N = int(raw_input().strip()) #raw_input returns a string
if N%2 == 0 and (N > 20 or N in range(2, 6)) :
    print 'Not Weird'
else:
    print 'Weird'
