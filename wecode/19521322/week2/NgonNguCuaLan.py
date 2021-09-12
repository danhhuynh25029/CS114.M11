s = list(input().split())
tmp = {"lios":1,"etr":2,"initis":3}
tmp1 = {"liala":1,"etra":2,"inites":3}
result = []
result1 = []
for i in range(0,len(s)):
	for j in range(3,7):
		a = s[i]
		if(a[len(a)-j:] in tmp):
			result.append(tmp[a[len(a)-j:]])
			result1.append(0)
			break
		if(a[len(a)-j:] in tmp1):
			result.append(tmp1[a[len(a)-j:]])
			result1.append(1)		
			break
if( (sum(result1) > 0 and 0 in result1) or len(result) == 0 or len(result) != len(s)):
	print("NO")
elif( len(result) == 1 and len(result) == len(s)):
	print("YES")
else:
	t = True
	t1 = result.count(2)
	if(t1 != 1):
		print("NO")
	else:
		for i in range(0,len(result)-1):
			if(result[i+1] < result[i]):
				t = False
				break
		if(t == True):
			print("YES")
		else:
			print("NO")
