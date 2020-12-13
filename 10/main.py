import copy
from functools import reduce

with open("test.txt") as file:
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
            data["ones"] = data["ones"] + 1
        elif abs(item - input_data[i + 1]) == 3:
            data["threes"] = data["threes"] + 1
    return data["ones"] * data["threes"]


def second_answer(input_data):
    # add starting point 0
    input_data.append(0)
    # sort list in number order
    input_data.sort()
    # add device adapter in
    input_data.append(max(input_data) + 3)
    possible_combinations = []
    print(input_data)
    for i, item in enumerate(input_data):
        combination = []
        counter = 2
        if i >= len(input_data) - 1:
            break
        if input_data[i + 1] == item + 1:
            start = i
            end = None
            while input_data[i + counter] == item + counter:
                end = i + counter
                counter += 1
            if end is not None:
                combination.append(input_data[start:end + 1])
                possible_combinations.append(combination[0])
    print(possible_combinations)
    possible_combinations = [4 if len(x) == 4 else 2 for x in possible_combinations]
    return_value = reduce(lambda x, y: x * y, possible_combinations)
    return return_value, possible_combinations


print(f'First answer: {first_answer(copy.deepcopy(file))}')
print(f'Second answer: {second_answer(file)}')
