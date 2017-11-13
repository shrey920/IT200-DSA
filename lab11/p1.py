import math

class node:
	def __init__(self):
		self.key=None
		self.dist=math.inf
		self.color='white'
		self.parent=None
		self.start=0
		self.end=0
		
class DFS:
	def __init__(self,l,a):
		self.t=0
		self.d=[]
		self.l=l
		self.a=a
		self.T=[]
		self.B=[]
		self.F=[]
		self.C=[]

	def dfs(self,s):
		u=self.a[s]
		self.d.append(u)
		u.start=self.t+1
		self.t=u.start
		u.color='grey'
		for i in self.l[u.key]:
			v=self.a[i]
			if v.color=='white':
				self.T.append([u.key,v.key])
				self.dfs(i)
				v.parent=u
			else:
				if u.start<v.start and u.end==0 and v.end!=0:
					self.F.append([u.key,v.key])
				elif u.start>v.start and v.end==0 and u.end==0:
					self.B.append([u.key,v.key])
				elif v.end!=0 and v.end<u.start :
					self.C.append([u.key,v.key])
				
		u.color='black'
		u.end=self.t+1
		self.t=u.end

	def printdfs(self):
		print("Node \tStart\tEnd")
		for u in self.d:
			print (u.key,"\t",u.start,"\t",u.end)
		print("Tree edges: ",self.T)
		print("Forward edges: ",self.F)
		print("Back edges: ",self.B)
		print("Cross edges: ",self.C)

def main():
	n=int(input("Enter no. of vertices: "))
	l=[[]for i in range(n)]
	print("Enter the edges and type -1 to stop: ")
	b=input().split(' ')
	while int(b[0])!=-1:
		i=int(b[0])
		j=int(b[1])
		if i>n or j>n:
			print("Invalid")
		else:
			l[i].append(j)		
		b=input().split(' ')
	print("The adjacency list is:")
	a=[node() for i in range(n)]
	for i in range(n):
		a[i].key=i
		print("Vertex ",i,": ",l[i])
	s=int(input("Enter source vertex: "))
	D=DFS(l,a)
	D.dfs(s)
	D.printdfs()

if __name__ == '__main__':
	main()