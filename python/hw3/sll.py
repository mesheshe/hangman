# Course: CS261 - Data Structures
# Student Name: Elias Meshesha 
# Assignment: 3
# Description: This assignemnt provides implements Bag ADT and Deque ADT with SLL data structure



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        One of Deque's characteristics is ability to add to the front of the 
        list and this function does so. It performs the task in O(1) time
        """
        node = SLNode(value)
        node.next = self.head.next
        self.head.next = node
        
    def get_the_node_before_tail(self, node):
        """
        Helper function that returns the node before self.tail 
        """
        if node.next == self.tail:
            return node
        return self.get_the_node_before_tail(node.next)

    def add_back(self, value: object) -> None:
        """
        One of Deque's characteristics is ability to add to the back of the 
        list and this function does so. It performs the task in O(N) time
        """
        # traverse the list to find last node
        node_before_sentinel = self.get_the_node_before_tail(self.head)
        node = SLNode(value)
        node.next = node_before_sentinel.next  # could have written self.tail
        node_before_sentinel.next = node  

    def return_node_before_index(self, node, index, pos = 0):
        """
        This helper function returns the node before the index given. 
        Originally without the existance of sentinels, the default case should 
        be if (pos == index - 1), but due to the sentinels being counted, we 
        are just looking at (pos == index) to get the node before index 
        """
        if (pos == index):  # pos is the position of the node before curr node at index. 
            return node     # due to the head sentinel being counted as well in pos 
        return self.return_node_before_index(node.next, index, pos+1)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This is a bag implementation. If insert index is valid, inserts the index. 
        Runtime is O(N)
        """
        if (index < 0) or ((self.length() < index) and (self.is_empty() is False and index != 1)):
            raise SLLException
        
        node = SLNode(value)
        node_before_index = self.return_node_before_index(self.head, index)
        node.next = node_before_index.next
        node_before_index.next = node

    def remove_front(self) -> None:
        """
        This is a deque implementation. If the list is not empty, then it the front 
        sentinel points to the current head.next. Runtime is O(1) 
        """
        if (self.is_empty()):
            raise SLLException
        self.head.next = self.head.next.next

    def get_the_node_before_before_tail(self, node):
        """
        Helper function that gets the node before the node before tail
        Smallest case that will be passed here is for a LL of length 1
        in that case self.head will be passed and calling next on it 
        will result in the first node, and calling next again will result 
        the self.tail node, and so this funciton will return head
        Therefore we can say that this will work for every case n >= 1. 
        Since we have proved it worked for 1. 
        """
        if node.next.next == self.tail:
            return node
        return self.get_the_node_before_before_tail(node.next)

    def remove_back(self) -> None:
        """
        This is a deque implementaion. It will remove the last node from the back.
        This is a O(N) operation. 
        """
        if (self.is_empty()):
            raise SLLException
        
        node = self.get_the_node_before_before_tail(self.head)
        node.next = node.next.next
  
    def remove_at_index(self, index: int) -> None:
        """
        This is a bag implementation. If the index is valid, it removes the node at  
        the index specified. This is a O(N) operation. 
        """
        if index >= self.length() or index < 0 or self.is_empty():
            raise SLLException
        
        node = self.return_node_before_index(self.head, index)
        node.next = node.next.next

    def get_front(self) -> object:
        """
        This is a deque implemention. It gets the value at the first node if the list is 
        not empty. This is a O(1) operation 
        """
        if self.is_empty():  # do we implement??
            raise SLLException
        return self.head.next.value

    def get_back(self) -> object:
        """
        This is a deque implemention. It gets the value at the last node if the list is 
        not empty. This is a O(N) operation 
        """
        if self.is_empty():
            raise SLLException
        return self.get_the_node_before_tail(self.head).value

    def remove_a_value(self, node,value, prevNode = None):
        """
        Helper function: if true, function returns the node before target, otherwise, 
        returns False
        """
        if node == self.tail:
            return False
        if node.value == value:
            return prevNode
        prevNode = node
        return self.remove_a_value(node.next, value, prevNode)

    def remove(self, value: object) -> bool:
        """
        This is a bag implementation. This takes in a value and the first instance
        of it that is found is removed. If removed, it returns True else returns False.
        This is a O(N) operation. 
        """
        node_or_bool = self.remove_a_value(self.head, value) 
        if (node_or_bool == False):
            return False
        node_or_bool.next = node_or_bool.next.next 
        return True

    def count_value(self, node, value,count = 0):
        """
        Helper functions that counts the number of times that value is observed as we 
        progress through the SLL. Returns the count after self.tail is reached.
        """
        if node == self.tail:
            return count
        if node.value == value:
            count += 1
        return self.count_value(node.next, value, count)

    def count(self, value: object) -> int:
        """
        This is a bag implementation. This takes in a value and returns the number of 
        times that value is observed in the list. This is a O(N) operation. 
        """
        return self.count_value(self.head, value)

    def get_the_slice(self, originalNode, size, newLL = None, newLLnode = None):
        """
        Helper function that takes in a starting node and a size and returns a new LL 
        that contains a slice specified by the size.
        """
        if size == 0:
            return newLL
        newNode = SLNode(originalNode.value)
        
        if newLL is None: 
            newLL = LinkedList()
            newNode.next = newLL.tail
            newLL.head.next = newNode
        else:
            newNode.next = newLL.tail
            newLLnode.next = newNode
        return self.get_the_slice(originalNode.next, size - 1, newLL, newNode)

    def slice(self, start_index: int, size: int) -> object:
        """
        This function takes a slice of the current list. It takes in a start index
        and a size. This is a O(N) operation. 
        """
        length = self.length()
        if start_index >= length or start_index + size > length or start_index < 0 or size < 0:
            raise SLLException
        if self.length() == 0:
            raise SLLException
        if size == 0:
            return LinkedList()
        node = self.return_node_before_index(self.head, start_index).next
        return self.get_the_slice(node, size)

if __name__ == '__main__':

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)
    
    
    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)
    
    
    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))
    
    
    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))
    
    
    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)
    
    
    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)
    
    
    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))
    
    
    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())
    #
    
    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)
    
    
    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))
    #
    #
    
    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")
    #
    #
    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

