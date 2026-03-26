def main():
    reserve = 1
    with open("input_nums.txt") as file:
        numbers = file.readlines()
        result = 0
        for num in numbers:
            num = num.replace("\n", "")
            largest_tenth, num_index = get_largest_num(num[:-reserve])
            largest_ones, _ = get_largest_num(num[num_index + reserve :])
            result += (largest_tenth * 10) + largest_ones
        print(f"result => {result}")


def get_largest_num(st: str):
    current_largest = int(st[0])
    for ch in st:
        if int(ch) > current_largest:
            current_largest = int(ch)
    largest_num_index = st.index(str(current_largest))
    return current_largest, largest_num_index


if __name__ == "__main__":
    main()


# correct answer: 17330
