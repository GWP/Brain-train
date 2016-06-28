#!/usr/bin/python


import os
import sys
import random

def addprob(difficulty):
        a = random.randint(-100*10**difficulty, 100*10**difficulty)
    b = random.randint(-100*10**difficulty, 100*10**difficulty)
    attempt = float(raw_input("{} + {}\n".format(a,b)))
    while attempt != a + b:
        print "incorrect, try again"
        attempt = float(raw_input("{} + {}\n".format(a,b)))
    print "correct!"

def subtractprob(difficulty):
        a = random.randint(-100*10**difficulty, 100*10**difficulty)
    b = random.randint(-100*10**difficulty, 100*10**difficulty)
        attempt = float(raw_input("{} - {}\n".format(a,b)))
    while attempt != a - b:
        print "incorrect, try again"
        attempt = float(raw_input("{} - {}\n".format(a,b)))
    print "correct!"

def multprob(difficulty):
    a = round(random.random()*10*difficulty, 0)
    b = round(random.random()*10*difficulty, 0)
    attempt = float(raw_input("{} * {}\n".format(a,b)))
    while attempt != round(a * b, 4):
        print "incorrect, try again"
        attempt = float(raw_input("{} * {}\n".format(a,b)))
    print "correct!"

def divprob(difficulty):
    a = round(random.random()*10*difficulty, 0)
    b = round(random.random()*10*difficulty, 0)
    attempt = float(raw_input("{} / {}\n".format(a,b)))
    while attempt != round(a / b, 4):
        print "incorrect, try again"
        attempt = float(raw_input("{} / {}\n".format(a,b)))
    print "correct!"

#def probprob():

#def percentageprob():

def hexprob(difficulty):
    hexmap = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E']
    power = len(hexnum)-1
    direction = random.random()
    if direction > 0.5:
        num = "".join([hexmap[random.randint(0,16)] for i in range(difficulty)])
        b = "decimal"
        correct = 0
        for d in hexnum.items():
            increase = hexmap.index(d) * 16 ** power
            correct = correct + increase
            power = power - 1
    else:
        num = random.random()*10*difficulty
        b = "hexadecimal"
        correct = ''
        while num / 16 >= 1:
            rem = num % 16
            correct = correct + hexmap[rem]
            num = num // 16
    inputu = raw_input("Convert {} to {}\n".format(num,b))
    attempt = [int(inputu) if direction > 0.5 else str(inputu)]
    while attempt != correct:
        print "incorrect, try again"
        inputu = raw_input("Convert {} to {}\n".format(num,b))
        attempt = [int(inputu) if direction > 0.5 else str(inputu)]














if __name__ == "__main__":
    difficulty = int(sys.argv[2])
    if sys.argv[1] == "set":
        addprob(difficulty)
        subtractprob(difficulty)
        multprob(difficulty)
        divprob(difficulty)





