n = int(input())
result = []
while(n > 0):
	x,k = list(map(int,input().split()))
	arr = list(map(int,input().split()))
	result.append(arr.count(k))
	n -= 1
print(*result,sep="\n")