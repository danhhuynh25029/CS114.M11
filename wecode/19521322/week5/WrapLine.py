s = input().strip()
n = int(input())
i = 1
tmp = ""
arr =[]
for i in range(0,len(s)):
	if s[i] != " ":
		tmp += s[i]
		if(i == len(s) - 1):
			arr.append(tmp)
	else:
		if(len(tmp) > 0):
			arr.append(tmp)
			tmp = ""
		arr.append(" ")
# print(arr)
i = 0
tmp = ""
while i < len(arr):
	if(len(arr[i]) > n):
		if(i == len(arr) - 1):
			print(arr[i])
			i += 1
		else:
			tmp = arr[i]
			for j in range(i+1,len(arr)):
				if(arr[j] != " "):
					break
				else:
					tmp += arr[j]
					i += 1
			print(tmp)
			i += 1

	else:
		tmp = arr[i]
		j = i + 1
		while j < len(arr):
			if(len(tmp) + len(arr[j]) <= n):
				tmp = tmp + arr[j]
				j += 1
				i += 1
			else:
				break
		print(tmp)
		i += 1