
class LinkNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def get_tail_node(self, node):
        if node.next == None:
            return node
        node = node.next
        return self.get_tail_node(node)
    def insert(self, val):
        node = LinkNode(val)
        if not self.head:
            self.head = node
        else:
            tail_node = self.get_tail_node(self.head)
            print(tail_node)
            tail_node.next = node

    def reverse(self, node):
        if not node.next:
            self.head = node
            return node

        curr_node = self.reverse(node.next)
        curr_node.next = node
        return  node

linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
print(linked_list)
reversed = linked_list.reverse(linked_list.head)
reversed.next = None

print()