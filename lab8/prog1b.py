class trien:
        def __init__(self):
                self.child=[None]*26
                self.endc=None
class triedata:
        def __init__(self,r):
                self.root=r
        def insert(self,key):
                temp=self.root
                for i in range(len(key)):
                        l=ord(key[i])-ord('a')
                        if l<26 and l>=0:
                                if temp.child[l]==None:
                                        temp.child[l]=trien()
                                temp=temp.child[l]
                temp.endc='#'
        def search(self,key):
                temp=self.root
                for i in range(len(key)):
                        l=ord(key[i])-ord('a')
                        if temp.child[l]==None:
                                return(False)
                        temp=temp.child[l]
                if temp!=None and temp.endc=='#':
                        return(True)
arr=['their','fun','person','today']
trie=triedata(trien())
for key in arr:
        trie.insert(key)
n=input('Enter any word:')
if trie.search(n):
        print("It's present")
else:
        print("It's not present")

			

			
