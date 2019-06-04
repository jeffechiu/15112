from tkinter import *
import random
import math
from isLegal import *

###################################
#Board Code
###################################

#taken from notes
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def threeTiles(data):
    row = []
    for i in range(3):
        tile = random.choice(data.pieces)
        data.pieces.remove(tile)
        row += [tile]
    return row

def fourTiles(data):
    row = []
    for i in range(4):
        tile = random.choice(pieces)
        data.pieces.remove(tile)
        row += [tile]
    return row

def fiveTiles(data):
    row = []
    for i in range(5):
        tile = random.choice(data.pieces)
        data.pieces.remove(tile)
        row += [tile]
    return row

def drawTile(data, canvas, x, y, tiles):
    for i in range(len(tiles)):
        if tiles[i] == 'wood':
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.WOOD, outline = 'black', width = 3)
        elif tiles[i] == 'brick':
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.BRICK, outline = 'black', width = 3)
        elif tiles[i] == 'sheep':
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.SHEEP, outline = 'black', width = 3)
        elif tiles[i] == 'wheat':
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.WHEAT, outline = 'black', width = 3)
        elif tiles[i] == 'stone':
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.STONE, outline = 'black', width = 3)
        else:
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.DESERT, outline = 'black', width = 3)

def drawNums(data, canvas, x, y, numLst):
    for i in range(len(numLst)):
        if not numLst[i] == 'desert':
            if numLst[i] == 6 or numLst[i] == 8:
                canvas.create_text(x+i*130, y, text = str(numLst[i]), fill = "red", font = "Helvetica 20")
            else:
                canvas.create_text(x+i*130, y, text = str(numLst[i]), fill = "black", font = "Helvetica 20")

###################################
#Resources and Settling
###################################

def dices():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1+dice2

def coordConverter(coord):
    if coord[1] == 1:
        x = 170+130*coord[0]
        y = 75
    if coord[1] == 2:
        x = 105+130*coord[0]
        y = 112.5
    if coord[1] == 3:
        x = 105+130*coord[0]
        y = 187.5
    if coord[1] == 4:
        x = 40+130*coord[0]
        y = 225
    if coord[1] == 5:
        x = 40+130*coord[0]
        y = 300
    if coord[1] == 6:
        x = -25+130*coord[0]
        y = 337.5
    if coord[1] == 7:
        x = -25+130*coord[0]
        y = 412.5
    if coord[1] == 8:
        x = 40+130*coord[0]
        y = 450
    if coord[1] == 9:
        x = 40+130*coord[0]
        y = 525
    if coord[1] == 10:
        x = 105+130*coord[0]
        y = 562.5
    if coord[1] == 11:
        x = 105+130*coord[0]
        y = 637.5
    if coord[1] == 12:
        x = 170+130*coord[0]
        y = 675
    return ((x, y))

####
#Get Legal Functions
####



####
#Draw Functions
####

def drawSettlement(canvas, x, y, color):
    canvas.create_oval((x-15, y-15), (x+15, y+15), fill = color, width = 2)

def drawCity(canvas, x, y, color):
    canvas.create_rectangle((x-15, y-15), (x+15, y+15), fill = color, width = 2)

def drawRoad(canvas, x1, y1, x2, y2, color):
    canvas.create_line(x1, y1, x2, y2, fill = color, width = 8)    

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

def displayPossibleRoad(canvas, data):
    roads = getLegalRoad(data)
    for road in roads:
        drawPossible(canvas, road[0], road[1])

def updateOccupied(data):
    data.occupied = []
    data.p1Sc, data.p2Sc, data.p3Sc, data.p4Sc = 0, 0, 0, 0
    for key in data.p1Ex:
        if key == "settle":
            for i in data.p1Ex[key]:
                data.p1Sc += 1
        if key == "city":
            for i in data.p1Ex[key]:
                data.p1Sc += 2
        if key != "road":
            for expans in data.p1Ex[key]:
                data.occupied += [expans]
    for key in data.p2Ex:
        if key == "settle":
            for i in data.p2Ex[key]:
                data.p2Sc += 1
        if key == "city":
            for i in data.p2Ex[key]:
                data.p2Sc += 2
        if key != "road":
            for expans in data.p2Ex[key]:
                data.occupied += [expans]
    for key in data.p3Ex:
        if key == "settle":
            for i in data.p3Ex[key]:
                data.p3Sc += 1
        if key == "city":
            for i in data.p3Ex[key]:
                data.p3Sc += 2
        if key != "road":
            for expans in data.p3Ex[key]:
                data.occupied += [expans]
    for key in data.p4Ex:
        if key == "settle":
            for i in data.p4Ex[key]:
                data.p4Sc += 1
        if key == "city":
            for i in data.p4Ex[key]:
                data.p4Sc += 2
        if key != "road":
            for expans in data.p4Ex[key]:
                data.occupied += [expans]

