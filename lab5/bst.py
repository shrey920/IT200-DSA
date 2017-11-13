class treeNode:
	def __init__(self,p=None,k=None,l=None,r=None):
		self.parent=p
		self.key=k
		self.leftChild=l
		self.rightChild=r



class binarySearchTree:

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
				x.rightChild.parent=x.parent
			else:
				y=self.predecessor(x.key)
				self.delete(y.key)
				x.key=y.key



	def printTree(self,x):
		if x.leftChild!=None:
			self.printTree(x.leftChild)
		if x!=None:
			print (x.key, end=", ")
		else:
			return
		if x.rightChild!=None:
			self.printTree(x.rightChild)


def main():
	T=binarySearchTree()
	T.insert(5)
	T.insert(1)
	T.insert(2)
	T.insert(3)
	T.insert(4)
	T.insert(6)
	T.insert(7)
	T.insert(8)
	T.insert(9)
	T.printTree(T.root)
	print()
	
	print(T.minimum(T.root).key)



main()
