def delete_at_position(head, position):
    if not head:
        return head  
    
    if position == 0:
        return head.next  
    current = head
    count = 0
    
    while current and count < position - 1:
        current = current.next
        count += 1
    
    if not current or not current.next:
        print("Position out of bounds")
        return head
    
    current.next = current.next.next  


