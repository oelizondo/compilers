import Node

class Stack:
    def __init__(self):
        self.head = None
        self.top_ptr = None

    def push(self, data):
        if self.head == None:
            self.head = Node.Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node.Node(data)
            self.top_ptr = temp.next

    def top(self):
        return self.top_ptr.data

    def pop(self):
        value = self.head.data
        temp = self.head.next
        self.head = temp
        return value

    def at(self, position):
        return self._at(position, self.head)

    def _at(self, position, data):
        if position == 0:
            return data.data
        self._at(position - 1, data.next)

    def display(self):
        self._display(self.head)

    def _display(self, node):
        print(node.data)
        if node.next == None:
            return
        self._display(node.next)
