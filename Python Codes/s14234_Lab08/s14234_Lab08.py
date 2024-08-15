"""
A program which takes known stress proteins of Arabidopsis thaliana, build the graph of DREB2A protein interactions
and determine the majority voting score of the unknown proteins in the PPI network.

Date: 24/01/2022
Inputs: known stress protiens txt file, string interactions of DREB2A protein tsv file
Output: degree of DREB2A protein, number of unknown proteins and an output file containing
        the majority voting scores of unknown proteins.
Author: Anushka Udara
"""
import networkx as nx
from collections import OrderedDict

stress_proteins = set()
# making the known stress proteins set
# Duplicates are not allowed in sets.
with open("AT_stress_proteins.txt") as file:
    for line in file:
        if "#" not in line and line != "\n":
            line = line.split("\t")
            stress_proteins.add(line[1].upper())

# making the graph object
G = nx.Graph()

# reading the interactions file and entering edges
with open("string_interactions.tsv") as file:
    for line in file:
        if "#" not in line and line != "\n":
            line = line.split("\t")
            G.add_edge(line[0].upper(), line[1].upper())

print("Degree of DREB2A protein: ", G.degree("DREB2A"))

# printing the unknown number of proteins
# and inserting their names to a list
unknown_p_id = set()
for node in G.nodes:
    if node not in stress_proteins:
        unknown_p_id.add(node)

print("number of unknown proteins: ", len(unknown_p_id))

# Calculating the majority score
neighbors = []
majority_voting_score = {}
# python set operator is needed
nodes = unknown_p_id.intersection(G.nodes)
for node in nodes:
    voting = 0
    neighbors = G.neighbors(node)
    # checking whether the neighbors of the node is in known stress proteins list
    # If yes, increment the voting score of the particular node
    for neighbor in neighbors:
        if neighbor in stress_proteins:
            voting += 1
    # Enter the relevant majority voting score of the node, after checking all neighbors
    majority_voting_score[node] = voting

# Sorting the dictionary in descending order by values
reversed_mvs = OrderedDict(sorted(majority_voting_score.items(), key=lambda k: k[1], reverse=True))


# Writing the sorted dictionary in descending order by values, to an output file
with open("Majority voting scores.txt", "w") as file:
    for key in reversed_mvs:
        data = key + ": " + str(reversed_mvs.get(key)) + "\n"
        file.writelines(data)