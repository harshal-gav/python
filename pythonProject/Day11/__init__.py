class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def add(self, data):
        new_node = Node(data)
        if self.head==None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def add_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def add_after(self, after_data, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == after_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next






ll=LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add_at_front(6)
ll.add_after(2,7)
ll.delete(2)
ll.delete(6)
ll.delete(5)
ll.display()


