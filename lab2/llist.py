class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head=ListNode()

    def insert(self,x,p):
        """Insert element x in the position after p"""
        temp=ListNode(x,p.next)
        p.next=temp

        
    def delete(self,p):
        """Delete the node following node p in the linked list."""
        p.next=p.next.next

    def printl(self):
        """ Print all the elements of a list in a row."""
        temp=self.head.next
        l=[]
        while temp!=None:
            l.append(temp.value)
            temp=temp.next   
        return l      

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        temp=self.head
        while i!=0:
            temp=temp.next
            i=i-1
        self.insert(x,temp)

    def search(self,x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp=self.head.next
        i=0
        f=False
        while temp!=None:
            if temp.value==x:
                f=True
                return i
            i=i+1
            temp=temp.next
        if f==False:
            return "Not Found"

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        i=0
        temp=self.head.next
        while temp!=None:
            i=i+1
            temp=temp.next
        return i

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if self.head.next==None:
            return True
        else:
            return False


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print ('List is: ', L.printl())
    L.insert(12,L.head.next)
    print ('List is: ', L.printl())
    L.insert(2,L.head)
    print('List is: ', L.printl())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ',L.printl())
    L.delete(L.head.next)
    print('List is: ',L.printl())
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ',L.printl())
    print("3 found at position "+str(L.search(3)))

if __name__ == '__main__':
    main()