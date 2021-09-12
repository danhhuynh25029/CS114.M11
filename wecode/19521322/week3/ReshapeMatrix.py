import sys
m,n = list(map(int,sys.stdin.readline().split()))
a,b = list(map(int,sys.stdin.readline().split()))
arr = []
if(a*b != m*n):
	s = ""
	for i in range(m):
		s += sys.stdin.readline()
		#arr = arr + s[0:len(s)-1].split()
	sys.stdout.write(''.join(s))
else:
	tmp = []
	result = ""
	if(a == 1):
		for i in range(m):
			s = sys.stdin.readline()
			arr = arr + s[0:len(s)-1].split()
		sys.stdout.write(' '.join(arr) + '\n')
	else:
		max = max(m,a)
		for i in range(max):
			if(i < m):
				s = sys.stdin.readline().split()
				s1 = tmp + s
				if(len(s1) >= b):
					result += ' '.join(s1[0:b]) + "\n"
					tmp = s1[b:len(s1)]
				else:
					tmp = s1
			else:
				result += ' '.join(tmp[0:b]) + "\n"
				tmp = tmp[b:]
		sys.stdout.write(result) 
