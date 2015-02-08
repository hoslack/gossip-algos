import numpy as np
import networkx as nx

#the whole graph is local, which is quite annoying
#but is interesting enough.
#a next step is to turn this parallel.

def make_graph(guess=0):
    net = nx.Graph()
    net.add_node(1, val=10, guess=guess)
    net.add_node(2, val=12, guess=guess)
    net.add_node(3, val=3, guess=guess)
    net.add_node(4, val=22, guess=guess)
    net.add_node(5, val=2, guess=guess)
    net.add_node(6, val=-2, guess=guess)
    net.add_node(7, val=222, guess=guess)
    net.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,1),(1,4),(5,3)])
    return net

def gossip_minimum(graph):
    pass

def gossip_mininum_test():
    net = make_graph(guess=100000)

def gossip_sum(graph):
    #each node has a value and its own guess for minimum
    #at each point, the node takes a random neighbor and
    #compare the guess it has and its neighbor's guess and take min
    #then generate some random numbers according to exponential distribution
    #then actually say that the mean is the estimator,
    #due to properties of the exponential distribution. hey! you have mean, so you have sum!
    pass

def gossip_sum_test():
    net = make_graph(guess=0)
