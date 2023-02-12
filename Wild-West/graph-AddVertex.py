# Graph - Add Vertex

class Graph:
    def __init__(self):
        self.adjacencyList = {}
    
    def addVertex(self, vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []

graph = Graph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
print(graph.adjacencyList["A"]) #[]
print(graph.adjacencyList["B"]) #[]
print(graph.adjacencyList["C"]) #[]