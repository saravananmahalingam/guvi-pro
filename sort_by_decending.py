# sort by reverse
a=int(input())
b=list(map(int,input().split()))
b.sort()
c=b[::-1]
for i in c:
	print(i)
