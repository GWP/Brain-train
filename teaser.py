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

if __name__ == "__main__":
	difficulty = int(sys.argv[2])
	if sys.argv[1] == "set":
		addprob(difficulty)
		subtractprob(difficulty)
		multprob(difficulty)
		divprob(difficulty)
		
