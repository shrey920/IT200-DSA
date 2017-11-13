def fact(x):
	f=1
	for i in range(1,x+1):
		f=f*i
	return f

def factr(x):
	if x==0:
		return 1
	else:
		return x*factr(x-1)

x=int(input("Enter a number: "))
f1=fact(x)
print ("Factorial by iteration: ",f1)
f2=factr(x)
print ("Factorial by recursion: ",f2)