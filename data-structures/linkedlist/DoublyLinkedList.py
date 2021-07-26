# for Garbage collection
import gc

class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next 
        self.prev = prev 
        self.data = data

class DoublyList:
    def __init__(self):
        self.head = None


    def push(self, new_data): # add a new node at the front
        aux = Node(data = new_data) # creating the node

        aux.next = self.head
        aux.prev = None

        if self.head is not None:
            self.head.prev = aux

        self.head = aux
    
    def append(self, new_data): # add a new node at the end
    
            aux = Node(data = new_data)
            last = self.head
    
            # next is null because it is the last node
            aux.next = None
    
            #empty list
            if self.head is None:
                aux.prev = None
                self.head = aux
                return
    
            while (last.next is not None):
                last = last.next
    
            last.next = aux
            aux.prev = last

    def printList(self, node):
        print("Traversal in forward direction")
        while node:
            print(" %d" % (node.data)),
            last = node
            node = node.next
 
        print("Traversal in reverse direction")
        while last:
            print(" %d" % (last.data)),
            last = last.prev

    def deleteNode(self, aux):
        if self.head is None or aux is None:
            return
         
        # head node
        if self.head == aux:
            self.head = aux.next
        # not the last node
        if aux.next is not None:
            aux.next.prev = aux.prev
        # not the first node
        if aux.prev is not None:
            aux.prev.next = aux.next

        # garbage collector
        gc.collect()



# testing 
l1 = DoublyList()
l1.append(6)
l1.push(7)
l1.push(1)
l1.append(4)
l1.printList(l1.head)
l1.deleteNode(l1.head.next) # 7
l1.printList(l1.head)
