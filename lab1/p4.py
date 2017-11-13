n=int(input("Enter size: "))
a=[]
for i in range(0,n):
	a.append(int(input("Enter integer: ")))
b=a
#bubble sort
for i in range(0,n-1):
	for j in range(0,n-i-1):
		if a[j]>a[j+1]:
			t=a[j]
			a[j]=a[j+1]
			a[j+1]=t
print ("Bubble sorted list is: ", a)

#selection sort
for i in range(0,n-1):
	for j in range(i+1,n-1):
		if b[i]>b[j]:
			t=j
		temp=b[i]
		b[i]=b[t]
		b[t]=temp
print ("Selection sorted list is: ", b)