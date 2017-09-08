#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3


import os
import sys
import random
import signal

def sig_term_handler(signal, frame):
    print("ta for now!")
    sys.exit(0)

signal.signal(signal.SIGTERM, sig_term_handler)

def get_digits(difficulty):
    dif_a = difficulty // 2 + 1
    dif_b = (difficulty - 1) // 2 + 1
    return dif_a, dif_b

def addprob(difficulty):
    a = random.randint(-100*10**difficulty, 100*10**difficulty)
    b = random.randint(-100*10**difficulty, 100*10**difficulty)
    attempt = float(input("{} + {}\n".format(a,b)))
    while attempt != a + b:
        print("incorrect, try again")
        attempt = float(input("{} + {}\n".format(a,b)))
    print("correct!")

def subtractprob(difficulty):
    a = random.randint(-100*10**difficulty, 100*10**difficulty)
    b = random.randint(-100*10**difficulty, 100*10**difficulty)
    attempt = float(input("{} - {}\n".format(a,b)))
    while attempt != a - b:
        print("incorrect, try again")
        attempt = float(input("{} - {}\n".format(a,b)))
    print("correct!")

def multprob(difficulty):
    difa, difb = get_digits(difficulty)
    a = round(random.random()*10**difa, 0)
    b = round(random.random()*10**difb, 0)
    attempt = float(input("{} * {}\n".format(a,b)))
    while attempt != round(a * b, 4):
        print("incorrect, try again")
        attempt = float(input("{} * {}\n".format(a,b)))
    print("correct!")

def divprob(difficulty):
    diffs = get_digits(difficulty)
    difa = random.choice(diffs)
    difb = diffs[0] if difa == diffs[1] else diffs[1]
    a = round(random.random()*10**difa, 0)
    b = round(random.random()*10**difb, 0)
    attempt = float(input("{} / {}\n".format(a,b)))
    while attempt != round(a / b, 4):
        print("incorrect, try again")
        attempt = float(input("{} / {}\n".format(a,b)))
    print("Correct!")

#def probprob():

#def percentageprob():

def hexprob(difficulty):
    hexmap = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    direction = random.random()
    if direction > 0.5:
        num = "".join([hexmap[random.randint(0,15)] for _ in range(difficulty)])
        b = "decimal"
        power = len(num)-1
        correct = 0
        for c in num:
            increase = hexmap.index(c) * 16 ** power
            correct = correct + increase
            power = power - 1

    else:
        num = random.randint(0, 10**(difficulty+1))
        tempnum = num
        b = "hexadecimal"
        correct = ''
        while tempnum / 16 >= 1:
            rem = int(tempnum % 16)
            correct = hexmap[rem] + correct
            tempnum = tempnum // 16
        correct = hexmap[tempnum] + correct

    inputu = input("Convert {} to {}\n".format(num,b))
    attempt = int(inputu) if direction > 0.5 else str(inputu).upper()
    while attempt != correct:
        print("incorrect, try again")
        inputu = input("Convert {} to {}\n".format(num,b))
        attempt = int(inputu) if direction > 0.5 else str(inputu).upper()
    print("Correct!")














if __name__ == "__main__":
    difficulty = int(sys.argv[2])
    if sys.argv[1] == "set":
        addprob(difficulty)
        subtractprob(difficulty)
        multprob(difficulty)
        divprob(difficulty)
        hexprob(difficulty)
        exit(0)





