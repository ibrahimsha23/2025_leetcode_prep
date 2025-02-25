import heapq
# heap = []            # creates an empty heap
# heappush(heap, item) # pushes a new item on the heap
# item = heappop(heap) # pops the smallest item from the heap
# item = heap[0]       # smallest item on the heap without popping it
# heapify(x)           # transforms list into a heap, in-place, in linear time
# item = heapreplace(heap, item) # pops and returns smallest item, and adds
#                                # new item; the heap size is unchanged

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class HeapType:
    MIN = "min"
    MAX = "max"

class HeapImp:

    def __init__(self, type:int):
        """
        type would be in the range of -1: max or 0: min
        :param type:
        """
        self.root = None
        self.type = HeapType.MAX if type == -1 else HeapType.MIN

    def heapify_hallucinate(self):
        pass
    def add_child_node_bfs(self, root, node):
        que = [root]
        while que:
            current_root = que.pop(0)
            if current_root.left and current_root.right:
                que.extend([current_root.left, current_root.right])
                continue
            elif not current_root.left:
                current_root.left = node
            elif not current_root.right:
                current_root.right = node

    def add_child_node_dfs(self, root, node):
        if not root:
            root = node
            return

        if not root.left:
            root.left = node
            return

        if not root.right:
            root.right = node
            return

        if root.left and root.right:
            self.add_child_node_dfs(root.left, node)


    def add_node(self, node):
        if not self.root:
            self.root = node
        else:
            # self.add_child_node_bfs(self.root, node)
            self.add_child_node_dfs(self.root, node)



array =  [4, 10, 3, 5, 1, 2]
heap = HeapImp(-1)
for i in array:
    print(i)
    node = Node(i)
    heap.add_node(node)
    # heap.add_child_node_dfs(heap.root, node)
print("hello world")


