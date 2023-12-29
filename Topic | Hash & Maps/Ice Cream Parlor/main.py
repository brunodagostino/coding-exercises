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

def create_map(cost) -> dict[int, list]:
    map = dict()

    for i in range(len(cost)):
        if cost[i] not in map:
            index_list = list()
            index_list.append(i)
            map[cost[i]] = index_list
        else:
            map[cost[i]].append(i)

    return map

def icecream_parlor(m, cost) -> list[int]:
    indices = []
    icecream_one = 0
    icecream_two = 0
    map = create_map(cost=cost)

    for i in range(len(cost)):
        remaining_cost = m - cost[i]

        if remaining_cost in map:
            icecream_one = i
            icecream_two = map[remaining_cost][0]

            if icecream_one == icecream_two:
                if len(map[remaining_cost]) > 1:
                    icecream_two = map[remaining_cost][1]
                    break
            else:
                break
    
    indices.append(icecream_one + 1)
    indices.append(icecream_two + 1)
    
    return sorted(indices)


# Test cases
test_cases = [
    (6, [1, 3, 4, 5, 6]),
    (4, [1, 4, 5, 3, 2]),
    (4, [2, 2, 4, 3]),
    (50, [1, 3, 4, 5, 6]),
]

for m, cost in test_cases:
    result = icecream_parlor(m=m, cost=cost)
    print(result)