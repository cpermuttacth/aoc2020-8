with open("input.txt") as file:
    file = file.read().splitlines()


def first_answer(input_data, preample_length):
    invalid_numbers = []
    for i, item in enumerate(input_data):
        if i < preample_length:
            continue
        preample = input_data[-len(input_data) + i - preample_length:i]
        # add to invalid numbers if it's not possible to find a combination
        if min(preample) >= item / 2:
            invalid_numbers.append(item)
            continue
        # drop numbers from preample that are bigger than the number we're searching
        preample = [x for x in preample if x < item]
        if check_combinations(preample, item):
            continue
        else:
            invalid_numbers.append(item)
    return invalid_numbers[0]


def second_answer(input_data, input_value):
    possible_combinations = []
    for i in range(0, len(input_data)):
        if i > len(input_data):
            break
        combination = [input_data[i]]
        counter = 1
        while i < len(input_data) - 1:
            combination.append(input_data[i + counter])
            if sum(combination) == input_value:
                possible_combinations.append(combination)
                break
            elif sum(combination) > input_value:
                break
            counter += 1

    biggest_list = max(possible_combinations, key=len)
    return min(biggest_list) + max(biggest_list)


def check_combinations(input_data, value):
    for x in input_data:
        for y in input_data:
            if x + y == value:
                return True
    return False


file = [int(i) for i in file]
first = first_answer(file, 25)
print(f'First answer: {first}')
print(f'Second answer: {second_answer(file, first)}')
