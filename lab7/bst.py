class treeNode:
	def __init__(self,p=None,k=None,l=None,r=None):
		self.parent=p
		self.key=k
		self.leftChild=l
		self.rightChild=r



class BST:

	def __init__(self):
		self.root=None


	def search(self,k,x):
		if self.root==None or x==None:
			return None
		if k==x.key:
			return x
		if k<x.key:
			return self.search(k,x.leftChild)
		else:
			return self.search(k,x.rightChild)

	def minimum(self,x):
		while x.leftChild!=None:
			x=x.leftChild
		return x

	def maximum(self,x):
		while x.rightChild!=None:
			x=x.rightChild
		return x

	def successor(self,k):
		x=self.search(k,self.root)
		if x.rightChild!=None:
			return self.minimum(x.rightChild)
		y=x.parent
		while y!=None and x!=y.leftChild:
			x=y
			y=y.parent
		if y==None:
			return None
		else:
			return y

	def predecessor(self,k):
		x=self.search(k,self.root)
		if x==None:
			return None
		if x.leftChild!=None:
			return self.maximum(x.leftChild)
		y=x.parent
		while y!=None and x!=y.rightChild:
			x=y
			y=y.parent
		if y==None:
			return None
		else:
			return y

	
	def insert(self,k):
		z=treeNode(None,k,None,None)
		if self.root==None:
			self.root=z
		else:
			x=self.root
			while x!=None:
				y=x
				if x.key>k:
					x=x.leftChild
				else:
					x=x.rightChild
			if k>y.key:
				y.rightChild=z
			else:
				y.leftChild=z
			z.parent=y
		
	
		

	def delete(self,k):
		x=self.search(k,self.root)
		if x.leftChild==None and x.rightChild==None:
			y=x.parent
			z=y
			if y.leftChild==x:
				y.leftChild=None
			else:
				y.rightChild=None
		else:
			if x.leftChild==None:
				if x.parent.leftChild==x:
					x.parent.leftChild=x.rightChild
				else:
					x.parent.rightChild=x.rightChild
				x.rightChild.parent=x.parent
			elif x.rightChild==None:
				if x.parent.leftChild==x:
					x.parent.leftChild=x.leftChild
				else:
					x.parent.rightChild=x.leftChild
				x.leftChild.parent=x.parent
			else:
				y=self.predecessor(x.key)
				self.delete(y.key)
				x.key=y.key
			z=x

			



	def printTree(self,x):
		if x.leftChild!=None:
			self.printTree(x.leftChild)
		if x!=None:
			print (x.key, end=", ")
		else:
			return
		if x.rightChild!=None:
			self.printTree(x.rightChild)

	def printTreePre(self,x):
		if x!=None:
			print (x.key, end=", ")
		else:
			return
		if x.leftChild!=None:
			self.printTreePre(x.leftChild)
		if x.rightChild!=None:
			self.printTreePre(x.rightChild)
	

	def LevelOrder(self):
		h = self.height(self.root)
		l=[]
		for i in range(1, h+1):
			self.GivenLevel(self.root,i,l)
		return l
 
 
	def GivenLevel(self,root, level,l):
		if root is None:
			return
		if level == 1:
			l.append(root.key)
		elif level > 1 :
			self.GivenLevel(root.leftChild , level-1,l)
			self.GivenLevel(root.rightChild , level-1,l)
 

	def height(self,node):
		if node is None:
			return 0
		else :
			lheight = self.height(node.leftChild)
			rheight = self.height(node.rightChild)
		if lheight > rheight :
			return lheight+1
		else:
			return rheight+1