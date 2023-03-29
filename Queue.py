class Node:
    def __init__(self,data,next=None) -> None:
        self.data=data
        self.next=next

class Queue:

    def __init__(self):
        self.head=None
        self.tail=None


    def enqueue(self,data):
        if self.head is None:
            newNode=Node(data)
            self.head=newNode
            self.tail=newNode
        else:
            tail=self.tail
            newNode=Node(data)
            tail.next=newNode
            self.tail=newNode
    def dequeue(self):
        
        if self.head is None:
            print("self.head",self.head)
        else:
            head=self.head
            self.head=head.next



    def printLink(self):
        head=self.head
        arr=[]

        while head:
            arr.append(head.data)  
            head=head.next
        print(arr)

qu=Queue()
qu.enqueue(2)
qu.enqueue(4)
qu.enqueue(4)
qu.enqueue(5)
qu.enqueue(7)
qu.printLink()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.printLink()
qu.dequeue()
qu.dequeue()
qu.printLink()

