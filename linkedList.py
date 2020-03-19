class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("previous node does not exist")
        new_node = Node(data)
        adjacent_node = prev_node.next
        prev_node.next = new_node
        new_node.next = adjacent_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


liss = LinkedList()
liss.append("A")
liss.append("B")
liss.insert_after_node(liss.head.next, "D")
liss.append("B")
liss.print_list()
