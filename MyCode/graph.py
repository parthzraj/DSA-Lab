class graph:
    def __init__(self, vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self,src,dest):
        if(0<=src<self.size and 0<=dest<self.size):
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else: 
            print("invalid edge")


    def print(self):
         for row in self.mat:
             print(' '.join(map(str, row)))



g = graph(5)
g.print()


