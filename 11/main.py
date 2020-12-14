import copy
import numpy

with open("input.txt") as file:
    file = file.read().splitlines()
    file = [list(i) for i in file]


def first_answer(input_data):
    directions = {
        "n": numpy.array([-1, 0]),
        "s": numpy.array([1, 0]),
        "w": numpy.array([0, -1]),
        "e": numpy.array([0, 1]),
        "nw": numpy.array([-1, -1]),
        "ne": numpy.array([-1, 1]),
        "sw": numpy.array([1, -1]),
        "se": numpy.array([1, 1]),
    }

    input_copy = None
    while input_data != input_copy:
        input_copy = copy.deepcopy(input_data)
        for i, row in enumerate(input_copy):
            for j, item in enumerate(row):
                position = numpy.array([i, j])
                # skip floor
                if input_copy[i][j] == ".":
                    continue
                seat_taken = True if input_copy[i][j] == "#" else False
                occupied = 0
                for direction in directions.values():
                    adjacent = numpy.add(position, direction)
                    # check if the direction is legal
                    if 0 <= adjacent[0] < len(input_copy) and 0 <= adjacent[1] < len(row):
                        seat_status = input_copy[adjacent[0]][adjacent[1]]
                        if seat_status == "#":
                            occupied += 1
                if seat_taken and occupied >= 4:
                    input_data[i][j] = "L"
                elif not seat_taken and occupied == 0:
                    input_data[i][j] = "#"
    return sum(x.count("#") for x in input_data)


def second_answer(input_data):
    directions = {
        "n": numpy.array([-1, 0]),
        "s": numpy.array([1, 0]),
        "w": numpy.array([0, -1]),
        "e": numpy.array([0, 1]),
        "nw": numpy.array([-1, -1]),
        "ne": numpy.array([-1, 1]),
        "sw": numpy.array([1, -1]),
        "se": numpy.array([1, 1]),
    }

    input_copy = None
    while input_data != input_copy:
        input_copy = copy.deepcopy(input_data)
        for i, row in enumerate(input_copy):
            for j, item in enumerate(row):
                position = numpy.array([i, j])
                # skip floor
                if input_copy[i][j] == ".":
                    continue
                seat_taken = True if input_copy[i][j] == "#" else False
                occupied = 0
                for direction in directions.values():
                    adjacent = numpy.add(position, direction)
                    # keep going into same direction until we hit wall or a seat
                    while True:
                        if 0 <= adjacent[0] < len(input_copy) and 0 <= adjacent[1] < len(row):
                            if input_copy[adjacent[0]][adjacent[1]] == "#":
                                occupied += 1
                                break
                            elif input_copy[adjacent[0]][adjacent[1]] == "L":
                                break
                            else:
                                adjacent = numpy.add(adjacent, direction)
                        else:
                            break
                if seat_taken and occupied >= 5:
                    input_data[i][j] = "L"
                elif not seat_taken and occupied == 0:
                    input_data[i][j] = "#"

    return sum(x.count("#") for x in input_data)


print(f'First answer: {first_answer(copy.deepcopy(file))}')
print(f'Second answer: {second_answer(file)}')
