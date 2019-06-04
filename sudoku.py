#Jeffrey Chiu, andrewid: jchiu2, Section A
from tkinter import *
from sudoku import *

#########################################################
# Customize these functions
# You will need to write many many helper functions, too.
#########################################################
import copy

def init(data):
    #set all initial values
    data.rows = 9
    data.cols = 9
    data.lines = 4
    data.X = 4
    data.Y = 4
    data.copyboard = copy.deepcopy(data.board)
    data.anothercopy = copy.deepcopy(data.board)
    data.selection = (data.X, data.Y)

def moveHighlight(data, key):
    #set a key so that the highlighted box will move based on command
    if key == "U": #U for Up
        if data.Y == 0: data.Y = 8
        else: data.Y = data.Y-1
    if key == "D": #D for Down
        if data.Y == 8: data.Y = 0
        else: data.Y = data.Y+1
    if key == "L": #L for Left
        if data.X == 0: data.X = 8
        else: data.X = data.X-1
    if key == "R": #R for Right
        if data.X == 8: data.X = 0
        else: data.X = data.X+1

def playGame(data, num):
    if num != 0: #numbers from 1-9 can be played, but not 0
        #set condition to see if box is currently empty
        if data.anothercopy[data.Y][data.X] == 0:
            data.anothercopy[data.Y][data.X] = num
            if isLegalSudoku(data.anothercopy): #check if the sudoku works
                data.board[data.Y][data.X] = num
            else:
                data.anothercopy[data.Y][data.X] = 0 #reset the copy

def makeBackSpace(data):
    #set a condition to check if the box is an initial value
    if data.copyboard[data.Y][data.X] == 0:
        #reset both the board and copy so that a value can be played in it after
        #current value is deleted out
        data.board[data.Y][data.X] = 0
        data.anothercopy[data.Y][data.X] = 0

def gameFinished(data):
    #make boolean to see determine if all boxes are filled
    for row in range(data.rows):
        for col in range(data.cols):
            value = data.board[row][col]
            if value == 0: #if any box is empty, or 0, then game is not over
                return False
    return True

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)
    #taken from notes

def drawLines(canvas, data):
    margin = 15 #set a margin so that it doesn't push on the edges
    width, height = data.width, data.height
    sqrtrow, sqrtcol = data.rows**0.5, data.cols**0.5
    #linewidth and lineheight is distance from one line to the next
    linewidth, lineheight = (width-2*margin)/sqrtrow, (height-2*margin)/sqrtcol
    for lines in range(data.lines):
        #draw lines to make board more clear
        canvas.create_line(margin, margin+linewidth*lines,
                            width-margin, margin+linewidth*lines, width=5)
        canvas.create_line(margin+lineheight*lines, margin,
                            margin+lineheight*lines, height-margin, width=5)

def setUpNumbers(canvas, data):
    margin = 15 #set a margin so that it doesn't push on the edges
    width, height = data.width, data.height
    #set a width and height value for every box value to place numbers
    boxw, boxh = (width-2*margin)/data.rows, (height-2*margin)/data.cols
    colorC, colorO = rgbString(199, 235, 94), rgbString(81, 138, 85)
    for row in range(data.rows):
        for col in range(data.cols):
            num = (data.board[row])[col]
            if num != 0:
                #differentiate colors of input numbers and initial numbers
                if data.copyboard[row][col] != 0:
                    fill = colorO #colorO = color original
                else:
                    fill = colorC #colorC = color changed
                canvas.create_text(margin+boxw/2+(col)*boxw,
                margin+boxh/2+(row)*boxh, text = num,
                fill = fill, font = "Neuton 40") #make the numbers

def gameFinishedText(canvas, data):
    #create Congratulations text at the end
    margin = 15
    width, height = data.width, data.height
    if gameFinished(data):
        canvas.create_text((width-2*margin)/2+margin, 
                            (height-2*margin)/2+margin, 
                            text = "Congratulations!",
                            anchor = "center", fill = "white",
                            font = "MoskauGrotesk 50")

def keyPressed(event, data):
    #set a condition to see if the board is filled or game is finished
    if not gameFinished(data):
        #set keysyms to account for highlighted box moving around
        if event.keysym == "Up":
            moveHighlight(data, "U")
            data.selection = (data.X, data.Y)
        elif event.keysym == "Down":
            moveHighlight(data, "D")
            data.selection = (data.X, data.Y)
        elif event.keysym == "Left":
            moveHighlight(data, "L")
            data.selection = (data.X, data.Y)
        elif event.keysym == "Right":
            moveHighlight(data, "R")
            data.selection = (data.X, data.Y)
        #insert digits and backspace in board to play game
        elif event.keysym.isdigit():
            playGame(data,int(event.keysym))
        elif event.keysym == "BackSpace":
            makeBackSpace(data)

def drawBoard(canvas, data):
    margin = 15 #set a margin so it doesn't push on the edges
    width, height = data.width, data.height 
    #set a width and height for every box
    boxw, boxh = (width-2*margin)/data.rows, (height-2*margin)/data.cols
    colorHigh, colorBoard = rgbString(135, 93, 166), rgbString(94, 52, 90)
    for rows in range(data.rows):
        for cols in range(data.cols):
            #set color differences for the highlighted box and other boxes
            if data.selection == (cols, rows):
                fill = colorHigh #colorHigh = color of highlighted box
            else:
                fill = colorBoard #colorBoard = color of board
            #create the board
            canvas.create_rectangle(margin+cols*boxw, margin+rows*boxh, 
            (cols+1)*boxw+margin, (rows+1)*boxh+margin, fill = fill)
    #insert the other functions to make the game work
    drawLines(canvas, data)
    setUpNumbers(canvas, data)
    gameFinishedText(canvas, data)

def redrawAll(canvas, data):
    
    drawBoard(canvas, data)
    
    pass

########################################
# Do not modify the playSudoku function.
########################################

def playSudoku(sudokuBoard, width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.board = sudokuBoard

    # Initialize any other things you want to store in data
    init(data)

    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    # set up events
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    # Draw the initial screen
    redrawAll(canvas, data)

    # Start the event loop
    root.mainloop()  # blocks until window is closed
    print("bye!")

def main():
    
    board = [
            [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
            [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
            [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
            [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
            [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
            [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
            [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
            [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
            [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
        ]
    
    board1 = [
    [1,2,3,4,5,6,7,8,9],
    [5,0,8,1,3,9,6,2,4],
    [4,9,6,8,7,2,1,5,3],
    [9,5,2,3,8,1,4,6,7],
    [6,4,1,2,9,7,8,3,5],
    [3,8,7,5,6,4,0,9,1],
    [7,1,9,6,2,3,5,4,8],
    [8,6,4,9,1,5,3,7,2],
    [2,3,5,7,4,8,9,1,6]
    ]
    
    board2 = [
    [4,0,0,0,0,0,3,0,0],
    [3,0,0,9,0,4,0,0,5],
    [0,5,0,3,0,0,0,0,0],
    [5,0,3,0,0,6,0,0,7],
    [9,4,6,0,0,0,1,5,3],
    [1,0,0,5,0,0,9,0,8],
    [0,0,0,0,0,7,0,8,0],
    [6,0,0,8,0,1,0,0,4],
    [0,0,8,0,0,0,0,0,6] ]
    
    playSudoku(board)
    playSudoku(board1)
    playSudoku(board2)
    
if __name__ == '__main__':
    main()
