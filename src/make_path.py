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

class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
    def __eq__(self, other):
        return ((self.node1 == other.node1) and (self.node2 == other.node2)) or ((self.node1 == other.node2) and (self.node2 == other.node1))
    def __ne__(self, other):
        return not (((self.node1 == other.node1) and (self.node2 == other.node2)) or ((self.node1 == other.node2) and (self.node2 == other.node1)))
    def is_include(self, node):
        return (node1 == node) or (node2 == ndoe)

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
                res.append(res)
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
        for child in current_node:
            if child in checked:
                continue
            #not checked
            checked.append(child)
            node_queue.put((child, current_path, current_depth + 1))
            
                
        
    
