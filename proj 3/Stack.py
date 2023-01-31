###################################
# PROJECT 3 - STACK
# Author: Sayem Lincoln
# PID: A54207835
###################################

class Stack:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self, capacity=2):
        """
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack.
        """
        self._capacity = capacity
        self._data = [0] * self._capacity
        self._size = 0

    def __str__(self):
        """
        Prints the elements in the stack from bottom of the stack to top,
        followed by the capacity.
        :return: string
        """
        if self._size == 0:
            return "Empty Stack"

        output = []
        for i in range(self._size):
            output.append(str(self._data[i]))
        return "{} Capacity: {}".format(output, str(self._capacity))

    ###### COMPLETE THE FUNCTIONS BELOW ######

    # --------------------Accessor Functions---------------------------------
    def get_size(self):
        """
        Returns number of items currently in the stack
        """
        return self._size

    def is_empty(self):
        """
        Returns True if the stack is empty, False if not
        """
        if self.get_size() == 0:
            return True
        else:
            return False

    def top(self):
        """
        Returns, but not remove, the top item from the stack
        Returns None if stack is empty
        """
        if self.is_empty():
            return None
        else:
            return self._data[self.get_size() - 1]

    # ---------------------------Mutator Functions------------------------------

    def push(self, addition):
        """
        Adds an item to the top of the stack
        Returns nothing
        """
        self.grow()
        self._data.insert(self._size,addition)
        self._size += 1
        
    def pop(self):
        """
        Removes and returns the top value from the stack, or None if empty
        """
        if self.is_empty():
            return None
        else:
            item = self.top()
            self._data[self._size - 1] = 0
            self._size -= 1
            self.shrink()
            return item
           
    def grow(self):
        """
        Resize the stack to be 2 times its previous size when stack size equals capacity
        """
        if self._size == self._capacity:
            self._data = self._data + [0] * self._capacity
            self._capacity = 2 * self._capacity

    def shrink(self):
        """
        Resize the stack to be half its current size when stack size is less than or equal to half its capacity
        """
        if self._size <= self._capacity / 2 and self._capacity >= 4:
            self._capacity = int(self._capacity / 2) 
            self._data = self._data[:self._capacity + 1]


'''
Add doc strings here too!
'''
def Palindrome(phrase):
    """
    This function takes in a phrase and returns True if it is a palindrome, False if not
    """
    # convert all uppercase characters in the phrase into lowercase characters
    phrase = phrase.lower()
    # determine the length of the phrase
    n = len(phrase)
    # create an object stack1 of a class of Stack
    stack1 = Stack(n)
    for i in range(n):
        # all the letters of the phrase are placed in the stack1
        if phrase[i].isalpha():
            stack1.push(phrase[i])
    
    # create an object stack2 of a class of Stack
    stack2 = Stack(n)
    for i in range(n):
        # all the letters of the phrase are placed in the stack in reverse order
        if phrase[n - 1 - i].isalpha():
            stack2.push(phrase[n - 1 - i])
    
    # compare two stacks
    if stack1._data == stack2._data:
        return True
    else:
        return False