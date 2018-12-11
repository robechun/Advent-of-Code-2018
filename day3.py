from collections import defaultdict


def overlap():
    file_input = open('input/day3_input.txt', "r")
    encountered = {}
    overlap = 0
    # claims = set()

    for line in file_input.readlines():
        hash = line.find('#')
        at = line.find('@')
        comma = line.find(',')
        colon = line.find(':')
        x = line.find('x')

        # claim = int(line[hash + 1: at - 1])
        i_section = int(line[comma + 1: colon])
        j_section = int(line[at + 2: comma])

        width = int(line[colon + 2: x])
        height = int(line[x + 1:])

        for i in range(i_section, i_section + height):
            for j in range(j_section, j_section + width):
                if i in encountered:
                    if j in encountered[i]:
                        if encountered[i][j] == 1:
                            overlap += 1
                        encountered[i][j] += 1
                    else:
                        encountered[i][j] = 1
                else:
                    encountered[i] = {}
                    encountered[i][j] = 1

    print(overlap)


if __name__ == '__main__':
    overlap()
