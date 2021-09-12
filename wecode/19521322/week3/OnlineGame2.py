import sys
result= []
tmp = {}
while True:
	s = list(sys.stdin.readline().strip().split())
	if(len(s) == 1):
		if(s[0] == '0'):
			break
	if(len(s) == 2): 
		if(s[0] == '2'):
			if(tmp.get(s[1]) == None or tmp.get(s[1]) == '0'):
				result.append('0')
			else:
				result.append('1')
		elif(s[0] == '3'):
			if(tmp.get(s[1]) != None):
				tmp[s[1]] = '0'
		elif(s[0] == '1'):	
			tmp[s[1]] = s[0]
sys.stdout.write('\n'.join(result))
