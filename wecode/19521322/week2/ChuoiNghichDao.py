n = int(input())
result = []
arr = []
i = 0
def check(a : list)->str:
	s = a[0]
	s1 = a[1]
	for i in range(0,len(s)):
		if s[i] in s1:
			return "YES"
	return "NO"
while(i < n ):
	s = input()
	s1 = input()
	arr.append([s,s1])
	i += 1
for i in range(0,len(arr)):
	a = check(arr[i])
	result.append(a)
print(*result,sep="\n")
