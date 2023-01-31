########################################
# PROJECT 6 - BinarySearchTree
# Author: Sayem Lincoln
# PID: A54207835
########################################


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Describes equality comparison for nodes ('==')
        :param other: node being compare to
        :return: True if equal, False if not equal
        """
        return type(other) is type(self) and self.value == other.value

    def __repr__(self):
        """
        Defines string representation of a node (str())
        :return: string representing node
        """
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        :return nothing
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result


    ### Implement/Modify the functions below ###

    def insert(self, value):
        """
        Takes value and inserts it into the BST
        :param t1: If the value already exists in the tree, nothing is changed.
        :param t2: When inserting new nodes, lesser values are inserted on the left
                    and greater values are inserted on the right.
        :return: Nothing
        """
        if self.root != None:
            node = self.search(value, self.root)
            if node.value == value:
                return None
            if node.value > value:
                node.left = Node(value, node)
            else:
                node.right = Node(value, node)
            self.size += 1
        else:
            self.root = Node(value)
            self.size = 1
             

    def remove(self, value):
        """
        Finds and removes a node with the given value
        :param t1: replace with the minimum of the right subtree
        :return: Nothing
        """
        node = self.search(value, self.root)
        if node == None or node.value != value: # There is no such value in tree
            return None
            
        if self.size == 1:
            self.root = None
            self.size = 0
            return None
            
        if node.left == None and node.right == None: # 1. node is a leaf
            if node.parent.value > node.value:
                node.parent.left = None
            else:
                node.parent.right = None
            self.size -= 1
                
        elif node.left == None or node.right == None: # 2. node has only one child
            child = node.left or node.right
            if node.parent != None: # if we delete not root
                if node.parent.value > node.value:
                    node.parent.left = child
                else:
                    node.parent.right = child
            else:
                self.root = child
            child.parent = node.parent
            self.size -= 1
                
        else: # 3. node has two children
            # removed node will be replaced by minimum node in right subtree
            replace_node = self.min(node.right) 
            self.remove(replace_node.value) 
            if node.parent != None: # if we delete not root
                replace_node.parent = node.parent
                replace_node.left, replace_node.right = node.left, node.right
                if node.parent.value > node.value:
                    node.parent.left = replace_node
                else:
                    node.parent.right = replace_node
            else:
                self.root.value = replace_node.value
            
        

    def search(self, value, node):
        """
        Recursively searches the subtree for the given value.
        :param t1: If the value is found, return the node
        :return: If the value is not found, return the
        potential parent node. If the tree is empty, return None.
        """
        if self.root == None:
            return None
            
        if node.value == value:
            return node
        if node.value > value:
            if node.left == None:
                return node
            else:
                return self.search(value, node.left)
        else:
            if node.right == None:
                return node
            else:
                return self.search(value, node.right)
        

    def inorder(self, node, inorder_list=list()):
        """
        Recursively performs an in-order traversal of the BST starting at the specified
        node, and stores the values of the nodes in the parameter inorder_list
        :param t1: O(n)
        :return: The list of values is returned.
        """
        if self.root == None:
            return None
        if node != None:
            self.inorder(node.left, inorder_list)
            inorder_list.append(node.value)
            self.inorder(node.right, inorder_list)
        return inorder_list

    def preorder(self, node, preorder_list=list()):
        """
        Recursively performs an pre-order traversal of the BST starting at the specified
        node, and stores the values of the nodes in the parameter inorder_list
        :param t1: O(n)
        :return: The list of values is returned.
        """
        if self.root == None:
            return None
            
        if node != None:
            preorder_list.append(node.value)
            self.preorder(node.left, preorder_list)
            self.preorder(node.right, preorder_list)
        return preorder_list

    def postorder(self, node, postorder_list=list()):
        """
        Recursively performs an post-order traversal of the BST starting at the specified
        node, and stores the values of the nodes in the parameter inorder_list
        :param t1: O(n)
        :return: The list of values is returned.
        """
        if self.root == None:
            return None
            
        if node != None:
            self.postorder(node.left, postorder_list)
            self.postorder(node.right, postorder_list)
            postorder_list.append(node.value)
        return postorder_list

    def depth(self, value):
        """
        Finds the depth of the node with the specified value.
        :param t1: height of the node
        :return: If the value is not in the tree, return -1.
        """
        node = self.search(value, self.root)
        if node.value != value:
            return -1
        if node.parent == None:
            return 0
        else:
            return 1 + self.depth(node.parent.value)
            

    def height(self, node):
        """
        Finds and returns the height of the BST
        :param t1: O(n)
        :return: height of the BST
        """
        if self.root == None:
            return None
        if node.left == None and node.right == None:
            return 0
        else:
            if node.left != None:
                left = self.height(node.left)
            else:
                left = -1
            if node.right != None:
                right = self.height(node.right)
            else:
                right = -1
            return max(left, right) + 1

            
    def min(self, node):
        """
        Moves recursively through the subtree tofind the node with the minimum value.
        :param t1: the node with the minimum value
        :return: That node is returned. If the tree is empty, return None
        """
        if self.root == None:
            return None
        if node.left == None:
            return node
        return self.min(node.left)

        
    def max(self, node):
        """
        Moves recursively through the subtree to find the node with the maximum value.
        :param t1: the node with the maximum value.
        :return: That node is returned. If the tree is empty, return None.
        """
        if self.root == None:
            return None
        if node.right == None:
            return node
        return self.max(node.right)

        
    def get_size(self):
        """
        Gets and returns the size of the BST.
        :param t1: O(1)
        :return: the size of the BST.
        """
        return self.size