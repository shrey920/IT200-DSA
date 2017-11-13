class BinaryHeap:
	def __init__(self):
		self.l=[None]

	def buildHeap(self,*a):
		for x in a:
			self.insert(int(x))
		
	def heapify(self,i,l):
		while 2*i<l:
			if l==2*i+1 or self.l[2*i]>self.l[2*i+1]:
				j=2*i
			else:
				j=2*i+1
			if self.l[i]<self.l[j]:
				self.swap(i,j)
			i=j


	def insert(self,k):
		self.l.insert(1,k)
		self.heapify(1,len(self.l))

	def printHeap(self):
		print (self.l[1:])


	def swap(self,a,b):
		t=self.l[a]
		self.l[a]=self.l[b]
		self.l[b]=t

	def maximum(self):
		return (self.l[1])

	def extractMax(self):
		max=self.l[1]
		self.l[1]=self.l.pop()
		self.heapify(1,len(self.l))		
		return max

	def traverse(self):
		i=1
		while i<len(self.l):
			if i in (2,4,8,16):
				print("")
			print(self.l[i],end=", ")
			i=i+1

def main():
	H=BinaryHeap()
	H.buildHeap(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
	H.printHeap()
	print(H.maximum())
	H.insert(16)
	H.printHeap()
	print(H.maximum())
	H.traverse()
	H.extractMax()
	H.printHeap()
	H.traverse()

if __name__ == '__main__':
	main()