def updateOccRoads(data):
    for key in data.p1Ex:
        if key == "road":
            for coords in data.p1Ex[key]:
                data.occupiedRoads += [coords]
    for key in data.p2Ex:
        if key == "road":
            for coords in data.p2Ex[key]:
                data.occupiedRoads += [coords]
    for key in data.p3Ex:
        if key == "road":
            for coords in data.p3Ex[key]:
                data.occupiedRoads += [coords]
    for key in data.p4Ex:
        if key == "road":
            for coords in data.p4Ex[key]:
                data.occupiedRoads += [coords]

def mapper(coord):
    if coord == (1, 1): return [0]
    if coord == (2, 1): return [1]
    if coord == (3, 1): return [2]
    if coord == (1, 2): return [0]
    if coord == (2, 2): return [0, 1]
    if coord == (3, 2): return [1, 2]
    if coord == (4, 2): return [2]
    if coord == (1, 3): return [0, 3]
    if coord == (2, 3): return [0, 1, 4]
    if coord == (3, 3): return [1, 2, 5]
    if coord == (4, 3): return [2, 6]
    if coord == (1, 4): return [3]
    if coord == (2, 4): return [0, 3, 4]
    if coord == (3, 4): return [1, 4, 5]
    if coord == (4, 4): return [2, 5, 6]
    if coord == (5, 4): return [6]
    if coord == (1, 5): return [3, 7]
    if coord == (2, 5): return [3, 4, 8]
    if coord == (3, 5): return [4, 5, 9]
    if coord == (4, 5): return [5, 6, 10]
    if coord == (5, 5): return [6, 11]
    if coord == (1, 6): return [7]
    if coord == (2, 6): return [3, 7, 8]
    if coord == (3, 6): return [4, 8, 9]
    if coord == (4, 6): return [5, 9, 10]
    if coord == (5, 6): return [6, 10, 11]
    if coord == (6, 6): return [11]
    if coord == (1, 7): return [7]
    if coord == (2, 7): return [7, 8, 12]
    if coord == (3, 7): return [8, 9, 13]
    if coord == (4, 7): return [9, 10, 14]
    if coord == (5, 7): return [10, 11, 15]
    if coord == (6, 7): return [11]
    if coord == (1, 8): return [7, 12]
    if coord == (2, 8): return [8, 12, 13]
    if coord == (3, 8): return [9, 13, 14]
    if coord == (4, 8): return [10, 14, 15]
    if coord == (5, 8): return [11, 15]
    if coord == (1, 9): return [12]
    if coord == (2, 9): return [12, 13, 16]
    if coord == (3, 9): return [13, 14, 17]
    if coord == (4, 9): return [14, 15, 18]
    if coord == (5, 9): return [15]
    if coord == (1, 10): return [12, 16]
    if coord == (2, 10): return [13, 16, 17]
    if coord == (3, 10): return [14, 17, 18]
    if coord == (4, 10): return [15, 18]
    if coord == (1, 11): return [16]
    if coord == (2, 11): return [16, 17]
    if coord == (3, 11): return [17, 18]
    if coord == (4, 11): return [18]
    if coord == (1, 12): return [16]
    if coord == (2, 12): return [17]
    if coord == (3, 12): return [18]

def drawResources(data):
    for key in data.p1Ex:
        for i in data.p1Ex[key]:
            if key == "settle":
                hexes = mapper(i)
                for num in hexes:
                    if data.nums[num] == data.roll:
                        if data.allTiles[num] != 'desert':
                            data.p1Res[data.allTiles[num]] += 1
            if key == "city":
                hexes = mapper(i)
                for num in hexes:
                    if data.nums[num] == data.roll:
                        if data.allTiles[num] != 'desert':
                            data.p1Res[data.allTiles[num]] += 2
    for key in data.p2Ex:
        for i in data.p2Ex[key]:
            if key == "settle":
                hexes = mapper(i)
                for num in hexes:
                    if data.nums[num] == data.roll:
                        if data.allTiles[num] != 'desert':
                            data.p2Res[data.allTiles[num]] += 1
            if key == "city":
                hexes = mapper(i)
                for num in hexes:
                    if data.nums[num] == data.roll:
                        if data.allTiles[num] != 'desert':
                            data.p2Res[data.allTiles[num]] += 2
    for key in data.p3Ex:
        for i in data.p3Ex[key]:
            if key == "settle":
                hexes = mapper(i)
                for num in hexes:
                    if data.nums[num] == data.roll:
                        if data.allTiles[num] != 'desert':
                            data.p3Res[data.allTiles[num]] += 1
            if key == "city":
                hexes = mapper(i)
                for num in hexes:
                    if data.nums[num] == data.roll:
                        if data.allTiles[num] != 'desert':
                            data.p3Res[data.allTiles[num]] += 2
    for key in data.p4Ex:
        for i in data.p4Ex[key]:
            if key == "settle":
                hexes = mapper(i)
                for num in hexes:
                    if data.nums[num] == data.roll:
                        if data.allTiles[num] != 'desert':
                            data.p4Res[data.allTiles[num]] += 1
            if key == "city":
                hexes = mapper(i)
                for num in hexes:
                    if data.nums[num] == data.roll:
                        if data.allTiles[num] != 'desert':
                            data.p4Res[data.allTiles[num]] += 2

