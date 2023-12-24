class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def prepend(self, data) -> None:
        new_head = Node(data=data)
        new_head.next = self.head # type: ignore
        self.head = new_head
    
    def append(self, data) -> None:
        if self.head == None:
            self.head = Node(data=data)
            
            return
        
        current = self.head

        while current.next != None:
            current = current.next
        
        current.next = Node(data=data) # type: ignore

def insert_node_at_position(head, data, position) -> Node:
    if head == None:
        return head
    
    if position == 0:
        new_node = Node(data=data)
        new_node.next = head
        head = new_node
        
        return head
    
    current = head
    i = 0

    while current.next != None and i != position - 1:
        current = current.next
        i += 1
    
    if i == position - 1:
        new_node = Node(data=data)
        new_node.next = current.next
        current.next = new_node
    
    return head


llist = LinkedList()
llist.append(data=1)
llist.append(data=2)
llist.append(data=3)
data = 4
position = 2
llist_head = insert_node_at_position(head=llist.head, data=data, position=position)
while llist_head:
    print(llist_head.data)
    llist_head = llist_head.next

llist = LinkedList()
llist.append(data=16)
llist.append(data=13)
llist.append(data=7)
data = 1
position = 2
llist_head = insert_node_at_position(head=llist.head, data=data, position=position)
while llist_head:
    print(llist_head.data)
    llist_head = llist_head.next