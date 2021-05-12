# Course: CS261 - Data Structures
# Student Name: Elias Meshesha 
# Assignment: 2
# Description: Utilizing StaticArray class that was written before as the underlying storage
#              container, this program will implement Array ADT via a dynamic array implementation.
#              That means that the array will double in capacity when size is full, as well as 
#              decrease by 1/2 of size when the size of array is 1/3 the capacity. The following
#              methods will be what defines a dynamic array: resize(), append(), insert_at_index(),
#              remove_at_index(), slice(), merge(), map(), filter(), reduce()

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        This method changes the capacity of the underlying storage for the
        array elements to new_capacity. It copies over the old data into the 
        new array, so as to preserve the values and their order
        """
        if new_capacity <= 0 or new_capacity < self.size:
            return
        new_data = StaticArray(new_capacity)
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
        return

    def append(self, value: object) -> None:
        """
        This method adds value to the end of the list (at self.size). If the list
        is already at full capacity before the addition, resize() is called. self.size
        gets increased by one at the end 
        """
        if self.size == self.capacity:
            self.resize(self.capacity*2)
        self.data[self.size] = value
        self.size += 1
        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Provided that index is valid, this method adds value to the Dynamic Array 
        at index. It does so first by making room for the addition by moving everything
        down by 1, then finally inserting it. self.size gets increased by one at the end
        """
        if index > self.size or index < 0:
            raise DynamicArrayException 
        if self.size == self.capacity:
            self.resize(self.capacity*2)
        if index == self.size:
            self.data[index] = value
            self.size +=  1
            return
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1
        return

    def remove_at_index(self, index: int) -> None:
        """
        Provided that the index is valid, this method first checks if a call to resize() 
        is necessary by first checking if the array size is currently below 1/3 of capacity.
        Once those checks are donne, this method removes the value at index from the 
        array, and it does so by moving everything to the right of the index over to the 
        to the left by one, then it decreases self.size.   
        """
        if index >= self.size or index < 0:
            raise DynamicArrayException 
        if self.size < 1/4*self.capacity and self.capacity > 10:
            if self.size*2 < 10:
                self.resize(10)
            else:
                self.resize(self.size*2)
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i+1]
        self.size-= 1
        return
        
    def slice(self, start_index: int, size: int) -> object:
        """
        Provided that the slice index is valid, this method returns a new dynamic array
        that holds the orginal array's value from start_index to start_index + size - 1  
        """
        end = start_index + size
        if size<0 or start_index<0 or start_index>=self.size or end<0 or end>self.size: 
            raise DynamicArrayException
        returnList = DynamicArray()
        returnList.size = 0
        returnList.capacity = 4 
        for i in range(start_index, end):
            returnList.append(self.data[i])
        return returnList

    def merge(self, second_da: object) -> None:
        """
        This method takes another Dynamic Array object as a parameter, and appends all 
        elements from this second array to the current one, in the same order as they 
        are stored in the second array.
        """
        for i in range(second_da.size):
            self.append(second_da.data[i])
        return

    def map(self, map_func) -> object:
        """
        This method creates a new array whose value is the original's value except each 
        value had the map_func done on it, before it got added to the new array. 
        """
        returnObj = DynamicArray()
        returnObj.size = 0
        returnObj.capacity = 4
        for i in range(self.size):
            returnObj.append(map_func(self.data[i]))
        return returnObj

    def filter(self, filter_func) -> object:
        """
        This method returns a new array where each value in the array came from the original
        array except before the value was added to the new array, the value had to pass the
        test specified by filter_func.
        """
        returnArray = DynamicArray()
        returnArray.size = 0
        returnArray.capacity = 4
        for i in range(self.size):
            if filter_func(self.data[i]):
                returnArray.append(self.data[i])
        return returnArray

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method sequentially applies the reduce_func to all elements of the Dynamic 
        Array and returns the resulting value. The method takes an optional initializer
        parameter. If this parameter is not provided, the first value in the array is 
        used as the initializer. If the Dynamic Array is empty, the method returns the 
        value of the initializer
        """
        if self.is_empty():
            return initializer
        elif self.size == 1 and initializer is None:
            return self.data[0]
        accum = 0 
        if initializer is None:
            for i in range(self.size - 1):
                if i == 0:
                    accum = reduce_func(self.data[i], self.data[i + 1])
                else:
                    accum = reduce_func(accum, self.data[i + 1])
        else: 
            for i in range(self.size):
                if i == 0:
                    accum = reduce_func(initializer, self.data[i])
                else:
                    accum = reduce_func(accum, self.data[i])
        return accum

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":
    
    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    
    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)
    

    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)

    
    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)
    

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)
    
    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)
    

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)
    

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)
    

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")
    

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")
    

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)
    

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))
    

    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))
    

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))


    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    