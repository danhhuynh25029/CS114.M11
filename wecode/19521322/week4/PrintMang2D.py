import sys
m,n = list(map(int,input().split()))
arr = []
if(m <= 1000 and n <= 1000):
	for i in range(0,m):
		arr.append(list(input().strip().split()))
	tmp = []
	
	for i in range(0,n):
		k = 0
		for j in range(0,m):
			arr[j][i] = str(int(arr[j][i]))
			k = max(len(arr[j][i]),k)
		tmp.append(k)
	result = arr.copy()
	for i in range(0,n):
		for j in range(0,m):
			if(len(arr[j][i]) < tmp[i]):
				result[j][i] = " "*(tmp[i] - len(arr[j][i])) + arr[j][i]
	for i in result:
		print(*i,sep =" ")