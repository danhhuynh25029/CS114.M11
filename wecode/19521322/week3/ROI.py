import sys
h,w = list(map(int,input().split()))
arr = [] 
arr1 = []
for i in range(0,h+1):
	if(i == h):
		arr1 = list(map(int,input().split()))
		break
	arr.append(list(input().split()))
for i in range(0,h):
	for j in range(0,w):
		if(i >= arr1[0] and i <= arr1[2] and j >= arr1[1] and j <= arr1[3]):
			continue
		else:
			arr[i][j] = '0'
for i in range(0,h):
	sys.stdout.write(' '.join(arr[i]) + '\n')
