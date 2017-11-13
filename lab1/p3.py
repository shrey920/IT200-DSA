def prime(n):
	if n==2:
		return True
	elif n==1 or n<=0:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True

n=int(input("Enter a number: "))
print ("The number is prime: ",prime(n))