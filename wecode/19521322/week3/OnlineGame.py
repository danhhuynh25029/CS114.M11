import sys
result= []
tmp = {}
while True:
	s = list(sys.stdin.readline().split())
	if(s[0] == '0'):
		break
	elif(s[0] == '2'):
		if(tmp.get(s[1]) == None):
			result.append('0')
		else:
			result.append('1')
	else:	
		tmp[s[1]] = s[0]
sys.stdout.write('\n'.join(result))
