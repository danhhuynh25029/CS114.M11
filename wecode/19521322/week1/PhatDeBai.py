n = int(input())
k = int(input())
p = int(input())
q = int(input())
# n 10
# k 9
# p 1
# q 2
#1 2 
#3 4
#5 6
#7 8
#9 5
#1 
result = [0,0]
alice = 0
tmp = 0
if q % 2 == 0:
	tmp  = p*q
else:
	tmp = p*2-q
if(tmp % k == 0):
	alice = k
else:
	alice = (tmp % k)
if(alice > n//2 or k >= n or (n - k < alice)):
	print(-1)
else:
	if (tmp <= k):
		if((tmp + k) % 2 == 0):
			result[0] = (tmp+k)//2
			result[1] = 2
		else:
			result[0] = (tmp+k)//2 + 1
			result[1] = 1
	else:
		if((tmp - k) % 2 == 0):
			result[0] = (tmp-k)//2
			result[1] = 2
		else:
			result[0] = (tmp-k)//2 + 1
			result[1] = 1
	print(*result,sep=" ")

	

