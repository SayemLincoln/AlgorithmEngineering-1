###################################
# PROJECT 5- Queue.py
# Author: Sayem Lincoln
# PID: A54207835
###################################

class Node:
  """Lightweight, nonpublic class for storing a singly linked node.
    should only be called within the LinkedQueue class definition """

  __slots__ = 'val', 'next'         # streamline memory usage

  def __init__(self, val, next):
    self.val = val
    self.next = next

  def __lt__(self, other):
    ''' assumes other is of same type, invoked with "<" '''
    return self.val <= other.val

  def __le__(self, other):
    ''' assumes other is of same type, invoked with "<=" '''
    return self.val <= other.val



class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  def __init__(self):
    """Create an empty queue."""
    self.head = None
    self.tail = None
    self.size = 0


  def __str__(self):
    ''' string implementation of current elements in queue '''
    head = self.head
    values = list()
    while head:
      values.append(str(head.val))
      head = head.next

    return ", ".join(values)

  __repr__ = __str__


################## start modifying below this line ######################
  def __len__(self):
    """precondition: none  
    postcondition:  none"""
    length = 0
    node = self.head
    while node:
        length += 1
        node = node.next
    
    return length
    
  def is_empty(self):
    """precondition: none  
    postcondition:  none"""
    return self.head == None

  def dequeue(self):
    """precondition: none  
    postcondition:  Update queue: remove item from linked list queue """
    if not self.head:
        return None
    value=self.head.val
    self.head = self.head.next
    self.size-=1
    return value
    
    


  def enqueue(self, element):
    """precondition:  None  
    postcondition:  Update queue - add element to end of linked list queue"""
    if not self.head:
            self.head = Node(element, None)
            return
            
    node = self.head
    while node.next:
        node = node.next
    node.next = Node(element, None)
    self.tail = node.next
    self.size+=1


  def get_middle(self):
    """precondition:  linked list queue is not empty 
    postcondition:  update size of linked list queue"""
    self.size=self.__len__()
    
    index=self.size//2 
    node = self.head
    while node and index:
        node = node.next
        index -= 1
    if node:
        return node.val
    return

