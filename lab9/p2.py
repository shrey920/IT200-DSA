import math

class node:
	def __init__(self):
		self.dist=None
		self.color=None
		self.parent=None

def bfs(l,s):
	a=[node() for i in range(len(l))]
	for i in a:
		i.dist=math.inf
		i.color='white'
		i.parent=None

	a[s].key=s
	a[s].dist=0
	a[s].color='grey'
	a[s].parent=None
	q=[]
	q.append(s)

	while len(q)>0:
		u=q.pop(0)
		print("Node: ",u,"Distance: ",a[u].dist)
		for i in l[u]:
			v=a[i]
			if v.color=='white':
				v.dist=a[u].dist+1
				v.color='grey'
				v.parent=a[u]
				q.append(i)
			a[u].color='black'


def main():
	n=int(input("Enter no. of vertices: "))
	l=[[]for i in range(n)]
	print("Enter the edges and type -1 to stop: ")
	b=input().split(' ')
	while int(b[0])!=-1:
		i=int(b[0])
		j=int(b[1])
		if i>4 or j>4:
			print("Invalid")
		else:
			l[i].append(j)
			l[j].append(i)		
		b=input().split(' ')
	print("The adjacency list is:")
	for i in range(n):
		print("Vertex ",i,": ",l[i])
	s=int(input("Enter source vertex: "))
	bfs(l,s)

if __name__ == '__main__':
	main()