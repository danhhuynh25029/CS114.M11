n,m,a = list(map(int,input().split()))
result = 0

if( m == n):
	k = 0
	if (m % a == 0):
		k = m//a
	else:
		k = m//a +1
	if(n % a == 0):
		result += (n//a)*k
	else:
		result += ((n//a)+1)*k
else:
	tmp = max(n,m)
	tmp1 = min(n,m)
	k = 0
	if(tmp1 % a == 0):
		k = tmp1//a
	else:
		k = tmp1//a + 1
	if(tmp % a == 0):
		result += (tmp//a)*k
	else:
		result += ((tmp//a)+1)*k
print(result)
