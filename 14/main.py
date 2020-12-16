import itertools
import re

with open("input.txt") as file:
    file = file.read().splitlines()


def first_answer(input_data):
    data = {}
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for item in input_data:
        if "mask" in item:
            mask = parse_input(item)
            continue
        address, value = parse_input(item)
        # apply mask to value
        value = list(value)
        for i, bit in enumerate(value):
            if mask[i] != "X":
                value[i] = mask[i]
        # change value back to 10 base
        value = int("".join(value), 2)
        data.update({address: value})

    total_sum = sum(data.values())
    return total_sum


def second_answer(input_data):
    data = {}
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    for item in input_data:
        if "mask" in item:
            mask = parse_input(item)
            continue
        address, value = parse_input(item)
        # change address to 2 base
        address = format(address, '036b')
        # apply mask to address
        address = list(address)
        # first apply ones from the mask
        for i, bit in enumerate(address):
            if mask[i] == "1":
                address[i] = "1"
        # generate all binary combinations for n amount of bits
        binary_combinations = [list(i) for i in itertools.product(['0', '1'], repeat=mask.count("X"))]
        # apply all combinations into value and add them to data list
        mask = list(mask)
        for floating_value in binary_combinations:
            for i, bit in enumerate(mask):
                if bit == "X":
                    address[i] = floating_value[0]
                    floating_value.pop(0)
            data.update({int("".join(address), 2): int(value, 2)})
    total_sum = sum(data.values())
    return total_sum


def parse_input(input_line):
    if "mask" in input_line:
        return input_line.split("= ")[1]
    else:
        divided = input_line.split(" = ")
        address = int(re.search(r'\d+', divided[0]).group())
        value = int(divided[1])
        return address, format(value, '036b')


print(f'First answer: {first_answer(file)}')
print(f'Second answer: {second_answer(file)}')
