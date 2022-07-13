
from blessed import Terminal
import random
import copy
from collections import deque


# Defining the variables and functions that will be used in the game.
term = Terminal()
UP = term.KEY_UP
RIGHT = term.KEY_RIGHT
LEFT = term.KEY_LEFT
DOWN = term.KEY_DOWN

DIRECTIONS = [LEFT, UP, RIGHT, DOWN]

MOVEMENT_MAP = {LEFT: [0,-1], UP:[-1, 0], RIGHT:[0, 1], DOWN:[1, 0]}

WASD_MAP = {
    'w' : UP,
    'a' : LEFT,
    's' : DOWN,
    'd' : RIGHT,
    'W' : UP,
    'A' : LEFT,
    'S' : DOWN,
    'D' : RIGHT,
}

dead = False

#------------------------------------------------------------config-------------------------------------------------------

BORDER = ''
BODY = ''
HEAD = ''
SPACE = ''
APPLE = ''

#initial snale position
snake = deque([[6, 5], [6, 4], [6, 3]])

#initial speed 

food = [5, 10]
h, w = 10, 15 # height, weight

score = 0
# initial speed 
speed = 3

MAX_SPEED = 3

#N1 and N2 represent the snake's movement frequency
#The snake will only move n1 out of n2 turns

n1 = 1
n2 = 2

# M represents how often the snake will grow
#The snake wil grow every M turns

M = 9


#------------------------------------------------------------config end -------------------------------------------------------

messages = ['Hurry we are dreaming', 'You can beat me']

message = None

def list_empty_spaces(world, space):
    result = []
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == space:
                result.append([i, j])
    return result

with term.cbreak(), term.hidden_cursor():
    #clear the screen
    print(term.home + term.clear)

    #Initiliaze the world