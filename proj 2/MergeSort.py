
class LinkedListNode:
    def __init__(self, val = None):
        """
        :param val of node
        :return None

        Constructor for Linked List Node, initialize next to None object
        """
        self.val = val
        self.next = None

    def __le__(self, other):
        '''
        :param other: Linked list node
        :return: boolean value of less than equal to other
        '''
        if isinstance(other, LinkedListNode):
            return self.val <= other.val





class LinkedList:
    def __init__(self):
        """
        :param None
        :return None

        Constructor for Singly Linked List, initialize head to None object
        """
        self.head = None

    def __repr__(self):
        '''
        :param: none
        :return: string representation of linked list
        '''
        result = []
        current = self.head

        while current:
            result.append(str(current.val))
            current = current.next

        return " -> ".join(result)

    __str__ = __repr__


    def push_back(self, data):
        '''
        :param data:  val for new node to be added to Linked list
        :return: None
        '''
        node = LinkedListNode(data)
        if self.head:
            last = self.head
            while last.next:
                last = last.next
            last.next = node

        else:
            self.head = node




'''
ANYTHING BEFORE THIS COMMENT SHOULDN'T BE MODIFIED IN ANYWAY!
'''
# --------- START MODIFYING HERE ---------


def MergeSort(head):
    if not head or not head.next:
        return head

    # Split the list into two halves
    leftTail = head
    rightTail = head.next
    while True:
        if not rightTail.next:
            break
        rightTail = rightTail.next
        if not rightTail.next:
            break
        leftTail = leftTail.next
        rightTail = rightTail.next

    leftHead = head
    rightHead = leftTail.next
    leftTail.next = None

    # Recursively sort the sublists
    leftHead = MergeSort(leftHead)
    rightHead = MergeSort(rightHead)

    # Merge the sorted sublists
    head = LinkedListNode()
    current = head

    while leftHead or rightHead:
        if not rightHead or leftHead and leftHead.val <= rightHead.val:
            current.next = leftHead
            current, leftHead = current.next, leftHead.next
        else:
            current.next = rightHead
            current, rightHead = current.next, rightHead.next

    head = head.next


    return head
