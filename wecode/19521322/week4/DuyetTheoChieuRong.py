import sys

class Node:
	def __init__(self,val):
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
	def BFS(self, root)->list:
		if root is None:
			return
		tmp = [root]
		result = [root.root]
		while len(tmp) > 0:
			c = tmp.pop(0)
			if c.l is not None:
				tmp.append(c.l)
				result.append(c.l.root)
			if c.r is not None:
				tmp.append(c.r)
				result.append(c.r.root)
		return result

tmp = []
while True:
	n = list(map(int,sys.stdin.readline().split()))
	if(n[0] == 0):
		root = Node(tmp[0])
		tmp = list(dict.fromkeys(tmp))
		for i in range(1,len(tmp)):
			root.Insert(tmp[i])
		result = root.BFS(root)
		print(*result,sep=" ")
		exit()
	else:
		tmp.append(n[0])