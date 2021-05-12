# Course: CS261 - Data Structures
# Student Name: Elias Meshesha 
# Assignment: 2 
# Description: Implements a MaxStack ADT, which is like a normal stack but this
#              program also keeps track of the max value in the current stack. 
#              It will implement the following methods, which define it as a stack:
#              push(), pop(), peak(). It will utilize dynamic array as the base 
#              storage container.    

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()
        self.da_max = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.da_val.length()) + " elements. ["
        out += ', '.join([str(self.da_val[i]) for i in range(self.da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        This method adds the given value to the top of the stack, and since it 
        utilizes dynamic array's append() function, it takes amortized O(1). It
        also adds the value to a max stack if the value is larger than the value
        currently at the top of the max stack. 
        """
        if self.is_empty():
            self.da_max.append(value)
        elif value >= self.da_max.get_at_index(self.da_max.length() - 1):
                self.da_max.append(value)
        self.da_val.append(value)
        

    def pop(self) -> object:
        """
        Removes the value at the top of the stack and returns it. It uses remove_at_index()
        function of the dynamic array's method. Becaause resizing occurs for the remove 
        function only when the size of the array get's 1/3 of capacity, which means if we 
        spread the cost of resizing over the lifetime of the array, we can say that it does
        the job in amortized constant time. Also if the value we are popping off is equal 
        to the current top of our max stack, we also pop that value off that stack. 
        """
        if self.is_empty():
            raise StackException
        val = self.da_val.get_at_index(self.size() - 1)
        if val == self.da_max.get_at_index(self.da_max.length() - 1):
            self.da_max.remove_at_index(self.da_max.length() - 1)    
        self.da_val.remove_at_index(self.size() - 1)
        return val

    def top(self) -> object:
        """
        Returns the top value of our current stack. It is constant time since, it just needs
        to grab the memory address where our array starts and then add an offset to it, based
        on the (size of each element)*index, and then return the value at the memory location.  
        """
        if self.is_empty():
            raise StackException
        return self.da_val.get_at_index(self.size() - 1)

    def get_max(self) -> object:
        """
        Returns the current top of self.da_max. This behaves similarly to the top() function
        above and has similar time complexity.  
        """
        if self.is_empty():
            raise StackException
        return self.da_max.get_at_index(self.da_max.length() - 1)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)
    

    print("\n# pop example 1")
    s = MaxStack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))
    

    print("\n# top example 1")
    s = MaxStack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
    

    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
    