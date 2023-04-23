from asciimatics.screen import Screen

class Node: 
    def __init__(self, name): 
        self.name = name
        self.adjacent = {}

    def add_edge(self, node, weight):
        self.adjacent[node] = weight

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        new_node = Node(name)
        self.nodes[name] = new_node
        return new_node

    def add_edge(self, node1, node2, weight=0):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)

        self.nodes[node1].add_edge(self.nodes[node2], weight)
        self.nodes[node2].add_edge(self.nodes[node2], weight)

    def greedy(self, start_node):
        self.start_node = self.nodes[start_node]
        for node, weight in self.start_node.adjacent.items():
            print(f"Node: {node.name} | Weight: {weight}")

def create_city_graph(): # NOTE: Used chatGPT to create this function 
    # Create a new graph object
    city_graph = Graph()

    # Add the nodes to the graph
    london = city_graph.add_node('London, England')
    berlin = city_graph.add_node('Berlin, Germany')
    paris = city_graph.add_node('Paris, France')
    rome = city_graph.add_node('Rome, Italy')
    madrid = city_graph.add_node('Madrid, Spain')
    vienna = city_graph.add_node('Vienna, Austria')

    # Add the edges between the nodes with the specified weights
    london.add_edge(berlin, 325)
    london.add_edge(paris, 160)
    london.add_edge(rome, 280)
    london.add_edge(madrid, 250)
    london.add_edge(vienna, 425)

    berlin.add_edge(paris, 415)
    berlin.add_edge(rome, 550)
    berlin.add_edge(madrid, 675)
    berlin.add_edge(vienna, 375)

    paris.add_edge(rome, 495)
    paris.add_edge(madrid, 215)
    paris.add_edge(vienna, 545)

    rome.add_edge(madrid, 380)
    rome.add_edge(vienna, 480)

    madrid.add_edge(vienna, 730)
    
    print(
            """+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|                 | London, England | Berlin, Germany |  Paris, France  |   Rome, Italy   |  Madrid, Spain  | Vienna, Austria |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| London, England |      ------     |       325       |       160       |       280       |       250       |       425       |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Berlin, Germany |       325       |      ------     |       415       |       550       |       675       |       375       |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|  Paris, France  |       160       |       415       |      ------     |       495       |       215       |       545       |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|   Rome, Italy   |       280       |       550       |       495       |      ------     |       380       |       480       |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
|  Madrid, Spain  |       250       |       675       |       215       |       380       |      ------     |       730       |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
| Vienna, Austria |       425       |       375       |        545      |        480      |       730       |      ------     |
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+"""
    )

    # Return the completed graph
    return city_graph




graph = create_city_graph()

graph.greedy('Rome, Italy') 

