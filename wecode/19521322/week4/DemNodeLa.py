import sys
class Node:
	def  __init__(self,val):
		self.l = None
		self.r = None
		self.root = val
	def Insert(self,n):
		if(self.root):
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
			else:
				pass
				
	def Print(self):
		if(self.l):
			self.l.Print()
		print(self.root)
		
		if(self.r):
			self.r.Print()
	def Count(self):
		if(self.root != None):
			if(self.l == None and self.r == None):
				global result
				result += 1
			else:
				if(self.l != None):
					self.l.Count()
				if(self.r != None):
					self.r.Count()
result = 0

root = Node(int(sys.stdin.readline()))
while True:
	n = int(sys.stdin.readline())
	if(n == 0):
		root.Count()
		print(result)
		break
	else:
		root.Insert(n)