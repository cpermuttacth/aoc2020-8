with open("input.txt") as file:
    data = file.readlines()


def first_answer(input_data):
    valid_passwords = 0
    for item in input_data:
        split_line = (item.strip()).split(" ")
        minimum, maximum = split_line[0].split("-")
        required = split_line[1].strip(":")
        password = split_line[2]
        number_or_required_chars = password.count(required)
        if int(minimum) <= number_or_required_chars <= int(maximum):
            valid_passwords += 1
    return valid_passwords


def second_answer(input_data):
    valid_passwords = 0
    for item in input_data:
        split_line = (item.strip()).split(" ")
        first, second = split_line[0].split("-")
        required = split_line[1].strip(":")
        password = split_line[2]
        required_locations = [index + 1 for index, char in enumerate(password) if char == required]
        if (int(first) in required_locations) != (int(second) in required_locations):
            valid_passwords += 1
    return valid_passwords


print(f'First answer: {first_answer(data)}')
print(f'Second answer: {second_answer(data)}')
