import sys
k,n = list(sys.stdin.readline().split())
result = 1
if(len(k) == len(n)):
	result = 1
else:
	if(int(n)%(10**len(k)) >= int(k)):
		result +=  int(n[0:len(n)-len(k)])
	else:
		result =  int(n[0:len(n)-len(k)])
sys.stdout.write(str(result))