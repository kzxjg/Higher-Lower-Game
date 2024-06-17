from game_data import *
from art import *
import random


game_cont = True

op1 = random.choice(data)
op2 = random.choice(data)

if(op1['name'] == op2['name']):
    op2 = random.choice(data)


print(logo)

score = 0

while game_cont == True:

    print(f"Compare A : {op1['name']}, a {op1['description']} from {op2['country']}")
    print(vs)
    print(f"Against B : {op2['name']}, a {op2['description']} from {op2['country']}")
    
    answer = input("Which of the two has more followers : ")

    if(score > 0):
        print(f"Your score is {score}")


    if answer == 'B' :
        if op2['follower_count'] >= op1['follower_count']:
            score += 1
            op1 = op2
            op2 = random.choice(data)
            if(op1['name'] == op2['name']):
                op2 = random.choice(data)

        elif(op1['follower_count'] > op2['follower_count']):
            game_cont = False


    elif answer == 'A':
        if op1['follower_count'] >= op2['follower_count']:
            score += 1
            op2 = random.choice(data)
            print(f"Current score is {score}")
            if(op1['name'] == op2['name']):
                op2 = random.choice(data)

        elif(op2['follower_count'] > op1['follower_count']):
            game_cont = False


print(logo)
print(f"Final score is {score}")
print("Game over")
