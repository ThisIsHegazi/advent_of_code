with open("./input.txt") as f:
    lines = f.readlines()
    no_of_lines = len(lines)
    no_of_chars = len(lines[0].strip())


def main():
    total_access = 0
    while True:
        once_access = 0

        for line_ndx in range(no_of_lines):
            new_line = []

            for char_ndx in range(no_of_chars):

                if lines[line_ndx][char_ndx] == "@":
                    neighbors = get_neighbors(
                        line_ndx, char_ndx, no_of_lines, no_of_chars
                    )

                    if neighbors < 4:
                        once_access += 1
                        new_line.append(".")

                    else:
                        new_line.append(lines[line_ndx][char_ndx])

                else:
                    new_line.append(lines[line_ndx][char_ndx])

            new_line.append("\n")

            str_new_line = "".join(new_line)
            lines[line_ndx] = str_new_line
        total_access += once_access
        if once_access == 0:
            break
    print(total_access)


def get_neighbors(line_ndx, char_ndx, lines_count, char_count):
    line_ne, char_ne = determine_lines_neighbors(
        line_ndx, char_ndx, lines_count, char_count
    )
    result = 0
    for i in line_ne:
        for j in char_ne:
            if i == j == 0:
                continue
            if lines[line_ndx + i][char_ndx + j] == "@":
                result += 1
    return result


def determine_lines_neighbors(line_ndx, char_ndx, lines_count, chars_count):

    if line_ndx == 0:
        lines = [0, 1]
    elif line_ndx == (lines_count - 1):
        lines = [-1, 0]
    else:
        lines = [-1, 1, 0]

    if char_ndx == 0:
        chars = [0, 1]
    elif char_ndx == (chars_count - 1):
        chars = [-1, 0]
    else:
        chars = [-1, 1, 0]
    return lines, chars


if __name__ == "__main__":
    main()
