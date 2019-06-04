# Jeffrey Chiu, andrewid: jchiu2, Section A
# Partners: Andy Zhang(andyz), David Yuan(dyuan1)
# Barebones timer, mouse, and keyboard events
from tkinter import *
import copy
import random

####################################
# customize these functions
####################################
def myDeepCopy(a):
    if (isinstance(a, list) or isinstance(a, tuple)):
        return [myDeepCopy(element) for element in a]
    else:
        return copy.copy(a)
#taken from notes

def init(data):
    data.rows, data.cols = 15, 10 #row and column numbers
    data.margin, data.cellSize = 25, 20 #margin and box size
    data.emptyColor = "blue" #color of empty board
    #make the list for the board
    data.board = [([data.emptyColor]*data.cols) for rows in range(data.rows)]
    #make all the pieces into lists and put them into another list
    iPiece = [
            [True, True, True, True]
            ]
    jPiece = [
            [ True, False, False],
            [ True, True, True]
            ]
    lPiece = [
            [False, False, True],
            [True, True, True]
            ]
    oPiece = [
            [True, True],
            [True, True]
            ]
    sPiece = [
            [False, True, True],
            [True, True, False]
            ]
    tPiece = [
            [False, True, False],
            [True, True, True]
            ]
    zPiece = [
            [True, True, False],
            [False, True, True]
            ]
    tetrisPieces = [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]
    tetrisPieceColors = ["red", "yellow", "magenta", "pink", "cyan", "green",
                        "orange"] #get all piece colors
    data.tetrisPieces, data.tetrisPieceColors = tetrisPieces, tetrisPieceColors
    data.firstpiece = newFallingPiece(data) #place the first piece on board
    data.isGameOver, data.score = False, 0 #start initial end variables
    
def playTetris():
    #set the dimensions for the board so that it can be played upon
    rows, cols = 15, 10
    cellSize = 20
    margin = 25
    width, height = cellSize*cols+2*margin, cellSize*rows+2*margin
    run(width, height)
    
def drawBoard(canvas, data):
    #draw the board
    margin, cellSize = data.margin, data.cellSize
    #loop through every iteration of the board and create a rectangle
    #fill every rectangle with the element of the list
    for row in range(data.rows):
        for col in range(data.cols):
            canvas.create_rectangle(margin+cellSize*col, margin+cellSize*row,
                                    margin+cellSize*(col+1),
                                    margin+cellSize*(row+1),
                                    fill = data.board[row][col], width = 3)

def newFallingPiece(data):
    #used random to randomly generate a piece
    randomIndex = random.randint(0, len(data.tetrisPieces)-1)
    #find the piece and color of piece randomly generated
    data.fallingPiece = data.tetrisPieces[randomIndex]
    data.fallingPieceColor = data.tetrisPieceColors[randomIndex]
    #set starting dimensions for where the pieces start from
    data.fallingPieceRow = 0
    data.fallingPieceCol = data.cols//2-len(data.fallingPiece[0])//2
    
def drawFallingPiece(canvas, data):
    margin = data.margin
    #loop through every iteration, to find where to draw the new pieces
    for row in range(len(data.fallingPiece)):
        newRow = data.fallingPiece[row]
        for col in range(len(newRow)):
            newCol = newRow[col]
            #only draw pieces where newCol is True
            if newCol == True:
                canvas.create_rectangle(
                margin+data.fallingPieceCol*data.cellSize+col*data.cellSize,
                margin+data.fallingPieceRow*data.cellSize+row*data.cellSize,
                margin+data.fallingPieceCol*data.cellSize+(col+1)*data.cellSize,
                margin+data.fallingPieceRow*data.cellSize+(row+1)*data.cellSize,
                fill = data.fallingPieceColor, width = 3)

def fallingPieceIsLegal(data):
    #to test if the falling piece can place legally
    for row in range(len(data.fallingPiece)):
        newRow = data.fallingPiece[row] #identifies the row
        for col in range(len(newRow)):
            newCol = newRow[col] #identifies the column
            #check if the column is in the range of columns
            if newCol == True:
                if data.fallingPieceCol+col not in range(data.cols):
                    return False
                #check if the row is in the range of rows
                elif data.fallingPieceRow+row not in range(data.rows):
                    return False
                #check if it doesn't interfere with other pieces
                elif data.board[data.fallingPieceRow+row][
                    data.fallingPieceCol+col] != data.emptyColor:
                    return False
    return True

def moveFallingPiece(data, drow, dcol):
    #shift the rows and columns
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol
    #reset everything if it is false
    if fallingPieceIsLegal(data) == False:
        data.fallingPieceRow -= drow
        data.fallingPieceCol -= dcol
        #add return statements for timerFired and to place the board
        return False
    return True

