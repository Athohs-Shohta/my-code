#!/usr/bin/env python3

'''Welcome to my Secret Santa Generator'''

import asciiart

#this code is for a Secret Santa generator
print('Welcome to my Secret Santa Generator!!!', asciiart.Snowflake)

#This represents the number of people who are in the list
number = ""
while type(number) is not int:
    number = input('How many people will be in this list?\n---->')
    try:
        number = int(number)
    except:
        print("\nPlease enter a number. Do not use letters or special characters.\n")

    #this is a list of names created
name_list = []

#this is the input of names for the generator
for _ in range(int(number)):
    name_list.append(input('\nPlease input name below:\n---->'))

print(f'\nSee the name below for the Secret Santa!\n')

#this randomizes the original input
import random

shuffled_list = sorted(name_list, key=lambda x: random.random())

print("Original list:\n", name_list)
print("Shuffled list:\n", shuffled_list)

#Days till christmas in code quiz

#this represents the days till christmas
import datetime
today = datetime.date.today()
someday = datetime.date(2024, 12, 25)
diff = someday - today
diff.days

#this is the loop that checks users input to answer
round = 0
answer = " "

while round < 3 and answer != diff.days:
    round += 1     # increase the round counter by 1
    answer = int(input('\nHow many days till Christmas?\n---->'))
    if answer == int(diff.days): # logic to check if user gave correct answer
        print(f'\nCorrect! There are {diff.days} days til christmas!!!\nGet them presents ASAP!!!')
        print(asciiart.Merry)
    elif round == 3:    # logic to ensure round has not yet reached 3
        print(f'\nNot correct, womp womp. There are {diff.days} days till Christmas!!!\nGet them presents ASAP!!!')
    else:                 # if answer was wrong
        print("Womp Womp, try again.")
