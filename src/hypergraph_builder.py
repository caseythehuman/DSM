# src/hypergraph_builder.py

import hypernetx as hnx
import matplotlib.pyplot as plt

def build_hypergraph(relationships):
    hyperedges = {}
    for subject, verb, obj in relationships:
        key = f"{verb}"
        if key not in hyperedges:
            hyperedges[key] = set()
        hyperedges[key].update([subject, obj])
    H = hnx.Hypergraph(hyperedges)
    return H

def visualize_hypergraph(H):
    plt.figure(figsize=(10, 8))
    hnx.draw(H, with_node_labels=True, with_edge_labels=True)
    plt.show()
