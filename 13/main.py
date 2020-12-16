from functools import reduce
from math import gcd

with open("input.txt") as file:
    file = file.read().splitlines()
    time = int(file[0])
    buses = tuple(file[1].split(","))
    file = (time, buses)


def first_answer(input_data):
    earliest_possible_time = input_data[0]
    # store wait time and bus id
    earliest_time = [None, None]
    for item in input_data[1]:
        if item == "x":
            continue
        departure_time = earliest_possible_time // int(item) * int(item) + int(item)
        if earliest_time[0] is None:
            earliest_time[0] = departure_time
            earliest_time[1] = int(item)
        if departure_time < earliest_time[0]:
            earliest_time[0] = departure_time
            earliest_time[1] = int(item)
    result = (earliest_time[0] - earliest_possible_time) * earliest_time[1]
    return result


def second_answer(input_data):
    return input_data


def find_smallest_common_denominator(pattern):
    return reduce(lambda a, b: a * b // gcd(a, b), pattern)


print(f'First answer: {first_answer(file)}')
print(f'Second answer: {second_answer(file[1])}')
