"""
Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.


Excercises solved by A. Ricardo Alonso Aróstegui

18/03/21.
"""

from random import *
from turtle import *
from freegames import path

while True:
    length = int(input("Please insert the size of the grid sides: ")) if input("Type Y if you want a custom size grid: ") == 'Y' else 4 # This variable manages how many rows/columns the grid will have, , accomplishing what EXERCISE 2 specifies.
    
    if length % 2 != 0:
        print("The grid side size must be an even number\n")
    elif length > 10:
        print("The grid side size must be smaller or equal to 10")
    else:
        break        

area = length ** 2
remainingTiles = area / 2 # We define the remaining tiles as the total tiles over 2.
car = path('car.gif')
tiles = list(range(int(remainingTiles)))
state = {'mark': None}
hide = [True] * area
taps = 0
xPixels = 400 / length
useLetters = True if input("Type L if you want to use letters instead of numbers: ") == 'L' else False

if useLetters: # If user decided to use letters we make the tiles list of letters, accomplishing what EXERCISE 5 specifies.
    seed(1)

    for i in range (len(tiles)):
        while True: # This while cycle will make sure we are using only letters, and that none of them are repeating
            element = tiles[i] if type(tiles[i]) is int else randrange(65, 90)

            if (element >= 65 and element <= 90) or (element >= 97 and element <= 122):
                char = chr(element)
            else:
                char = chr(randrange(65, 90))

            if not (char in tiles):
                tiles[i] = char
                break

tiles *= 2
            

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(xPixels)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // xPixels + ((y + 200) // xPixels) * length)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % length) * xPixels - 200, (count // length) * xPixels - 200 # The adding of xPixels variable makes the square adapt to any grid side size.

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global taps, remainingTiles

    spot = index(x, y)
    mark = state['mark']
    taps += 1 # Adds 1 to the count of taps, accomplishing what EXERCISE 1 specifies.
    print("You have made %d taps." % (taps))

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        
        if remainingTiles <= 1: # If there's not remaining tiles then it notifies you that you won, accomplishing what EXERCISE 3 specifies.
            print("\nYou won!\nYou made %d movements" % (taps))
        else: # Else it just subtracts a tile to the remaining tiles count.
            remainingTiles -= 1

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(area):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        if len(str(tiles[mark])) == 1:
            goto(x + (xPixels / 2 - 5), y) # If the length of the tile equals 1 it goes to a centered position, accomplishing what EXERCISE 4 specifies.
        else:
            goto(x + 5, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