def drawInitResources(data, coord):
    hexes = mapper(coord)
    if data.turn == 1:
        for num in hexes:
            if data.allTiles[num] != 'desert':
                data.p1Res[data.allTiles[num]] += 1
    if data.turn == 2:
        for num in hexes:
            if data.allTiles[num] != 'desert':
                data.p2Res[data.allTiles[num]] += 1
    if data.turn == 3:
        for num in hexes:
            if data.allTiles[num] != 'desert':
                data.p3Res[data.allTiles[num]] += 1
    if data.turn == 4:
        for num in hexes:
            if data.allTiles[num] != 'desert':
                data.p4Res[data.allTiles[num]] += 1

def buildSettle(data):
    if data.turn == 1:
        data.p1Res["wood"] -= 1
        data.p1Res["brick"] -= 1
        data.p1Res["wheat"] -= 1
        data.p1Res["sheep"] -= 1
    if data.turn == 2:
        data.p2Res["wood"] -= 1
        data.p2Res["brick"] -= 1
        data.p2Res["wheat"] -= 1
        data.p2Res["sheep"] -= 1
    if data.turn == 3:
        data.p3Res["wood"] -= 1
        data.p3Res["brick"] -= 1
        data.p3Res["wheat"] -= 1
        data.p3Res["sheep"] -= 1
    if data.turn == 4:
        data.p4Res["wood"] -= 1
        data.p4Res["brick"] -= 1
        data.p4Res["wheat"] -= 1
        data.p4Res["sheep"] -= 1

def buildCity(data):
    if data.turn == 1:
        data.p1Res["wheat"] -= 2
        data.p1Res["stone"] -= 3
    if data.turn == 2:
        data.p2Res["wheat"] -= 2
        data.p2Res["stone"] -= 3
    if data.turn == 3:
        data.p3Res["wheat"] -= 2
        data.p3Res["stone"] -= 3
    if data.turn == 4:
        data.p4Res["wheat"] -= 2
        data.p4Res["stone"] -= 3

def buildRoad(data):
    if data.turn == 1:
        data.p1Res["brick"] -= 1
        data.p1Res["wood"] -= 1
    if data.turn == 2:
        data.p2Res["brick"] -= 1
        data.p2Res["wood"] -= 1
    if data.turn == 3:
        data.p3Res["brick"] -= 1
        data.p3Res["wood"] -= 1
    if data.turn == 4:
        data.p4Res["brick"] -= 1
        data.p4Res["wood"] -= 1


###################################
#Initialization Code
###################################

def init(data):
    ###
    #Board stuff
    ###
    data.pieces = ['wood', 'wood', 'wood', 'wood', 'brick', 'brick', 'brick', 'sheep', 'sheep',
    'sheep', 'sheep', 'wheat', 'wheat', 'wheat', 'wheat', 'stone', 'stone', 'stone', 'desert']
    data.first, data.second, data.third, data.fourth, data.fifth = [], [], [], [], []   
    for tile in range(3):
        tile = random.choice(data.pieces)
        data.first += [tile]
        data.pieces.remove(tile)
        secondTile = random.choice(data.pieces)
        data.fifth += [secondTile]
        data.pieces.remove(secondTile)
    for tile in range(4):
        tile = random.choice(data.pieces)
        data.second += [tile]
        data.pieces.remove(tile)
        secondTile = random.choice(data.pieces)
        data.fourth += [secondTile]
        data.pieces.remove(secondTile)
    for tile in range(5):
        tile = random.choice(data.pieces)
        data.third += [tile]
        data.pieces.remove(tile)
    data.allTiles = data.first + data.second + data.third + data.fourth + data.fifth
    data.inNums = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
    data.nums = []
    for i in range(18):
        num = random.choice(data.inNums)
        data.nums += [num]
        data.inNums.remove(num)
    data.nums.insert(data.allTiles.index('desert'), 'desert')
    data.firN, data.seN, data.thN, data.foN, data.fifN = data.nums[0:3], data.nums[3:7], data.nums[7:12], data.nums[12:16], data.nums[16:19]
    ###
    #Player Turns
    ###
    data.p1Res, data.p2Res = {"wood":0, "brick":0, "wheat":0, "stone":0, "sheep":0}, {"wood":0, "brick":0, "wheat":0, "stone":0, "sheep":0}
    data.p3Res, data.p4Res = {"wood":0, "brick":0, "wheat":0, "stone":0, "sheep":0}, {"wood":0, "brick":0, "wheat":0, "stone":0, "sheep":0}
    data.p1Sc, data.p2Sc, data.p3Sc, data.p4Sc = 0, 0, 0, 0
    data.p1Ex, data.p2Ex = {"settle":[], "city":[], "road":[]}, {"settle":[], "city":[], "road":[]}
    data.p3Ex, data.p4Ex = {"settle":[], "city":[], "road":[]}, {"settle":[], "city":[], "road":[]}
    data.occupied = []
    data.occupiedRoads = []
    data.drawRoads = []
    data.pColors = ["red", "blue", "white", "purple"]
    data.resources = ['wood', 'brick', 'sheep', 'wheat', 'stone']
    data.turn = 1
    data.round = 1
    data.phase = "place1"
    data.prevCoord = (0, 0)
    data.roll = 0
    ###
    #Resource Colors
    ###
    data.WHEAT = rgbString(255, 255, 0)
    data.STONE = rgbString(128, 128, 128)
    data.SHEEP = rgbString(0, 255, 0)
    data.BRICK = rgbString(124, 10, 2)
    data.WOOD = rgbString(0, 100, 0)
    data.DESERT = rgbString(204, 204, 0)

