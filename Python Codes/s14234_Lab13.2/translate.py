"""
This python file reads the mRNA fasta file and separate mRNA header and sequence into two variables.
Translate the mRNA sequence into an amino acid sequence using the biopython.seq translate function.
Write the amino acid sequence header and sequence to a fasta file.

Input: mRNA fasta file
output: amino acid fasta file
author: Anushka Udara
Date: 12/03/2022
"""
from Bio.Seq import translate
fasta_header = ""
mRNA_sequence = ""

# reading the downloaded cds fasta file
# and separating fasta header and sequence to two variables
with open("mRNA_seq.fasta", "r") as file:
    for line in file:
        line = line.strip()
        if "NM_000188.3" in line:
            fasta_header = line
        else:
            mRNA_sequence += line

# transcribing the cds sequence into mRNA sequence.
aa_sequence = translate(mRNA_sequence)

# modifying the fasta header
fasta_header = fasta_header.replace("transcribed", "") + " translated"

# writing the mRNA sequence to a fasta file with
# the fasta with "transcribed" word.
with open("aa_seq.fasta", "w") as file:
    file.writelines(fasta_header + "\n")
    file.writelines(aa_sequence + "\n")

