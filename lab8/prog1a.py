class trien:
	def __init__(self):
		self.child=[None]*26
class triedata:
	def __init__(self,r):
		self.root=r
	def insert(self,key):
		temp=self.root
		for i in range(len(key)):
			l=ord(key[i])-ord('a')
			if temp.child[l]==None:
				temp.child[l]=trien()
			temp=temp.child[l]
	def search(self,key):
		temp=self.root
		for i in range(len(key)):
			l=ord(key[i])-ord('a')
			if temp.child[l]==None:
				return(False)
			temp=temp.child[l]
		if temp!=None:
			return(True)
arr=['their','who','fun','person','today',]
trie=triedata(trien())
for key in arr:
	trie.insert(key)
n=input('Enter any word:')
if trie.search(n):
	print("Its present")
else:
	print("its not present")

			


			