def keyPressed(event, data):
    if data.phase == "roll":
        if event.keysym == "space":
            data.roll = dices()
            drawResources(data)
            data.phase = "build"

def mousePressed(event, data):
    coords = getLegalSetInit(data)
    if data.phase == "build":
        if 1000<event.x<1150 and 662.5<event.y<737.5:
            if data.turn == 4:
                data.round += 1
                data.turn = 1
            else:
                data.turn += 1
            data.phase = "roll"
    elif data.phase == "place1" or data.phase == "place2":
        for coord in coords:
            if coord[1] == 1:
                smallX = 170+130*coord[0]-10
                bigX = 170+130*coord[0]+10
                smallY = 65
                bigY = 85
            if coord[1] == 2:
                smallX = 105+130*coord[0]-10
                bigX = 105+130*coord[0]+10
                smallY = 102.5
                bigY = 122.5
            if coord[1] == 3:
                smallX = 105+130*coord[0]-10
                bigX = 105+130*coord[0]+10
                smallY = 177.5
                bigY = 197.5
            if coord[1] == 4:
                smallX = 40+130*coord[0]-10
                bigX = 40+130*coord[0]+10
                smallY = 215
                bigY = 235
            if coord[1] == 5:
                smallX = 40+130*coord[0]-10
                bigX = 40+130*coord[0]+10
                smallY = 290
                bigY = 310
            if coord[1] == 6:
                smallX = -25+130*coord[0]-10
                bigX = -25+130*coord[0]+10
                smallY = 327.5
                bigY = 347.5
            if coord[1] == 7:
                smallX = -25+130*coord[0]-10
                bigX = -25+130*coord[0]+10
                smallY = 402.5
                bigY = 422.5
            if coord[1] == 8:
                smallX = 40+130*coord[0]-10
                bigX = 40+130*coord[0]+10
                smallY = 440
                bigY = 460
            if coord[1] == 9:
                smallX = 40+130*coord[0]-10
                bigX = 40+130*coord[0]+10
                smallY = 515
                bigY = 535
            if coord[1] == 10:
                smallX = 105+130*coord[0]-10
                bigX = 105+130*coord[0]+10
                smallY = 552.5
                bigY = 572.5
            if coord[1] == 11:
                smallX = 105+130*coord[0]-10
                bigX = 105+130*coord[0]+10
                smallY = 627.5
                bigY = 647.5
            if coord[1] == 12:
                smallX = 170+130*coord[0]-10
                bigX = 170+130*coord[0]+10
                smallY = 665
                bigY = 685
            if smallX<event.x<bigX and smallY<event.y<bigY:
                if data.turn == 1:
                    data.p1Ex["settle"] += [coord]
                if data.turn == 2:
                    data.p2Ex["settle"] += [coord]
                if data.turn == 3:
                    data.p3Ex["settle"] += [coord]
                if data.turn == 4:
                    data.p4Ex["settle"] += [coord]
                if data.phase == "place2":
                    drawInitResources(data, coord)
                updateOccupied(data)
                if data.phase == "place1":
                    data.prevPhase = "place1"
                if data.phase == "place2":
                    data.prevPhase = "place2"
                data.prevCoord = coord
                data.phase = "placeR"
    elif data.phase == "placeR":
        roads = getLegalRoad(data)
        for road in roads:
            smallX = road[0]-10
            bigX = road[0]+10
            smallY = road[1]-10
            bigY = road[1]+10
            if smallX<event.x<bigX and smallY<event.y<bigY:
                if data.turn == 1:
                    data.p1Ex["road"] += [road]
                if data.turn == 2:
                    data.p2Ex["road"] += [road]
                if data.turn == 3:
                    data.p3Ex["road"] += [road]
                if data.turn == 4:
                    data.p4Ex["road"] += [road]
                updateOccRoads(data)
                if data.prevPhase == "place1":
                    if data.turn == 4:
                        data.round += 1
                        data.phase = "place2"
                    else:
                        data.turn += 1
                        data.phase = "place1"
                elif data.prevPhase == "place2":
                    if data.turn == 1:
                        data.round += 1
                        data.phase = "roll"
                    else:
                        data.turn -= 1
                        data.phase = "place2"

