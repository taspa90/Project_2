#loadgame variable
game=0
level=0
#variable GuessGame
#variable MemoryGame

def welcome(name):
 name = input('Enter Your Name')
 return name

print ('Hello ' +welcome(1))
print('and welcome to the World of Games (WoG).Here you can find many cool games to play\n')

def load_game (game, level):
 game = int(input('Please choose a game to play:\n'
  '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n'
  '2. Guess Game - guess a number and see if you choose like the computer\n'))
 level = int(input('Please choose game difficulty from 1 to 5:'))
 return game,level
load_game(game,level)

if game == 2:
 import GuessGame

