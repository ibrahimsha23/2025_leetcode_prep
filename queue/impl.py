class QUEUE:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self.__data = [None] * self.DEFAULT_CAPACITY
        self.size = 0
        self.front_index = 0
    def push(self, ele):
        if len(self.__data) == self.size:
            raise Empt


