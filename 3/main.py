from functools import reduce

with open("input.txt") as file:
    data = file.read().splitlines()


def first_answer(input_data):
    slope_width = len(input_data[0])
    counter = 0
    position = 0
    for item in input_data:
        if "#" in item[position]:
            counter += 1
        position += 3
        if position >= slope_width:
            position -= slope_width
    return counter


def second_answer(input_data):
    slope_width = len(input_data[0])
    steps = [1, 3, 5, 7, 1]
    down_steps = [1, 1, 1, 1, 2]
    output = []
    for i, step in enumerate(steps):
        counter = 0
        position = 0
        for j, item in enumerate(input_data):
            if down_steps[i] == 2 and j % 2 != 0:
                continue
            if "#" in item[position]:
                counter += 1
            position += step
            if position >= slope_width:
                position -= slope_width
        output.append(counter)
    return reduce(lambda x, y: x * y, output)


print(f'First answed: {first_answer(data)}')
print(f'Second answer: {second_answer(data)}')
