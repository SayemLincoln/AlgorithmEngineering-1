########################################
# PROJECT  - LinkedList.py
# Author: Sayem Lincoln
# PID: A54207835
########################################

class HashListNode:
    def __init__(self, key, val = None):
        """
        DO NOT EDIT
        :param val of node
        :return None

        Constructor for Linked List Node, initialize next to None object
        """
        self.value = val
        self.key = key
        self.next = None

    def __str__(self):
        '''
        DO NOT EDIT
        String representation of a linked list node

        :return: String representation
        '''
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        '''
        DO NOT EDIT
        Equality operator
        :return: True if equal, false if not
        '''

        if self and other:
            return self.value == other.value and self.next == other.next \
                   and self.key == other.key
        elif not self and not other:
            return True

        return False

class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        :param None
        :return None

        Constructor for Singly Linked List, initialize head to None object
        """
        self.head = None
        self.tail = None

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """

        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next
                temp_other = temp_other.next
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True


    # -------------------------------
    # ----- DO NOT MODIFY ABOVE -----
    # ----- MODIFY BELOW ------------
    # -------------------------------


    def __repr__(self):
        """
        For debugging use
        :return: string representation of linked list.
        """
        if self.head == None:
            result = ''
        else:
            result = self.head.__str__() 
            temp_self = self.head.next
            while temp_self is not None:
                result += '->' + temp_self.__str__()
                temp_self = temp_self.next

        return result


    __str__ = __repr__


    def append(self, key, value):
        """
         Pushes new node with key and value to the end of linked list.
        :return: nothing
        """
        temp = HashListNode(key, value)
        if self.head == None:
            self.head = temp
        else:
            temp_self = self.head
            while temp_self.next is not None:
                temp_self = temp_self.next
            temp_self.next = temp


    def remove(self, key):
        """
         Removes node with specific key from linked list.
        :return: nothing
        """
        if self.head.key == key:
            self.head = self.head.next
        else:
            previous_self = self.head
            temp_self = self.head.next
            while temp_self is not None:
                if temp_self.key == key:
                    previous_self.next = temp_self.next
                previous_self = temp_self
                temp_self = temp_self.next


    def find(self, key):
        """
         Returns node with key if present in linked list. Otherwise returns false.
        :return: True if present, False otherwise
        """
        if self.head != None:
            if self.head.key == key:
                return self.head
            else:
                temp_self = self.head.next
                while temp_self is not None:
                    if temp_self.key == key:
                        return temp_self
                    temp_self = temp_self.next

            return False

        return False

