'''
Using biopython RE packages to print fast record details,
run blast search and search for ABRE elements in xml files.
Input: Refseq sequences containing fasta file
Output: BLAST results containing xml file
date: 05/01/2022
author: Anushka Udara
'''
from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Blast import NCBIXML
import re

# entering email for NCBI
NCBIWWW.email = "audara19@gmail.com"
E_VALUE_THRESH = 0.05

# opening and looping through all fasta records
for record in SeqIO.parse("ATdreb2a.fasta", "fasta"):

    # printing sequence ID, description, sequence and length
    print(record.id)
    print(record.description)
    print(record.seq)
    print(len(record.seq), "\n")


# Running the web based BLAST program and saving output in a xml file.
# fasta_string = SeqIO.read("ATdreb2a.fasta", "fasta")
# result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string.format("fasta"))
#
#
# with open("dreb2a_blast.xml","w") as file:
#     file.write(result_handle.read())

# opening the blast output file
re_handle = open("dreb2a_blast.xml")
# parsing the blast putput file
blast_records = NCBIXML.parse(re_handle)
blast_record = next(blast_records)

# printing blast hit title, alignment length, E-value, score, hit/subject sequence, and hit sequence length.
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print("****Alignment****")
            print("sequence:", alignment.title)
            print("length:", alignment.length)
            print("e value:", hsp.expect)
            print("score", hsp.score)
            print(hsp.query[0:75] + "...")
            print(hsp.match[0:75] + "...")
            print(hsp.sbjct[0:75] + "...\n")


# making ABRE element search string
ABRE = "[TC]ACGT[GT]C"
ABRE_count = 0

# searching for ABRE element blast hit sequences
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        # incrementing ABRE count, if re.search doesn't give a None result
        # it gives a match object if the search string is found
        for result in re.finditer(ABRE, hsp.sbjct):
            if result is not None:
                ABRE_count += 1
                # print the detected ABRE element and its location in sequence
                print(result)
                print("detected ABRE element: ", result.group(), "  span of ABRE element: ", result.span(), "\n")

print("ABRE count", ABRE_count)





