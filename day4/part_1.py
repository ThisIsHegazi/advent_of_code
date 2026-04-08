with open("./input.txt") as f:
    lines = f.readlines()
    no_of_lines = len(lines)
    no_of_chars = len(lines[0].strip())


def main():
    access_points = 0
    loop = 0
    for line_ndx in range(no_of_lines):
        for char_ndx in range(no_of_chars):
            if lines[line_ndx][char_ndx] == "@":
                neighbors = get_neighbors(line_ndx, char_ndx, no_of_lines, no_of_chars)
                if neighbors < 4:
                    access_points += 1
    print(access_points)


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
