class Stack :
    l=[]

    def push(self,x):
        self.l.append(x)

    def isEmpty(self):
        if len(self.l) == 0:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.l.pop(len(self.l)-1)

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.l[len(self.l)-1]

def apply(s,a,b):
    if s=='+':
        return a+b
    elif s=='-':
        return a-b
    elif s=='*':
        return a*b
    elif s=='/':
        return a/b
    else:
        return None

def main():
    S=Stack()
    x='5 10 / 2 +'
    x=x.split(' ')
    print(x)
    for i in range(len(x)):
        s=x[i]
        if s.isdigit():
            S.push(s)
        else:
            b=float(S.pop())
            a=float(S.pop())
            ans=apply(s,a,b)
            if ans==None:
                print ("Invalid")
            else:
                S.push(ans)
    print("Answer is ",S.pop())


if __name__=='__main__':
    main()