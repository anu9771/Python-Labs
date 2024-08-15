from Bio import Entrez
from Bio import SeqIO
import os

# creating a folder to keep the temporary files created.
# https://www.pythontutorial.net/python-basics/python-directory/#:~:text=To%20create%20a%20new%20directory,the%20c%3A%5Ctemp%20directory.
Dir = "D:/Pycharm workspace/s14234_lab13/temporary_files"
if not os.path.exists(Dir):
    os.mkdir("D:/Pycharm workspace/s14653_lab13/temporary_files")

Entrez.email = "audara19@gmail.com"
id_list = ["AAK43967.1", "AED90870.1", "NP_567720.1", "AAK59861.1"]

for Id in id_list:
    handle = Entrez.efetch(db="protein", id=Id, rettype="fasta", retmode="text")
    record = SeqIO.read(handle, "fasta")
    handle.close()
    with open("temporary_files/" + str(Id) + ".fasta", "w") as file:
        file.writelines(record.description + "\n")
        file.writelines(record.seq)
# create a separate folder to write the intermediate files
