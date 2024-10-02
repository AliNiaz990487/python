class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, *initial_values):
        self.head = None
        for v in initial_values:
            self.insert_at_head(v)

    def insert_at_head(self, data):
        if self.head is None: 
            self.head = LinkedList.Node(data)
            return self
        
        new_node = LinkedList.Node(data)
        new_node.next = self.head
        self.head = new_node
        return self

    def insert_at_tail(self, data):
        if self.head is None:
            self.head = LinkedList.Node(data)
            return self
        
        current = self.head
        while current is not None:
            tail = current
            current = current.next
        
        new_node = LinkedList.Node(data)
        tail.next = new_node
        return self
    
    def insert_at_postion(self, data, position):
        if self.head is None or position == 0:
            self.insert_at_head(data)
            print("Warning: position is ignored becaused head is None.")
            return self
        
        current = self.head
        count = 1
        while current is not None and count <= position:
            position_node = current
            current = current.next
            count += 1


        new_node = LinkedList.Node(data)
        new_node.next = position_node.next
        position_node.next = new_node
        return self


    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=", ")
            current = current.next
        print()


linked_list = LinkedList()
linked_list.insert_at_postion(10, 0)
linked_list.insert_at_tail(5).insert_at_tail(12).insert_at_head(7)
linked_list.print_list()