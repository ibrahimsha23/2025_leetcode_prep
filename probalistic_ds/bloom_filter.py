# from hash.hash import *

from bitarray import bitarray

class BloomFilter:
    """
    Bloom filter :
    1. hashing
    2. add
    3. exists
    4. stats: size, load factor, false positive error rate
    5. resize
    6.
    """

    def __init__(self, capacity):
        self.bit_array = bitarray(capacity)
        self.bit_array.setall(0)
        self.capacity = capacity

    def resize(self):
        pass

    def hashing(self, item):
        return hash(item) % self.capacity

    def add(self, item):
        hashed_index = self.hashing(item)
        print(f"Hashed index - {item}", hashed_index)
        self.bit_array[hashed_index] = 1

    def exists(self, item):
        hashed_index = self.hashing(item)
        print(f"========Hashed index - {item}", hashed_index)
        if self.bit_array[hashed_index]:
            return True
        return False

    def stats(self):
        pass


bloom = BloomFilter(100)
bloom.add("apple")
bloom.add("banana")
bloom.add("cherry")

print(bloom.exists("apple"))
print(bloom.exists("grape"))

print(bloom.bit_array)
