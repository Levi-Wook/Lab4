#TurtleGraphics.py
#Name:Levi
#Date:9/18
#Assignment:Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(beep, size):
    for i in range(4):
        beep.forward(size)
        beep.right(90)

def drawPolygon(beep, sides):
    for s in range(sides):
        beep.forward(50)
        beep.right(360/sides)
        
def fillCorner(beep, corner):
    drawSquare(beep, 100)
    
    if corner == 1:
     beep.begin_fill()
     drawSquare(beep, 50)
     beep.end_fill()
    elif corner == 2:
        beep.forward(50)
        beep.begin_fill()
        drawSquare(beep, 50)
        beep.end_fill()
    
def squaresInSquares(beep, squares):
    L = 25
    for r in range(squares):
        drawSquare(beep, L)
        beep.up()
        beep.left(90)
        beep.forward(25)
        beep.left(90)
        beep.forward(25)
        beep.left(180)
        beep.down()
        L = L + 50
        



def main():
    beep = turtle.Turtle()
    
    #drawSquare(beep, 100)
    
    #drawPolygon(beep, 5) #draws a pentagon
    #drawPolygon(beep, 8) #draws an octagon

    #fillCorner(beep, 2) #draws a square with top right corner filled in.
    # fillCorner(beep, 3) #draws a square bottom left corner filled in.

    squaresInSquares(beep, 5) #draws 5 concentric squares
    # squaresInSquares(beep, 3) #draws 3 concentric squares


main()


