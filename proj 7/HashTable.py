########################################
# PROJECT  - HashTable.py
# Author: Sayem Lincoln
# PID: A54207835
########################################


from LinkedList import LinkedList, HashListNode


class HashTable:
    """
    Hash table class, utilizes linked list for resolving collisions with separate chaining
    """
    def __init__(self, tableSize=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.tableSize = tableSize
        self.numItems = 0
        self.table = [LinkedList() for i in range(self.tableSize)]

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.tableSize != other.tableSize:
            return False
        for i in range(self.tableSize):
            if self.table[i] != other.table[i]:
                return False
        return True

    def hash_function(self, x):
        """
        DO NOT EDIT
        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.tableSize


    # ------------------------------------------
    # ---------- DO NOT MODIFY ABOVE -----------
    # ------------------------------------------
    # -------------- MODIFY BELOW --------------


    def __repr__(self):
        """
        :return: tableSize: string representation of Hash Table
        """
        result = ''
        i = 0
        for linkedlist in self.table:
            result += '[' + str(i) + ']: ' +  linkedlist.__repr__() + '\n'
            i += 1
            
        return result
        #return "--------------\nHASH TABLE REPRESENTATION - TO DO\n--------------\n"

    def insert(self, key, value):
        """
        Inserts key and value into hash table, location based off of key hash from the provided hash_function
        :param x: key is guaranteed to be a string
        :return: nothing
        """
        if key !='' and key != None:
            index = self.hash_function(key)
            if self.table[index].find(key):
                self.table[index].find(key).value = value
            else:
                self.table[index].append(key, value)
                self.numItems += 1
            if self.numItems > 0.75 * self.tableSize:
                self.double()


    def find(self, key):
        """
        :param x: Returns HashListNode in table with specific key
        :return: key is found true, otherwise False.
        """
        for linkedlist in self.table:
            if linkedlist.find(key):
                return linkedlist.find(key)
        return False


    def lookup(self, key):
        """
        :param x: Returns the value of the Node in the table with specific key.
        :return: key is found true, otherwise False.
        """
        for linkedlist in self.table:
            if linkedlist.find(key):
                return linkedlist.find(key).value
        return False


    def delete(self, key):
        """
        :param x: Deletes the HashListNode with specific key from hash table
        :return: nothing
        """
        for linkedlist in self.table:
            if linkedlist.find(key):
                linkedlist.remove(key)
                self.numItems -= 1

    def double(self):
        """
        :param x: Doubles the size of hash table, rehashes values. 
        :return: nothing
        """
        for i in range(self.tableSize):
            self.table.append(LinkedList())
        self.tableSize *= 2
        self.rehash()
        
    def rehash(self):
        """
        :param x: Rehashes all keys of hash table. 
        :return: nothing
        """
        for linkedlist in self.table:
            if linkedlist.head != None:
                k = 1
                temp = linkedlist.head
                while temp != None:
                    k += 1 
                    temp = temp.next 

                temp = linkedlist.head
                self.delete(linkedlist.head.key)
                self.insert(temp.key, temp.value)
                temp = temp.next 
                i = 1
                while temp != None and  i <= k:
                    i += 1
                    temp1 = temp 
                    self.delete(temp.key)
                    self.insert(temp1.key, temp1.value)
                    temp = temp1.next 


def FindWords(phrase, k):
    """
    Parses through a string (phrase), utilizing HashTable class in order to find
    substrings of the phrase that appear exactly k times, case insensitive
        :param x: substrings in set should be cast as lowercase before being appended, order does 
        not matter. Each substring should be of length greater than 1.
        :return: a lowercase set of all substrings that appear k times.
        """
    hash_table = HashTable()
    n = len(phrase)
    for i in range(2, n):
        for j in range(n - i + 1):
            if hash_table.find(phrase[j: j + i]):
                temp = hash_table.find(phrase[j: j + i])
                hash_table.insert(phrase[j: j + i], temp.value + 1)
            else:
                hash_table.insert(phrase[j: j + i], 1)
    
    result = set()

    for linkedlist in hash_table.table:
        temp = linkedlist.head
        if temp != None:
            if temp.value == k:
                result.add(temp.key)
            
            if temp.next != None:
                temp = temp.next
                while temp is not None:
                    if temp.value == k:
                        result.add(temp.key)
                    temp = temp.next
    return(result)
            
