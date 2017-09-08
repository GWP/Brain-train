import random

def is_valid_problem_input(ptype, difficulty):
    valid_types = ['add', 'sub', 'mult', 'div', 'hex', 'set']
    valid_difficulties = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    if ptype in valid_types and difficulty in valid_difficulties:
        return True
    return False

def get_digits(difficulty):
    assert type(difficulty) == int, "difficulty is not an int: {}".format(difficulty)

    dif_a = difficulty // 2 + 1
    dif_b = (difficulty - 1) // 2 + 1
    return dif_a, dif_b


def generate_numbers(ptype, difficulty):
    assert ptype in ['add', 'sub', 'mult', 'div'], "problem type is invalid: {}".format(ptype)
    assert type(difficulty) == int, "difficulty is not an int" % difficulty

    while True:
        if ptype in ['add', 'sub']:
            num1 = random.randint(-100 * 10 ** difficulty, 100 * 10 ** difficulty)
            num2 = random.randint(-100 * 10 ** difficulty, 100 * 10 ** difficulty)

        elif ptype == 'mult':
            difa, difb = get_digits(difficulty)
            num1 = round(random.random() * 10 ** difa, 0)
            num2 = round(random.random() * 10 ** difb, 0)

        elif ptype == 'div':
            diffs = get_digits(difficulty)
            difa = random.choice(diffs)
            difb = diffs[0] if difa == diffs[1] else diffs[1]
            num1 = round(random.random() * 10 ** difa, 0)
            num2 = round(random.random() * 10 ** difb, 0)

        else:
            raise Exception('Invalid problem type!')

        if num1 != 0 and num2 != 0:
            return num1, num2
