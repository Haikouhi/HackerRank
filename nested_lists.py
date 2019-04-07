#given the names and grades for each student in a class of n students, store them in a nested list 
#print the names of any students having the second lowest grade
#if there are multiple students with the same grqade, order their names alpha and print each names on a new line


#version 1
def secondLowestMarks(students):
    lowest_mark = min(students, key = lambda stu: stu[1])[1];
    students = [stu for stu in students if stu[1] != lowest_mark]
    #filter(lambda stu: stu[1] == lowest_mark, students);
    second_lowest_mark = min(students, key = lambda stu: stu[1])[1];
    return sorted([stu[0] for stu in students if stu[1] == second_lowest_mark]);

def secondLowestMarks2(students):
    "If there's a tie for lowest mark we include all."
    students.sort();
    picked_students = sorted(filter(lambda x: x[1] == students[1][1], students));
    return [stu[0] for stu in picked_students];

if __name__ == "__main__":
    num_students = int(input());
    students = [[input(),float(input())] for i in range(num_students)];
    for student in secondLowestMarks(students):
        print(student);





#version 2
n=[]
r=[]
for i in range(int(input())):
    n.append(input())
    r.append(float(input()))
m=min(r)
re=[]
for i in range(len(r)):
    if r[i]==m :r[i]=1000000000
m=min(r)
for i in range(len(r)):
    if r[i]==m:re.append(n[i]) 
re.sort()
for i in re :print(i)




#version 3
N = int(input())
final = list()
for i in range(N):
    lst = list()
    name = str(input())
    marks = float(input())
    lst.append(name)
    lst.append(marks)
    final.append(lst)
k = list()
for i in range(len(final)):
    k.append(final[i][1])
x = min(k)
k1 = list()
for i in range(len(k)):
	if x != k[i]:
		k1.append(k[i])
y = min(k1)
student = list()
for i in range(len(final)):
    if y == final[i][1]:
        student.append(final[i][0])
student.sort()
for i in range(len(student)):
    print(student[i])