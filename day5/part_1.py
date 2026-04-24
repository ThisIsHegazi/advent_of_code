def get_range_id(file: str) -> tuple[list, list]:
    with open(file) as f:
        lines = f.readlines()
        ranges = []
        id_list = []
        ids = False
        for i in lines:
            if i == "\n":
                ids = True
                continue
            if ids:
                id_list.append(i[:-1])
            else:
                ranges.append(i[:-1])
    return id_list, ranges


def check_fresh(id_list, ranges: list[str]):
    total_fresh = 0
    for i in id_list:
        for r in ranges:
            range_start, range_end = r.split("-")
            range_start = int(range_start)
            range_end = int(range_end)
            if int(i) >= range_start and int(i) <= range_end:
                total_fresh += 1
                break
    return total_fresh


i_list, r_list = get_range_id("day5/input.txt")
print(check_fresh(i_list, r_list))
