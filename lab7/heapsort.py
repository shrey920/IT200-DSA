class BinaryHeap:
	def __init__(self):
		self.l=[None]

	def buildHeap(self,*a):
		for x in a:
			self.l.append(int(x))
		for i in range(len(self.l)-1,0,-1):
			self.heapify(i,len(self.l))

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
		self.l.append(k)
		self.heapify(len(self.l))

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

	def heapSort(self,l):
		self.swap(1,l)
		self.heapify(1,l)
		if l-1>1:
			self.heapSort(l-1)

		
def main():
	H=BinaryHeap()
	H.buildHeap(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
	H.printHeap()
	print(H.maximum())
	H.buildHeap(16)
	H.printHeap()
	print(H.maximum())
	H.extractMax()
	H.printHeap()
	H.heapSort(15)
	print("Sorted list is: ")
	H.printHeap()

if __name__ == '__main__':
	main()