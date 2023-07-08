class Node:
    def __init__(self,data):
        self.data= data
        self.right_child = None
        self.left_child = None
        
class binarySearchTree:
    def __init__(self):
        self.root_node = None
        
    def insert(self, data):
        if not self.root_node:
            self.root_node = Node(data)
        else:
            self.insertNode(data, self.root_node)
            
    def insertNode(self, data, node):
        if data < node.data:
            if node.left_child:
                self.insertNode(data, node.left_child)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child:
                self.insertNode(data, node.right_child)
            else:
                node.right_child = Node(data)
        
    def getMinValue(self):
        if self.root_node:
            return self.getMin(self.root_node)
    
    def getMin(self, node):
        if node.left_child:
            return self.getMin(node.left_child)
        return node.data
    
    def getMaxValue(self):
        if self.root_node:
            return self.getMax(self.root_node)
        
    def getMax(self, node):
        if node.right_child:
            return self.getMax(node.right_child)
        return node.data
        
    def traverse(self):
        if self.root_node:
            self.traverseInOrder(self.root_node)
            
    def traverseInOrder(self, node):
        if node.left_child:
            self.traverseInOrder(node.left_child)
        
        print(node.data)
        
        if node.right_child:
            self.traverseInOrder(node.right_child)
            

    def remove(self, data):
        if self.root_node:
            self.root_node = self.removeNode(data,self.root_node)
            
    def removeNode(self, data, node):
        if not node:
            return node
        
        if data < node.data:
            node.left_child = self.removeNode(data, node.left_child)
        elif data > node.data:
            node.right_child = self.removeNode(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print('Removing a leaf node')
                del node
                return None
            
            if not node.left_child:
                print('Removing a node with a single right child')
                temp_node = node.right_child
                del node
                return temp_node
            elif not node.right_child:
                print('Removing a node with a single left child')
                temp_node = node.left_child
                del node
                return temp_node
            
            print('Removing a node with two children')
            temp_node= self.getPredecessor(node.left_child)
            node.data = temp_node.data
            node.left_child = self.removeNode(temp_node.data, node.left_child)
            
        return node
            
    def getPredecessor(self, node):
        if node.right_child:
            return self.getPredecessor(node.right_child)
        return node
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            
        
        
        