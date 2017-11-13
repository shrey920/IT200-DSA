import timeit

n=int(input("Enter size: "))
a=[]
for i in range(0,n):
	a.append(int(input("Enter integer: ")))
b=a

t1=timeit.default_timer()
#bubble sort
for i in range(0,n-1):
	for j in range(0,n-i-1):
		if a[j]>a[j+1]:
			t=a[j]
			a[j]=a[j+1]
			a[j+1]=t
time=timeit.default_timer()-t1
print ("Bubble sorted list is: ", a)
print ("Runtime= ",time)

t1=timeit.default_timer()
#selection sort
for i in range(0,n-1):
	for j in range(i,n-1):
		if b[i]>b[j]:
			t=b[i]
			b[i]=b[j]
			b[j]=t
time=timeit.default_timer()-t1
print ("\nSelection sorted list is: ", b)
print ("Runtime= ",time)