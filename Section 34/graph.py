#graph
class Graph:
    def __init__(self, gdict = None) -> None:
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)





graph = Graph(customDict)

print(graph.gdict)

def test_cases():


print( test_cases())