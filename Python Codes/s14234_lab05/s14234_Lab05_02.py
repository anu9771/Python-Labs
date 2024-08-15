'''
python oop concepts
Input: coding sequences containing fasta file
Output: sequence type and base counts
date: 05/12/2021
author: Anushka Udara
'''


class Sequence:
    global fasta_Dict
    fasta_Dict = {}

    global header
    header = ""

    global sequence
    sequence = ""

    global fullHeader
    fullHeader = ""

    sequence_count = 0

    def __init__(self, Gene_name, Gene_ID, Species_name, Subspecies_name, sequence):
        self.Gene_ID = Gene_ID
        self.Gene_name = Gene_name
        self.Sequence_type = type
        self.sequence = sequence
        self.Sequence_length = sum(Sequence.get_Character_Count(self, sequence).values())
        self.Species_name = Species_name
        self.Subspecies_name = Subspecies_name
        Sequence.sequence_count += 1

    @staticmethod
    def fasta_Split(filename):

        global listItem
        listItem = ""

        with open(filename, "r") as file:

            for line in file:
                if line != "\n":
                    line = line.strip()
                    # separating the header using ">" sign

                    if line[0] == ">":
                        line = line.replace(">", "")

                        fullHeader = line
                        sequence = ""

                    else:
                        sequence += line
                        # adding full header and sequence as a list to the listItem variable
                        listItem = fullHeader.split() + [sequence]

                    fasta_Dict[fullHeader] = listItem

        return fasta_Dict

    def get_Seq_Type(self, sequence):

        amino_acids = ["K", "N", "R", "S", "I", "M", "Q", "H", "P", "R", "L", "E", "D", "V", "Y", "S", "W", "F"]
        flag = False

        for base in sequence:

            # checking whether the sequence is a protein
            if base in amino_acids:

                type = "protein"
                break


            # checking whether the sequence is an mRNA
            elif base == "U":

                type = "mRNA"
                break

            else:
                type = "DNA"

                # # checking whether the sequence is an DNA
                # elif base == "T":
                #     for letter in sequence:
                #         if letter not in amino_acids:
                #             # global Sequence_type
                #             Sequence_type = "DNA"
                #             flag = True
                #             break
                # elif flag:
                #     break

        return type

    def get_Character_Count(self, sequence):
        character_Dict = {}
        A_count = 0
        T_count = 0
        G_count = 0
        C_count = 0

        for base in sequence:

            if base == "A":
                A_count += 1

            elif base == "T":
                T_count += 1

            if base == "G":
                G_count += 1

            if base == "C":
                C_count += 1
        # adding base counts to the dictionary
        character_Dict["A"] = A_count
        character_Dict["T"] = T_count
        character_Dict["G"] = G_count
        character_Dict["C"] = C_count

        return character_Dict
