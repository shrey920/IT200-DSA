def fib(n):
	if n==1:
		print (0)
		return
	elif n==2:
		print (0,",",1)
		return
	elif n>2:
		f1=0
		f2=1
		print (f1,",",f2, end=", ")
		for i in range(2,n):
			f=f1+f2
			print (f, end=", ")
			f1=f2
			f2=f

def fibr(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibr(n-1)+fibr(n-2)


n=int(input("Enter limit: "))
print ("Fibonacci series by iteration: ")
fib(n)
print ("\nFibonacci series by recursion: ")
for i in range(0,n):
	print (fibr(i),end=", ")
print ()