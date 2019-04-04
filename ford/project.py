#!/usr/bin/python2.7
"""Ford Fulkerson Algorithm
    Longest Path: Find the longest path from the source node to the sink node.
"""

import networkx as nx
import matplotlib.pyplot as plt
import webbrowser

__author__ = "Disaiah Bennett"
__version__ = 0.1

class Graph:
    """Graph containing the nodes and edges.
    """
    def __init__(self, graph=None, pos=None, source=None, sink=None):
        """Graph Class
            Param
                graph: None - Type of graph the class object will be assigned.
                pos: None - Position of the nodes in the image of the graph.
        """
        # If graph is None, the graph will be set to the default graph value.
        self.graph = nx.DiGraph() if graph is None else graph

        # If pos is None, the node's position will be set to the default pos value.
        self.pos = {
            'S': [0, 1], 'A': [1, 2], 'B': [1, 0],
            'C': [2, 2], 'D': [2, 0], 'T': [3, 1],
        } if pos is None else pos

        self.source = 'S' if source is None else source
        self.sink = 'T' if sink is None else sink

        self.path = True

    def add_sample_nodes_edges(self):
        """Adding Sample Nodes & Edges.
            Return:
                True: bool - Success when adding nodes & edges.
                False: bool - Error when adding nodes & edges.
            Example:
                >>> graph = Graph()
                >>> graph.add_sample_nodes_edges()
        """
        # Default sample node edges
        try:
            self.graph.add_edges_from([("S", "A", {'capacity': 9, 'flow': 0}),
                                       ("S", "B", {'capacity': 9, 'flow': 0}),
                                       ("A", "B", {'capacity': 10, 'flow': 0}),
                                       ("A", "C", {'capacity': 8, 'flow': 0}),
                                       ("B", "C", {'capacity': 1, 'flow': 0}),
                                       ("B", "D", {'capacity': 3, 'flow': 0}),
                                       ("C", "T", {'capacity': 10, 'flow': 0}),
                                       ("D", "C", {'capacity': 8, 'flow': 0}),
                                       ("D", "T", {'capacity': 7, 'flow': 0})])

        except TypeError as error:
            print(error)
            return False

        return True

    def display(self):
        """Display a graph of the nodes with it's connected edge(s).
            Example:
                >>> graph = Graph()
                >>> plt = graph.display()
        """

        # Get the color values for the nodes
        _ = self.graph.number_of_nodes()
        node_colors = range(2, _ + 2)

        # Set the size of the image to be displayed
        plt.figure(figsize=(8, 4))
        plt.axis('off')

        # Draw the nodes
        nx.draw_networkx_nodes(self.graph, self.pos, node_color=node_colors, node_size=600)

        # Draw the edges that are linking the nodes
        nx.draw_networkx_edges(self.graph, self.pos, edge_color='gray', width=3)

        # Draw the nodes label
        nx.draw_networkx_labels(self.graph, self.pos, font_color='white')

        for u, v, edge in self.graph.edges(data=True):
            label = "%d/%d" % (edge['flow'], edge['capacity']) # labels for each
            color = 'green' if edge['flow'] < edge['capacity'] else 'red'
            x = self.pos[u][0] * .6 + self.pos[v][0] * .4
            y = self.pos[u][1] * .6 + self.pos[v][1] * .4
            t = plt.text(x, y, label, size=16, color=color,
                         horizontalalignment='center', verticalalignment='center')

        plt.savefig("sample.png") # save the displaying figure as a png file
        #plt.show() # display the plot data

    def ford_folkerson(self, source, sink):
        """Ford Folkerson Algorithm
            Param:
                source: string - source node.
                sink: string - sink node.
            Return:
                Nothing
            Example:
                >>> graph.ford_folkerson(source, sink)
        """
        while self.path:
            print("Hello", source, sink)
            break

def go_to_github():
    try:
        webbrowser.open("https://dislbenn")
    except webbrowser.Error() as error:
        print(error)

def main():
    """Senior Project Implementation
    """
    graph = Graph() # Create graph object

    if graph.add_sample_nodes_edges(): # Adding Sample Data
        print("[\033[1;32mSUCCESS\033[0m] - Sample Node Added: ", graph.graph.nodes())
        print("[\033[1;32mSUCCESS\033[0m] - Sample Edges Added: ", graph.graph.edges())

    else: # Exit the program if sample data could not be loaded.
        print("[\033[1;31mFAILED\033[0m] - Sample Data Failed To Be Added")
        exit()

    graph.display() # Display the graph
    graph.ford_folkerson(graph.source, graph.sink)

    choice = input("Visit github repository? Enter y/N: ")
    if choice.lower() == "y":
        go_to_github()

if __name__ == "__main__":
    main()
