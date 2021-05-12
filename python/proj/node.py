class CDLLException(Exception):
    
    """
    
    Custom exception class to be used by Circular Doubly Linked List
    
    DO NOT CHANGE THIS CLASS IN ANY WAY
    
    """
    
    pass


class DLNode:
    
    """
    
    Doubly Linked List Node class
    
    DO NOT CHANGE THIS CLASS IN ANY WAY
    
    """


    def __init__(self, value: object) -> None:
    
        self.next = None
    
        self.prev = None
    
        self.value = value


class CircularList:
    
    def __init__(self, start_list=None):
    
        """
    
        Initializes a new linked list with sentinel
    
        DO NOT CHANGE THIS METHOD IN ANY WAY
    
        """
    
        self.sentinel = DLNode(None)
    
        self.sentinel.next = self.sentinel
    
        self.sentinel.prev = self.sentinel


        # populate CDLL with initial values (if provided)
    
        # before using this feature, implement add_back() method
    
        if start_list is not None:
    
            for value in start_list:
    
                self.add_back(value)


    def __str__(self) -> str:
    
        """
    
        Return content of singly linked list in human-readable form
    
        DO NOT CHANGE THIS METHOD IN ANY WAY
    
        """
    
        out = 'CDLL ['
    
        if self.sentinel.next != self.sentinel:
    
            cur = self.sentinel.next.next
    
            out = out + str(self.sentinel.next.value)
    
            while cur != self.sentinel:
    
                out = out + '  ' + str(cur.value)
    
                cur = cur.next
    
        out = out + ']'
    
        return out


    def length(self) -> int:
    
        """
    
        Return the length of the linked list


        This can also be used as troubleshooting method. This method works
    
        by independently measuring length during forward and backward
    
        traverse of the list and return the length if results agree or error
    
        code of -1 or -2 if thr measurements are different.


        Return values:
    
        >= 0 - length of the list
    
        -1 - list likely has an infinite loop (forward or backward)
    
        -2 - list has some other kind of problem


        DO NOT CHANGE THIS METHOD IN ANY WAY
    
        """


        # length of the list measured traversing forward
    
        count_forward = 0
    
        cur = self.sentinel.next
    
        while cur != self.sentinel and count_forward < 101_000:
    
            count_forward += 1
    
            cur = cur.next


        # length of the list measured traversing backwards
    
        count_backward = 0
    
        cur = self.sentinel.prev
    
        while cur != self.sentinel and count_backward < 101_000:
    
            count_backward += 1
    
            cur = cur.prev


        # if any of the result is > 100,000 -> list has a loop
    
        if count_forward > 100_000 or count_backward > 100_000:
    
            return -1


        # if counters have different values -> there is some other problem
    
        return count_forward if count_forward == count_backward else -2


    def is_empty(self) -> bool:
    
        """
    
        Return True is list is empty, False otherwise
    
        DO NOT CHANGE THIS METHOD IN ANY WAY
    
        """
    
        return self.sentinel.next == self.sentinel


    # ------------------------------------------------------------------ #
    
    def add_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        node = DLNode(value)
        node.prev = self.sentinel.prev
        self.sentinel.prev.next = node
        node.next = self.sentinel
        self.sentinel.prev = node

    def remove_at_index(self, index: int) -> None :
    
        """
    
        TODO: Write this implementation
    
        """
        length = self.length()
        if index < 0 or index >= length or self.is_empty():
          raise CDLLException

        curr = self.sentinel
        if index <= length // 2:
          curr = curr.next
          for i in range(index):
              curr = curr.next
        else:
          curr = curr.prev
          for i in range(length - 1, index, -1):
            curr = curr.prev
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.next = None
        curr.prev = None
        curr = None
        return


my = CircularList([1,2,3,6,7,8,4])
print(my)
my.remove_at_index(4)
print(my)