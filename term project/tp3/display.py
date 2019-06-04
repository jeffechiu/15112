from getLegalInit import *
from getLegalRoad import *
from getLegalSettle import *
from getLegalCity import *

def drawPossible(canvas, x, y):
    canvas.create_oval((x-10, y-10), (x+10, y+10), width = 3)

def displayPossibleSetInit(canvas, data):
    coords = getLegalSetInit(data)
    for coord in coords:
        if coord[1] == 1:
            drawPossible(canvas, 170+130*coord[0], 75)
        if coord[1] == 2:
            drawPossible(canvas, 105+130*coord[0], 112.5)
        if coord[1] == 3:
            drawPossible(canvas, 105+130*coord[0], 187.5)
        if coord[1] == 4:
            drawPossible(canvas, 40+130*coord[0], 225)
        if coord[1] == 5:
            drawPossible(canvas, 40+130*coord[0], 300)
        if coord[1] == 6:
            drawPossible(canvas, -25+130*coord[0], 337.5)
        if coord[1] == 7:
            drawPossible(canvas, -25+130*coord[0], 412.5)
        if coord[1] == 8:
            drawPossible(canvas, 40+130*coord[0], 450)
        if coord[1] == 9:
            drawPossible(canvas, 40+130*coord[0], 525)
        if coord[1] == 10:
            drawPossible(canvas, 105+130*coord[0], 562.5)
        if coord[1] == 11:
            drawPossible(canvas, 105+130*coord[0], 637.5)
        if coord[1] == 12:
            drawPossible(canvas, 170+130*coord[0], 675)

def displayPossibleRoadInit(canvas, data):
    roads = getLegalRoadInit(data)
    for road in roads:
        drawPossible(canvas, road[0], road[1])

def displayPossibleRoad(canvas, data):
    coords = getLegalRoad(data)
    for coord in coords:
        drawPossible(canvas, coord[0], coord[1])

def displayPossibleSettle(canvas, data):
    coords = getLegalSettle(data)
    for coord in coords:
        drawPossible(canvas, coord[0], coord[1])

def displayPossibleCity(canvas, data):
    coords = getLegalCity(data)
    for coord in coords:
        drawPossible(canvas, coord[0], coord[1])