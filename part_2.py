def main():

    reserve = 1
    with open("input_nums.txt") as file:
        numbers = file.readlines()
        result = 0
        for num in numbers:
            num = num.replace("\n", "")
            num_result = get_largest_reserve(num)
            result += num_result
        print(f"result => {result}")


def get_largest_reserve(st: str):
    reserve = 11
    highest_ndx = 0
    st_len = len(st)
    result = 0
    while reserve > -1:
        if reserve == 0:
            largest_num, largest_n_ndx = get_largest_num(st[highest_ndx:], highest_ndx)
        else:
            largest_num, largest_n_ndx = get_largest_num(
                st[highest_ndx:-reserve], highest_ndx
            )
        result += largest_num * (10**reserve)
        highest_ndx = largest_n_ndx + 1
        reserve -= 1
    return result


def get_largest_num(st: str, ndx):
    current_largest = int(st[0])
    for ch in st:
        if int(ch) > current_largest:
            current_largest = int(ch)
    largest_num_index = st.index(str(current_largest))
    return current_largest, largest_num_index + ndx


if __name__ == "__main__":
    main()


# correct answer: 171518260283767
