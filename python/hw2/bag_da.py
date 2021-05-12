# Course: CS261 - Data Structures
# Student Name: Elias Meshesha 
# Assignment: 2
# Description: The following program implements a Bag ADT. A bag ADT is characterized 
#              with the following methods add(), remove(), count(), clear(), and equal();
#              So a bag allows the user to add a value, as well as remove a value from it,
#              it is also possible to count how many instances of a value there exists, as 
#              well as compare the contents of two bags together. This program will use  
#              dynamic array as the underlying data storage.   

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Add a given value to the bag. Since this method adds to the end of the
        dynamic array list, which has the best case of constant time complexity 
        and the worst case of O(n). Of course, since resizing occurs so infrequently, 
        we can spread the cost over the entire lifetime of the array, and we find 
        that it has an amortized O(1) complexity. 
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        This method iterates through the bag and removes the value if found. Removing
        the array also entails filling in the whole, so the rest of the array has to
        be moved to the left by one which is O(N) work. This method will only remove
        1 value and return true. So in both cases, where we remove and we don't remove 
        a value, we are still doing O(N) work. Because if the value is not found, we would 
        have had to check every object inside the bag, which means we did O(N) work.    
        """
        for i in range(self.size()):
            if self.da.get_at_index(i) == value:
                self.da.remove_at_index(i)
                return True 
        return False 

    def count(self, value: object) -> int:
        """
        This method iterates through the bag and adds to count each time the 
        content of the bag matches the value specified. Returns the count in 
        the end. Iterating through a list is O(N) work, since every element 
        has to be visited. 
        """
        count = 0
        for i in range(self.size()):
            if self.da.get_at_index(i) == value:
                count += 1 
        return count

    def clear(self) -> None:
        """
        Clears the bag by assigning self.da to a new bag. This is constant time work since
        the program is simply allocating memory, creating the bag object and assigning to 
        self.da, a reference to that memory allocation. 
        """
        self.da = DynamicArray()

    def equal(self, second_bag: object) -> bool:
        """
        This method when called on a bag, compares the content of this.bag to the contents
        of a second bag. This method returns true if all content matches and false otherwise.
        This method does O(N**2) work by having a for loop that iterates through the content
        of this.bag, and for each content, count(content) is called on both bags and the 
        resulting counts are compared against each other. Since count is called twice, the 
        work done inside the function is 2N and the outerloop is N, and so an O(N**2) overall.         
        """
        if self.size() != second_bag.size():
            return False
        for i in range(self.size()):
            if self.count(self.da.get_at_index(i)) != second_bag.count(self.da.get_at_index(i)):
                return False
        return True

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)
    

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))
    

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)


    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
    