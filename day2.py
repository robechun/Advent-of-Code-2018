def checksum():
    file_input = open("day2_input.txt", "r")
    twoFreq = 0
    threeFreq = 0

    for line in file_input.readlines():
        countDict = {}
        twoCounted = False
        threeCounted = False
        for c in line:
            if c in countDict:
                countDict[c] += 1
            else:
                countDict[c] = 1

        for k, v in countDict.items():
            if v == 2 and not twoCounted:
                twoFreq += 1
                twoCounted = True
            if v == 3 and not threeCounted:
                threeFreq += 1
                threeCounted = True

    checksumVal = twoFreq * threeFreq
    print("Checksum is: %d" % checksumVal)


def commonLetters():
    file_input = open("day2_input.txt", "r")
    lines = []

    for line in file_input.readlines():
        lines.append(line)

    for i in range(0, len(lines)):
        for j in range(i + 1, len(lines)):
            diff = 0
            diffPos = 0
            for k in range(0, len(lines[i])):
                if diff > 1:
                    break
                if lines[i][k] != lines[j][k]:
                    diffPos = k
                    diff += 1

            if diff == 1:
                print("Common Letters: %s"
                      % lines[j][:diffPos] + lines[j][diffPos + 1:])


if __name__ == "__main__":
    checksum()
    commonLetters()
