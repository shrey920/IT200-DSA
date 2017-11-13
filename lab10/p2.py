class BinaryHeap:
	def __init__(self):
		self.l=[None]

	def isEmpty(self):
		if len(self.l)==1:
			return True
		else:
			return False

	def updateHeap(self,v):
		i=self.l.index(v)
		while i>0:
			self.heapify(i,len(self.l))
			i=i//2
		

	def buildHeap(self,a):
		for x in a:
			self.insert(x)
		

	def heapify(self,i,l):
		while 2*i<l:
			if l==2*i+1 or self.l[2*i].dist<self.l[2*i+1].dist:
				j=2*i
			else:
				j=2*i+1
			if self.l[i].dist>self.l[j].dist:
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

	def minimum(self):
		return (self.l[1])

	def extractMin(self):
		min=self.l[1]
		if len(self.l)>2:
			self.l[1]=self.l.pop()
			self.heapify(1,len(self.l))	
		else:
			self.l.pop()	
		return min

	def traverse(self):
		i=1
		while i<len(self.l):
			if i in (2,4,8,16):
				print("")
			print(self.l[i],end=", ")
			i=i+1

import math

class node:
	def __init__(self):
		self.key=None
		self.dist=math.inf
		self.color='white'
		self.parent=None
		self.start=0
		self.end=0
		self.p=[]


def main():
	n=int(input("Enter no. of vertices: "))
	l=[[]for i in range(n)]
	print("Enter the edges and weights and type -1 to stop: ")
	b=input().split(' ')
	while int(b[0])!=-1:
		if len(b)!=3:
			print("Invalid")
			b=input().split(' ')
			continue
		i=int(b[0])
		j=int(b[1])
		w=int(b[2])
		if i>n or j>n:
			print("Invalid")
		else:
			l[i].append([j,w])		
		b=input().split(' ')
	print("The adjacency list is:")
	a=[node() for i in range(n)]
	for i in range(n):
		a[i].key=i
		print("Vertex ",i,": ",l[i])
	s=int(input("Enter source vertex: "))
	dijkstra(l,a,s)

def dijkstra(l,a,s):
	print("Node\tDist\tPath")
	a[s].dist=0
	H=BinaryHeap()
	H.buildHeap(a)
	a[s].p=[s]
	while not H.isEmpty():
		w=H.extractMin()
		for i in l[w.key]:
			v=a[i[0]]
			if w.dist + i[1] < v.dist:
				v.dist=w.dist + i[1]
				v.p=[]
				for q in w.p:
					v.p.append(q)
				v.p.append(i[0])
				H.updateHeap(v)
		print(w.key,'\t',w.dist,'\t',w.p)

	
if __name__ == '__main__':
	main()