def rotateFallingPiece(data):
    #make a copy for setting the center of the rotated piece if rotation failed
    data.fallingPieceCopy = copy.deepcopy(data.fallingPiece)
    #set a current row variable so the length can be found later on and
    #create a new list to rotate the variable
    curRow, newRow, rotatedPiece = data.fallingPiece[0], [], []
    #loop through every iteration of the piece, but add to list from the end of
    #the column to the beginning to account for rotating counterclockwise
    for col in range(len(curRow)):
        for row in range(len(data.fallingPiece)):
            newRow += [data.fallingPiece[row][len(curRow)-1-col]]
        rotatedPiece += [newRow]
        newRow = []
    #make a copy for fallingPiece so that it can be re-centered later if
    #rotation failed
    data.fallingPiece = myDeepCopy(rotatedPiece)
    #identify the new rows so the new lengths of rows can be found
    newCurRow = data.fallingPiece[0]
    #set copies of old row and copy so it can be re-centered later if rotation
    #failed
    data.rowCopy, data.colCopy = data.fallingPieceRow, data.fallingPieceCol
    #find center rows and columns of old piece before rotated
    data.oldCenterRow = data.fallingPieceRow + len(data.fallingPieceCopy)//2
    data.oldCenterCol = data.fallingPieceCol + len(curRow)//2
    #set new center rows and columns equal to old center rows and columns
    data.newCenterCol, data.newCenterRow = data.oldCenterCol, data.oldCenterRow
    #set new fallingPiece points for row and column of rotated piece
    data.fallingPieceRow = data.newCenterRow-len(data.fallingPiece)//2
    data.fallingPieceCol = data.newCenterCol-len(newCurRow)//2
    #reset everything if rotation fails
    if fallingPieceIsLegal(data) == False:
        data.fallingPiece = myDeepCopy(data.fallingPieceCopy)
        data.fallingPieceRow, data.fallingPieceCol = data.rowCopy, data.colCopy

def placeFallingPiece(data):
    #iterate through entire board
    for row in range(data.rows):
        for col in range(data.cols):
            #find the fallingPieceRow and fallingPieceCol as it relates to board
            if data.fallingPieceRow == row and data.fallingPieceCol == col:
                for pieceRow in range(len(data.fallingPiece)):
                    for pieceCol in range(len(data.fallingPiece[0])):
                        if data.fallingPiece[pieceRow][pieceCol] == True:
                            data.board[row+pieceRow][col+pieceCol] = \
                            data.fallingPieceColor
    #if after pieces are filled and a row is full, remove the row
    removeFullRows(data)

def removeFullRows(data):
    newBoard = [] #make a new board to add the rows with empty spots in them
    #iterate through all rows
    for row in data.board:
        #if there is an empty spot in the board, add the row to the new board
        if data.emptyColor in row:
            newBoard += [row]
    #set a variable to find the number of new rows that shall be added
    difference = len(data.board)-len(newBoard)
    #make an empty line, and add them to the top of the board
    newLine = [[data.emptyColor]*data.cols]
    newBoard = difference*myDeepCopy(newLine) + newBoard
    #increment score every time a row is cleared
    data.score += difference**2
    #set the newboard into the data.board
    data.board = myDeepCopy(newBoard)

def drawScore(canvas, data):
    #draw the score on the board
    canvas.create_text(data.width/2, data.margin/2, 
                        text = "Score:"+str(data.score), fill = "blue")

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    #only run everything except for restart if the game is not over
    if data.isGameOver == False:
        if event.keysym == "Left":
            moveFallingPiece(data, 0, -1)
        if event.keysym == "Right":
            moveFallingPiece(data, 0, 1)
        if event.keysym == "Down":
            moveFallingPiece(data, 1, 0)
        if event.keysym == "Up":
            rotateFallingPiece(data)
    if event.keysym == "r":
        init(data)

def timerFired(data):
    if data.isGameOver == False:
        if moveFallingPiece(data, 1, 0) == False:
            placeFallingPiece(data)
            newFallingPiece(data)
            #if game over, stop running the game
            if not fallingPieceIsLegal(data):
                data.isGameOver = True        

def redrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "orange")
    drawScore(canvas, data)
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)
    #make a game over screen when the game ends
    if data.isGameOver == True:
        canvas.create_rectangle(data.margin, data.margin+data.cellSize,
                                data.width-data.margin,
                                data.margin+data.cellSize*3, fill = "black")
        canvas.create_text(data.width/2, data.margin+data.cellSize*2,
                            text = "Game Over!", fill = "yellow",
                            font = "Verdana 20")

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 500 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

