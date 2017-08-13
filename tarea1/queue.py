import Node

class Queue:
    def init(self):
        self.head = None
        self.back = None
        self.size = None

    def push(self, data):
        if self.head == None:
            self.head = Node.Node(data)
            self.back = self.head
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node.Node(data)
            self.back = temp.next
        self.size += 1

    def front(self):
        return self.head.data

    def pop_front(self):
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value

    def back(self):
        return self.back.data

    def pop_back(self):
        self.size -= 1
        if self.size == 1:
            self.head = None
            return None
        elif self.size == 2:
            value = self.back.data
            self.back = self.head
            return value
        else:
            return self._pop_back(self.head, self.size)

    def _pop_back(node, size):
        if size == 2:
            value = self.back.data
            self.back = node
            return value
        self._pop_back(node.next, size - 1)

    def at(self, position):
        return self._at(position, self.head)

    def _at(self, position, data):
        if position == 0:
            return data.data
        self._at(position - 1, data.next)

    def length(self):
        return self.size

    def display(self):
        self._display(self.head)

    def _display(self, node):
        print(node.data)
        if node.next == None:
            return
        self._display(node.next)
