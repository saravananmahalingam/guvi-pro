# append all values to the list check it is a square
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
li=[]
for i in a:
	if i not in li:
		li.append(i)
for i in b:
	if i not in li:
		li.append(i)
for i in c:
	if i not in li:
		li.append(i)
for i in d:
	if i not in li:
		li.append(i)
if len(li)%2==0:
	print("yes")
else:
	print("no")
