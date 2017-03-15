

class Stack(object):

    def __init__(self):

        self.array = []

    def push(self, obj):

        self.array.append(obj)

    def pop(self):

        popped = self.array[-1]
        self.array = self.array[:-1]
        return popped

    def min_stack(self):

        min_val = self.array.pop()
        copied_array = [min_val]

        while self.array:
            if self.array[-1] < min_val:
                min_val = self.array.pop()
                copied_array.append(min_val)
            else:   
                copied_array.append(self.array.pop())

        while copied_array:
            self.array.append(copied_array.pop())     

        return min_val


class Node(object):

    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):

        return "<Node %s>" % self.data

class Stack_LL(object): # include edge cases and errors, other methods

    def __init__(self):

        self.head = None
        self.tail = None

    def __repr__(self):
        output = []
        node = self.head
        while node:
            output.append(node.data)
            node = node.next

        return "><".join(output)


    def push(self, node):

        if self.head == None:
            print "IF"
            self.head = node
            self.head.prev = None
            self.tail = node
            self.tail.next = None
        else:   
            print "ELSE"
            next_to_last = self.tail
            self.tail.next = node
            # self.tail.prev = self.tail
            self.tail = node

            self.tail.prev = next_to_last
            
            self.tail.next = None


    def pop(self):

        popped = self.tail
        self.tail = self.tail.prev
        self.tail.next = None

        return popped




