n = int(input())
i = 0
arr = []
result = []
while( i < n):
	a = int(input())
	tmp = list(map(int,input().split()))
	arr.append(tmp)
	i += 1
for i in range(0,len(arr)):
	if(sum(arr[i]) % len(arr[i]) == 0):
		result.append(sum(arr[i])//len(arr[i]))
	else:
		if((sum(arr[i]) // len(arr[i]))*len(arr[i]) == sum(arr[i])):
			result.append(sum(arr[i])//len(arr[i]))
		else:
			result.append(sum(arr[i])//len(arr[i])+1)
print(*result,sep="\n")
