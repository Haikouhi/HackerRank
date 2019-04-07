# first and last name 

#version 1
start = "Hello "
end = "! You just delved into python."
first_name = input().rstrip() + " "
last_name = input().rstrip()
print(start + first_name + last_name + end)


#verison 2
a = input()
b = input()
c = "Hello "+a+" "+b+"! You just delved into python."
print(c)


#version 3
fname = input().rstrip()
lname = input().rstrip()
print ("Hello " + fname + " " + lname + "! You just delved into python.")