def timerFired(data):
    pass

def redrawAll(canvas, data):
    ###
    #board stuff
    ###
    drawTile(data, canvas, 300, 75, data.first)
    drawTile(data, canvas, 235, 187.5, data.second)
    drawTile(data, canvas, 170, 300, data.third)
    drawTile(data, canvas, 235, 412.5, data.fourth)
    drawTile(data, canvas, 300, 525, data.fifth)
    drawNums(data, canvas, 300, 150, data.firN)
    drawNums(data, canvas, 235, 262.5, data.seN)
    drawNums(data, canvas, 170, 375, data.thN)
    drawNums(data, canvas, 235, 487.5, data.foN)
    drawNums(data, canvas, 300, 600, data.fifN)
    #Port 1
    canvas.create_oval((150, 130), (190, 170), fill = "black", width = 0)
    canvas.create_line((170, 225), (170, 150), width = 5)
    canvas.create_line((235, 187.5), (170, 150), width = 5)
    canvas.create_text((170, 150), text = "3:1", font = "Helvetica 13 bold", fill = "white")
    #Port 2
    canvas.create_oval((345, 17.5), (385, 57.5), fill = "black", width = 0)
    canvas.create_line((300, 75), (365, 37.5), width = 5)
    canvas.create_line((365, 112.5), (365, 37.5), width = 5)
    canvas.create_text((365, 37.5), text = "3:1", font = "Helvetica 13 bold", fill = "white")
    #Port 3
    canvas.create_oval((605, 17.5), (645, 57.5), fill = data.BRICK, width = 0)
    canvas.create_line((560, 75), (625, 37.5), fill = data.BRICK, width = 5)
    canvas.create_line((625, 112.5), (625, 37.5), fill = data.BRICK, width = 5)
    canvas.create_text((625, 37.5), text = "2:1", font = "Helvetica 13 bold", fill = "white")
    #Port 4
    canvas.create_oval((735, 242.5), (775, 282.5), fill = "black", width = 0)
    canvas.create_line((690, 225), (755, 262.5), width = 5)
    canvas.create_line((690, 300), (755, 262.5), width = 5)
    canvas.create_text((755, 262.5), text = "3:1", font = "Helvetica 13 bold", fill = "white")
    #Port 5
    canvas.create_oval((735, 467.5), (775, 507.5), fill = data.WHEAT, width = 0)
    canvas.create_line((690, 450), (755, 487.5), fill = data.WHEAT, width = 5)
    canvas.create_line((690, 525), (755, 487.5), fill = data.WHEAT, width = 5)
    canvas.create_text((755, 487.5), text = "2:1", font = "Helvetica 13 bold", fill = "black")
    #Port 6
    canvas.create_oval((605, 692.5), (645, 732.5), fill = data.WOOD, width = 0)
    canvas.create_line((625, 637.5), (625, 712.5), fill = data.WOOD, width = 5)
    canvas.create_line((560, 675), (625, 712.5), fill = data.WOOD, width = 5)
    canvas.create_text((625, 712.5), text = "2:1", font = "Helvetica 13 bold", fill = "white")
    #Port 7
    canvas.create_oval((345, 692.5), (385, 732.5), fill = data.SHEEP, width = 0)
    canvas.create_line((365, 637.5), (365, 712.5), fill = data.SHEEP, width = 5)
    canvas.create_line((300, 675), (365, 712.5), fill = data.SHEEP, width = 5)
    canvas.create_text((365, 712.5), text = "2:1", font = "Helvetica 13 bold", fill = "white")
    #Port 8
    canvas.create_oval((150, 580), (190, 620), fill = "black", width = 0)
    canvas.create_line((170, 525), (170, 600), fill = "black", width = 5)
    canvas.create_line((235, 562.5), (170, 600), fill = "black", width = 5)
    canvas.create_text((170, 600), text = "3:1", font = "Helvetica 13 bold", fill = "white")
    #Port 9
    canvas.create_oval((20, 355), (60, 395), fill = data.STONE, width = 0)
    canvas.create_line((105, 337.5), (40, 375), fill = data.STONE, width = 5)
    canvas.create_line((105, 412.5), (40, 375), fill = data.STONE, width = 5)
    canvas.create_text((40, 375), text = "2:1", font = "Helvetica 13 bold", fill = "white")
    #Drawing Expansions
    for key in data.p1Ex:
        for i in data.p1Ex[key]:
            if key == "settle": expans = "s"
            elif key == "city": expans = "c"
            elif key == "road": expans = "r"
            if expans == "r":
                if i[1] % 0.5 != 0:
                    y1 = i[1] - 18.75
                    y2 = i[1] + 18.75
                    x1 = i[0] + 32.5
                    x2 = i[0] - 32.5
                    for coords in data.occupied:
                        if coordConverter(coords) == (x1, y1) or coordConverter(coords) == (x2, y2):
                            drawRoad(canvas, x1, y1, x2, y2, data.pColors[0])
                            break
                        if coords == data.occupied[-1]:
                            drawRoad(canvas, x1, y2, x2, y1, data.pColors[0])
                else:
                    y1 = i[1]-37.5
                    y2 = i[1] + 37.5
                    x = i[0]
                    drawRoad(canvas, x, y1, x, y2, data.pColors[0])
            if i[1] == 1:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 75, data.pColors[0])
                else:
                    drawCity(canvas, 170+130*i[0], 75, data.pColors[0])
            if i[1] == 2:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 112.5, data.pColors[0])
                else:
                    drawCity(canvas, 105+130*i[0], 112.5, data.pColors[0])
            if i[1] == 3:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 187.5, data.pColors[0])
                else:
                    drawCity(canvas, 105+130*i[0], 187.5, data.pColors[0])
            if i[1] == 4:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 225, data.pColors[0])
                else:
                    drawCity(canvas, 40+130*i[0], 225, data.pColors[0])
            if i[1] == 5:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 300, data.pColors[0])
                else:
                    drawCity(canvas, 40+130*i[0], 300, data.pColors[0])
            if i[1] == 6:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 337.5, data.pColors[0])
                else:
                    drawCity(canvas, -25+130*i[0], 337.5, data.pColors[0])
            if i[1] == 7:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 412.5, data.pColors[0])
                else:
                    drawCity(canvas, -25+130*i[0], 412.5, data.pColors[0])
            if i[1] == 8:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 450, data.pColors[0])
                else:
                    drawCity(canvas, 40+130*i[0], 450, data.pColors[0])
            if i[1] == 9:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 525, data.pColors[0])
                else:
                    drawCity(canvas, 40+130*i[0], 525, data.pColors[0])
            if i[1] == 10:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 562.5, data.pColors[0])
                else:
                    drawCity(canvas, 105+130*i[0], 562.5, data.pColors[0])
            if i[1] == 11:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 637.5, data.pColors[0])
                else:
                    drawCity(canvas, 105+130*i[0], 637.5, data.pColors[0])
            if i[1] == 12:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 675, data.pColors[0])
                else:
                    drawCity(canvas, 170+130*i[0], 675, data.pColors[0])
        for i in data.p2Ex[key]:
            if key == "settle": expans = "s"
            elif key == "city": expans = "c"
            elif key == "road": expans = "r"
            if expans == "r":
                if i[1] % 0.5 != 0:
                    y1 = i[1] - 18.75
                    y2 = i[1] + 18.75
                    x1 = i[0] + 32.5
                    x2 = i[0] - 32.5
                    for coords in data.occupied:
                        if coordConverter(coords) == (x1, y1) or coordConverter(coords) == (x2, y2):
                            drawRoad(canvas, x1, y1, x2, y2, data.pColors[1])
                            break
                        if coords == data.occupied[-1]:
                            drawRoad(canvas, x1, y2, x2, y1, data.pColors[1])
                else:
                    y1 = i[1]-37.5
                    y2 = i[1] + 37.5
                    x = i[0]
                    drawRoad(canvas, x, y1, x, y2, data.pColors[1])
            if i[1] == 1:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 75, data.pColors[1])
                else:
                    drawCity(canvas, 170+130*i[0], 75, data.pColors[1])
            if i[1] == 2:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 112.5, data.pColors[1])
                else:
                    drawCity(canvas, 105+130*i[0], 112.5, data.pColors[1])
            if i[1] == 3:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 187.5, data.pColors[1])
                else:
                    drawCity(canvas, 105+130*i[0], 187.5, data.pColors[1])
            if i[1] == 4:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 225, data.pColors[1])
                else:
                    drawCity(canvas, 40+130*i[0], 225, data.pColors[1])
            if i[1] == 5:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 300, data.pColors[1])
                else:
                    drawCity(canvas, 40+130*i[0], 300, data.pColors[1])
            if i[1] == 6:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 337.5, data.pColors[1])
                else:
                    drawCity(canvas, -25+130*i[0], 337.5, data.pColors[1])
            if i[1] == 7:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 412.5, data.pColors[1])
                else:
                    drawCity(canvas, -25+130*i[0], 412.5, data.pColors[1])
            if i[1] == 8:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 450, data.pColors[1])
                else:
                    drawCity(canvas, 40+130*i[0], 450, data.pColors[1])
            if i[1] == 9:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 525, data.pColors[1])
                else:
                    drawCity(canvas, 40+130*i[0], 525, data.pColors[1])
            if i[1] == 10:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 562.5, data.pColors[1])
                else:
                    drawCity(canvas, 105+130*i[0], 562.5, data.pColors[1])
            if i[1] == 11:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 637.5, data.pColors[1])
                else:
                    drawCity(canvas, 105+130*i[0], 637.5, data.pColors[1])
            if i[1] == 12:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 675, data.pColors[1])
                else:
                    drawCity(canvas, 170+130*i[0], 675, data.pColors[1])
        for i in data.p3Ex[key]:
            if key == "settle": expans = "s"
            elif key == "city": expans = "c"
            elif key == "road": expans = "r"
            if expans == "r":
                if i[1] % 0.5 != 0:
                    y1 = i[1] - 18.75
                    y2 = i[1] + 18.75
                    x1 = i[0] + 32.5
                    x2 = i[0] - 32.5
                    for coords in data.occupied:
                        if coordConverter(coords) == (x1, y1) or coordConverter(coords) == (x2, y2):
                            drawRoad(canvas, x1, y1, x2, y2, data.pColors[2])
                            break
                        if coords == data.occupied[-1]:
                            drawRoad(canvas, x1, y2, x2, y1, data.pColors[2])
                else:
                    y1 = i[1]-37.5
                    y2 = i[1] + 37.5
                    x = i[0]
                    drawRoad(canvas, x, y1, x, y2, data.pColors[2])
            if i[1] == 1:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 75, data.pColors[2])
                else:
                    drawCity(canvas, 170+130*i[0], 75, data.pColors[2])
            if i[1] == 2:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 112.5, data.pColors[2])
                else:
                    drawCity(canvas, 105+130*i[0], 112.5, data.pColors[2])
            if i[1] == 3:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 187.5, data.pColors[2])
                else:
                    drawCity(canvas, 105+130*i[0], 187.5, data.pColors[2])
            if i[1] == 4:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 225, data.pColors[2])
                else:
                    drawCity(canvas, 40+130*i[0], 225, data.pColors[2])
            if i[1] == 5:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 300, data.pColors[2])
                else:
                    drawCity(canvas, 40+130*i[0], 300, data.pColors[2])
            if i[1] == 6:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 337.5, data.pColors[2])
                else:
                    drawCity(canvas, -25+130*i[0], 337.5, data.pColors[2])
            if i[1] == 7:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 412.5, data.pColors[2])
                else:
                    drawCity(canvas, -25+130*i[0], 412.5, data.pColors[2])
            if i[1] == 8:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 450, data.pColors[2])
                else:
                    drawCity(canvas, 40+130*i[0], 450, data.pColors[2])
            if i[1] == 9:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 525, data.pColors[2])
                else:
                    drawCity(canvas, 40+130*i[0], 525, data.pColors[2])
            if i[1] == 10:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 562.5, data.pColors[2])
                else:
                    drawCity(canvas, 105+130*i[0], 562.5, data.pColors[2])
            if i[1] == 11:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 637.5, data.pColors[2])
                else:
                    drawCity(canvas, 105+130*i[0], 637.5, data.pColors[2])
            if i[1] == 12:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 675, data.pColors[2])
                else:
                    drawCity(canvas, 170+130*i[0], 675, data.pColors[2])
        for i in data.p4Ex[key]:
            if key == "settle": expans = "s"
            elif key == "city": expans = "c"
            elif key == "road": expans = "r"
            if expans == "r":
                if i[1] % 0.5 != 0:
                    y1 = i[1] - 18.75
                    y2 = i[1] + 18.75
                    x1 = i[0] + 32.5
                    x2 = i[0] - 32.5
                    for coords in data.occupied:
                        if coordConverter(coords) == (x1, y1) or coordConverter(coords) == (x2, y2):
                            drawRoad(canvas, x1, y1, x2, y2, data.pColors[3])
                            break
                        if coords == data.occupied[-1]:
                            drawRoad(canvas, x1, y2, x2, y1, data.pColors[3])
                else:
                    y1 = i[1]-37.5
                    y2 = i[1] + 37.5
                    x = i[0]
                    drawRoad(canvas, x, y1, x, y2, data.pColors[3])
            if i[1] == 1:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 75, data.pColors[3])
                else:
                    drawCity(canvas, 170+130*i[0], 75, data.pColors[3])
            if i[1] == 2:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 112.5, data.pColors[3])
                else:
                    drawCity(canvas, 105+130*i[0], 112.5, data.pColors[3])
            if i[1] == 3:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 187.5, data.pColors[3])
                else:
                    drawCity(canvas, 105+130*i[0], 187.5, data.pColors[3])
            if i[1] == 4:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 225, data.pColors[3])
                else:
                    drawCity(canvas, 40+130*i[0], 225, data.pColors[3])
            if i[1] == 5:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 300, data.pColors[3])
                else:
                    drawCity(canvas, 40+130*i[0], 300, data.pColors[3])
            if i[1] == 6:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 337.5, data.pColors[3])
                else:
                    drawCity(canvas, -25+130*i[0], 337.5, data.pColors[3])
            if i[1] == 7:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 412.5, data.pColors[3])
                else:
                    drawCity(canvas, -25+130*i[0], 412.5, data.pColors[3])
            if i[1] == 8:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 450, data.pColors[3])
                else:
                    drawCity(canvas, 40+130*i[0], 450, data.pColors[3])
            if i[1] == 9:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 525, data.pColors[3])
                else:
                    drawCity(canvas, 40+130*i[0], 525, data.pColors[3])
            if i[1] == 10:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 562.5, data.pColors[3])
                else:
                    drawCity(canvas, 105+130*i[0], 562.5, data.pColors[3])
            if i[1] == 11:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 637.5, data.pColors[3])
                else:
                    drawCity(canvas, 105+130*i[0], 637.5, data.pColors[3])
            if i[1] == 12:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 675, data.pColors[3])
                else:
                    drawCity(canvas, 170+130*i[0], 675, data.pColors[3])
    ###
    #dice and turns
    ###
    if data.turn == 1:
        canvas.create_rectangle((755, 75), (905, 150), fill = "yellow", width = 5)
    else:
        canvas.create_rectangle((755, 75), (905, 150), width = 5)
    canvas.create_text(830, 112.5, text = "Player 1\n%d Points" % data.p1Sc, font = "Helvetica 15")
    if data.turn == 2:
        canvas.create_rectangle((955, 75), (1105, 150), fill = "yellow", width = 5)
    else:
        canvas.create_rectangle((955, 75), (1105, 150), width = 5)
    canvas.create_text(1030, 112.5, text = "Player 2\n%d Points" % data.p2Sc, font = "Helvetica 15")
    if data.turn == 3:
        canvas.create_rectangle((1155, 75), (1305, 150), fill = "yellow", width = 5)
    else:
        canvas.create_rectangle((1155, 75), (1305, 150), width = 5)
    canvas.create_text(1230, 112.5, text = "Player 3\n%d Points" % data.p3Sc, font = "Helvetica 15")
    if data.turn == 4:
        canvas.create_rectangle((1355, 75), (1505, 150), fill = "yellow", width = 5)
    else:
        canvas.create_rectangle((1355, 75), (1505, 150), width = 5)
    canvas.create_text(1430, 112.5, text = "Player 4\n%d Points" % data.p4Sc, font = "Helvetica 15")
    canvas.create_text(1130, 600, text = ("Number Rolled: %d" % data.roll),
        font = "Helvetica 50")
    canvas.create_text(940, 275, text = "Wood: %d" % data.p1Res["wood"], font = "Helvetica 25")
    canvas.create_text(940, 325, text = "Brick: %d" % data.p1Res["brick"], font = "Helvetica 25")
    canvas.create_text(940, 375, text = "Wheat: %d" % data.p1Res["wheat"], font = "Helvetica 25")
    canvas.create_text(940, 425, text = "Stone: %d" % data.p1Res["stone"], font = "Helvetica 25")
    canvas.create_text(940, 475, text = "Sheep: %d" % data.p1Res["sheep"], font = "Helvetica 25")
    if data.phase == "build":
        canvas.create_rectangle((1055, 662.5), (1205, 737.5), width= 5)
        canvas.create_text(1130, 700, text = "End Turn", font = "Helvetica 25")
    if data.phase == "place1" or data.phase == "place2":
        displayPossibleSetInit(canvas, data)
    if data.phase == "placeR":
        displayPossibleRoad(canvas, data)
    # canvas.create_rectangle(1105, 250, 1255, 350, width = 5)
    # canvas.create_text(
    # canvas.create_rectangle(1105, 400, 1255, 500, width = 5)
    # canvas.create_rectangle(1305, 250, 1455, 350, width = 5)
    # canvas.create_rectangle(1305, 400, 1455, 500, width = 5)

###################################
#Animation Framework
###################################

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
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
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

run(1555, 750)