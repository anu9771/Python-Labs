"""
This python program asks the user to input the NCBI genbank accession number of the required
gene or nucleotide sequence.
download the required DNA sequence, in fasta format.
then, write its description and sequence to a fasta file.

Input: genbank accession number
output: description and sequence containing fasta file.
author: Anushka Udara
Date: 12/03/2022
"""
from Bio import Entrez
from Bio import SeqIO


# giving the email address to the GenBank
Entrez.email = "m.lakshanjayasinghe@gmail.com"
accession_number = input("Enter the required GenBank accession number with version")

# --------search biopython to set db as either DNA or mRNA
handle = Entrez.efetch(db="nucleotide", id=accession_number, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
handle.close()

# Writing the sequence to a fasta file.
with open("cds_seq.fasta", "w") as file:
    file.writelines(record.description + "\n")
    file.writelines(record.seq + "\n")
