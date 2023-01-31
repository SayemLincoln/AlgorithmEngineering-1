# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 19:57:57 2018

@author: srlin
"""
from CircularQueue import *

queue = CircularQueue()
queue.enqueue(23)
queue.enqueue(42)
queue.enqueue(2)
queue.enqueue(195)
queue.enqueue(23)
queue.enqueue(42)
queue.enqueue(2)
queue.enqueue(195)

print(queue)

for i in range(6):
    queue.dequeue()
    

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(queue)