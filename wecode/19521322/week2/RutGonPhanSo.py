n = int(input())
result = ["1"]*n
i = 0
def ucln(a:int,b:int)->int:
	if(b == 0):
		return a
	else:
		return ucln(b,a%b);
while (i < n):
	tmp = list(map(int,input().split()))
	u = ucln(tmp[0],tmp[1])
	a = tmp[0]//u
	b = tmp[1]//u
	if(b == 1):
		result[i] = f"{a}"
	else:
		result[i] = f"{a} {b}" 
	i += 1
print(*result,sep="\n")
