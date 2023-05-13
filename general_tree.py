class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def addChild(self, data):
        self.child = self
        print('self.child',self.child.data, "self", self.data)
        print("TreeNode(data)", TreeNode(data))
        self.children.append(TreeNode(data))
        for child in self.children:
            print("self.child.data", child.data.data)
    
def buildTree():
    root = TreeNode("Electronis")
    laptop = TreeNode("laptop")
    car = TreeNode("car")
    root.addChild(laptop)
    root.addChild(car)
    
if __name__ == "__main__":
    buildTree()