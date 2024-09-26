# dynamic array
# Things we need for an advanced array
# size of it and protection from going past that
# size of objects
# to append need space
# track allocated and used
# if we run out of space, we need to make a new one with more space
# then copy each item over

class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * capacity
    def append(self, value):
        if self.count >= self.capacity:
            self.resize_array()
        self.storage[self.count] = value
        self.count += 1
        #add to the end
        
    def insert(self, value, index):
        if self.count >= self.capacity:
            self.resize_array()
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        self.storage[index] = value
        self.count += 1
        #add to somewhere
    def remove(self, index):
        value = self.storage[index]
        for i in range(index, self.count -1, 1):
            self.storage[i] = self.storage[i+1]
        self.count -= 1
        return value

    def print_array(self):
        for value in self.storage:
            print(value)
            
    def resize_array(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

        
    def add_to_front(self, value): 
        self.insert(value, 0)
    
        