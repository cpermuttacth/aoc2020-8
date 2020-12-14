import numpy
from scipy.ndimage.interpolation import rotate

with open("test.txt") as file:
    file = file.read().splitlines()
    file = [(i[0], int(i[1:])) for i in file]


def first_answer(input_data):
    directions = {
        "N": numpy.array([-1, 0]),
        "S": numpy.array([1, 0]),
        "W": numpy.array([0, -1]),
        "E": numpy.array([0, 1])
    }
    turnings = {
        "N": ("E", "S", "W"),
        "S": ("W", "N", "E"),
        "W": ("N", "E", "S"),
        "E": ("S", "W", "N"),
    }
    heading = "E"
    position = numpy.array([0, 0])
    for item in input_data:
        action = item[0]
        value = item[1]
        if action in ["N", "S", "W", "E"]:
            movement = numpy.multiply(directions[action], value)
            position = numpy.add(position, movement)
        elif action == "F":
            movement = numpy.multiply(directions[heading], value)
            position = numpy.add(position, movement)
        else:
            radius = int(value / 90 - 1)
            if action == "R":
                heading = turnings[heading][radius]
            else:
                # fix heading direction
                radius = 2 if radius == 0 else 0 if radius == 2 else 1
                heading = turnings[heading][radius]

    return abs(position[0]) + abs(position[1])


def second_answer(input_data):
    # change in position system
    directions = {
        "N": numpy.array([0, 1]),
        "S": numpy.array([0, -1]),
        "W": numpy.array([1, 0]),
        "E": numpy.array([-1, 0])
    }
    # for matrix rotations
    turnings = {
        90: {
            "R": numpy.array([[0, -1], [1, 0]]),
            "L": numpy.array([[0, 1], [-1, 0]])
        },
        180: {
            "R": numpy.array([[-1, 0], [0, -1]]),
            "L": numpy.array([[-1, 0], [0, 1]])
        },
        270: {
            "R": numpy.array([[0, 1], [-1, 0]]),
            "L": numpy.array([[0, -1], [-1, 0]])
        }
    }
    position = numpy.array([0, 0])
    waypoint = numpy.array([10, 1])
    for item in input_data:
        action = item[0]
        value = item[1]
        if action in ["N", "S", "W", "E"]:
            movement = numpy.multiply(directions[action], value)
            waypoint = numpy.add(waypoint, movement)
        elif action == "F":
            movement = numpy.multiply(waypoint, value)
            position = numpy.add(position, movement)
        else:
            nulled_position = numpy.array([[0, 0], numpy.subtract(waypoint, position)])
            waypoint = numpy.dot(nulled_position, turnings[value][action])[1]
            waypoint = numpy.add(waypoint, position)
        position = position
    return position, waypoint


print(f'First answer: {first_answer(file)}')
print(f'Second answer: {second_answer(file)}')
