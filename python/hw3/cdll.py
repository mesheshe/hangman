# Course: CS261 - Data Structures
# Student Name: Elias Meshesha
# Assignment: 3
# Description: This assignment provides practice with doubly linked list


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
                out = out + ' <-> ' + str(cur.value)
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

    def add_front(self, value: object) -> None:
        """
        One of Deque's characteristics is ability to add to the front of the 
        list and this function does so. It performs the task in O(1) time
        """
        node = DLNode(value)
        self.sentinel.next.prev = node
        node.next = self.sentinel.next
        node.prev = self.sentinel
        self.sentinel.next = node

    def add_back(self, value: object) -> None:
        """
        One of Deque's characteristics is ability to add to the back of the 
        list and this function does so. It performs the task in O(1) time
        """
        node = DLNode(value)
        node.prev = self.sentinel.prev
        self.sentinel.prev.next = node
        self.sentinel.prev = node
        node.next = self.sentinel

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This is a bag implementation. If insert index is valid, inserts the index. 
        Runtime is O(N)
        """
        length = self.length()
        if (index < 0) or ((length < index) and (self.is_empty() is False and index != 1)):
            raise CDLLException

        node = DLNode(value)
        curr = self.sentinel
        if (index > length//2):   # if it is in the later half 
            for num in range (length, index, -1): # Will take curr position since curr will
                curr = curr.prev                  #  be the node at index
        else:
            for num in range(index + 1): #will stop at index 
                curr = curr.next
        node.next = curr
        node.prev = curr.prev
        node.next.prev = node
        node.prev.next = node

    def remove_front(self) -> None:
        """
        This is a deque implementation. If the list is not empty, then it the front 
        sentinel points to the current head.next. Runtime is O(1) 
        """
        if self.is_empty():
            raise CDLLException
        
        self.sentinel.next = self.sentinel.next.next # formed a triangle 
        self.sentinel.next.prev = self.sentinel # the triangle with only a single line is now cut off

    def remove_back(self) -> None:
        """
        This is a deque implementaion. It will remove the last node from the back.
        This is a O(1) operation. 
        """
        if self.is_empty():
            raise CDLLException

        self.sentinel.prev = self.sentinel.prev.prev  # imagine a triangle 
        self.sentinel.prev.next = self.sentinel

    def remove_at_index(self, index: int) -> None:
        """
        This is a bag implementation. If the index is valid, it removes the node at  
        the index specified. This is a O(N) operation
        curr starts at self.sentinel and behaves differently for index > length/2
        for that case, the loop at least is performed once, but for the else there are 
        cases where the loop won't perform for index = 0, and so curr will equal self.sentinel
        """
        length = self.length()
        if index < 0 or index >= length or self.is_empty():
            raise CDLLException
        
        curr = self.sentinel
        if (index > length/2):   # if it is in the later half 
            for num in range (length, index, -1): # will stop at index we want to remove
                curr = curr.prev
            curr.next.prev = curr.prev     # curr loses the right element pointing to it
            curr.prev.next = curr.next     # curr loses the left element pointing to it. 
        else:                              # now curr has nothing pointing to it and is trashed
            for num in range(index): #will stop one short of index
                curr = curr.next
            curr.next = curr.next.next #skips over the right element
            curr.next.prev = curr      #now the right element is gone

    def get_front(self) -> object:
        """
        This is a deque implemention. It gets the value at the first node if the list is 
        not empty. This is a O(1) operation 
        """
        if self.is_empty():
            raise CDLLException
        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        This is a deque implemention. It gets the value at the last node if the list is 
        not empty. This is a O(1) operation 
        """
        if self.is_empty():
            raise CDLLException
        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        This is a bag implementation. This takes in a value and the first instance
        of it that is found is removed. If removed, it returns True else returns False.
        This is a O(N) operation.
        """
        # i don't need to check for is_empty because I already am below
        curr = self.sentinel.next
        while (curr != self.sentinel and curr.value != value):    
            curr = curr.next 
        if curr == self.sentinel:
            return False
        curr.prev.next = curr.next    # Removing curr 
        curr.next.prev = curr.prev
        curr.next = curr.prev = None
        return True

    def count(self, value: object) -> int:
        """
        This is a bag implementation. This takes in a value and returns the number of 
        times that value is observed in the list. This is a O(N) operation. 
        """
        count = 0
        goForward = self.sentinel.next
        goBackward = self.sentinel.prev
        while (goForward != goBackward and goForward.next != goBackward): # odd and even stop conditions
            if goForward.value == value:
                count+= 1
            if goBackward.value == value:
                count += 1
            goForward = goForward.next
            goBackward = goBackward.prev
        # goForward and goBackward could be self.sentinel but 
        # sentinel have value of None so the following test should still 
        # work
        if goForward == goBackward:  # checking the value at stop condition for odd number of length
            if goBackward.value == value:
                count += 1
        else:                        # checking the value at the stop condition for even length
            if goBackward.value == value:  
                count += 1
            if goForward.value == value:   
                count += 1
        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        Swap the nodes at the given indexes. This takes O(N)
        """
        length = self.length()
        if index1 < 0 or index2 < 0 or index1 >= length or index2 >= length or self.is_empty():
            raise CDLLException
        if index1 == index2:
            return
        curr = self.sentinel
        if index1 > length//2:
            for num in range(length, index1, -1):
                curr = curr.prev
        else:
            curr = curr.next    # if we didn't have this, the node it will stop at is just before index
            for num in range(index1):
                curr = curr.next
        curr2 = self.sentinel
        if index2 > length/2:
            for num in range(length, index2, -1):
                curr2 = curr2.prev
        else:
            curr2 = curr2.next          # if we didn't have this, the node it will stop at is just before index
            for num in range(index2):
                curr2 = curr2.next
        # The following code assumes curr and curr2 are the nodes at the indices of interest   
        if curr2.next != curr:  # guarantees no self loops 
            curr2.next.prev = curr   # next four lines reset the link going to our nodes
        if curr2.prev != curr:     
            curr2.prev.next = curr
        if curr.next != curr2:
            curr.next.prev = curr2
        if curr.prev != curr2:
            curr.prev.next = curr2
        if curr.next != curr2 and curr2.next != curr:
            temp = curr.next          # next six lines reset the link going from our node to the other links in the list     
            temp2 = curr.prev
            curr.next = curr2.next 
            curr.prev = curr2.prev
            curr2.next = temp
            curr2.prev = temp2
        else:
            if curr2.next == curr:
                # Work smarter not harder, I only wanted to do this once, so I 
                # picked my perspective to be the case were curr is an earlier node
                # and curr2 is later. So this if statement is insuring that is the case
                # This way I only have to worry about one situation 
                temp = curr
                curr = curr2
                curr2= temp
            # I drew the picture of the situation before this elif statment for the 
            # case where curr is a node that appears earlier in the list and curr2 
            # appears later. Can't code without the picture's help
            curr2.prev = curr.prev
            curr2.next.prev.next = curr2.next
            curr2.next = curr
            curr.prev = curr2
        
    def reverse(self) -> None:
        """
        Reverses a doubly linked list. This takes O(N) time 
        """
        length = self.length()
        if self.is_empty() or length == 1:
            return
        curr = self.sentinel.next    
        curr2 = self.sentinel.prev
        for num in range(length//2):
            preserveForward = curr.next
            preserveBackward = curr2.prev
            if curr2.next != curr:  # guarantees no self loops 
                curr2.next.prev = curr   # next four lines reset the link going to our nodes
            if curr2.prev != curr:     
                curr2.prev.next = curr
            if curr.next != curr2:
                curr.next.prev = curr2
            if curr.prev != curr2:
                curr.prev.next = curr2
            if curr.next != curr2 and curr2.next != curr:
                temp = curr.next          # next six lines reset the link going from our node to the other links in the list     
                temp2 = curr.prev
                curr.next = curr2.next 
                curr.prev = curr2.prev
                curr2.next = temp
                curr2.prev = temp2
            else: #curr2  curr node       
                curr2.prev = curr.prev
                curr2.next.prev.next = curr2.next #curr.next = curr2.next  (in other words) 
                curr2.next = curr
                curr.prev = curr2
            curr = preserveForward
            curr2 = preserveBackward

    def sort(self) -> None:
        """
        Sorts the doubly linked list using insertion 
        """
        length = self.length() # self.length() only needs to run once
        if self.is_empty() or length == 1:
            return 
        curr = self.sentinel.next.next
        while curr != self.sentinel:
            preserveNext  = curr.next
            value = curr.value
            pos = curr.prev
            while pos != self.sentinel and pos.value > value:
                pos = pos.prev
            if pos.next.value > value:  # don't want to do work if we don't have to 
                # detached curr from original pos 
                preserveNext.prev.prev.next = preserveNext
                preserveNext.prev = preserveNext.prev.prev
                # pos represents the node with pos.value <= curr.value
                curr.next = pos.next
                pos.next.prev = curr
                curr.prev = pos
                pos.next = curr
            curr = preserveNext

    def rotate(self, steps: int) -> None:
        """
        Rotates the doubly linked list. This is O(N) operation. 
        """
        length = self.length()
        if self.is_empty() or length == 1:
            return
        is_Negative = False
        if steps < 0:
            is_Negative = True
            steps *= -1
        rotateBy = steps % length  # Further optimization could be figuring out if it  
        for num in range(rotateBy): # cheaper to rotate left or right then do so, but...
            if not is_Negative:    # if positive focus on right side of self.sentinel 
                self.sentinel.next.prev = self.sentinel.prev
                self.sentinel.prev.next = self.sentinel.next
                self.sentinel.next = self.sentinel.prev
                self.sentinel.prev.prev.next = self.sentinel
                self.sentinel.prev  = self.sentinel.prev.prev
                self.sentinel.next.prev = self.sentinel
            else:                  # picture was drawn to come up with this
                self.sentinel.prev.next = self.sentinel.next
                self.sentinel.next.prev = self.sentinel.prev
                self.sentinel.prev = self.sentinel.next
                self.sentinel.next = self.sentinel.next.next
                self.sentinel.next.prev = self.sentinel
                self.sentinel.prev.next = self.sentinel          
                
    def remove_duplicates(self) -> None:
        """
        Removes all duplicates from a list
        """
        length = self.length()
        if self.is_empty() or length == 1:
            return
        curr = self.sentinel.next  # This is a do while loop
        val = curr.value           # since we are guaranteed at least 2
        start_node = curr          # this won't break
        curr = curr.next
        while curr != self.sentinel:
            preserveNext = curr.next
            if curr.value != val and start_node == curr.prev:
                val = curr.value
                start_node = curr
            elif curr.value != val and start_node != curr.prev:
                # I initially solved this probem thinking we were returning 
                # a list with no duplicates, which means to remove all duplicates 
                # of a number. So I included the start_node. So to remove everything 
                # that has duplicates, we move start_node back by one node
                start_node = start_node.prev
                start_node.next.prev = None
                curr.prev.next = None
                start_node.next = curr
                curr.prev = start_node
                val = curr.value
                start_node = curr 
            curr = preserveNext
        # checking to make sure the last node is not a duplicate 
        if start_node != curr.prev:
            start_node = start_node.prev
            start_node.next.prev = None
            curr.prev.next = None
            start_node.next = curr
            curr.prev = start_node

    def odd_even(self) -> None:
        """
        This method regroups list nodes by first grouping all ODD nodes together followed by all
        EVEN nodes.
        """
        length = self.length()
        if self.is_empty() or length <= 2:
            return
        odd = None
        even = None
        evenHead = None # why no oddHead, cause oddHead = self.sentinel 
        num = 1
        curr = self.sentinel.next
        while num == 1 or curr != self.sentinel:
            preserveNext = curr.next
            curr.prev = None
            if num % 2 == 1:
                if odd is None:
                    odd = curr
                    odd.prev = self.sentinel  # it was deattached at the start
                else:
                    odd.next = curr
                    odd.next.prev = odd
                    odd = odd.next
            else:
                if evenHead is None:
                    evenHead = curr
                    even = curr
                    even.next = None
                else:
                    even.next = curr
                    even.next.prev = even
                    even = even.next
            num += 1
            curr = preserveNext
        
        even.next = curr
        even.next.prev = even
        odd.next = evenHead
        odd.next.prev = odd

    def add_integer(self, num: int) -> None:
        """
        This function adds the num passed to it, to the list of nodes with each node holding a digit. 
        Runtime is O(N) + O(log K). The complexity is O(log k), cause the number is divided by 10
        every iteration and the iteration keeps going so long the number is not equal to 0. 
        """
        carry = 0
        curr = self.sentinel.prev
        while curr != self.sentinel and (num != 0 or carry != 0):
            digit = num % 10
            num = num//10 
            carryDigit = carry % 10
            carry = carry//10
            summation = digit + curr.value + carryDigit
            if summation < 10:
               curr.value = summation 
            else:
                sumDigit = summation % 10
                curr.value = sumDigit
                carry += (summation//10)
            curr = curr.prev

        while num != 0 or carry != 0:
            # In here the second number is 0 so we are only adding the value
            # passed in and the carry from the previous while loop 
            digit = num % 10
            num = num//10 
            carryDigit = carry % 10
            carry = carry//10
            summation = digit + carryDigit
            if summation < 10:
               self.add_front(summation) 
            else:
                sumDigit = summation % 10
                node = DLNode(sumDigit)
                node.next = self.sentinel.next
                node.next.prev = node
                node.prev = self.sentinel
                self.sentinel.next = node  
                carry += (summation//10)

if __name__ == '__main__':

    print('\n# add_front example 1')
    lst = CircularList()
    print(lst)
    lst.add_front('A')
    lst.add_front('B')
    lst.add_front('C')
    print(lst)
    #
    print('\n# add_back example 1')
    lst = CircularList()
    print(lst)
    lst.add_back('C')
    lst.add_back('B')
    lst.add_back('A')
    print(lst)
    #
    print('\n# insert_at_index example 1')
    lst = CircularList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F'), (4,'E')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))
    """
    #
    print('\n# remove_front example 1')
    lst = CircularList([1, 2])
    print(lst)
    for i in range(3):
        try:
            lst.remove_front()
            print('Successful removal', lst)
        except Exception as e:
            print(type(e))
    
    print('\n# remove_back example 1')
    lst = CircularList()
    try:
        lst.remove_back()
    except Exception as e:
        print(type(e))
    lst.add_front('Z')
    lst.remove_back()
    print(lst)
    lst.add_front('Y')
    lst.add_back('Z')
    lst.add_front('X')
    print(lst)
    lst.remove_back()
    print(lst)
    
    print('\n# remove_at_index example 1')
    lst = CircularList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)
    #
    print('\n# get_front example 1')
    lst = CircularList(['A', 'B'])
    print(lst.get_front())
    print(lst.get_front())
    lst.remove_front()
    print(lst.get_front())
    lst.remove_back()
    try:
        print(lst.get_front())
    except Exception as e:
        print(type(e))
    #
    print('\n# get_back example 1')
    lst = CircularList([1, 2, 3])
    lst.add_back(4)
    print(lst.get_back())
    lst.remove_back()
    print(lst)
    print(lst.get_back())
    #
    print('\n# remove example 1')
    lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)
    #
    print('\n# count example 1')
    lst = CircularList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    #
    print('\n# swap_pairs example 1')
    lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
                  (4, 2), (3, 3), (1, 2), (2, 1))
    #
    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            lst.swap_pairs(i, j)
            print(lst)
        except Exception as e:
            print(type(e))
    
    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        lst = CircularList(case)
        lst.reverse()
        print(lst)
    #
    print('\n# reverse example 2')
    lst = CircularList()
    print(lst)
    lst.reverse()
    print(lst)
    lst.add_back(2)
    lst.add_back(3)
    lst.add_front(1)
    lst.reverse()
    print(lst)
    #
    print('\n# reverse example 3')
    
    
    class Student:
        def __init__(self, name, age):
            self.name, self.age = name, age
    
        def __eq__(self, other):
            return self.age == other.age
    
        def __str__(self):
            return str(self.name) + ' ' + str(self.age)
    
    
    s1, s2 = Student('John', 20), Student('Andy', 20)
    lst = CircularList([s1, s2])
    print(lst)
    lst.reverse()
    print(lst)
    print(s1 == s2)
    
    print('\n# reverse example 4')
    lst = CircularList([1, 'A'])
    lst.reverse()
    print(lst)
    #
    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        lst = CircularList(case)
        print(lst)
        lst.sort()
        print(lst)
    #
    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        lst = CircularList(source)
        lst.rotate(steps)
        print(lst, steps)
    #
    print('\n# rotate example 2')
    lst = CircularList([10, 20, 30, 40])
    for j in range(-1, 2, 2):
        for _ in range(3):
            lst.rotate(j)
            print(lst)
    #
    print('\n# rotate example 3')
    lst = CircularList()
    lst.rotate(10)
    print(lst)
    #
    print('\n# remove_duplicates example 1')
    test_cases = (
        [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
        [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
        [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
        list("abccd"),
        list("005BCDDEEFI")
    )
    #
    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)
    
    print('\n# odd_even example 1')
    test_cases = (
        [1, 2, 3, 4, 5], list('ABCDE'),
        [], [100], [100, 200], [100, 200, 300],
        [100, 200, 300, 400],
        [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    )
    #
    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.odd_even()
        print('OUTPUT:', lst)
    
    print('\n# add_integer example 1')
    test_cases = (
      ([1, 2, 3], 10456),
      ([], 25),
      ([2, 0, 9, 0, 7], 108),
      ([9, 9, 9], 9_999_999)
    )
    for list_content, integer in test_cases:
        lst = CircularList(list_content)
        print('INPUT :', lst, 'INTEGER', integer)
        lst.add_integer(integer)
        print('OUTPUT:', lst)
    """