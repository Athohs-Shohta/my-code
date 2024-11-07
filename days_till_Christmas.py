#Days till christmas in code quiz

#this represents the days till christmas
import datetime
today = datetime.date.today()
someday = datetime.date(2024, 12, 25)
diff = someday - today
diff.days

#this changes it into an interger
diff = int(diff.days)

#this changes the user input to an interger
days_guess = int(input('\nHow many days till christmas?\n'))

#this challenges the user for the correct answer of 49
if days_guess == diff:
    print(f'\nCorrect! There are {diff} days til christmas!!!\nGet them presents ASAP!!!')
else:
    print(f'\nNot correct, womp womp. There are {diff} days till Christmas!!!\nGet them presents ASAP!!!')
