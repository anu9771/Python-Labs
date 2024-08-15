from Bio import Entrez
from Bio import SeqIO
import os

# creating a folder to keep the temporary files created.
# https://www.pythontutorial.net/python-basics/python-directory/#:~:text=To%20create%20a%20new%20directory,the%20c%3A%5Ctemp%20directory.
Dir = "D:/Pycharm workspace/s14653_lab13/temporary_files"
if not os.path.exists(Dir):
    os.mkdir("D:/Pycharm workspace/s14653_lab13/temporary_files")

Entrez.email = "m.lakshanjayasinghe@gmail.com"
accession_number = input("Enter the required GenBank accession number with version")


handle = Entrez.efetch(db="protein", id=accession_number, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
handle.close()
with open("temporary_files/" + str(Id) + ".fasta", "w") as file:
    file.writelines(record.description + "\n")
    file.writelines(record.seq+"\n")
