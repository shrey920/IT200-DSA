def main():
	n=int(input("Enter n:"))
	print("Enter the numbers: ")
	A=[0]*n
	for i in range(n):
		A[i]=int(input())
	quickSort(A,0,n)
	print("The sorted list is: ",A)

def quickSort(A,low,high):
	if low<high-1:
		
		quickSort(A,low,p)
		quickSort(A,p,high)
		merge(A,low,p,high)



def merge(A,low,mid,high):
	a=A[low:mid]
	b=A[mid:high]
	l=0
	r=0
	i=low
	while l<len(a) and r<len(b):
		if a[l]>b[r]:
			A[i]=b[r]
			r=r+1
		else:
			A[i]=a[l]
			l=l+1
		i=i+1
	while(l<len(a)):
		A[i]=a[l]
		l=l+1
		i=i+1
	while(r<len(b)):
		A[i]=b[r]
		r=r+1
		i=i+1

if __name__ == '__main__':
	main()