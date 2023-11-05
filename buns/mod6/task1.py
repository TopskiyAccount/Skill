class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0:
            return None  
        current = self.head
        for i in range(index):
            if current is None:
                return None  
            current = current.next
        return current.data if current else None

    def remove(self, index):
        if index < 0:
            return 
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if current is None:
                return  
            current = current.next
        if current and current.next:
            current.next = current.next.next

    def insert(self, n, val):
        if n < 0:
            return  
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(n - 1):
            if current is None:
                return  
            current = current.next
        if current:
            new_node.next = current.next
            current.next = new_node

    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_node:
            data = self.current_node.data
            self.current_node = self.current_node.next
            return data
        else:
            raise StopIteration
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)

    for item in linked_list:
        print(item)

    print("Get(1):", linked_list.get(1))
    linked_list.remove(1)
    print("After removing index 1:")
    for item in linked_list:
        print(item)

    linked_list.insert(1, 5)
    print("After inserting 5 at index 1:")
    for item in linked_list:
        print(item)
        
        