####################################
#Test Functions
####################################

def testFallingPieceIsLegal():
    class Struct(object): pass
    testData = Struct()
    print("Testing fallingPieceIsLegal()...", end="")
    testData.rows, testData.cols = 15, 15
    testData.fallingPiece = [[False, True, True],[True, True, False]]
    testData.fallingPieceRow, testData.fallingPieceCol = 0, 6
    testData.emptyColor = "blue"
    testData.board = [([testData.emptyColor]*testData.cols) \
                        for row in range(testData.rows)]
    assert(fallingPieceIsLegal(testData) == True)
    testData.fallingPieceRow, testData.fallingPieceCol = 14, 6
    assert(fallingPieceIsLegal(testData) == False)
    testData.board[5][7] = "yellow"
    testData.fallingPieceRow, testData.fallingPieceCol = 5, 6
    assert(fallingPieceIsLegal(testData) == False)
    print("Passed!")

def testMoveFallingPiece():
    class Struct(object): pass
    testData = Struct()
    print("Testing moveFallingPiece()...", end="")
    testData.rows, testData.cols = 15, 15
    testData.fallingPiece = [[False, True, True],[True, True, False]]
    testData.fallingPieceRow, testData.fallingPieceCol = 0, 6
    testData.emptyColor = "blue"
    testData.board = [([testData.emptyColor]*testData.cols) \
                        for row in range(testData.rows)]
    assert(moveFallingPiece(testData, 13, 0) == True)
    assert(moveFallingPiece(testData, 0, 6) == True)
    assert(moveFallingPiece(testData, 0, -6) == True)
    assert(moveFallingPiece(testData, 14, 0) == False)
    assert(moveFallingPiece(testData, 0, 7) == False)
    assert(moveFallingPiece(testData, 0, -7) == False)
    testData.board[2][6] = "yellow"
    assert(moveFallingPiece(testData, 1, 0) == False)
    print("Passed!")
    
def returnRotatePiece(data):
    #copy pasted function from rotateFallingPiece to test it with a return
    data.fallingPieceCopy = copy.deepcopy(data.fallingPiece)
    curRow, newRow, rotatedPiece = data.fallingPiece[0], [], []
    for col in range(len(curRow)):
        for row in range(len(data.fallingPiece)):
            newRow += [data.fallingPiece[row][len(curRow)-1-col]]
        rotatedPiece += [newRow]
        newRow = []
    data.fallingPiece = myDeepCopy(rotatedPiece)
    newCurRow = data.fallingPiece[0]
    data.rowCopy, data.colCopy = data.fallingPieceRow, data.fallingPieceCol
    data.oldCenterRow = data.fallingPieceRow + len(data.fallingPieceCopy)//2
    data.oldCenterCol = data.fallingPieceCol + len(curRow)//2
    data.newCenterCol, data.newCenterRow = data.oldCenterCol, data.oldCenterRow
    data.fallingPieceRow = data.newCenterRow-len(data.fallingPiece)//2
    data.fallingPieceCol = data.newCenterCol-len(newCurRow)//2
    if fallingPieceIsLegal(data) == False:
        data.fallingPiece = myDeepCopy(data.fallingPieceCopy)
        data.fallingPieceRow, data.fallingPieceCol = data.rowCopy, data.colCopy
    return data.fallingPiece

def RFPboard(testData):
    testData.rows, testData.cols = 15, 15
    testData.emptyColor = "blue"
    testData.board = [([testData.emptyColor]*testData.cols) \
                        for row in range(testData.rows)]

def testRotateFallingPiece():
    class Struct(object): pass
    testData = Struct()
    print("Testing rotateFallingPiece()...", end="")
    RFPboard(testData)
    testData.fallingPieceRow, testData.fallingPieceCol = 6, 6
    testData.fallingPiece = [[False, True, True],[True, True, False]]
    solution1 = [[True, False], [True, True], [False, True]]
    assert(returnRotatePiece(testData) == solution1)
    testData.fallingPiece = [[True, True], [True, True]]
    solution2 = [[True, True], [True, True]]
    assert(returnRotatePiece(testData) == solution2)
    testData.fallingPiece = [[False, True, False], [True, True, True]]
    solution3 = [[False, True], [True, True], [False, True]]
    assert(returnRotatePiece(testData) == solution3)
    testData.fallingPieceRow, testData.fallingPieceCol = 6, 14
    testData.fallingPiece = [[True, False], [True, False], [True, True]]
    solution4 = [[True, False], [True, False], [True, True]]
    assert(returnRotatePiece(testData) == solution4)
    print("Passed!")
    
