class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data;
        self.prev=prev;
        self.next=None;
        
class DoubleLinklist:
    def __init__(self):
        self.head=None
        self.tail=None


    def insert_data(self,data):
        if self.head is None:
            newNode=Node(data)
            self.head=newNode
            self.tail=newNode
        else:
            tail=self.tail
            tail.next=Node(data,tail)
            self.tail=tail.next
           
    def insert_at_begging(self,data):
        head=self.head
        newNode=Node(data)
        head.prev=newNode
        newNode.next=head
        self.head=newNode

    def insert_by_index(self,index,data):
        head=self.head
        count=0
        while count<index-1:
            count+=1
            head=head.next
        newNode=Node(data)
        head.next.prev=newNode
        newNode.next=head.next
        newNode.prev=head
        head.next=newNode
    def delete_beginning(self):
        temp=self.head
        if temp is None:
            return "Empty linkedlist"
        else:
            self.head=temp.next
            self.head.prev=None
            del(temp)

    def delete_by_index(self,index):
        temp=self.head
        count=0
        if temp is None:
            return "Empty linkedlist"
        else:
            while count<index:
                count+=1
                temp=temp.next
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
            del(temp)
            
    def reverse_double_linkedlist(self):
        curr=self.head
        while curr:
            nextNode=curr.next
            curr.next=curr.prev
            curr.prev=nextNode
            curr=nextNode
   
        currnt=self.head
        self.head=self.tail
        self.tail=currnt
        
        




    def printLink(self):
        head=self.head
        arr=[]
        preArr=[]
        while head:
            arr.append(head.data)
            previous=head.prev
            if previous:
                preArr.append(previous.data)
            else:
                preArr.append(None)   
            head=head.next
        print(arr,"prev",preArr)





dLink=DoubleLinklist()
dLink.insert_data(2)
dLink.insert_data(3)
dLink.insert_data(4)
dLink.insert_data(5)
dLink.insert_data(6)
dLink.insert_at_begging(11)
dLink.insert_by_index(3,22)
dLink.delete_beginning()
dLink.printLink()
dLink.delete_by_index(3)
dLink.printLink()
dLink.reverse_double_linkedlist()
dLink.printLink()