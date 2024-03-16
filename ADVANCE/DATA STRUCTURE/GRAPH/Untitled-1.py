class Graph():
    def __init__(self):
        self.graph={}

    def addvertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
        else:
            print("Vertex Already exsists")

    def addedge(self,ver1,ver2,isDirected=True):
        self.addvertex(ver1)
        self.addvertex(ver2)
        self.graph[ver1].append(ver2)
        if not isDirected:
            self.graph[ver2].append(ver1)

vj=Graph()
vj.addedge("a","b")