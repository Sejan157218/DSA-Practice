class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data;
        self.prev=prev;
        self.next=None;
        
class DoubleLinklist:
    def __init__(self):
        self.head=None
        self.temp=None


    def insert_data(self,data):
        if self.head is None:
            newNode=Node(data)
            self.head=newNode
            self.temp=newNode
        else:
            temp=self.temp
            temp.next=Node(data,temp)
            self.temp=temp.next
           


                
            
    def printLink(self):
        head=self.head
        while head:
            previous=head.prev
            print("head",head.data)
            if previous:
                print("ff",previous.data)
            head=head.next





dLink=DoubleLinklist()
dLink.insert_data(2)
dLink.insert_data(3)
dLink.insert_data(4)
dLink.insert_data(5)
dLink.insert_data(6)
dLink.printLink()