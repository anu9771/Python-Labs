"""
This python file reads the DNA fasta file, separate fasta header and sequence into two variables.
Transcribe the DNA sequence to mRNA using replace function.
Write the mRNA header and mRNA sequence to a fasta file.

Input: DNA fasta file
output: mRNA fasta file
author: Anushka Udara
Date: 12/03/2022
"""

fasta_header = ""
cds_sequence = ""

# reading the downloaded cds fasta file
# and separating fasta header and sequence to two variables
with open("cds_seq.fasta", "r") as file:
    for line in file:
        line = line.strip()
        if "NM_000188.3" in line:
            fasta_header = line
        else:
            cds_sequence += line

# transcribing the cds sequence into mRNA sequence.
transcribed_sequence = cds_sequence.replace("T", "U")

# writing the mRNA sequence to a fasta file with
# the fasta with "transcribed" word.
with open("mRNA_seq.fasta", "w") as file:
    file.writelines(fasta_header + " transcribed\n")
    file.writelines(transcribed_sequence + "\n")






