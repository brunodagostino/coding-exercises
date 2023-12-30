import heapq


def q_heap_1(heap, query) -> None:
    if query[0] == 1:
        heapq.heappush(heap, query[1])
    elif query[0] == 2:
        heap.remove(query[1])
        heapq.heapify(heap)
    elif query[0] == 3:
        print(heap[0])


heap = []

# Test cases
test_cases = [
    (1, 4),
    (1, 9),
    (3,),
    (2, 4),
    (3,),
]

for query in test_cases:
    q_heap_1(heap=heap, query=query)