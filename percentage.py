#you have a record of n students
#each record contains the students' name and percent mark in several subjects
#the marks can be floating values 
#the user enters some integer n followed by the names and marks
#you are required to save the record in a dictionary data type
#the user then enters a students name
#output the average percentage marks obtained by that student 
#correct to two decimal places 


#version 1
N = input();

map = {};
for i in range(0,int(N)):
    S = input().split();
    lst = (float(S[1]) + float(S[2]) + float(S[3]))/3.0;
    map[S[0]] = lst;

print("%0.2f" %map[input()]);



#version 2 
N = int(input())
stud_dict = dict()

for i in range(N):
    tmp = input().split(' ')
    name = tmp[0]
    stud_dict[name] = (float(tmp[1]), float(tmp[2]), float(tmp[3]))
    
name = input()
print('%.2f' % (sum(stud_dict[name]) / 3.0))