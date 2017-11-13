str1=input("Enter str1: ")
str2=input("Enter str2: ")
str3=input("Enter str3: ")
str4=""
i=0
while i!=len(str1):
	if str1[i:i+len(str2)]==str2:
		i=i+len(str2)-1
		str4=str4+str3
	else:
		str4=str4+str1[i]
	i=i+1
print(str4)