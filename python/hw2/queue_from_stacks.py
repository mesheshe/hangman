# Course: CS261 - Data Structures
# Student Name: Elias Meshesha 
# Assignment: 2
# Description: This program unlike queue_da uses max_stack_da as the underlying storage 
#              container, while queue_da utilizes dynamic array. This is most realistic
#              as queues basiclly behave as stacks except now you can only add from one 
#              side and remove from the other side.

from max_stack_da import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def is_empty(self) -> bool:
        """
        Return True if queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.size()

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        This method adds to the queue by utilizing the max_stack's push method 
        which does amoritized O(1) work. 
        """
        
        self.s1.push(value)

    def dequeue(self) -> object:
        """
        This method removes and returns the value at the front of the queue. There is
        an assumption made and that is pushing and popping using Max_stack takes constant 
        time. Therefore, when we are calling push and pop inside the for loop, we can say 
        that overall we are doing O(N) work for that loop. Since we are doing the loop 
        twice for the method, this method would have an overall complexity of O(2N) which 
        decomposes to O(N).
        """
        if self.is_empty():
            raise QueueException
        for n in range(self.size() - 1):
            self.s2.push(self.s1.pop())
        value = self.s1.pop()
        for n in range(self.s2.size()):
            self.s1.push(self.s2.pop())
        return value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# enqueue example 1')
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)


    print('\n# dequeue example 1')
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue(), q)
        except Exception as e:
            print("No elements in queue", type(e))
