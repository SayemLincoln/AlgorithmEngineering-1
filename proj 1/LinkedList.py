########################################
# PROJECT 1 - Linked List
# Author: Sayem Lincoln
# PID: A54207835
#Date - 1/25/2018
########################################


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)


class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        Create/initialize an empty linked list
        """
        self.head = None  # Node
        self.tail = None  # Node
        self.size = 0     # Integer

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next_node
                temp_other = temp_other.next_node
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a linked list
        :return: string of list of values
        """
        temp_node = self.head
        values = []
        if temp_node is None:
            return None
        while temp_node is not None:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)

    ###### COMPLETE THE FUNCTIONS BELOW #####

    # ------------------------Accessor Functions---------------------------

    def length(self):
        """
        Gets the number of nodes of the linked list
        :return: size of list
        """
        return self.size

    def is_empty(self):
        """
        Determines if the linked list is empty
        :return: True if list is empty and False if not empty
        """
        return self.head == None

    def front_value(self):
        """
        Gets the first value of the list
        :return: value of the list head
        """
        if self.head is None:
            return None
        return self.head.value

    def back_value(self):
        """
        Gets the last value of the list
        :return: value of the list tail
        """
        if self.tail is None:
            return None
        return self.tail.value

    def count(self, val):
        """
        Counts the number of times a value 'val' occurs in the list
        :param val: value to find and count
        :return: number of time 'val' occurs
        """
        temp_node = self.head
        freq = 0
        while temp_node is not None:
            if val == temp_node.value:
                freq += 1
            temp_node = temp_node.next_node
        return freq

    def find(self, val):
        """
        Searches for and returns the first node with the value 'val'
        :param val: value to search for
        :return: True if value is in list, False if value is not found
        """
        temp_node = self.head
        while temp_node is not None:
            if val == temp_node.value:
                return True
            temp_node = temp_node.next_node
        return False

    # ------------------------Mutator Functions---------------------------

    def push_front(self, val):
        """
        Adds a node to the front of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        #condidtions for checking head
        new_head = Node(val, self.head)
        if self.head is not None:
            self.head = new_head
        else:
            self.head = self.tail = new_head
        self.size += 1

    def push_back(self, val):
        """
        Adds a node to the back of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        #condidtions for checking tail
        new_tail = Node(val, None)
        if self.tail is not None:
            self.tail.next_node = new_tail
            self.tail = new_tail
        else:
            self.head = self.tail = new_tail
        self.size += 1

    def pop_front(self):
        """
        Removes a node from the front of the list
        :return: the value of the removed node
        """
        #conditions for removing head
        old_head = self.head
        if self.head is None:
            return None
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = old_head.next_node
        self.size -= 1
        return old_head.value

    def pop_back(self):
        """
        Removes a node from the back of the list
        :return: the value of the removed node
        """
        #conditions for removing tail
        old_tail = self.tail
        temp_node = self.head
        if self.head is None:
            return None
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            while not temp_node.next_node == self.tail:
                temp_node = temp_node.next_node
            temp_node.next_node = None
            self.tail = temp_node
        self.size -= 1
        return old_tail.value
