# sum of last 2 values equal times and get first value
N,A,B=map(int,input().split())
flag=0
for n in range(0,N):
	if(n*A + n*B)==N:
		flag=1
if flag==1:
	print("YES")
else:
	print("NO")
