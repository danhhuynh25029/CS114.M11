import sys
import bisect
n = int(input())
arr = list(map(int,input().split()))
# 1 3 5 7 10 n
def find(arr,k,x):
	p = bisect.bisect_left(arr,x)
	left = p -1
	right = p + 1
	t_r = False
	t_l = False
	i = k - 1
	while i > 0:
		if left < 0 or right >= len(arr):
			if left < 0:
				right += 1
				t_l = True
				t_r = True
			if right >= len(arr):
				left -= 1
				t_l = True
				t_r = True
		else:
			if x - arr[left] <= arr[right] - x:
				# if left - 1 >= 0:
				left -= 1
				t_l = True
			else:
				# if right + 1 < len(arr):
				right += 1
				t_r = True
		i -= 1
	if t_l == True or left == p - 1:
		left += 1
	if t_r == True or right == p + 1:
		right -= 1
	return left,right

while True:
	tmp = list(map(int,input().split()))
	if(len(tmp) == 0):
		break
	else:
		k,x = tmp[0],tmp[1]
		if x >= arr[len(arr)-1]:
			print(arr[-k],arr[len(arr)-1])
		elif x <= arr[0]:
			print(arr[0],arr[k-1])
		else:
			min,max = find(arr,k,x)
			print(arr[min],arr[max])
