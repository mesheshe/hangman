# Course: CS261 - Data Structures
# Student Name: Elias Meshesha
# Assignment: 2
# Description: Implements a queue ADT. A queue ADT is defined through the use
#              of the following two methods: enqueue and dequeue. It will use 
#              dynamic array as the underlying storage container.

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da[i]) for i in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        This method adds the given value to the end of the queue, and it utilizes 
        the append function of dynamic array, which has the best case of constant 
        time and the worst case of O(N) when resizing is required. If we amortize
        the resize cost we see that over the lifetime of the array, it does amortized
        O(1) work. 
        """
        self.da.append(value)

    def dequeue(self) -> object:
        """
        This method removes and returns the value at the front of the queue. It 
        utilizes the dynamic array remove_at_index to remove the index at the 
        start of the array, which means filling up the hole we created at the 
        start of the array, and that takes O(N) work at all times, since the 
        hole will traverse through the entire list. 
        """
        if self.is_empty():
            raise QueueException
        value = self.da.get_at_index(0)
        self.da.remove_at_index(0)
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)


    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
