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
        self.nodes[node2].add_edge(self.nodes[node1], weight)

    def greedy(self, start_node):
        start_node = current_node = self.nodes[start_node]
        visited_nodes = set()
        lowest = None

        print(start_node.name, '--->', end=' ')
        visited_nodes.add(start_node.name)

        for x in range(6):
            for node, weight in current_node.adjacent.items():
                if node.name in visited_nodes:
                    continue

                if lowest is None:
                    lowest = node
                    continue

                if weight < lowest.adjacent[current_node]:
                    lowest = node

            if lowest is None:
                current_node = start_node
                print(current_node.name)
                break
            else:
                current_node = lowest
                visited_nodes.add(current_node.name)
                lowest = None
                print(current_node.name, '--->', end=' ')

    def get_node_names(self):
        return list(self.nodes.keys())


# create a new graph object
graph = Graph()

# add nodes to the graph
graph.add_node('London, England')
graph.add_node('Berlin, Germany')
graph.add_node('Paris, France')
graph.add_node('Rome, Italy')
graph.add_node('Madrid, Spain')
graph.add_node('Vienna, Austria')

# add edges to the graph
graph.add_edge('London, England', 'Berlin, Germany', 325)
graph.add_edge('London, England', 'Paris, France', 160)
graph.add_edge('London, England', 'Rome, Italy', 280)
graph.add_edge('London, England', 'Madrid, Spain', 250)
graph.add_edge('London, England', 'Vienna, Austria', 425)

graph.add_edge('Berlin, Germany', 'Paris, France', 415)
graph.add_edge('Berlin, Germany', 'Rome, Italy', 550)
graph.add_edge('Berlin, Germany', 'Madrid, Spain', 675)
graph.add_edge('Berlin, Germany', 'Vienna, Austria', 375)

graph.add_edge('Paris, France', 'Rome, Italy', 495)
graph.add_edge('Paris, France', 'Madrid, Spain', 215)
graph.add_edge('Paris, France', 'Vienna, Austria', 545)

graph.add_edge('Rome, Italy', 'Madrid, Spain', 380)
graph.add_edge('Rome, Italy', 'Vienna, Austria', 480)

graph.add_edge('Madrid, Spain', 'Vienna, Austria', 730)

print("""
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
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
+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+-----------------+
"""
)

list = graph.get_node_names()

for index, name in enumerate(list):
    print(f'{index + 1}. {name}')
print()

try:
    start = int(input('==> Which node do you want to start at?: ')) - 1
    graph.greedy(list[start])
except:
    print('Please enter a valid number')


