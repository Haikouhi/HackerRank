#consider a list (list=[]), you can perform the following commands
    #insert i e:insert integer e at position i
    #print:print the list
    #remove e:delete the first occurence of integer e
    #append e: insert integer e at the end of the list
    #sort: sort the list
    #pop: pop the last element from the list 
    #reverse: reverse the list

    #initialize your list and read the value of n followed by n lines of commands
    #where each command will be of the 7 types listed above
    # #iterate through each command in order and perform the corresponding operation on your list 



#verison 1 
test =int(input())
s=[]
for _ in range (test):
    cmd=list(input().split())
    
    if cmd[0]=='insert':
        s.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0]=="remove":
        s.remove(int(cmd[1]))
    elif cmd[0]=="append":
        s.append(int(cmd[1]))
    elif cmd[0]=="sort":
        s.sort()
    elif cmd[0]=="pop":
        s.pop()
    elif cmd[0]=="reverse":
        s.reverse()
    elif cmd[0]=="count":
        v=s.count(int(cmd[1]))
        print(v)
    elif cmd[0]=="index":
        x=s.index(int(cmd[1]))
        print(x)
   
    elif cmd[0]== 'print':
        print(s)


#verison 2
i=int(input()); l=[]
for _ in range(i):
  s=input()
  c,*v=s.split(); v=map(int,v)
  if c=='insert': l.insert(*v)
  elif c=='remove': l.remove(*v)
  elif c=='append': l.append(*v)
  elif c=='sort': l.sort()
  elif c=='reverse': l.reverse()
  elif c=='pop': l.pop(*v)
  elif c=='print': print(l)
  else: raise RuntimeError("invalid command")