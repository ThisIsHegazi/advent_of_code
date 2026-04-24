def get_ranges(file: str):
    with open(file) as f:
        lines = f.readlines()
        ranges = []
        ids = False
        for i in lines:
            if i == "\n":
                ids = True
                continue
            if not ids:
                start = int(i.split("-")[0])
                end = int(i.split("-")[1][:-1])
                ranges.append([start, end])
        ranges.sort(key=lambda x: x[0])
    return ranges


def check_overlap(ranges):
    new_ranges = [ranges[0]]
    for i in range(1, len(ranges)):
        for j in range(len(new_ranges)):
            if ranges[i][0] > new_ranges[j][1] or ranges[i][1] < new_ranges[j][0]:
                if j == len(new_ranges) - 1:
                    new_ranges.append(ranges[i])
                continue
            new_ranges[j] = [
                min(ranges[i][0], new_ranges[j][0]),
                max(ranges[i][1], new_ranges[j][1]),
            ]
    return new_ranges


def get_total_fresh(ranges):
    total_fresh = 0
    for i in ranges:
        total_fresh += i[1] - i[0] + 1
    return total_fresh


overlap_handled = check_overlap(get_ranges("day5/input.txt"))
print(get_total_fresh(overlap_handled))
