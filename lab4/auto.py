class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """

    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head = ListNode()

    def insert(self, k, x, p):
        """Insert element x in the position after p"""
        temp = ListNode(k, x, p.next)
        p.next = temp

    def delete(self, p):
        """Delete the node following node p in the linked list."""
        p.next = p.next.next

    def printl(self):
        """ Print all the elements of a list in a row."""
        temp = self.head.next
        while temp != None:
            print(temp.value,",", temp.key, end=". ")
            temp = temp.next

    def insertAtIndex(self, x, i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        temp = self.head
        while i != 0:
            temp = temp.next
            i = i - 1
        self.insert(x, temp)

    def correct(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp = self.head.next
        i = 0
        f = False
        while temp != None:
            if temp.key == x:
                f = True
                #print("Hi")
                print(temp.value,end=", ")
            i = i + 1
            temp = temp.next
        if f == False:
            return None

    def search(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp = self.head.next
        i = 0
        f = False
        while temp != None:
            if temp.value == x:
                f = True
                return i
            i = i + 1
            temp = temp.next
        if f == False:
            return None

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        i = 0
        temp = self.head.next
        while temp != None:
            i = i + 1
            temp = temp.next
        return i

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if self.head.next == None:
            return True
        else:
            return False


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next.
    """

    def __init__(self, key=None, val=None, nxt=None):
        self.key = key
        self.value = val
        self.next = nxt


def main():
    T=[LinkedList() for i in range(30) ]
    f = open('ispell.dict', 'r')
    d=f.read()
    d=d.split("\n")
    for i in d:
        x=i
        k = 0
        n = 1
        for e in range(0, len(x)):
            k = k + ord(x[e:e + 1])*n
            n = n*33
        key = k
        k = k % 30
        T[k].insert(key, x, T[k].head)
    s = input("Enter word: ")
    f=0
    k = 0
    n = 1
    for i in range(0, len(s)):
        k = k + ord(s[i:i + 1])*n
        n=n*33
    key = k % 30
    i = T[key].search(s)
    if i != None:
        print("Valid word.")
    else:
        n = 1
        for p in range(len(s)):
        	for o in range(97,123):
        		k1=k
        		k1=k1+(o-ord(s[p]))*n
        		key=k1%30
        		T[key].correct(k1)
        	n=n*33



main()