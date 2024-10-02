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
        count = 0
        while current is not None and count <= position:
            position_node = current
            current = current.next
            count += 1


        new_node = LinkedList.Node(data)
        new_node.next = position_node.next
        position_node.next = new_node
        return self

    def delete_at_head(self):
        if self.head is None: return self

        new_head = self.head.next
        del self.head
        self.head = new_head 
        return self
    
    def delete_at_tail(self):
        if self.head is None:
            return self
        
        if self.head.next is None:
            del self.head
            self.head = None
            return self
        
        current = self.head
        while current.next.next is not None:
            current = current.next

        tail = current.next
        current.next = None
        del tail
        return self

    def delete_at_position(self, position):
        if self.head is None:
            return self
        if position == 0:
            return self.delete_at_head()
            

        current = self.head
        prev = None
        count = 0
        
        while current is not None and count < position:
            prev = current
            current = current.next
            count += 1
        
        prev.next = current.next
        del current
        
        return self
        
    def reverse(self):
        if self.head is None: return self
        if self.head.next is None: return self

        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next  
            current.next = prev       
            prev = current            
            current = next_node      
        
        self.head = prev  
        return self


    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=", ")
            current = current.next
        print()
    

linked_list = LinkedList(2, 4, 8)
linked_list.insert_at_postion(10, 0)
linked_list.insert_at_tail(5).insert_at_tail(12).insert_at_head(7)
# linked_list.delete_at_head().delete_at_tail()

# linked_list.delete_at_position(1)
linked_list.print_list()
linked_list.reverse()
linked_list.print_list()