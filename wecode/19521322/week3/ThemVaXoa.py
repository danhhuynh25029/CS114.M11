import sys
result = []
while(True):
	s = sys.stdin.readline()
	if(len(s[0:len(s)-1]) == 1 and int(s) == 6):
		break
	arr = list(map(int,s[0:len(s)-1].split()))	
	if(arr[0] == 0 and arr[1] < 1000):
		result.insert(0	,arr[1])					
	elif(arr[0] == 1 and arr[1] < 1000):
		result.insert(len(result),arr[1])
	elif(arr[0] == 2 and arr[1] < 1000 and arr[2] < 1000):
		if(arr[1] in result):
			result.insert(result.index(arr[1])+1,arr[2])
		else:
			result.insert(0,arr[2])
	elif(arr[0] == 3 and arr[1] < 1000):
		if(arr[1] in result):
			result.remove(arr[1])
	elif(arr[0] == 4 and arr[1] < 1000):
		if(arr[1] in result):
			while (True):
				if(arr[1] not in result):
					break
				else:
					result.remove(arr[1])
	elif(arr[0] == 5):
		if(len(result) > 0):
			result.remove(result[0])
if(len(result) == 0):
	print("blank")
else:
	print(*result,sep=" ")	
