'''
Usage of functions to determine sequence type, AT content
Input: sequence containing fasta file
Output: sequence type and AT content
date: 05/12/2021
author: Anushka Udara
'''
def insertCodes():
    header = ""
    sequence = ""

    with open("OSDREB_sequences.FASTA", "r") as file:
        for line in file:

            line = line.strip()
            if line[0] == ">":
                header = line
                sequence = ""
            else:
                sequence += str(line)
            MyDict[header] = sequence

    return MyDict


def findATContent(sequence):
    atContent = 0
    baseCount = 0

    for base in sequence:
        baseCount += 1
        if base == "A" or base == "T":
            atContent += 1
    # printing AT content
    print("AT content in DNA sequence: " + str(round(atContent / baseCount * 100, 2)) + "%")
    print("")

    return


# This method assumes that only natural sequences are given.
def checkSequence(sequence):
    amino_acids = ["K", "N", "R", "S", "I", "M", "Q", "H", "P", "R", "L", "E", "D", "V", "Y", "S", "W", "F"]
    flag = False

    for base in sequence:

        # checking whether the sequence is a protein
        if base in amino_acids:


            print("This \"" + header + "\" is a protein")
            print("")
            break

        else:
            # checking whether the sequence is an RNA
            if base == "U":
                print("This \"" + header + "\" is a RNA sequence")
                print("")
                break

            # checking whether the sequence is an DNA
            elif base == "T":
                for letter in sequence:
                    if letter not in amino_acids:
                        print("This \"" + header + "\" is a DNA sequence")
                        findATContent(sequence)
                        flag = True
                        break
            elif flag:
                break
    return



MyDict = {}

insertCodes()

for header in MyDict:
    checkSequence(MyDict.get(header))
