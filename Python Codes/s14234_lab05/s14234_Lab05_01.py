"""
python oop sub classes
Input: coding sequences containing fasta file
Output: Printing the necessary details of sequences.
date: 12/12/2021
author: Anushka Udara
"""
from s14653_2 import Sequence


class DNAseq(Sequence):

    def __init__(self, Gene_name, Gene_ID, Species_name, Subspecies_name, sequence):
        # getting several attribute values from the parent class Sequence's constructor
        super(DNAseq, self).__init__(Gene_name, Gene_ID, Species_name, Subspecies_name, sequence)

        self.Sequence_length = self.Sequence_length
        self.Sequence_type = type
        self.AT_content = self.get_ATcontent(sequence)
        self.TranscribedSequence = self.transcribe_Sequence(sequence)

        if self.Gene_name == "DREB1A":
            print(Gene_ID, self.Sequence_length, self.Sequence_type, self.AT_content)

        if self.Gene_name == "DREB2B.isoform_1":
            DREB2B = MRNAseq(Gene_name, Gene_ID, Species_name, Subspecies_name, self.TranscribedSequence)

    def transcribe_Sequence(self, sequence):
        # replacing thymine with Uracil
        sequence = sequence.replace("T", "U")

        return sequence

    def get_ATcontent(self, sequence):
        ATcount = 0
        count = 0

        for base in sequence:
            count += 1
            if base == "A" or base == "T":
                ATcount += 1

        ATcontent = round(ATcount / count * 100, 2)

        return ATcontent


class MRNAseq(Sequence):

    def __init__(self, Gene_name, Gene_ID, Species_name, Subspecies_name, sequence, ):
        # getting several attribute values from the parent class Sequence's constructor
        super(MRNAseq, self).__init__(Gene_name, Gene_ID, Species_name, Subspecies_name, sequence)

        self.Sequence_length = self.Sequence_length
        self.Sequence_type = type
        self.AT_content = self.get_ATcontent(sequence)
        self.__Amino_acid_codons = self.upload_Codons()
        self.Translated_sequence = self.translate_Sequence(self.__Amino_acid_codons, sequence)

        # if self.Gene_name == "DREB2B.isoform_1":
        #     print(self.Sequence_length, self.Sequence_type, self.AT_content, self.sequence)
        #     DREB2B = Proteinseq(Gene_name, Gene_ID, Species_name, Subspecies_name, self.Translated_sequence)

        if self.Gene_name == "DREB2B.isoform_1":
            print(self.Sequence_length, self.Sequence_type, self.AT_content, self.sequence)
            DREB2B = Proteinseq(Gene_name, Gene_ID, Species_name, Subspecies_name, self.Translated_sequence)

    def get_ATcontent(self, sequence):
        ATcount = 0
        count = 0

        for base in sequence:
            count += 1
            if base == "A" or base == "U":
                ATcount += 1

        ATcontent = round(ATcount / count * 100, 2)

        return ATcontent

    @classmethod
    def upload_Codons(cls):
        global __Amino_acid_codons
        __Amino_acid_codons = {}

        with open("codon_table.txt", "r") as file:
            for line in file:

                line = line.split()
                if "#" not in line:
                    codon = line[0]
                    amino_acid = line[2]
                    __Amino_acid_codons[codon] = amino_acid

        return __Amino_acid_codons

    def translate_Sequence(self, Amino_acid_codons, mRNA_sequence):
        flag = False
        num = 0
        amino_acid_sequence = ""

        while range(len(mRNA_sequence)):
            codon = mRNA_sequence[num] + mRNA_sequence[num + 1] + mRNA_sequence[num + 2]
            num += 3
            if codon == "UAA" or codon == "UGA" or codon == "UAG":
                break
            elif codon in Amino_acid_codons:
                amino_acid_sequence += Amino_acid_codons[codon]

        return amino_acid_sequence


class Proteinseq(Sequence):

    def __init__(self, Gene_name, Gene_ID, Species_name, Subspecies_name, sequence, Uniprot_ID=None,
                 Reviewed_status=None):
        # getting several attribute values from the parent class Sequence's constructor
        super(Proteinseq, self).__init__(Gene_name, Gene_ID, Species_name, Subspecies_name, sequence)

        self.Sequence_length = self.Sequence_length
        self.Sequence_type = type
        self.Uniprot_ID = Uniprot_ID
        self.Reviewed_status = Reviewed_status
        self.Hydrophobicity = self.get_Hydrophobicity(sequence)

        if self.Gene_name == "DREB2B.isoform_1":
            print(self.sequence, self.Sequence_length)

        if self.Gene_name == "DREB2A":
            print(self.Uniprot_ID, self.Reviewed_status, self.Sequence_type, self.Hydrophobicity)

    def get_Hydrophobicity(self, sequence):
        hydro_amino_acids = ["A", "I", "L", "M", "F", "W", "Y", "V"]
        hydrophobicity_count = 0
        count = 0

        for amino_acid in sequence:
            count += 1
            if amino_acid in hydro_amino_acids:
                hydrophobicity_count += 1

        Hydrophobicity = round(hydrophobicity_count / count * 100, 2)

        return Hydrophobicity


if __name__ == "__main__":

    # calling this method to add fasta headers and sequences to a dictionary
    fasta_Dict = Sequence.fasta_Split(filename="OSDREB_sequences.FASTA")

    MRNAseq.upload_Codons()

    for key in fasta_Dict:
        data = fasta_Dict.get(key)
        # getting the sequence type
        type = Sequence.get_Seq_Type(data[0], data[-1])

        # creating objects based on the sequence types
        if type == "DNA":
            key = DNAseq(data[0], data[1], data[2], data[3], data[-1])
        elif type == "mRNA":
            key = MRNAseq(data[0], data[1], data[2], data[3], data[-1])
        elif type == "protein":
            key = Proteinseq(data[0], data[1], data[2], data[3], data[-1], data[4], data[5])

    print(Sequence.sequence_count)
