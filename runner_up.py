#given the participants' score sheet for your Uni Sports Day, you are required to find the runner-up score
#you are given n scores
#store them in a list and find the score of the runner-up

n=input()
a=map(int,input().split())
a=list(set(a))
a.remove(max(a))
print (max(a))
