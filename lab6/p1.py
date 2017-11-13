class treeNode:
	def __init__(self,p=None,k=None,l=None,r=None):
		self.parent=p
		self.key=k
		self.leftChild=l
		self.rightChild=r



class AVLTree:

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

	def height(self,z):
		hl=hr=0
		if z==None:
			return 0
		if z.leftChild==None and z.rightChild==None:
			return 1
		else:
			if z.leftChild!=None:
				hl=self.height(z.leftChild)
			if z.rightChild!=None:
				hr=self.height(z.rightChild)
		if hl>=hr:
			return hl+1
		else:
			return hr+1


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
		self.compare(z)
		
		
	def compare(self,z):
		while z!=None:
			hl=self.height(z.leftChild)
			hr=self.height(z.rightChild)
			if abs(hl-hr)<=1:
				z=z.parent
			elif hl>=hr:
				y=z.leftChild
				h1=self.height(y.leftChild)
				h2=self.height(y.rightChild)
				if h1>=h2:							#Case 1
					self.rotateright(y,z)
					z=y.parent

				else:								#Case 3
					x=y.rightChild
					self.rotateleft(x,y)
					self.rotateright(x,z)
					z=x.parent

			else:
				y=z.rightChild
				h1=self.height(y.leftChild)
				h2=self.height(y.rightChild)
				if h1<=h2:							#Case 2
					self.rotateleft(y,z)
					z=y.parent

				else:								#Case 4
					x=y.leftChild
					self.rotateright(x,y)
					self.rotateleft(x,z)
					z=x.parent
			self.compare(z)
				
	def rotateleft(self,y,z):
		z.rightChild=y.leftChild
		if y.leftChild!=None:
			y.leftChild.parent=z
		y.leftChild=z
		y.parent=z.parent
		if self.root==z:
			self.root=y
		if z.parent!=None:
			if z.parent.rightChild==z:
				z.parent.rightChild=y
			else:
				z.parent.leftChild=y
		z.parent=y

	def rotateright(self,y,z):
		z.leftChild=y.rightChild
		if y.rightChild!=None:
			y.rightChild.parent=z
		y.rightChild=z
		y.parent=z.parent
		if self.root==z:
			self.root=y
		if z.parent!=None:
			if z.parent.rightChild==z:
				z.parent.rightChild=y
			else:
				z.parent.leftChild=y
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
		self.compare(z)

			



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
	


	
def main():
	T=AVLTree()
	for i in range(1,16):
		T.insert(i)
	print("Root=",T.root.key)
	print("Height of the AVL tree= ",T.height(T.root))
	T.printTree(T.root)
	print()
	T.printTreePre(T.root)
	print()
	T.delete(8)
	print("Root=",T.root.key)
	print("Height of the AVL tree= ",T.height(T.root))
	T.printTree(T.root)
	print()
	T.printTreePre(T.root)
	print()


main()
