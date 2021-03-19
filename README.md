
Proyect: Semana Tec Herramientas computacionales: el arte de la programación (TC1001S.100)

Professor Gilberto Echeverría Furió.

By:
A. Ricardo Alonso Aróstegui - A01029011

/*
Add names here
*/

March 19, 2021

Memory.py:

    To solve the first exercise of this videogame we define a 
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
    centeringit, or if it is greater than 1 (not centering it).

    Finally, for the fifth exercise we made the code generate some 
    random numbers, or if possible reuse the numbers previously 
    inserted in the tiles list. Then it uses this numbers as ASCII 
    codes and converts them to its character.