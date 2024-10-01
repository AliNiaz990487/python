class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def insert_at_location(head, data, position):
    new_node = Node(data)
    if position == 0: 
        new_node.next = head
        return new_node
    
    current = head
    count = 0
    
    while current and count < position - 1:
        current = current.next
        count += 1
    
    if not current: 
        print("Position out of bounds")
        return head
    
    new_node.next = current.next 
    current.next = new_node  
    
    return head



head = Node(1)
head = insert_at_location(head, 3, 1)
head = insert_at_location(head, 2, 1)
new_head = reverse_linked_list(head)
while new_head:
    print(new_head.data, end=" ")  # 3 2 1
    new_head = new_head.next
