"""
Novel drug-target interaction prediction using common neighbors algorithm
using a bipartite graph object.
Input: DTI network extracted from the MATADOR database.
Output: a dictionary with Common neighbor scores of novel drug-targets.
date: 22.02.2022
Author: Anushka Udara
"""
import matplotlib.pyplot as plt
import networkx as nx

drugs = []
proteins = []

# create a graph object.
G = nx.Graph()

# enter drugs and proteins to separate lists
with open("DTIsubset.tsv") as file:
    for line in file:
        line = line.strip("\n").split("\t")
        if line[0] != "Drug_name":
            # Enter drugs and proteins/targets into separate lists.
            drugs.append(line[0])
            proteins.append(line[1])

# convert two lists to sets, to remove duplicates
drugs = set(drugs)
proteins = set(proteins)

# adding nodes to the graph
G.add_nodes_from(drugs, bipartite=0)
G.add_nodes_from(proteins, bipartite=1)

# add edges by reading
with open("DTIsubset.tsv") as file:
    for line in file:
        line = line.strip("\n").split("\t")
        if line[0] != "Drug_name":
            G.add_edge(line[0], line[1])


# ----------------- draw a bipartite graph--------------------------------

# Separate by group
l, r = nx.bipartite.sets(G)
pos = {}

# Update position for node from each group
pos.update((node, (1, index)) for index, node in enumerate(l))
pos.update((node, (2, index)) for index, node in enumerate(r))

nx.draw(G, pos=pos)
plt.show()

# draw the graph
nx.draw(G)
plt.show()

# ------------------------  searching for common neighbors of drugs and proteins-----------------
CN_score = {}

for protein in proteins:
    # finding neighbors of proteins
    protein_neighbors = nx.neighbors(G, protein)
    for neighbor in protein_neighbors:
        # finding set of neighbors of node protein's(target's) neighbors
        neighbors_of_neighbors = set(nx.neighbors(G, neighbor))
        for drug in drugs:
            # finding neighbors of drugs
            drug_neighbors = set(nx.neighbors(G, drug))

            # if this drug and protein/target doesn't have an already existing interaction
            if not G.has_edge(drug, protein):
                # getting the number of common neighbors of the drug and protein/target
                CN = len(drug_neighbors.intersection(neighbors_of_neighbors))
                # insert the pair and common neighbor score to a dictionary
                CN_score[str(drug)+"-"+str(protein)] = CN

# sorting the dictionary in descending order by values
Descending_CN_score = sorted(CN_score.items(), key=lambda k: k[1], reverse=True)

print(Descending_CN_score)
