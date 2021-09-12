import math
n = input()
arr = list(map(int,n))
for i in range(0,len(arr)):
	arr[i] = pow(arr[i],len(arr))
if(sum(arr) == int(n)):
	print(True)
else:
	print(False)
	
