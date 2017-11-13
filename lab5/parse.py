class TreeNode():
	def __init__(self,p=None,k=None,l=None,r=None):
		self.parent=p
		self.key=k
		self.left=l
		self.right=r

class ParseTree():
	def __init__(self):
		self.root=None
		
	def insert(self,x):
		x=x.split(',')
		i=0
		y=TreeNode()
		for i in x:
			if i=='(':
				z=TreeNode(x)
				y.left=z
				z.parent=y
				y=z
			elif i in ['+','-','*','/']:
				y.key=i
				z=TreeNode(x)
				y.right=z
				z.parent=y
				y=y.right
			elif i==')':
				self.root=y
				y=y.parent
			else :
				y.key=i
				y=y.parent


	def printPostfix(self,x):
		if x.left!=None:
			self.printPostfix(x.left)
		if x.right!=None:
			self.printPostfix(x.right)
		if x!=None:
			print(x.key,end=" ")

	def printPrefix(self,x):
		if x!=None:
			print(x.key,end=" ")
		if x.left!=None:
			self.printPrefix(x.left)
		if x.right!=None:
			self.printPrefix(x.right)

	def evaluateTree(self,x):
		if x.key in ['+','-','*','/']:
			a=self.evaluateTree(x.left)
			b=self.evaluateTree(x.right)
			return calc(a,b,x.key)
		else:
			return int(x.key)

def calc(a,b,op):
	if op=='+':
		return a+b
	elif op=='-':
		return a-b
	elif op=='*':
		return a*b
	else:
		return a/b

def main():
	exp="(,(,10,+,2,),*,(,9,-,2,),)"
	t=ParseTree()
	t.insert(exp)
	print(t.root.key)
	print("Prefix is: ")
	t.printPostfix(t.root)
	print()
	print("Postfix is: ")
	t.printPrefix(t.root)
	print()
	print("Answer= ",t.evaluateTree(t.root))



main()