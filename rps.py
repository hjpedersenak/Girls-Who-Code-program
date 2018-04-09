'''
Program by Hanna Pedersen
Rock, Paper, scissors game created for Girls Who Code 2018 Summer
Immersion Program, Teaching Assistant Position

Class letsPlay is with two randomly generated players.
Class letsPlay2 is with one user input and one randomly generated player.
'''

import random

class letsPlay:
    def __init__(self):
        self.rock = 0
        self.paper = 1
        self.scissors = 2

    # generate random num to determine rock, paper, or scissors
    def pseudoRand(self):
        pseudoRandom = random.randint(0, 2)
        return pseudoRandom

    def playRPS(self):
        ranOne = letsPlay.pseudoRand(self)
        ranTwo = letsPlay.pseudoRand(self)

        # checking for xMove
        if ranOne == 0:
            xMove = self.rock       # rock = 0
            str = 'rock'

        elif ranOne == 1:
            xMove = self.paper      # paper = 1
            str = 'paper'

        elif ranOne == 2:
            xMove = self.scissors   # scissors = 2
            str = 'scissors'

        # checking for yMove
        if ranTwo == 0:
            yMove = self.rock  # rock = 0
            str2 = 'rock'

        elif ranTwo == 1:
            yMove = self.paper  # paper = 1
            str2 = 'paper'

        elif ranTwo == 2:
            yMove = self.scissors  # scissors = 2
            str2 = 'scissors'

        print("Player 1 played: " + str)
        print("Player 2 played: " + str2)

        # logic for who wins
        if xMove == self.rock and yMove == self.rock:
            print("It's a tie!")
        elif xMove == self.rock and yMove == self.paper:
            print("Player 2 wins!")
        elif xMove == self.rock and yMove == self.scissors:
            print("Player 1 wins!")
        elif xMove == self.paper and yMove == self.rock:
            print("Player 1 wins!")
        elif xMove == self.paper and yMove == self.paper:
            print("It's a tie!")
        elif xMove == self.paper and yMove == self.scissors:
            print("Player 2 wins!")
        elif xMove == self.scissors and yMove == self.rock:
            print("Player 2 wins!")
        elif xMove == self.scissors and yMove == self.paper:
            print("Player 1 wins!")
        elif xMove == self.scissors and yMove == self.scissors:
            print("It's a tie!")

# letsPlay2 has one player as user input and one player as randomly generated
class letsPlay2:
    def __init__(self):
        self.rock = 0
        self.paper = 1
        self.scissors = 2

    # generate random num to determine rock, paper, or scissors
    def pseudoRand(self):
        pseudoRandom = random.randint(0, 2)
        return pseudoRandom

    def playRPS(self):
        #userIn = input("Choose rock, paper or scissors by entering 'r', 'p' or 's'!\n")

        check = True
        while check is True:
            userIn = input("Choose rock, paper or scissors by entering 'r', 'p' or 's'!\n")
            if userIn == 'r':
                xMove = self.rock
                str = 'rock'
                print("You played: " + str)
                break
            elif userIn =='p':
                xMove = self.paper
                str = 'paper'
                print("You played: " + str)
                break
            elif userIn == 's':
                xMove = self.scissors
                str = 'scissors'
                print("You played: " + str)
                break
            else:
                print("Incorrect input!")
                check is True

        # randomly generating yMove
        ran = letsPlay.pseudoRand(self)

        # checking for yMove
        if ran == 0:
            yMove = self.rock  # rock = 0
            str2 = 'rock'

        elif ran == 1:
            yMove = self.paper  # paper = 1
            str2 = 'paper'

        elif ran == 2:
            yMove = self.scissors  # scissors = 2
            str2 = 'scissors'

        print("Mr. Robot played: " + str2)

        # logic for who wins
        if xMove == self.rock and yMove == self.rock:
            print("It's a tie!")
        elif xMove == self.rock and yMove == self.paper:
            print("Mr. Robot wins!")
        elif xMove == self.rock and yMove == self.scissors:
            print("You win!!")
        elif xMove == self.paper and yMove == self.rock:
            print("You win!!")
        elif xMove == self.paper and yMove == self.paper:
            print("It's a tie!")
        elif xMove == self.paper and yMove == self.scissors:
            print("Mr. Robot wins!")
        elif xMove == self.scissors and yMove == self.rock:
            print("Mr. Robot wins!")
        elif xMove == self.scissors and yMove == self.paper:
            print("You win!!")
        elif xMove == self.scissors and yMove == self.scissors:
            print("It's a tie!")

if __name__ == '__main__':
    play = letsPlay()
    play2 = letsPlay2()
    print("Choice one: randomly generated player against randomly generated player.")
    print("Choice two: play against a randomly generated second player.")

    again = True
    while again is True:
        choose = input("Enter '1' for choice one!\nEnter '2' for choice two!\n")
        if choose is '1':
            play.playRPS()
        elif choose is '2':
            play2.playRPS()
        else:
            print("Incorrect input!")
            again is True

        playAgain = input("Want to play again? 'y/n'.\n")
        if playAgain is 'y':
            again = True
        elif playAgain is 'n':
            print("\n\nThanks for playing!")
            exit()
        else:
            print("Incorrect input! Starting again.")



