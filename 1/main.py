with open("input.txt") as file:
    data = file.readlines()


def find_first(input_data):
    for x in input_data:
        first = int(x.strip())
        for y in input_data:
            second = int(y.strip())
            result = first + second
            if result == 2020:
                print(f'Result: {first} and {second}')
                multi = first * second
                return multi


def find_second(input_data):
    for x in input_data:
        first = int(x.strip())
        for y in input_data:
            second = int(y.strip())
            for z in input_data:
                third = int(z.strip())
                result = first + second + third
                if result == 2020:
                    print(f'Result: {first}, {second} and {third}')
                    multi = first * second * third
                    return multi


# simple bruteforce solution
first_answer = find_first(data)
print(f'First answer: {first_answer}')
second_answer = find_second(data)
print(f'Second answer: {second_answer}')
