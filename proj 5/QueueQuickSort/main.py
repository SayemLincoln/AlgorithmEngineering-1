#!/usr/bin/python3
from QuickSort import quick_sort
from Queue import  LinkedQueue


def AddValues(queue, fp):
    '''
    :param queue: queue to add values to
    :param fp: file pointer to read from
    :return:  None
    '''
    for num in fp:
        queue.enqueue( float(num))



if __name__ == '__main__':
    fp = open(input("Please Enter File Name: "), "r")
    queue = LinkedQueue()

    AddValues(queue, fp)
    fp.close()

    quick_sort(queue)
    print(queue)
