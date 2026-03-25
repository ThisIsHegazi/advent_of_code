def main():
    with open("products_id.txt") as f:
        ranges = f.read()
        range_list = ranges.split(",")
        invalid_ids = []

        for rng in range_list:
            # getting every range
            split_rng = rng.split("-")
            start, end = split_rng[0], split_rng[1]
            int_start, int_end = int(start), int(end)
            current = int_start
            # looping over ranges
            while current <= int_end:
                if is_invalid(str(current)):
                    invalid_ids.append(current)
                current += 1
        print(sum(invalid_ids))


# to get all divisors of possible length of inputs( <= 10)
# to have all possible length of parts of number
divisors = {
    4: [2, 4],
    6: [2, 3, 6],
    8: [2, 4, 8],
    9: [3, 9],
    10: [2, 5, 10],
}
# if length of number is prime then the only way to be invalid is to be only one number repeated
primes = {2, 3, 5, 7}


def split_compare(s, n):
    # split every number to all possible parts and compare those parts if equal
    if len(s) % n != 0:
        return f"String length is not divisible by {n}"
    part_length = len(s) // n
    parts = [s[i : i + part_length] for i in range(0, len(s), part_length)]
    equal_parts = all(parts[0] == i for i in parts)
    return equal_parts


def is_invalid(n: str):
    len_n = len(n)
    # number with len of 1 is always valid
    if len_n == 1:
        return False
    # number with prime len have to be of the same number repeated to be invalid
    if len_n in primes:
        if n.count(n[0]) == len(n):
            return True
        return False
    # getting the divisors to get the possible parts and compare
    len_divisors = divisors[len_n]
    for i in len_divisors:
        if split_compare(n, i):
            return True
    return False


if __name__ == "__main__":
    main()

# correct answer: 79183223243
