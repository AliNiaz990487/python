class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


def count_nodes(head):
    if head is None:
        return 0

    return 1 + count_nodes(head.next)


head = Node(1)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print("Count of nodes is", count_nodes(head))
