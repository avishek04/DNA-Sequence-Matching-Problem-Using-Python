from sys import argv, exit

if(len(argv) != 3):
    print("Please insert correct files")
    exit(1)

def main():
    csvFile = open(argv[1], 'r')
    dnaIDs = csvFile.readline().rsplit(sep = ',')
    dnaIDs.pop(0)
    dnaIDs[len(dnaIDs) - 1] = dnaIDs[len(dnaIDs) - 1].rstrip()

    dnaValueList = []
    for line in csvFile:
        eachpersonDNA = line.rsplit(sep = ',')
        eachpersonDNA[len(eachpersonDNA) - 1] = eachpersonDNA[len(eachpersonDNA) - 1].rstrip()
        dnaValueList.append(eachpersonDNA)
    csvFile.close()

    txtFile = open(argv[2], 'r')
    dnaPattern = txtFile.readline()
    dnaPattern = dnaPattern.rstrip()
    txtFile.close()

    sequenceOutput = []
    for i in range(len(dnaValueList[0]) - 1):
        sequenceOutput.append(Count(dnaIDs[i], dnaPattern))

    if FindMatch(sequenceOutput, dnaValueList) == False:
        print("No match")

def FindMatch(sequence, DNAList):
    for i in range(len(DNAList)):
        name = DNAList[i][0]
        DNAList[i].pop(0)
        DNAList[i][len(DNAList[i]) - 1] = DNAList[i][len(DNAList[i]) - 1].rstrip()
        for j in range(len(DNAList[i])):
            DNAList[i][j] = int(DNAList[i][j])

        count = 0
        if DNAList[i] == sequence:
            print(name)
            return True
    return False

def Count(ID, DNAPattern):
    i = 0
    count = 0
    DNAcount = []
    for j in range(len(DNAPattern)):
        while DNAPattern[i:i + len(ID)] == ID:
            count = count + 1
            i = i + len(ID)
        DNAcount.append(count)
        count = 0
        i = j + 1
    return max(DNAcount)

main()