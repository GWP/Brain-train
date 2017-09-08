import random
from collections import defaultdict
from app.math_teasers.util import generate_numbers


def addprob(difficulty):
    difficulty = int(difficulty)
    a = random.randint(-100*10**difficulty, 100*10**difficulty)
    b = random.randint(-100*10**difficulty, 100*10**difficulty)
    question = "{} + {}\n".format(a, b)
    answer = float(a + b)
    return question, answer

def generate_hex_problem(difficulty):
    hexmap = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    direction = random.random()
    if direction > 0.5:
        num = "".join([hexmap[random.randint(0, 15)] for _ in range(difficulty)])
        target_type = "decimal"
        power = len(num) - 1
        correct = 0
        for c in num:
            increase = hexmap.index(c) * 16 ** power
            correct = correct + increase
            power = power - 1
    else:
        num = random.randint(0, 10 ** (difficulty + 1))
        tempnum = num
        target_type = "hexadecimal"
        correct = ''
        while tempnum / 16 >= 1:
            rem = int(tempnum % 16)
            correct = hexmap[rem] + correct
            tempnum = tempnum // 16
        correct = hexmap[tempnum] + correct

    return num, target_type, correct


def generate_problem(problem, difficulty):
    problem_map = {
        'add': Add_Problem(difficulty),
        'sub': Sub_Problem(difficulty),
        'mult': Mult_Problem(difficulty),
        'div': Div_Problem(difficulty),
    }
    problem_map_defaulted = defaultdict(lambda: None, problem_map)

    return problem_map_defaulted[problem]


class Problem:
    def __init__(self, difficulty):
        self.difficulty = int(difficulty)


class Add_Problem(Problem):
    def __init__(self, difficulty):
        Problem.__init__(self, difficulty)
        self.first_operand, self.second_operand = generate_numbers('add', self.difficulty)
        self.question = "{} + {}\n".format(self.first_operand, self.second_operand)
        self.operator = '+'
        self.answer = float(self.first_operand + self.second_operand)

class Sub_Problem(Problem):
    def __init__(self, difficulty):
        Problem.__init__(self, difficulty)
        self.first_operand, self.second_operand = generate_numbers('sub', self.difficulty)
        self.question = "{} - {}\n".format(self.first_operand, self.second_operand)
        self.operator = '-'
        self.answer = float(self.first_operand - self.second_operand)

class Mult_Problem(Problem):
    def __init__(self, difficulty):
        Problem.__init__(self, difficulty)
        self.first_operand, self.second_operand = generate_numbers('mult', self.difficulty)
        self.question = "{} * {}\n".format(self.first_operand, self.second_operand)
        self.operator = '*'
        self.answer = float(self.first_operand * self.second_operand)

class Div_Problem(Problem):
    def __init__(self, difficulty):
        Problem.__init__(self, difficulty)
        self.first_operand, self.second_operand = generate_numbers('div', self.difficulty)
        self.question = "{} / {}\n".format(self.first_operand, self.second_operand)
        self.operator = '/'
        self.answer = round(self.first_operand / self.second_operand, 4)

class Hex_Problem(Problem):
    def __init__(self, difficulty):
        Problem.__init__(self, difficulty)
        self.first_operand, self.target_type, self.answer = generate_hex_problem(self.difficulty)
        self.question = "Convert {} to {}\n".format(self.first_operand, self.target_type)

        # attempt = int(inputu) if direction > 0.5 else str(inputu).upper()





