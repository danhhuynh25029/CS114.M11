s = input()
result = list(s)
tmp = ["A","O","Y","E","U","I"]
i = 0
while (i < len(result)):
	if (result[i].upper() in tmp):
		result.remove(result[i])
	else:
		if(result[i].upper() == result[i]):
				result[i] = result[i].lower()
		i += 1
result = '.'.join(result)
print("."+result)


