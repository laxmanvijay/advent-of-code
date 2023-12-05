import re

with open('input.txt', 'r') as f:
    inp = f.readlines()

    found_digit = 0

    nums = "one two three four five six seven eight nine".split()
    regex = "(?=(" + "|".join(nums) + "|\\d))"

    def replaceWords(val: str):
        if val in nums:
            return str(nums.index(val) + 1)
        return val

    for calib_val in inp:
        resp = list(map(replaceWords, re.findall(regex, calib_val)))
        first_dig = resp[0]
        last_dig = resp[-1]

        str_dig = str(first_dig) + str(last_dig)

        found_digit += int(str_dig)

    print(found_digit)

