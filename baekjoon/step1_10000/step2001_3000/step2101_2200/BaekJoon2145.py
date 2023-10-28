result_list = []

while True:
    num_str = input()
    total = num_str

    if num_str == "0": break

    while True:
        total = str(total)
        digit_sum = sum(map(int, total))

        if digit_sum < 10:
            result_list.append(str(digit_sum)+"\n")
            break
        else:
            total = digit_sum

print("".join(result_list))