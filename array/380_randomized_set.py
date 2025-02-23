import random

class RandomizedSet(object):

    def __init__(self, data):
        self.data = {}
        self.list = []


    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        val = val[0]
        if val in self.data:
            return False
        self.list.append(val)
        self.data[val] = len(self.list) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.data:
            return False
        del self.list[val]
        del self.data[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        keys = self.data.keys()
        return random.choice(list(keys))


# Your RandomizedSet object will be instantiated and called as such:


if __name__ == "__main__":
    operations_data = [
        "RandomizedSet", "insert", "remove", "insert",
        "getRandom", "remove", "insert", "getRandom"
    ]
    input_data = [[], [1], [2], [2], [], [1], [2], []]
    len_input = len(input_data)
    obj = RandomizedSet()
    for i in range(1, len_input):
        operation = operations_data[i]
        val = input_data[i]
        if operation == "insert":
            obj.insert(val)
        elif operation == "remove":
            obj.remove(val)
        elif operation == "getRandom":
            obj.getRandom(val)







