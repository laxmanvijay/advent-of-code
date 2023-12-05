with open('input.txt', 'r') as f:
    inp = f.readlines()

    found_digit = 0

    for calib_val in inp:
        temp = [int(r) for r in calib_val if r.isdigit()]
        first_dig = temp[0]
        last_dig = temp[-1]

        str_dig = str(first_dig) + str(last_dig)

        found_digit += int(str_dig)

    print(found_digit)

