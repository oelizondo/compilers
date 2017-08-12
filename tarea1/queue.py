import Node

class Queue:
    def init(self):
        self.head = None
        self.back = None

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

    def front(self):
        return self.head.data

    def back(self):
        return self.back.data

    def at(self, position):
        return self._at(position, self.head)

    def _at(self, position, data):
        if position == 0:
            return data.data
        self._at(position - 1, data.next)
