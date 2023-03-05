
class Node:
    def __init__(self,data=None,next=None):
        self.data=data;
        self.next=next;
    
class linklist_of_array:
    def __init__(self):
        self.head=None

    def insert_array(self,data):
        if self.head is None:
            self.head=Node(data,self.head)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data)


    def printArray(self):
        itr=self.head
        listr=[]
        while itr:
            listr.append(itr.data)
            itr=itr.next
        print(listr)

    def reverseLinklist(self):
        
        preNode=None
        nextNode=curr=self.head
        while nextNode:
            nextNode=nextNode.next
            curr.next=preNode
            preNode =curr
            curr=nextNode
            
        self.head=preNode
        itr=self.head
        listr=[]
        while itr:
            listr.append(itr.data)
            itr=itr.next
        print(listr)   

    
    def list_of_arr(self,arr):
        for i in arr:
            self.insert_array(i)


li=linklist_of_array()
li.list_of_arr(["sejan","sajal","babu"])
li.list_of_arr([3,4,5,6,6,66,7,7,88,48,84,8,38,28])

li.printArray()
li.reverseLinklist()
