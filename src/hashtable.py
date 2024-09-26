# if collision, print a warning
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return self._hash_djb2(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        #because it's prime and has less opportunity for collision, set of magic numbers that work well for hash functions 
        hash = 5381
        #for every piece of our input parameter
        for x in key:
            # shifting bits, fill in gaps with zeros 
            # ord takes a parameter that's a character, and returns the integer value of the character (turn a string into a numeric value)
            hash = (( hash << 5 ) + hash) + ord(x)
        
        return hash & 0xFFFFFFFF

        #usage ("here is a string", self.capacity)



    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        #mod gives an integer between zero and the max size of the hash table
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # index = hash(key, self.capacity)
        # pair = LinkedPair(key, value)
        # #if bucket is not empty
        # if self.storage[index] is not None:
        #     # and if the key is something different, do you want to overwrite it
        #     if self.storage[index].key != key:
        #         # print warning
        #         print(f"There is already something written at this index: {self.storage[index]} - It is {value}")
        # #add pair to hash table
        # self.storage[index] = pair
        # is count larger than max capaxity?
        if self.count >= self.capacity:
            #if so, resize
            self.resize()
        #returns the integar index within the storage capacity (max) of the hashtable
        index = self._hash_mod(key)
        #if there is something in storage in that index, set the old value to the new value
        if self.storage[index] is not None:
            print("warning: index collision")
            self.storage[index].value = value

        self.storage[index] = LinkedPair(key, value)
        self.count += 1
        print("count", self.count)
        
        



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # get index via mod
        # overwrite old space as None, reduce count
        self.count -= 1
        # return index
        index = self._hash_mod(key)
        if self.storage[index]:
            self.storage[index] = None
        else:
            print(f"{key} does not exist in this table")
           


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #get index via mod
        # if self.storage[index] == None, nothing to retrieve
        # else if self.storage[index] ! empty
            # iterate through the linked list until key is found
            # if key is never found, return None
        index = self._hash_mod(key)
        pair = self.storage[index]
        if pair is None:
            return None
        else:
            return self.storage[index].value
        
            


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        
        if self.count < self.capacity:
            return
        
        # double capacity, assign new emprt storage "array" because log(n)
        self.capacity *= 2
        new_storage = [None] * self.capacity
        # reset count to zero
        self.count = 0
        #iterate through each item in storage
        for pair in self.storage:
            if pair is not None:
                #if there's a pair, add it to the new index
                new_index = self._hash_mod(pair.key)
                #and stick it in the new storage array
                new_storage[new_index] = pair
        # iterate through storage
        # for i in range(len(self.storage)):
        #     # for each index
        #     if self.storage[i]:
        #         hashedKey = self._hash_mod(self.storage[i].key)
        #         new_storage[hashedKey] = self.storage[i]
        # for pair in self.storage:
        #     if pair is not None:
        #         new_index = self._hash_mod(pair.key)
        #         new_storage[new_index] = pair
        #     else:
        #         continue
        self.storage = new_storage
        print("double size", self.capacity)



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    ht.insert("line_4", "booyea!")
    ht.insert("line_5", "boono!")
    ht.insert("line_6", "sdfsdfgdfgf")
    ht.insert("line_7", "eryeryeryerye")
    ht.insert("line_8", "bmvbbmbmvmvmvmv")
    ht.insert("line_9", "weqwqweqweqweqweq")
    ht.insert("line_10", "mlklkmlkmlkmlkmlklkm")
    ht.insert("line_11", "ygvygvygvygvygvyvygygvy")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.retrieve("line_4"))
    print(ht.retrieve("line_5"))
    print(ht.retrieve("line_6"))
    print(ht.retrieve("line_7"))
    print(ht.retrieve("line_8"))
    print(ht.retrieve("line_9"))
    print(ht.retrieve("line_10"))
    print(ht.retrieve("line_11"))

    # ht.remove("line_1")
    # ht.remove("line_2")
    # ht.remove("line_3")
    # ht.remove("line_7")
    # ht.remove("line_8")
    # ht.remove("line_9")
    # ht.remove("waffles")

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.retrieve("line_4"))
    print(ht.retrieve("line_5"))
    print(ht.retrieve("line_6"))


    print("")
