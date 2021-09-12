n = int(input())
i = 0
tmp = []
while( i < n):
	a = int(input())
	if(a <= 2):
		tmp.append(2)
	else:
		tmp.append(a%2)
	i += 1
print(*tmp,sep="\n")