def returnFallingPiece(data):
    #copy pasted function from placeFallingPiece to test it with a return
    for row in range(data.rows):
        for col in range(data.cols):
            if data.fallingPieceRow == row and data.fallingPieceCol == col:
                for pieceRow in range(len(data.fallingPiece)):
                    for pieceCol in range(len(data.fallingPiece[0])):
                        if data.fallingPiece[pieceRow][pieceCol] == True:
                            data.board[row+pieceRow][col+pieceCol] = \
                            data.fallingPieceColor
    return data.board

def PFPtestCase1(testData):
    testData.fallingPiece = [[True, True], [True, True]]
    testData.fallingPieceColor = "red"
    testData.rows, testData.cols = 15, 15
    testData.fallingPieceRow, testData.fallingPieceCol = 5, 5
    testData.emptyColor = "blue"
    testData.board = [([testData.emptyColor]*testData.cols) \
                        for row in range(testData.rows)]
    testData.solution1 = myDeepCopy(testData.board)
    testData.solution1[5][5], testData.solution1[5][6] = "red", "red"
    testData.solution1[6][5], testData.solution1[6][6] = "red", "red"
    
def PFPtestCase2(testData):
    testData.fallingPiece = [[True, True, True, True]]
    testData.solution2 = myDeepCopy(testData.board)
    testData.solution2[5][5], testData.solution2[5][6] = "red", "red"
    testData.solution2[5][7], testData.solution2[5][8] = "red", "red"

def PFPtestCase3(testData):
    testData.fallingPiece = [[False, True, True], [True, True, False]]
    testData.solution3 = myDeepCopy(testData.board)
    testData.solution3[5][6], testData.solution3[5][7] = "red", "red"
    testData.solution3[6][5], testData.solution3[6][6] = "red", "red"

def testPlaceFallingPiece():
    class Struct(object): pass
    testData = Struct()
    print("Testing placeFallingPiece()...", end="")
    PFPtestCase1(testData)
    assert(returnFallingPiece(testData) == testData.solution1)
    PFPtestCase2(testData)
    assert(returnFallingPiece(testData) == testData.solution2)
    PFPtestCase3(testData)
    assert(returnFallingPiece(testData) == testData.solution3)
    print("Passed!")

def returnRemoveRows(data):
    #copy pasted function from removeFullRows to test it with a return
    newBoard = []
    for row in data.board:
        if data.emptyColor in row:
            newBoard += [row]
    difference = len(data.board)-len(newBoard)
    newLine = [[data.emptyColor]*data.cols]
    newBoard = difference*myDeepCopy(newLine) + newBoard
    data.score += difference**2
    data.board = myDeepCopy(newBoard)
    return data.board, data.score

def RFRboard1(testData):
    testData.board = [([testData.emptyColor]*testData.cols) \
                    for row in range(testData.rows-1)]+[["red"]*testData.cols]

def RFRboard2(testData):
    testData.board = [([testData.emptyColor]*testData.cols) \
                    for row in range(testData.rows)]

def RFRboard3(testData):
    testData.board = [([testData.emptyColor]*testData.cols) \
                    for row in range(testData.rows-2)] + \
                    [["red"]+([testData.emptyColor]*(testData.cols-1))] + \
                    ["red"*testData.cols]

def RFRsolBoard3(testData):
    testData.sol3 = [([testData.emptyColor]*testData.cols) \
                    for row in range(testData.rows-1)] + \
                    [["red"]+([testData.emptyColor]*(testData.cols-1))]

def testRemoveFullRows():
    class Struct(object): pass
    testData = Struct()
    print("Testing removeFullRows()...", end="")
    testData.score = 0
    testData.rows, testData.cols = 15, 15
    testData.emptyColor = "blue"
    RFRboard1(testData)
    assert(returnRemoveRows(testData) ==([([testData.emptyColor]*testData.cols)\
                                    for row in range(testData.rows)], 1))
    testData.score = 2
    RFRboard2(testData)
    assert(returnRemoveRows(testData) == (testData.board, 2))
    testData.score = 16
    RFRboard3(testData)
    RFRsolBoard3(testData)
    assert(returnRemoveRows(testData) == (testData.sol3, 17))
    print("Passed!")

####################################
#testAll and Main
####################################

def testAll():
    testFallingPieceIsLegal()
    testMoveFallingPiece()
    testRotateFallingPiece()
    testPlaceFallingPiece()
    testRemoveFullRows()

def main():
    testAll()
    playTetris()

if __name__ == '__main__':
    main()