import sys
from collections import deque
class Node:
	def  __init__(self,val):
		self.l = None
		self.r = None
		self.root = val
	def Insert(self,n):
		if(self.root != None):
			if(n < self.root):
				if(self.l is None):
					self.l = Node(n)
				else:
					self.l.Insert(n)
			elif(n > self.root):
				if(self.r is None):
					self.r = Node(n)
				else:
					self.r.Insert(n)
def Height(node):
	if(node == None):
		return 0
	else:
		r = Height(node.r)
		l = Height(node.l)
		return max(r,l) + 1
tmp = deque()
while True:
	n = list(map(int,sys.stdin.readline().split()))
	if(n[0] == 3):
		root = Node(tmp[0])
		tmp = list(dict.fromkeys(tmp))
		for i in range(1,len(tmp)):
			root.Insert(tmp[i])
		print(Height(root))
		exit()
	elif(n[0] == 0):
		tmp.appendleft(n[1])
	elif(n[0] == 1):
		tmp.append(n[1])
	elif(n[0] == 2):
		if(n[1] in tmp):
			k = tmp.index(n[1])
			tmp.insert(k+1,n[2])
		else:
			tmp.appendleft(n[2])