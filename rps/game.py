# Write your code here
import random 
outcome = ['rock','paper','scissors','fire','gun','lightning',
            'devil','dragon','water','air','sponge','tree','wolf','human','snake']
            
win_conditions = {"paper": ["rock","air","water","devil","dragon","gun", "lightning"],
                  "scissors": ["paper","air","tree","paper","snake","human" ,"sponge"],
                  "rock": ["scissors", "snake","Human", "Fire", "Wolf ","Sponge", "Tree"],
                  "fire":["scissors","paper","snake","human","tree","wolf","sponge"],
                  "gun":["rock","tree","fire","scissors","snake","human", "wolf"],
                  "lightning":["gun","scissors","rock","tree","fire","snake", "human"],
                  "devil":["rock","fire","scissors","gun","lightning","snakes","human"],
                  "dragon":["devil","lightning","fire","rock","scissors","gun", "snake"],
                  "water":["devil","dragon","rock","fire","scissors","gun" ,"lightning"],
                  "air":["fire","rock","water","devil","gun","dragon" ,"lightning"],
                  "sponge":["paper","air","water","dragon","lightning","gun" ,"devil"],
                  "wolf":["sponge","paper","air","water","dragon","lightning", "devil"],
                  "tree":["wolf","sponge","paper","air","water","devil", "dragon"],
                  "human":["tree","wolf","sponge","paper","air","water", "dragon"],
                  "snake":["human","wolf","sponge","tree","paper","air", "water"]}


user_input = 0
rating = 0 

name = input('Enter your name: ')
print('Hello,', name)
game_options = input()
if len(game_options) == 0:
    game_options =  ["rock","paper","scissors"]
else:
    game_options = game_options.split(",")
    for i in game_options:
        if i not in outcome:
            print("Invalid input")
print("Okay, let's start")
    

file1 = open('rating.txt', 'r', encoding='utf-8')
for line in file1:
    if line.split()[0] == name:
        rating = int(line.split()[1])
file1.close()



while user_input != '!exit':
    user_input = input()
    if user_input == '!rating':
        print('Your rating:',rating)
        user_input = input()
    else:     
        computer = random.choice(game_options)
        if user_input in game_options:
            if win_conditions[user_input]:
                value_list = list(win_conditions[user_input])
                if user_input == computer:
                    print(f'There is a draw ({computer})')
                    rating += 50
                elif (computer in value_list):
                    print(f"Well done. The computer chose {computer} and failed")
                    rating += 100
                else:
                    print(f"Sorry, but the computer chose {computer}")
        else:
            print("Invalid input")
print('Bye!')
exit()