#!/bin/sh

import os
import sys
from time import sleep

if len(sys.argv) != 4: print("usage: python main.py <freq> <file>"); exit()

frequency = sys.argv[len(sys.argv)-2] #hz

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","--.--","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

def play(r: str):
    if r == "\n": sleep(1.5)
    elif r == " ": sleep(0.5)
    elif r == ".":
        os.system('play -n synth %s sin %s' % (200/1000, frequency))
    elif r == "-":
        os.system('play -n synth %s sin %s' % (500/1000, frequency))

def string_to_pseudomorse(string):
    for i in range(len(letters)):
        string = string.replace(letters[i], morse[i])
    return string

text = open(sys.argv[len(sys.argv)-1],'r').read()
text = string_to_pseudomorse(text.upper())
print(text, len(letters), len(morse))

for i in range(len(text)):
    play(text[i])
