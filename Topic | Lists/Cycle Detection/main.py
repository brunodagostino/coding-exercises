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

def has_cycle(head) -> int:
    cycle = 0
    map = dict()

    if head == None:
        return cycle
    
    if head.next == None:
        return cycle
    
    current = head

    while current != None:
        if hash(current) in map:
            cycle = 1
            break
        else:
            map[hash(current)] = current
        
        current = current.next
    
    return cycle


node_1 = Node(data=1)
node_2 = Node(data=2)
node_3 = Node(data=3)
node_1.next = node_2 # type: ignore
node_2.next = node_3 # type: ignore
node_3.next = None

result = has_cycle(head=node_1)
print(result)


node_1 = Node(data=1)
node_2 = Node(data=2)
node_3 = Node(data=3)
node_1.next = node_2 # type: ignore
node_2.next = node_3 # type: ignore
node_3.next = node_1 # type: ignore

result = has_cycle(head=node_1)
print(result)