
class Array:
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)

    def delete(self, value):
        if value in self.array:
            self.array.remove(value)

    def access(self, index):
        return self.array[index]

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        temp = self.head
        prev = None
        while temp and temp.value != value:
            prev = temp
            temp = temp.next
        if temp:
            if prev:
                prev.next = temp.next
            else:
                self.head = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
if __name__ == "__main__":
    # Arrays
    array = Array()
    array.insert(1)
    array.insert(2)
    array.delete(1)
    print("Array access:", array.access(0))

    # Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Stack pop:", stack.pop())

    # Queue
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print("Queue dequeue:", queue.dequeue())

    # Linked List
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.traverse()
    linked_list.delete(1)
    linked_list.traverse()
