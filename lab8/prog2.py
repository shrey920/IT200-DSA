class Trienode:
	def __init__(self):
		self.ch=[None]*26
		self.endptr=None
class Tries:
	def __init__(self):
		self.head=None
	def findkey(self,x):
		if ord(x)>90:
			t=ord(x)-32
		else:
			t=ord(x)
		return t%65
	def add(self,s,x):
		if self.head==None:
			self.head=Trienode()
		tmp=self.head.ch
		for i in range(len(s)):
			key=self.findkey(s[i])
			if tmp[key]==None:
				tmp[key]=Trienode()
			if i!=len(s)-1:
				tmp=tmp[key].ch
			else:
				if tmp[key].endptr==None:
					tmp[key].endptr=str(x)+" "
				else:
					tmp[key].endptr+=str(x)+" "

	def search(self,s):
		if self.head==None:
			print("Not Found")
		else:
			tmp=self.head.ch
			for i in range(len(s)):
				key=self.findkey(s[i])
				if tmp[key]==None:
					print("Not found")
					return
				else:
					tempo=tmp
					tmp=tmp[key].ch
			if tempo[key].endptr!=None:
				print("hooorayyyy!!!!,FOUND IT")
				print("location: ",tempo[key].endptr)
			else:
				print("Not Found")
t=Tries()
f=open("is.dict")
c=[]
for line in iter(f):
	for k in line:
		c.append(k)
x=1
s=""
j=['!','?','#',',','.',';',':','"',"'",' ','\n']
for i in range(len(c)):
	if c[i] in j:
		print(s)
		t.add(s,x)
		x=i+1
		s=""
	else:
		s+=c[i]
n=input("enter No. of words to search ")
for i in range(int(n)):
	t.search(input())  