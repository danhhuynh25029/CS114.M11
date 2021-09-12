n = int(input())
arr = list(map(int,input().split()))
k,x = list(map(int,input().split()))
result = []
tmp = {}
if(x not in arr):
	if(x > max(arr)):
		result = arr[n-k:]
	elif(x < min(arr)):
		result = arr[0:k]
	else:
		for i in range(0,n):
			tmp[i] = abs(arr[i]-x)
		keys = sorted(tmp.items(), key = lambda x : x[1])
		for i in keys:
			result.append(arr[i[0]])
			if(len(result) == k):
				break
else:
	for i in range(0,n):
		tmp[i] = abs(arr[i]-x)
	keys = sorted(tmp.items(), key = lambda x : x[1])
	for i in keys:
		result.append(arr[i[0]])
		if(len(result) == k):
			break
result.sort()
print(*result,sep=" ")
