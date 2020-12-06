with open("input.txt") as file:
    data = file.read().split("\n\n")


def first_answer(input_data):
    output = []
    for item in input_data:
        # remove newlines
        answers = item.replace("\n", "")
        unique = set(answers)
        output.append(len(unique))
    return sum(output)


def second_answer(input_data):
    output = []
    for item in input_data:
        counter = 0
        answers = item.replace("\n", "")
        number_of_answers = len(item.split("\n"))
        unique = list(set(answers))
        for char in unique:
            if answers.count(char) == number_of_answers:
                counter += 1
        output.append(counter)
    return sum(output)


print(f'First answed: {first_answer(data)}')
print(f'Second answer: {second_answer(data)}')
