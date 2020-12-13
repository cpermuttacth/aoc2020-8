import copy

with open("input.txt") as file:
    file = file.read().splitlines()


class Computer:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.accumulator = 0
        self.input_row = None
        self.step_counter = 0

    def step(self):
        self.step_counter += 1
        if 0 <= self.index < len(self.data):
            self.process_code()
        return {"input_row": self.input_row, "accumulator": self.accumulator,
                "index": self.index, "steps": self.step_counter}

    def process_code(self):
        self.input_row = self.data[self.index]
        instruction, value = self.parse_input()
        if instruction == "acc":
            self.instruction_acc(value)
        elif instruction == "jmp":
            self.instruction_jmp(value)
        elif instruction == "nop":
            self.instrcution_nop()
        else:
            print("PARSING ERROR!")
            print(self.index, self.accumulator, self.input_row)
            quit()

    def instruction_acc(self, value):
        self.accumulator += value
        self.index += 1

    def instruction_jmp(self, value):
        self.index += value

    def instrcution_nop(self):
        self.index += 1

    def parse_input(self):
        instruction, value = self.input_row.split(" ")
        value = (lambda x, y: y if x == "+" else -y)(value[0:1], int(value[1:]))
        return instruction, value


def first_answer(input_data):
    computer = Computer(input_data)
    used_rows = []
    while True:
        output = computer.step()
        used_rows.append(output["index"])
        if len(used_rows) != len(set(used_rows)):
            break
    del computer
    return output["accumulator"]


def second_answer(input_data):

    results = []
    for i, row in enumerate(input_data):
        input_copy = copy.deepcopy(input_data)
        # switch jmp to nop or nop to jmp
        if "jmp" in row:
            input_copy[i] = row.replace("jmp", "nop")
        elif "nop" in row:
            input_copy[i] = row.replace("nop", "jmp")
        else:
            continue
        computer = Computer(input_copy)
        used_rows = []
        while True:
            output = computer.step()
            used_rows.append(output["index"])
            if output["index"] >= len(input_copy):
                results.append(output["accumulator"])
                break
            if len(used_rows) > len(input_copy):
                break
        del computer
    return set(results)


print(f'First answer: {first_answer(file)}')
print(f'Second answer: {second_answer(file)}')  # arvatut 7
