
Proyect: Semana Tec Herramientas computacionales: el arte de la programación (TC1001S.100)

Professor Gilberto Echeverría Furió.

By:
A. Ricardo Alonso Aróstegui - A01029011
Arturo Sosa Carrillo - A01022687
Humberto Murrieta Pepping - A01029184

Link al video explicatorio: https://youtu.be/u7xF4CQ1AAw.


March 19, 2021

Memory.py:

    To solve the first exercise of this videogame we defined a
    variable named taps, initially as 0. This variable is declared
    as global inside the tap function, so each tap it adds one to
    the value.

    For the second exercise we modified the xy function, so it
    could adapt to any grid side size. We also defined a length
    function. Changing its value will change the grid size, as
    well as all of the other values required, so the grid will
    adapt to any custom size as long as its even and in the range  
    from 2 to 10.

    For the third exercise we just defined a variable that
    initially counts the remaining tiles. This will be updated
    each time a user finds two  matching cards, and will finally
    detect when there are no remaining tiles, notifying the user
    that he won as well as his movements count.

    For the fourth exercise we just added a condition in the draw
    function which detects if the length of the tile content is
    equal to one (single-digit) so it changes its x value,
    centering it, or if it is greater than 1 (not centering it).

    Finally, for the fifth exercise we made the code generate some
    random numbers, or if possible reuse the numbers previously
    inserted in the tiles list. Then it uses this numbers as ASCII
    codes and converts them to its character.

Snake.py:

    To increase the speed of the snake we introduced the command ontimer, 
    which makes the snake move (100/speed)miliseconds. 
    Complying with the requirements provided by the instructions within the excercise.
    As we increse velocity everytime the snake successfully takes in the food, 
    we reduce time while increasing the speed. 
    To accomplish this we introduced the command speed = len(snake). 

    To Solve the second exercise we observe the edges from the inside()
    function and use the to construct a condition such that when the
    snake gets out of the setup, it reappears on the other side of it.

    On the second exercise, we tried to make the food move contrary to what
    the user entered through the keyboard to make it run away from the Snake
    but that brought some bugs and didn't work correctly. Then we tried to
    make the food move with the move function from the "freegames" library
    as the snake does but when the snake touched the food, it didn't get
    consumed. Next, we tried to make it move by switching it's position on x
    and y by "food.x = food.x-1" but we got the same bug so we realized the
    food had to be static for the snake to eat it and decided to use a random
    number from 0 to 50 to decide if the food moved on x, on y or stayed static.

    To make it more congruent, we added the same behaviour from exercise 1 to
    the food so it could go around the edges. We decided to make this behaviour
    a function skipEdge() to recicle code and apply it to both objects.
