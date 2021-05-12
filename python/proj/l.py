import numpy as np

class Dynamic_Array:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0
        self._start = 0

    def __str__(self):
        retStr = "["
        for i in range(self._size):
          retStr += str(self._list[(self._start + i) % self._capacity])
          if i < self._size - 1:
            retStr += " "
        retStr += "]"
        return retStr   

    def _upsize(self):
      # This should double the capacity of the numpy array and copy over the old array, but is incomplete
        new_data = np.empty([self._capacity * 2], np.int16)
        for i in range(self._size):
          new_data[i] = self._list[i]
        self._capacity *= 2
        self._list = new_data

    def append(self, val):
        # Needs to check if there is room and call _upsize if there isn't
        if self._capacity == self._size:
          self._upsize()
        self._list[self._size] =  val
        self._size = self._size + 1

    def _resize(self, size):
      new_data = np.empty([size], np.int16)
      for i in range(self._size):
        j = (self._start + i) % self._capacity
        new_data[i] = self._list[j]
      self._capacity = size
      self._list = new_data
      self._start = 0  

    def add_back(self,val):
      if self._size == self._capacity:
        self._resize(self._size * 2)
      self._list[(self._start + self._size) % self._capacity] = val
      self._size += 1

    def remove_back(self):
      if self._size == 0:
        return
      if self._size < 1/4*self._capacity and self._capacity > 4:
        if self._size*2 > 4:
          self._resize(self._size*2)
        else:
          self._resize(4)
      self._size -= 1
      return self._list[(self._start + self._size) % self._capacity]

    def remove_front(self):
      if self._size < 1/4*self._capacity and self._capacity > 4:
        if self._size*2 > 4:
          self._resize(self._size*2)
        else:
          self._resize(4)
      self._start += 1
      self._size -= 1
      return self._list[(self._start - 1) % self._capacity]
    
    def add_front(self, val):
      if self._size == self._capacity:
        self._resize(self._size*2)
      i = (self._start - 1) % self._capacity  # self._start + self._capacity
      self._list[i] = val
      self._start = i
      self._size += 1

my_list = Dynamic_Array()
# To begin with this will throw an index out of bounds error until you properly handle the capacity
# doubling.
for i in range(17):
  if i % 2 == 0:
    my_list.add_front(i)
  else:
    my_list.add_back(i)
print(my_list)
for i in range(15):
  if i % 2 == 0:
    my_list.remove_front()
  else:
    my_list.remove_back() 
  print(my_list)
print(my_list)