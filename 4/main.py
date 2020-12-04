from itertools import groupby
import re

with open("input.txt") as file:
    data = file.read().splitlines()

# make sure there's no excess newlines
data = [list(y) for x, y in groupby(data, lambda z: z == "") if not x]
data = list(map(lambda x: " ".join(x), data))
# split strings into lists
data = list(map(lambda x: x.split(" "), data))
# split strings inside the lists into dicts
data = list(map(lambda z: dict(x.split(":") for x in z), data))
# remove 'cid' from dicts
data = list(map(lambda x: {k: v for k, v in x.items() if k != 'cid'}, data))


def first_answer(input_data):
    counter = 0
    required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    for item in input_data:
        if all(x in item for x in required_keys):
            counter += 1
    return counter


def second_answer(input_data):
    counter = 0
    required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    for item in input_data:
        if all(x in item for x in required_keys) \
                and 1920 <= int(item["byr"]) <= 2002 \
                and 2010 <= int(item["iyr"]) <= 2020 \
                and 2020 <= int(item["eyr"]) <= 2030 \
                and ((150 <= int(re.sub(r"\D", "", item["hgt"])) <= 193 and "cm" in item["hgt"])
                     or (59 <= int(re.sub(r"\D", "", item["hgt"])) <= 76 and "in" in item["hgt"])) \
                and bool(re.search("#[a-f0-9]{6}$", item["hcl"])) \
                and item["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth") \
                and bool(re.search(r"^[\d]{9}$", item["pid"])):
            counter += 1
    return counter


print(f'First answer: {first_answer(data)}')
print(f'Second answer: {second_answer(data)}')
