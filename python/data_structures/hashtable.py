
from re import I
from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Put docstring here
    """
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def set(self, key, value):
        '''
        Sets item into hashtable by first calculating hash, then if it doesn't have anything in it, then instantiate a linked list to hold valuse in case of possible collision. 
        '''
        idx = self.hash(key)
        bucket = self._buckets[idx]

        if not bucket:
            self._buckets[idx] = LinkedList()
 
        '''
        Checks to see if key exists and if does, updates that key, value pair
        '''
        current = self._buckets[idx].head

        while current:
            if current.value[0] == key:
                current.value = (key, value)
            current = current.next
                    
        self._buckets[idx].insert((key,value))

    def get(self, key):
        '''
        Retrieves a value based on key after calculating hash
        '''
        idx = self.hash(key)
        bucket = self._buckets[idx]

        if not bucket:
            raise KeyError("Key not found", key)

        current = bucket.head

        while current:
            if current.value[0] == key:
                return current.value[1]

            current = current.next
        raise KeyError("Nothing found with that key: ", key)

    def keys(self):
        keys = set()
        for bucket in self._buckets:
            try:
                if bucket:
                    container = bucket.head
                while bucket:
                    keys.add(container.value[0])
                    print(keys)
                    container = container.next
            finally: 
                continue
        return keys

    def contains(self, key):
        idx = self.hash(key)
        bucket = self._buckets[idx]

        if bucket is None:
            return False

        current = bucket.head

        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False

    def hash(self, key):
        '''
        Hash algorithim to convert character values
        '''
        sum = 0

        if type(key) == str:
            for char in key:
                sum += ord(char)
        if type(key) == int or type(key) == float:
            sum = key
        sum *= 599
        idx = sum % len(self._buckets)
        return idx
