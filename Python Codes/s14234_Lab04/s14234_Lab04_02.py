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

    def __init__(self, Gene_name, Gene_ID, Species_name, Subspecies_name, sequence):
        self.Gene_ID = Gene_ID
        self.Gene_name = Gene_name
        self.Sequence_type = Sequence.get_Seq_Type(self, sequence, Gene_ID)
        self.sequence = sequence
        self.Sequence_length = sum(Sequence.get_Character_Count(self, sequence).values())
        self.Sequence_count = len(fasta_Dict)
        self.Species_name = Species_name
        self.Subspecies_name = Subspecies_name

        # printing the Gene ID, sequence length and sequence type of Gene - DREB1A
        if Gene_name == "DREB1A":
            print(Gene_ID, self.Sequence_length, self.Sequence_type, "\n")

    @staticmethod
    def fasta_Split(filename):

        global listItem
        listItem = ""

        with open(filename, "r") as file:

            for line in file:
                line = line.strip()
                # separating the header using ">" sign

                if line[0] == ">":
                    line = line.replace(">", "")

                    fullHeader = line
                    line = line.split()
                    # preparing Gene ID(line[0]) to be set as the key
                    header = line[0]
                    sequence = ""

                else:
                    sequence += line
                    # adding full header and sequence as a list to the listItem variable
                    listItem = fullHeader.split() + [sequence]

                fasta_Dict[header] = listItem

        return fasta_Dict

    def get_Seq_Type(self, sequence, header):
        global Sequence_Type

        amino_acids = ["K", "N", "R", "S", "I", "M", "Q", "H", "P", "R", "L", "E", "D", "V", "Y", "S", "W", "F"]
        flag = False

        for base in sequence:

            # checking whether the sequence is a protein
            if base in amino_acids:

                Sequence_type = "protein"
                print("This \"" + header + "\" is a protein \n")
                break

            else:
                # checking whether the sequence is an mRNA
                if base == "U":

                    Sequence_type = "mRNA"
                    print("This \"" + header + "\" is an mRNA \n")
                    print("")
                    break

                # checking whether the sequence is an DNA
                elif base == "T":
                    for letter in sequence:
                        if letter not in amino_acids:
                            # global Sequence_type
                            Sequence_type = "DNA"
                            print("This \"" + header + "\" is a DNA \n")
                            flag = True
                            break
                elif flag:
                    break

        return Sequence_type

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

        # printing the base counts of Gene DREB1A
        if self.Gene_name == "DREB1A":
            print("Base counts of the DREB1A ")
            print("A_count: " + str(character_Dict["A"]) + ", T_count: " + str(character_Dict["T"]) + ", G_count: "
                  + str(character_Dict["G"]) + ", C_count: " + str(character_Dict["C"]) + " \n")

        return character_Dict


if __name__ == "__main__":

    # calling this method to add fasta headers and sequences to a dictionary
    Sequence.fasta_Split(filename="OSDREB_nucleotideSequences.FASTA")

    for key in fasta_Dict:
        data = fasta_Dict.get(key)

        # passing values for Gene_ID, Gene name,
        key = Sequence(data[0], data[1], data[2], data[3], data[-1])
