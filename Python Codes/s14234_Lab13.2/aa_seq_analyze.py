"""
This python file reads the amino acid sequence fasta file and enter the amino acid sequence into a variable.
Remove the ambiguous codons to calculate the molecular weight.
Calculate the length, molecular weight, alanine percentage and Glycine percentage.
Write these details to a text file.

Input: amino acid sequence fasta file
output: details containing text file
author: Anushka Udara
Date: 12/03/2022
"""

from Bio.SeqUtils.ProtParam import ProteinAnalysis


# method to calculate the necessary amino acid's percentage
def get_amino_acid_percentage(amino_acid):
    amino_acid_count = 0

    for a_acid in aa_sequence:
        if a_acid == amino_acid:
            amino_acid_count += 1

    amino_acid_percentage = amino_acid_count / length * 100

    return str(round(amino_acid_percentage, 2)) + "%"


aa_sequence = ""

# read the amino acid sequence fasta file
with open("aa_seq.fasta", "r") as file:
    for line in file:
        line = line.strip()
        if "NM_000188.3" not in line:
            aa_sequence += line

# removing ambiguous characters "*" in aa sequence
# A codon that codes for more than one amino acid is an undefined or ambiguous codon.
aa_sequence = aa_sequence.replace("*", "")

# creating the ProteinAnalysis object to calculate molecular weight
aa = ProteinAnalysis(aa_sequence)

# calculate required properties.
length = len(aa_sequence)
molecular_weight = aa.molecular_weight()
alanine_percentage = get_amino_acid_percentage("A")
glycine_percentage = get_amino_acid_percentage("G")

# write the particular protein's properties to a text file.
with open("aa_stats.txt", 'w') as file:
    file.writelines("Protein length: " + str(length) + "\n")
    file.writelines("Molecular weight: " + str(molecular_weight) + "\n")
    file.writelines("Alanine percentage: " + alanine_percentage + "\n")
    file.writelines("Glycine percentage: " + glycine_percentage + "\n")
