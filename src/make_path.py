import sys
import Queue

protein_list = ["MATR3", "HNRNPK", "PDIA3", "AHNAK"]

class Node:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other
    def __ne__(self, other):
        return self.name != other
    def to_string(self):
        return self.name
    
class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
    def __eq__(self, other):
        return ((self.node1 == other.node1) and (self.node2 == other.node2)) or ((self.node1 == other.node2) and (self.node2 == other.node1))
    def __ne__(self, other):
        return not (((self.node1 == other.node1) and (self.node2 == other.node2)) or ((self.node1 == other.node2) and (self.node2 == other.node1)))
    def is_include(self, node):
        return (self.node1 == node) or (self.node2 == node)
    def to_string(self):
        return self.node1.to_string() + ":" + self.node2.to_string()
    def get_pair(self, node):
        if self.node1 == node:
            return self.node2
        elif self.node2 == node:
            return self.node1
        else:
            return None

class Graph:
    def __init__(self):
        self.node_list = []
        self.edge_list = []
    def add_node(self, node):
        if not (node in self.node_list):
            self.node_list.append(node)
    def add_edge(self, edge):
        if not (edge in self.edge_list):
            self.edge_list.append(edge)
    def get_connect(self, node):
        res = []
        for e in self.edge_list:
            if e.is_include(node):
                res.append(e.get_pair(node))
        return res
    def to_string(self):
        res = ""
        res += "Node:\n"
        for n in self.node_list:
            res += n.to_string() + "\n"
        res += "Edge:\n"
        for e in self.edge_list:
            res += e.to_string() + "\n"
        return res
            
def make_graph(file_name):
    graph = Graph()
    with open(file_name, "r") as f:
        for line in f:
            #treat comment
            if line[0] == "#":
                continue
            array = line.strip().split("\t")
            #number of col is wrong
            if not (len(array) == 15):
                continue
            #parse line
            node1 = Node(array[0])
            node2 = Node(array[1])
            graph.add_node(node1)
            graph.add_node(node2)
            graph.add_edge(Edge(node1, node2))
    return graph
            
def search_path(graph, start, end, step):
    #res is list of path (list of nodes)
    res = []
    checked = []
    node_queue = Queue.Queue()
    node_queue.put((start, [], 0))
    while not node_queue.empty():
        info = node_queue.get()
        current_node = info[0]
        #print "search " + current_node.to_string()
        current_path = list(info[1])
        current_depth = info[2]
        current_path.append(current_node)
        #when end node, current_path is saved
        if current_node == end:
            res.append(current_path)
            continue
        #if depth >= step: cut branch
        if current_depth == step:
            continue
        #expand children nodes
        for child in graph.get_connect(current_node):
            if child in checked:
                continue
            #not checked
            if child != end:
                checked.append(child)
            node_queue.put((child, current_path, current_depth + 1))
    return res

def path_to_string(path):
    #path: list of node
    s = ""
    for (i, node) in enumerate(path):
        if (i == len(path) - 1):
            s += node.to_string()
        else:
            s += node.to_string() + "->"
    return s

def main(string_file_name):
    graph = make_graph(string_file_name)
    #for debug
    #print graph.to_string()
    target_list  = [(x, y) for x in protein_list for y in protein_list if x != y]
    for target in target_list:
        print "-----Search: " + target[0] + "->" + target[1] + "-----"
        res = search_path(graph, Node(target[0]), Node(target[1]), 9)
        for path in res:
            print path_to_string(path)
    return 0

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 2:
        print "invalid argment"
        sys.exit()
    main(argv[1])
                
