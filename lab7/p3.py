import bst

def heapify(l):
	for i in range(len(l)-1,0,-1):
		while 2*i<len(l):
			if len(l)==2*i+1 or l[2*i]>l[2*i+1]:
				j=2*i
			else:
				j=2*i+1
			if l[i]<l[j]:
				t=l[j]
				l[j]=l[i]
				l[i]=t
			i=j

def isHeap(T):
	l=T.LevelOrder()
	#heapify(l)
	print(l)
	for i in range(len(l)-1,0,-1):
		while 2*i<len(l):
			if len(l)==2*i+1 or l[2*i]>l[2*i+1]:
				j=2*i
			else:
				j=2*i+1
			if l[i]<l[j]:
				return False
			i=j
	return True

def main():
	T=bst.BST()
	for i in range(1,16):
		T.insert(i)
	print(isHeap(T))


if __name__ == '__main__':
	main()