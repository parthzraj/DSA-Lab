class graph:
    def __init__(self):
         self.adj = {}

    def add_vertex(self, vertex):
         if vertex not in self.adj:
              self.adj[vertex] = []

    def add_edeg(self,src,dest):
         self.add_vertex(src)
         self.add_vertex(dest)
         self.adj[src].append(dest)
         self.adj[dest].append(src)

    def printg(self):
         for vertex in self.adj:
              print(vertex, " -> ", self.adj[vertex], end="\n")


g = graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.printg()