with open("input.txt") as file:
    data = file.read().splitlines()


def first_answer(input_data):
    id_list = []
    for item in input_data:
        row, column = [0, 127], [0, 7]
        seat_input = list(item)
        # find out row and column
        for x in seat_input:
            distance_row = abs(row[0] - row[1]) / 2
            distance_column = abs(column[0] - column[1]) / 2
            if x == "F":
                row = [row[0], row[1] - distance_row]
            elif x == "B":
                row = [row[0] + distance_row, row[1]]
            elif x == "L":
                column = [column[0], column[1] - distance_column]
            elif x == "R":
                column = [column[0] + distance_column, column[1]]
        row = int(row[1])
        column = int(column[1])
        id_list.append(row * 8 + column)
    return max(id_list)


def second_answer(input_data):
    id_list = []
    for item in input_data:
        row, column = [0, 127], [0, 7]
        seat_input = list(item)
        # find out row and column
        for x in seat_input:
            distance_row = abs(row[0] - row[1]) / 2
            distance_column = abs(column[0] - column[1]) / 2
            if x == "F":
                row = [row[0], row[1] - distance_row]
            elif x == "B":
                row = [row[0] + distance_row, row[1]]
            elif x == "L":
                column = [column[0], column[1] - distance_column]
            elif x == "R":
                column = [column[0] + distance_column, column[1]]
        row = int(row[1])
        column = int(column[1])
        # remove seats from first and last row
        if 127 > row > 0:
            id_list.append(row * 8 + column)
    id_list.sort()
    # find the missing number
    seat_id = [x for x in range(id_list[0], id_list[-1] + 1) if x not in id_list][0]
    return seat_id


print(f'First answer: {first_answer(data)}')
print(f'Second answer: {second_answer(data)}')
