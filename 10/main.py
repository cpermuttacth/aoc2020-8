import copy
from functools import reduce

with open("input.txt") as file:
    file = file.read().splitlines()
    file = [int(i) for i in file]


def first_answer(input_data):
    # add starting point 0
    input_data.append(0)
    # sort list in number order
    input_data.sort()
    # add device adapter in
    input_data.append(max(input_data) + 3)
    data = {"ones": 0, "threes": 0}
    for i, item in enumerate(input_data):
        if i >= len(input_data) - 1:
            break
        if abs(item - input_data[i + 1]) == 1:
            data["ones"] += 1
        elif abs(item - input_data[i + 1]) == 3:
            data["threes"] += 1
    return data["ones"] * data["threes"]


def second_answer(input_data):
    # add starting point 0
    input_data.append(0)
    # sort list in number order
    input_data.sort()
    # add device adapter in
    input_data.append(max(input_data) + 3)
    possible_combinations = []
    # divide list into sublist when there's a gap of 3
    for i, item in enumerate(input_data):
        start = i
        end = None
        counter = 1
        while i + counter <= len(input_data) - 1 \
                and (input_data[i + counter] == item + counter or input_data[i + counter] == item + counter + 1):
            end = i + counter
            counter += 1
        if end is not None:
            possible_combinations.append(input_data[start:end + 1])
            for j in range(start, end):
                input_data[j] = 0
    possible_combinations = list(filter(lambda x: len(x) > 2, possible_combinations))
    # multiplier depends on the size of sublist
    values = {3: 2, 4: 4, 5: 7}
    possible_combinations = list(map(lambda x: values[len(x)], possible_combinations))
    return reduce((lambda x, y: x * y), possible_combinations)


print(f'First answer: {first_answer(copy.deepcopy(file))}')
print(f'Second answer: {second_answer(file)}')
