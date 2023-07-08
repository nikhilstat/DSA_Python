class Node:
    def __init__(self, data):
        """
        Class representing a node in a binary search tree.

        Parameters:
        - data: The data to be stored in the node.
        """
        self.data = data
        self.right_child = None
        self.left_child = None


class BinarySearchTree:
    def __init__(self):
        """
        Class representing a binary search tree.

        The tree is initialized with an empty root node.
        """
        self.root_node = None

    def insert(self, data):
        """
        Inserts a new node with the given data into the binary search tree.

        If the tree is empty, the new node becomes the root node. Otherwise,
        the insertNode() method is called to find the correct position for insertion.

        Parameters:
        - data: The data to be inserted into the tree.
        """
        if not self.root_node:
            self.root_node = Node(data)
        else:
            self.insertNode(data, self.root_node)

    def insertNode(self, data, node):
        """
        Recursively finds the correct position to insert a new node with the given data.

        If the data is less than the current node's data, the method is called again
        with the left child of the current node. If the data is greater, the method is
        called with the right child. The recursion continues until an appropriate
        position is found.

        Parameters:
        - data: The data to be inserted into the tree.
        - node: The current node being considered for insertion.
        """
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
        """
        Returns the minimum value in the binary search tree.

        Starts the search from the root node and recursively moves to the left child
        until the leftmost leaf node is reached.

        Returns:
        - The minimum value in the tree.
        """
        if self.root_node:
            return self.getMin(self.root_node)

    def getMin(self, node):
        """
        Recursively finds the minimum value in the binary search tree.

        Continuously moves to the left child of each node until the leftmost leaf node
        is reached.

        Parameters:
        - node: The current node being considered.

        Returns:
        - The minimum value in the subtree.
        """
        if node.left_child:
            return self.getMin(node.left_child)
        return node.data

    def getMaxValue(self):
        """
        Returns the maximum value in the binary search tree.

        Starts the search from the root node and recursively moves to the right child
        until the rightmost leaf node is reached.

        Returns:
        - The maximum value in the tree.
        """
        if self.root_node:
            return self.getMax(self.root_node)

    def getMax(self, node):
        """
        Recursively finds the maximum value in the binary search tree.

        Continuously moves to the right child of each node until the rightmost leaf node
        is reached.

        Parameters:
        - node: The current node being considered.

        Returns:
        - The maximum value in the subtree.
        """
        if node.right_child:
            return self.getMax(node.right_child)
        return node.data

    def traverse(self):
        """
        Performs an in-order traversal of the binary search tree and prints the node values.

        Starts the traversal from the root node and recursively visits the left child,
        prints the value of the current node, and then visits the right child.
        """
        if self.root_node:
            self.traverseInOrder(self.root_node)

    def traverseInOrder(self, node):
        """
        Recursively performs an in-order traversal of the binary search tree.

        Traverses the left subtree, prints the value of the current node, and then
        traverses the right subtree.

        Parameters:
        - node: The current node being visited.
        """
        if node.left_child:
            self.traverseInOrder(node.left_child)

        print(node.data)

        if node.right_child:
            self.traverseInOrder(node.right_child)

    def remove(self, data):
        """
        Removes a node with the given data from the binary search tree.

        If the tree is not empty, the removeNode() method is called to find and remove
        the node with the specified data.

        Parameters:
        - data: The data to be removed from the tree.
        """
        if self.root_node:
            self.root_node = self.removeNode(data, self.root_node)

    def removeNode(self, data, node):
        """
        Recursively finds and removes the node with the given data from the binary search tree.

        If the node is found, there are three cases to consider:
        1. If the node has no children, it is simply deleted.
        2. If the node has only one child, the child replaces the node.
        3. If the node has two children, the value of the node is replaced with the value
           of its in-order predecessor, and the predecessor node is then removed.

        Parameters:
        - data: The data to be removed from the tree.
        - node: The current node being considered.

        Returns:
        - The modified subtree after removal.
        """
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
            temp_node = self.getPredecessor(node.left_child)
            node.data = temp_node.data
            node.left_child = self.removeNode(temp_node.data, node.left_child)

        return node

    def getPredecessor(self, node):
        """
        Returns the in-order predecessor of a given node in the binary search tree.

        The in-order predecessor is the node with the maximum value in the left subtree
        of the given node.

        Parameters:
        - node: The current node being considered.

        Returns:
        - The in-order predecessor of the given node.
        """
        if node.right_child:
            return self.getPredecessor(node.right_child)
        return node
