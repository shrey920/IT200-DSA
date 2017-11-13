n=int(input("Enter no. of vertices: "))
a=[[0 for i in range(n)]for i in range(n)]
print("Enter the edges and type -1 to stop: ")
b=input().split(' ')
while int(b[0])!=-1:
	i=int(b[0])
	j=int(b[1])
	if i>4 or j>4:
		print("Invalid")
	else:
		a[i][j]=1
		a[j][i]=1
	b=input().split(' ')
print("The adjacency matrix is:")
for i in range(n):
	for j in range(n):
		print(a[i][j],end=' ')
	print("")
l=[[]for i in range(n)]
for i in range(n):
	for j in range(n):
		if a[i][j]==1:
			l[i].append(j)
print("The adjacency list is:")
for i in range(n):
	print("Vertex ",i,": ",l[i])
