import re
import copy

with open("input.txt") as file:
    data = file.read().splitlines()


def init_data(input_data):
    # split strings inside the lists into dicts
    input_data = dict(map(lambda x: x.split("contain"), input_data))
    # rename bags using unique names and add their 'costs'
    data_copy = copy.deepcopy(input_data)
    for key, value in data_copy.items():
        key_value = key.replace("bags", "").strip()
        input_data[key_value] = input_data.pop(key)
        item_value = value.split(",")
        items = []
        for item in item_value:
            unique_value = item.strip(".").strip("bags").strip("bag").strip(".").strip()
            items.append(unique_value)
        input_data[key_value] = items
    return input_data


def first_answer(input_data):
    valid_bags = ["shiny gold"]
    invalid_bags = [re.sub(r'\d+', '', x).strip() for x in input_data["shiny gold"]]
    input_data.pop("shiny gold")
    while len(input_data):
        lengths = (len(valid_bags), len(invalid_bags))
        input_data_copy = copy.deepcopy(input_data)
        for key, value in input_data_copy.items():
            if any(bag in valid_bags for bag in list(map(lambda x: re.sub(r'\d+', '', x).strip(), value))):
                valid_bags.append(key)
                input_data.pop(key)
            elif key in invalid_bags or 'no other' in value:
                invalid_bags.append(key)
                input_data.pop(key)
        if lengths == (len(valid_bags), len(invalid_bags)):
            break

    valid_bags = set(valid_bags)
    if "shiny gold" in valid_bags:
        valid_bags.remove("shiny gold")

    return len(valid_bags)


def second_answer(input_data):
    # drop all bags that 'shiny gold' can fit into
    input_data = {key: value for key, value in input_data.items() if not any('shiny gold' in x for x in value)}
    values = {}
    # price bags and remove them
    counter = 0
    while len(input_data) and counter < 10000:
        temp_data = copy.deepcopy(input_data)
        for key, value in temp_data.items():
            if 'no other' in value:
                values.update({key: 1})
                input_data.pop(key)
                continue
            for item in value:
                if type(item) != str:
                    continue
                name = re.sub(r'\d+', '', item).strip()
                if name not in input_data.keys() and name not in values.keys():
                    input_data.pop(key)
                    break
                if name in values.keys():
                    multiplier = int(re.search(r'\d+', item).group())
                    if values[name] == 1 and type(values[name]) == int:
                        price = values[name] * multiplier
                    else:
                        price = values[name] * multiplier + multiplier
                    input_data[key].append(price)
                    input_data[key].remove(item)
            # remove items that have their price calculated
            if all(isinstance(x, int) for x in value):
                values.update({key: sum(value)})
                input_data.pop(key)
        counter += 0
    print(len(values))
    print(values)
    return values["shiny gold"]


data = init_data(data)
print(f'First answer: {first_answer(copy.deepcopy(data))}')
print(f'Second answer: {second_answer(data)}')
