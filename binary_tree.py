class BinaryTree():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    
    def addChild(self, data):
        if self.data == data:
            return "data already exit"
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinaryTree(data)
    def search(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False
    
    
    def deleteData(self, data):
        if data < self.data:
            if self.left:
                self.left =  self.left.deleteData9data(data)
        if data > self.data:
            if self.right:
                self.right = self.right.deleteData(data)
        else:
           if self.left is None and self.right is None:
               return None
           if self.left is None:
               return self.left
           if self.right is None:
               return self.right
           minVal = self.right.findMin()
           self.data = minVal
           self.right = self.right.deleteData(minVal)
        return self
                
    
    def findMin(self):
        if self.left is None:
            return self.data
        return self.left.findMin()
    
    def findMAX(self):
        if self.right is None:
            return self.data
        return self.right.findMAX()
            
            
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
       
        return elements
    
    def pre_order_travarsal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_travarsal()  
        if self.right:
            elements += self.right.pre_order_travarsal()   
        return elements
    
    def post_order_travarsal(self):
        elements = []
        
        if self.left:
            elements += self.left.pre_order_travarsal()  
        if self.right:
            elements += self.right.pre_order_travarsal()   
        elements.append(self.data)
        return elements

if __name__ == "__main__":
    root = BinaryTree(10)
    root.addChild(7)
    root.addChild(12)
    root.addChild(6)
    root.addChild(16)
    print(root.in_order_traversal())
    print(root.pre_order_travarsal())
    print(root.post_order_travarsal())
    print(root.search(17))