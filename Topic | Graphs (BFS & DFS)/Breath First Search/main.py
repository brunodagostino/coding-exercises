class Node:
    def __init__(self, id) -> None:
        self.id = id
        self.adjacent = list()

class Graph:
    def __init__(self) -> None:
        self.node_lookup = dict()
    
    def get_node(self, id) -> Node:
        if id not in self.node_lookup:
            self.node_lookup[id] = Node(id=id)

        return self.node_lookup[id]

    def add_edge(self, source, destination) -> None:
        s = self.get_node(id=source)
        d = self.get_node(id=destination)

        s.adjacent.append(d)
    
    def has_path_dfs(self, source, destination) -> bool:
        s = self.get_node(id=source)
        d = self.get_node(id=destination)
        visited = set()

        return self._has_path_dfs(source=s, destination=d, visited=visited)
    
    def _has_path_dfs(self, source, destination, visited) -> bool:
        if source.id in visited:
            return False
        
        visited.add(source.id)

        if source == destination:
            return True
        
        for child in source.adjacent:
            if self._has_path_dfs(source=child, destination=destination, visited=visited):
                return True
        
        return False
    
    def has_path_bfs(self, source, destination) -> bool:
        return self._has_path_bfs(source=self.get_node(id=source), destination=self.get_node(id=destination))
    
    def _has_path_bfs(self, source, destination) -> bool:
        next_to_visit = list()
        visited = set()

        next_to_visit.append(source)

        while len(next_to_visit) > 0:
            node = next_to_visit.pop(0)

            if node == destination:
                return True
            
            if node.id in visited:
                continue

            visited.add(node.id)

            for child in node.adjacent:
                next_to_visit.append(child)
        
        return False

def bfs(graph, source) -> list[int]:
    result = []
    distances = {}
    next_to_visit = list(tuple())

    next_to_visit.append((graph.get_node(source), 0))

    while len(next_to_visit) > 0:
        node, dist = next_to_visit.pop(0)

        distances[node.id] = dist

        for child in node.adjacent:
            if child.id not in distances:
                next_to_visit.append((child, dist + 1))
    
    result = [-1] * (len(graph.node_lookup))

    for node, dist in distances.items():
        if node != source:
            result[node.id - 1] = dist * 6
    
    return result


n1 = Node(id=1)
n2 = Node(id=2)
n3 = Node(id=3)
n4 = Node(id=4)
n5 = Node(id=5)

graph = Graph()
graph.add_edge(source=n1, destination=n2)
graph.add_edge(source=n1, destination=n3)
graph.add_edge(source=n3, destination=n4)

print(bfs(graph=graph, source=n1))