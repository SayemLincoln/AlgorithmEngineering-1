###################################
# PROJECT 5- QuickSort.py
# Author: Sayem Lincoln
# PID: A54207835
###################################

from Queue import LinkedQueue, Node


def insertion_sort(queue):
    """precondition: none  
    postcondition:  Update queue: modify linked list queue 
    """ 
    
    head=queue.head
       
    if not head:
        return
        
    new_node = Node(head.val,None)
    new_node.next = queue.head
    queue.head = new_node

    
    dummy = new_node
    
    current = head
    while current is not None:
        if current.next is not None and current.next.val < current.val:
            
            #find insert position for smaller item (current->next)
            prev = dummy
            while prev.next is not None and prev.next.val < current.next.val:
                prev = prev.next
                
            #insert current->next after prev
            temp = prev.next
            prev.next = current.next
            current.next = current.next.next
            prev.next.next = temp
        else:
            current = current.next
            
    #skip new_node       
    queue.head=queue.head.next
       
 


def pick_pivot(queue, left, right):
    """precondition: the right node is after left node by >=2  
    postcondition:  none 
    """
    #gives a built-in scalar type & does not run 3 elements in queue

    size=0
    node = left
    while node != right:
        size+=1
        node = node.next
     
    index=size//2 
    node = left
    for i in range(index+1):
        node = node.next
        
    return node.val, node
    

    
 
def quick_sort(queue):
    """precondition: none  
    postcondition:  Update queue: modify linked list queue 
    """
    #modifying linked list queue here
    if(queue.size<=10):
        insertion_sort(queue)
    else:
        _quick_sort(queue,queue.head,queue.tail)
        
        

def swap(A, B):
    """precondition: A !=None, B!=None  
    postcondition:  none 
    """
    
    '''swaps the data in two nodes'''
    #swapping nodes here
    temp = A.val
    A.val=B.val
    B.val=temp


def isContinue(first, last):
      """precondition: None  
        postcondition: None 
      """
		
      '''boolean: returns True if the last is after first '''
        
         #checking for true and false here 
    		
      if first == last:
          return False
      elif first == None or last == None:
          return False
      else:
         counter=0;
         current = first
         while current != None:
              counter+=1
              if last == current and counter>=2:
                  return True
              current = current.next
      return False
  



def findPrevious(first, last, node):       
	'''find the item before the node''' """
 
    precondition: the right node is after left node by >=2  
    postcondition:  none 
    """
    #finding items here
		
	current = first
		
	while current != last.next:
		if current.next == node:
				
			return current
				
		current = current.next
	return None
  


def partition_chair(queue, left, right):
		'''partitions the queue using the last item as the pivot'''"""
  
              precondition: the right node is after left node by >=2  
              postcondition:  none 
              """		
              #partitioning character here
		val, pivot = pick_pivot(queue, left, right)		
		
		current = left
		switcher = current
		while current != right:
			if current.val < val:
				
				swap(switcher, current)
				switcher = switcher.next
			
			current = current.next
		swap(pivot, switcher)
		
		return switcher
   
def _quick_sort(queue,left, right):
    """precondition: none  
    postcondition:  Update queue: modify linked list queue 
    """ 
    #modifying linkedlist queue here
    if isContinue(left, right):
        node = partition_chair(queue,left, right)
        
        _quick_sort(queue,node.next, queue.tail)
        prev = findPrevious(queue.head,queue.tail, node)
        _quick_sort(queue,left, prev)				
			
