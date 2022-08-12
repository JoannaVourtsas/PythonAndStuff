#reference code from
#Creative Coding in Python : 30+ Programming Projects in Art, Games, and More (p.91)

import random #random library for random numbers

number_dice = input('Enter number of dice:') #ask how many times dice is going to roll
number_dice = int(number_dice) #change to numeric value

def dice(x): #function to create how many times the dice is rolled
    dice = [] #list of dice number/ currently empty
    for i in range(x): #base on how many times the dice is rolled
       dice.append(random.randint(1,6))#put x amount of numbers in the list ranging the numbers 1-6 
    return dice 

def find_winner(cdice_list, udice_list):
        computer_total = sum(cdice_list)
        user_total = sum(udice_list)
        print('Computer total', computer_total)
        print('User total',user_total )
        if user_total > computer_total:
            print('User wins')
        elif user_total < computer_total:
            print('Computer wins')
        else:
            print('It is a tie!')

userTurn = dice(number_dice)
print('User rolls',userTurn)

pcTurn = dice(number_dice)
print('Pc rolls', pcTurn)

find_winner(pcTurn,userTurn)
