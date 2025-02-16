class Graph: 
    def __init__(self):
        self.adj_list = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        return False
            
    def print_graph(self):
        for v in self.adj_list:
            print(v, 'vertex is ', self.adj_list[v])
            
            
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            
            
            
my_graph =  Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')

my_graph.print_graph()

my_graph.add_edge('A', 'B')

my_graph.print_graph()

            