class QueueImp:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * QueueImp.DEFAULT_CAPACITY
        self.size = 0
        self.front_index = 0

    def push(self, ele):
        if len(self.data) == self.size:
            self.resize(2 * QueueImp.DEFAULT_CAPACITY)
        avail = (self.front_index + self.size) % self.DEFAULT_CAPACITY
        self.data[avail] = ele
        self.size += 1
        return True

    def resize(self, capacity):
        old_data = self.data
        self.data = [None] * capacity
        walk = self.front_index
        for k in range(self.size):
            self.data[k] = old_data[walk]
            walk = (1+walk) % QueueImp.DEFAULT_CAPACITY
        QueueImp.DEFAULT_CAPACITY = capacity
        self.front_index = 0

    def pop(self):
        pop_ele = self.data[self.front_index]
        self.data[self.front_index] = None
        # shift the front index of element
        self.front_index = (1 + self.front_index) % 10


        self.size -= 1
        return pop_ele

if __name__ == "__main__":
    QueueImp_obj = QueueImp()
    for i in [10, 20, 30, 40, 50, 60, 70]:
        QueueImp_obj.push(i)

    # for k in range(3):
    #     QueueImp.pop()

    for k in range(55, 57):
        QueueImp_obj.push(k)

    for k in range(2):
        QueueImp_obj.pop()

    for k in range(100, 105):
        QueueImp_obj.push(k)
    print("hello world-----")

