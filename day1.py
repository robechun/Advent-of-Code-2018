def part1():
    file_input = open("day1_input.txt", "r")
    freq = 0

    for line in file_input.readlines():
        freq += int(line)

    print("Part 1 answer: %d" % freq)


def part2():
    seen = {0}
    values = []

    file_input = open("day1_input.txt", "r")
    freq = 0

    for line in file_input.readlines():
        value = int(line)
        values.append(value)
        freq += value
        if (freq in seen):
            print("Part 2 answer: %d" % freq)
            return
        seen.add(freq)

    while 1:
        for v in values:
            freq += v
            if (freq in seen):
                print("Part 2 answer: %d" % freq)
                return
            seen.add(freq)


if __name__ == "__main__":
    part1()
    part2()
