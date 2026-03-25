def main():
    with open("products_id.txt") as f:
        ranges = f.read().split(",")
        invalid_ids = set()
        for rng in ranges:
            split_rng = rng.split("-")
            current = int(split_rng[0])
            while current <= int(split_rng[1]):
                if is_invalid(str(current)):
                    invalid_ids.add(current)
                current += 1
        print(sum(invalid_ids))


def equal_halves(s: str):
    middle = len(s) // 2
    return s[:middle] == s[middle:]


def is_invalid(n: str):
    len_n = len(n)
    # id with length of 1 cannot be invalid
    if len_n == 1:
        return False
    # in part 1 of challenge id with odd length cannot be invalid
    if len_n % 2:
        return False
    return equal_halves(n)


if __name__ == "__main__":
    main()
# correct answer: 56660955519
