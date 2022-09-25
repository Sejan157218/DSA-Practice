# class Node:
#     def __init__(self,data=None,next=None):
#         self.data=data
#         self.next=next
        
# class linklist:
#     def __init__(self):
#         self.head=None

#     def insert_in_begining(self,data):
#         self.head=Node(data,self.head)

#     def print(self):
#         itr=self.head   
#         listr=''
#         while itr:
#             suffix=''
#             if itr.next:
#                 suffix="-->"

#             listr += str(itr.data)+suffix
#             itr=itr.next
#         print(listr)


#     def insert_in_end(self,data):
#         if self.head is None:
#             self.head=Node(data,None)
#             return
#         itr=self.head
#         while itr.next:
#             itr=itr.next
#         itr.next=Node(data)


# root=linklist()
# # root.insert_in_begining(5)
# # root.insert_in_begining(10)
# root.insert_in_end(10)
# root.insert_in_end(10)
# root.insert_in_end(10)
# root.print()






# class Node:
#     def __init__(self,data=None,next=None):
#         self.data=data
#         self.next=next


# class linklist:
#     def __init__(self):
#         self.head=None
    
#     # def insert_at_beginning(self,data):
#     #     node=Node(data,self.head)
#     #     self.head=node

#     def print(self):
#         itr=self.head
#         listr=[]
#         while itr:
#             listr.append(itr.data)
#             itr=itr.next
#         print(listr)

#     def get_length(self):
#         itr=self.head
#         count=0
#         while itr:
#             count +=1
#             itr=itr.next
#         return count


#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head=Node(data,self.head)
#             return
#         itr=self.head
#         while itr.next:
#             itr=itr.next
#         itr.next=Node(data)

#     def insert_at(self,index,data):
#         if index<0 or index > self.get_length():
#             return Exception ("invalid index")
#         if index==0:
#             self.head=Node(data,self.head)
#         itr=self.head
#         count=0
#         while itr:
#             if count==index-1:
#                 itr.next=Node(data,itr.next)
#                 break
#             count +=1
#             itr=itr.next

#     def remove_at(self,index):
#         if index<0 or index>self.get_length():
#             return Exception ("invalid index")

#         if index==0:
#             self.head=self.head.next
#             return
#         itr=self.head
#         count=0
#         while itr:
#             if count==index-1:
#                 itr.next=itr.next.next
#                 break
                
#             count +=1
#             itr=itr.next
        


# root=linklist()
# root.insert_at_beginning(5)
# root.insert_at_beginning(15)
# root.insert_at_beginning(25)
# root.insert_at_beginning(35)
# root.insert_at_beginning(45)
# root.insert_at_end(33)
# root.insert_at_end(333)
# root.insert_at_end(233)
# root.insert_at_beginning(345)
# root.insert_at(3,1)
# root.print()
# root.remove_at(0)
# root.print()

# root.remove_at(12)
# root.print()
# print(root.get_length())







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
        
    
    def list_of_arr(self,arr):
        for i in arr:
            self.insert_array(i)


li=linklist_of_array()
li.list_of_arr(["sejan","sajal","babu"])
li.list_of_arr([3,4,5,6,6,66,7,7,88,48,84,8,38,28])

li.printArray()