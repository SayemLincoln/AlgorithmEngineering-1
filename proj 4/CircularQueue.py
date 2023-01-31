###################################
# PROJECT 4 - CircularQueue
# Author: Sayem Lincoln
# PID: A54207835
###################################


class CircularQueue(object):
    def __init__(self, capacity=2):
        """
        Initialize the queue to be empty with a fixed capacity
        :param capacity: Initial size of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.list = [0] * self.capacity
        self.sum = 0
        self.read = 0
        self.write = 0

    def __eq__(self, other):
        return self.capacity == other.capacity \
               and self.size == other.size \
               and self.read == other.read \
               and self.write == other.write

    # ----------------------- MODIFY BELOW THIS LINE ---------------------------
    def __str__(self):
        """ Produce a string represantation of the queue """
        #Provides a string representation of a CircularQueue
        #This method will allow you to easily see the contents of your queue

        if self.size == 0:
            return "Queue is empty"

        content = ""
        ##  INSERT STRING OUTPUT CODE HERE!

        if (self.read + self.size == self.write):
            content += ", ".join(map(str, self.list[self.read:self.write]))
            
          
            # only the write pointer has been wrapped around
        else: 
            content += ", ".join(map(str, self.list[self.read:self.capacity]))
            content += ", "
            content += ", ".join(map(str, self.list[0:self.write]))

        return f"Contents: {content}"


    # DO NOT MODIFY or DELETE this line
    __repr__ = __str__

    def enqueue(self, number):
        """ Append a number to the end of the queue
        :param number: the value to be inserted
        """
        #Adds a number to the back of the queue.
        if self.size >= self.capacity:
            self.resize()
        self.list[self.write] = number
        self.write = (self.write + 1) % self.capacity
        self.size += 1
        self.sum += number

    def dequeue(self):
        """ Remove an element from the head of the queue if possible """
        #Removes an element from the front of a queue but do nothing if the queue is empty.
        if self.size == 0:
            return
        number = self.list[self.read]
        self.read = (self.read + 1) % self.capacity
        self.size -= 1
        self.sum -= number

    def get_average(self):
        """ Produce an average of the elements in the queue """
        #Returns the average of the elements contained in the queue
        if self.size == 0:
            return float(0)
        return self.sum / self.size

    def resize(self):
        """ Double the capacity of the queue """
        #Resizes the queue to be twice its previous size
        if self.read + self.size == self.write:
            self.list.extend([0] * self.capacity)
            self.capacity *= 2
        else:
            self.list.extend(self.list[0:self.write])
            self.list.extend([0] * (self.capacity - self.write))
            # assert(len(self.list) == 2 * self.capacity)
            self.write = self.read + self.size
            self.capacity *= 2
        


