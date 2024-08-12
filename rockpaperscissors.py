'''
This Code is for Rock-Paper-Scissors Game.
'''
# import random module
import random
# print multiline instruction
# performstring concatenation of string
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # take the input from user
    choice = int(input("Enter your choice :"))

    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please'))

    # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        CHOICE_NAME = 'Rock'
    elif choice == 2:
        CHOICE_NAME = 'Paper'
    else:
        CHOICE_NAME = 'Scissors'

    # print user choice
    print('User choice is \n', CHOICE_NAME)
    print('Now its Computers Turn....')

    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        COMP_CHOICE_NAME = 'RocK'
    elif comp_choice == 2:
        COMP_CHOICE_NAME = 'Paper'
    else:
        COMP_CHOICE_NAME = 'Scissors'
    print("Computer choice is \n", COMP_CHOICE_NAME)
    print(CHOICE_NAME, 'Vs', COMP_CHOICE_NAME)
    # we need to check of a draw
    if choice == comp_choice:
        print('Its a Draw', end="")
        RESULT = "DRAW"
    # condition for winning
    if (choice == 1 and comp_choice == 2):
        print('paper wins =>', end="")
        RESULT = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>', end="")
        RESULT = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins =>\n', end="")
        RESULT = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins =>\n', end="")
        RESULT = 'RocK'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins =>', end="")
        RESULT = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins =>', end="")
        RESULT = 'Rock'
    # Printing either user or computer wins or draw
    if RESULT == 'DRAW':
        print("<== Its a tie ==>")
    if RESULT == CHOICE_NAME:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")
    # if user input n or N then condition is True
    ans = input().lower()
    if ans == 'n':
        break
# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")
