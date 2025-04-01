import random

randomNumber = random.randint(0, 100)
print("Guess a number between 1 and 100")
Guess = 0

# function for the user's guess
def guess(b):
    b = int(input("What do you think the number i57s: "))
    return b

# function to compare the random number and user's input
def comparator(a):
    b = 0
    if a < randomNumber:
        b += 1
        return b
    if a > randomNumber:
        return b
    if a == randomNumber:
        b += -1
        return b

# function to  prints the following information depending on the value of previous function 
def remark(a):
    if a == -1:
        print("You guessed it!")
    if a == 0:
        print("You guessed higher.")
    if a == 1:
        print("You guessed lower.")

# call the functions
while Guess != randomNumber:
    Guess = guess(guess)
    compare = comparator(Guess)
    answer = remark(compare)