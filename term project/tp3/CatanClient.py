import socket
import threading
from queue import Queue

HOST = "128.237.119.227" # put your IP address here if playing on multiple computers
PORT = 50003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((HOST,PORT))
print("connected to server")

def handleServerMsg(server, serverMsg):
  server.setblocking(1)
  msg = ""
  command = ""
  while True:
    msg += server.recv(10).decode("UTF-8")
    command = msg.split("\n")
    while (len(command) > 1):
      readyMsg = command[0]
      msg = "\n".join(command[1:])
      serverMsg.put(readyMsg)
      command = msg.split("\n")

from tkinter import *
import random
from essentials import *
from drawBoard import *
from drawExpansions import *
from getLegalInit import *
from getLegalRoad import *
from getLegalSettle import *
from getLegalCity import *
from isLegal import *
from display import *
from update import *
from collectResources import *
from build import *
from trade import *
from tradeImplement import *

def init(data):
    data.timerDelay = 200
    data.count = 0
    data.otherPlayers = []
    ###
    #Board stuff
    ###
    data.screen = "game"
    data.allTiles = ['brick', 'wood', 'sheep', 'wheat', 'stone', 'wheat', 'brick', 'stone', 'sheep', 'wood', 'sheep', 'wheat', 'desert', 'wheat', 'stone', 'wood', 'wood', 'brick', 'sheep'] 
    data.first, data.second, data.third, data.fourth, data.fifth = data.allTiles[0:3], data.allTiles[3:7], data.allTiles[7:12], data.allTiles[12:16], data.allTiles[16:19]
    data.nums = [8, 5, 6, 5, 12, 2, 9, 6, 11, 9, 3, 8, 'desert', 4, 10, 11, 10, 3, 4]
    data.robber = data.allTiles.index('desert')
    data.firN, data.seN, data.thN, data.foN, data.fifN = data.nums[0:3], data.nums[3:7], data.nums[7:12], data.nums[12:16], data.nums[16:19]
    data.me = 0
    data.woodPort, data.brickPort, data.wheatPort, data.stonePort, data.sheepPort = 0, 0, 0, 0, 0
    ###
    #Player Turns
    ###
    data.p1Res, data.p2Res = {"wood":100, "brick":100, "wheat":100, "stone":100, "sheep":100}, {"wood":0, "brick":0, "wheat":0, "stone":0, "sheep":0}
    data.p3Res, data.p4Res = {"wood":0, "brick":0, "wheat":0, "stone":0, "sheep":0}, {"wood":0, "brick":0, "wheat":0, "stone":0, "sheep":0}
    data.p1Sc, data.p2Sc, data.p3Sc, data.p4Sc = 0, 0, 0, 0
    data.p1Ex, data.p2Ex = {"settle":[], "city":[], "road":[]}, {"settle":[], "city":[], "road":[]}
    data.p3Ex, data.p4Ex = {"settle":[], "city":[], "road":[]}, {"settle":[], "city":[], "road":[]}
    data.occupied = []
    data.occupiedRoads = []
    data.drawRoads = []
    data.pColors = ["red", "blue", "pink", "purple"]
    data.resources = ['wood', 'brick', 'sheep', 'wheat', 'stone']
    data.turn = 1
    data.round = 1
    data.phase = "place1"
    data.prevCoord = (0, 0)
    data.roll = 0
    data.allCoords = [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (4, 2), (1, 3), (2, 3), (3, 3), (4, 3), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (1, 10), (2, 10), (3, 10), (4, 10), (1, 11), (2, 11), (3, 11), (4, 11), (1, 12), (2, 12), (3, 12)]
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
    msg = ""
    if data.phase == "roll":
        if (int(data.me) == 1 and data.turn == 1) or (int(data.me) == 2 and data.turn == 2) or (int(data.me) == 3 and data.turn == 3) or (int(data.me) == 4 and data.turn == 4):
            if event.keysym == "space":
                data.roll = dices()
                collectResources(data)
                data.phase = "build"
                msg = "rolled %d\n" % data.roll
                print("sending: ", msg)
                data.server.send(msg.encode())

def mousePressed(event, data):
    msg = ""
    coords = getLegalSetInit(data)
    if data.phase == "build":
        #press on buttons while it's your turn, enable them to change phases
        if data.turn == 1 and int(data.me) == 1:
            if isLegalRoad(data):
                if 1105 < event.x < 1255 and 300 < event.y < 375:
                    data.phase = 'buildR'
            if isLegalSettle(data):
                if 1105 < event.x < 1255 and 400 < event.y < 475:
                    data.phase = 'buildS'
            if isLegalCity(data):
                if 1305 < event.x < 1455 and 300 < event.y < 375:
                    data.phase = 'buildC'
            if isLegalTrade(data):
                if 1305 < event.x < 1455 and 400 < event.y < 475:
                    data.phase = 'trade'
            #end turn button
            if 1300<event.x<1450 and 637.5<event.y<712.5:
                data.turn += 1
                data.phase = "roll"
                msg = "end 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())
        if data.turn == 2 and int(data.me) == 2:
            if isLegalRoad(data):
                if 1105 < event.x < 1255 and 300 < event.y < 375:
                    data.phase = 'buildR'
            if isLegalSettle(data):
                if 1105 < event.x < 1255 and 400 < event.y < 475:
                    data.phase = 'buildS'
            if isLegalCity(data):
                if 1305 < event.x < 1455 and 300 < event.y < 375:
                    data.phase = 'buildC'
            if isLegalTrade(data):
                if 1305 < event.x < 1455 and 400 < event.y < 475:
                    data.phase = 'trade'
            #end turn button
            if 1300<event.x<1450 and 637.5<event.y<712.5:
                data.turn += 1
                data.phase = "roll"
                msg = "end 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())
        if data.turn == 3 and int(data.me) == 3:
            if isLegalRoad(data):
                if 1105 < event.x < 1255 and 300 < event.y < 375:
                    data.phase = 'buildR'
            if isLegalSettle(data):
                if 1105 < event.x < 1255 and 400 < event.y < 475:
                    data.phase = 'buildS'
            if isLegalCity(data):
                if 1305 < event.x < 1455 and 300 < event.y < 375:
                    data.phase = 'buildC'
            if isLegalTrade(data):
                if 1305 < event.x < 1455 and 400 < event.y < 475:
                    data.phase = 'trade'
            #end turn button
            if 1300<event.x<1450 and 637.5<event.y<712.5:
                data.turn += 1
                data.phase = "roll"
                msg = "end 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())
        if data.turn == 4 and int(data.me) == 4:
            if isLegalRoad(data):
                if 1105 < event.x < 1255 and 300 < event.y < 375:
                    data.phase = 'buildR'
            if isLegalSettle(data):
                if 1105 < event.x < 1255 and 400 < event.y < 475:
                    data.phase = 'buildS'
            if isLegalCity(data):
                if 1305 < event.x < 1455 and 300 < event.y < 375:
                    data.phase = 'buildC'
            if isLegalTrade(data):
                if 1305 < event.x < 1455 and 400 < event.y < 475:
                    data.phase = 'trade'
            #end turn button
            if 1300<event.x<1450 and 637.5<event.y<712.5:
                data.turn = 1
                data.phase = "roll"
                msg = "end 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())
    #if player decides to build road
    elif data.phase == 'buildR':
        buildRoad(event, data)
    #if player decides to build settlement
    elif data.phase == 'buildS':
        buildSettle(event, data)
    #if player decides to build city
    elif data.phase == 'buildC':
        buildCity(event, data)
    elif data.phase == 'trade':
        if woodPossible(data):
            if 1105 < event.x < 1255 and 250 < event.y < 325:
                data.phase = "woodTrade"
        if brickPossible(data):
            if 1105 < event.x < 1255 and 350 < event.y < 425:
                data.phase = "brickTrade"
        if wheatPossible(data):
            if 1105 < event.x < 1255 and 450 < event.y < 525:
                data.phase = "wheatTrade"
        if stonePossible(data):
            if 1305 < event.x < 1455 and 300 < event.y < 375:
                data.phase = "stoneTrade"
        if sheepPossible(data):
            if 1305 < event.x < 1455 and 400 < event.y < 475:
                data.phase = "sheepTrade"
    elif data.phase == 'woodTrade':
        tradeWood(event, data)
    elif data.phase == 'brickTrade':
        tradeBrick(event, data)
    elif data.phase == 'wheatTrade':
        tradeWheat(event, data)
    elif data.phase == 'stoneTrade':
        tradeStone(event, data)
    elif data.phase == 'sheepTrade':
        tradeSheep(event, data)

            
    
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
    
            if data.turn == 1 and int(data.me) == 1:
                if smallX<event.x<bigX and smallY<event.y<bigY:
                    data.p1Ex["settle"] += [coord]
                    if data.phase == "place2":
                        collectInitResources(data, coord)
                    updateOccupied(data)
                    msg = "placeSettlement %d %d\n"%(coord[0],coord[1])
                    print("msg keypressed is ", msg)
                    print("sending: ", msg)
                    data.server.send(msg.encode())
                    if data.phase == "place1":
                        data.prevPhase = "place1"
                    if data.phase == "place2":
                        data.prevPhase = "place2"
                    data.prevCoord = coord
                    data.phase = "placeR"
            if data.turn == 2 and int(data.me) == 2:
                if smallX<event.x<bigX and smallY<event.y<bigY:
                    data.p2Ex["settle"] += [coord]
                    if data.phase == "place2":
                        collectInitResources(data, coord)
                    updateOccupied(data)
                    msg = "placeSettlement %d %d\n"%(coord[0],coord[1])
                    print("msg keypressed is ", msg)
                    print("sending: ", msg)
                    data.server.send(msg.encode())
                    if data.phase == "place1":
                        data.prevPhase = "place1"
                    if data.phase == "place2":
                        data.prevPhase = "place2"
                    data.prevCoord = coord
                    data.phase = "placeR"
            if data.turn == 3 and int(data.me) == 3:
                if smallX<event.x<bigX and smallY<event.y<bigY:
                    data.p3Ex["settle"] += [coord]
                    if data.phase == "place2":
                        collectInitResources(data, coord)
                    updateOccupied(data)
                    msg = "placeSettlement %d %d\n"%(coord[0],coord[1])
                    print("msg keypressed is ", msg)
                    print("sending: ", msg)
                    data.server.send(msg.encode())
                    if data.phase == "place1":
                        data.prevPhase = "place1"
                    if data.phase == "place2":
                        data.prevPhase = "place2"
                    data.prevCoord = coord
                    data.phase = "placeR"
            if data.turn == 4 and int(data.me) == 4:
                if smallX<event.x<bigX and smallY<event.y<bigY:
                    data.p4Ex["settle"] += [coord]
                    if data.phase == "place2":
                        collectInitResources(data, coord)
                    updateOccupied(data)
                    msg = "placeSettlement %d %d\n"%(coord[0],coord[1])
                    print("msg keypressed is ", msg)
                    print("sending: ", msg)
                    data.server.send(msg.encode())
                    if data.phase == "place1":
                        data.prevPhase = "place1"
                    if data.phase == "place2":
                        data.prevPhase = "place2"
                    data.prevCoord = coord
                    data.phase = "placeR"
    elif data.phase == "placeR":
        roads = getLegalRoadInit(data)
        for road in roads:
            smallX = road[0]-10
            bigX = road[0]+10
            smallY = road[1]-10
            bigY = road[1]+10
            if data.turn == 1 and int(data.me) == 1:
                if smallX<event.x<bigX and smallY<event.y<bigY:
                    data.p1Ex["road"] += [road]
                    updateOccRoads(data)
                    msg = "placeRoad %f %f\n"%(road[0], road[1])
                    data.server.send(msg.encode())
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
            if data.turn == 2 and int(data.me) == 2:
                if smallX<event.x<bigX and smallY<event.y<bigY:
                    data.p2Ex["road"] += [road]
                    updateOccRoads(data)
                    msg = "placeRoad %f %f\n"%(road[0], road[1])
                    data.server.send(msg.encode())
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
            if data.turn == 3 and int(data.me) == 3:
                if smallX<event.x<bigX and smallY<event.y<bigY:
                    data.p3Ex["road"] += [road]
                    updateOccRoads(data)
                    msg = "placeRoad %f %f\n"%(road[0], road[1])
                    data.server.send(msg.encode())
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
            if data.turn == 4 and int(data.me) == 4:
                if smallX<event.x<bigX and smallY<event.y<bigY:
                    data.p4Ex["road"] += [road]
                    updateOccRoads(data)
                    msg = "placeRoad %f %f\n"%(road[0], road[1])
                    data.server.send(msg.encode())
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
    while (serverMsg.qsize() > 0):
        msg = serverMsg.get(False)
        try:
            print("received: ", msg, "\n")
            msg = msg.split()
            command = str(msg[0])
            print(msg)
        
            if command == "myIDis":
                myPID = msg[1]
                data.me = myPID
            
            elif command == "newPlayer":
                newPID = msg[1]
                data.otherPlayers[newPID] = newPID

            elif command == "placeSettlement":
                locationX = int(msg[2])
                locationY = int(msg[3])
                newCoord = (int(locationX), int(locationY))
                if data.turn == 1:
                    data.p1Ex['settle'] += [newCoord]
                elif data.turn == 2:
                    data.p2Ex['settle'] += [newCoord]
                elif data.turn == 3:
                    data.p3Ex['settle'] += [newCoord]
                elif data.turn == 4:
                    data.p4Ex['settle'] += [newCoord]
                updateOccupied(data)
                if data.phase == "place1":
                    data.prevPhase = "place1"
                if data.phase == "place2":
                    data.prevPhase = "place2"
                data.prevCoord = newCoord
                data.phase = "placeR"
            
            elif command == "settle":
                locationX = float(msg[2])
                locationY = float(msg[3])
                newCoord = (locationX, locationY)
                if data.turn == 1:
                    data.p1Ex['settle'] += [reverseCoords(newCoord)]
                elif data.turn == 2:
                    data.p2Ex['settle'] += [reverseCoords(newCoord)]
                elif data.turn == 3:
                    data.p3Ex['settle'] += [reverseCoords(newCoord)]
                elif data.turn == 4:
                    data.p4Ex['settle'] += [reverseCoords(newCoord)]
                updateOccupied(data)
                data.phase = "build"
                

            elif command == "placeRoad":
                locationX = float(msg[2])
                locationY = float(msg[3])
                newCoord = (locationX, locationY)
                if data.turn == 1:
                    data.p1Ex['road'] += [newCoord]
                elif data.turn == 2:
                    data.p2Ex['road'] += [newCoord]
                elif data.turn == 3:
                    data.p3Ex['road'] += [newCoord]
                elif data.turn == 4:
                    data.p4Ex['road'] += [newCoord]
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
            
            elif command == "road":
                locationX = float(msg[2])
                locationY = float(msg[3])
                newCoord = (locationX, locationY)
                if data.turn == 1:
                    data.p1Ex['road'] += [newCoord]
                elif data.turn == 2:
                    data.p2Ex['road'] += [newCoord]
                elif data.turn == 3:
                    data.p3Ex['road'] += [newCoord]
                elif data.turn == 4:
                    data.p4Ex['road'] += [newCoord]
                updateOccRoads(data)
                data.phase = "build"

            elif command == "rolled":
                data.roll = int(msg[2])
                collectResources(data)
                data.phase = "build"
            
            elif command == "end":
                if data.turn == 4:
                    data.round += 1
                    data.turn = 1
                else:
                    data.turn += 1
                data.phase = "roll"
            
            elif command == "city":
                locationX = float(msg[2])
                locationY = float(msg[3])
                newCoord = (locationX, locationY)
                if data.turn == 1:
                    data.p1Ex['city'] += [reverseCoords(newCoord)]
                    data.p1Ex["settle"].remove(reverseCoords(newCoord))
                elif data.turn == 2:
                    data.p2Ex['city'] += [reverseCoords(newCoord)]
                    data.p2Ex["settle"].remove(reverseCoords(newCoord))
                elif data.turn == 3:
                    data.p3Ex['city'] += [reverseCoords(newCoord)]
                    data.p3Ex["settle"].remove(reverseCoords(newCoord))
                elif data.turn == 4:
                    data.p4Ex['city'] += [reverseCoords(newCoord)]
                    data.p4Ex["settle"].remove(reverseCoords(newCoord))
                updateOccupied(data)
                data.phase = "build"
            
            elif command == "end1":
                data.screen = "end1"
            
            elif command == "end2":
                data.screen = "end2"
            
            elif command == "end3":
                data.screen = "end3"
            
            elif command == "end4":
                data.screen = "end4"
                
        except:
            print("failed!")
        serverMsg.task_done()

def redrawAll(canvas, data):
        ###
        #board stuff
        ###
    if data.screen == "game":
        drawBoard(canvas, data)
        drawPorts(canvas, data)
        drawExpansions(canvas, data)
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
        canvas.create_text(1000, 675, text = ("Number Rolled: %d" % data.roll), font = "Helvetica 50")
        if int(data.me) == 1:
            canvas.create_text(940, 275, text = "Wood: %d" % data.p1Res["wood"], font = "Helvetica 25")
            canvas.create_text(940, 325, text = "Brick: %d" % data.p1Res["brick"], font = "Helvetica 25")
            canvas.create_text(940, 375, text = "Wheat: %d" % data.p1Res["wheat"], font = "Helvetica 25")
            canvas.create_text(940, 425, text = "Stone: %d" % data.p1Res["stone"], font = "Helvetica 25")
            canvas.create_text(940, 475, text = "Sheep: %d" % data.p1Res["sheep"], font = "Helvetica 25")
        if int(data.me) == 2:
            canvas.create_text(940, 275, text = "Wood: %d" % data.p2Res["wood"], font = "Helvetica 25")
            canvas.create_text(940, 325, text = "Brick: %d" % data.p2Res["brick"], font = "Helvetica 25")
            canvas.create_text(940, 375, text = "Wheat: %d" % data.p2Res["wheat"], font = "Helvetica 25")
            canvas.create_text(940, 425, text = "Stone: %d" % data.p2Res["stone"], font = "Helvetica 25")
            canvas.create_text(940, 475, text = "Sheep: %d" % data.p2Res["sheep"], font = "Helvetica 25")
        if int(data.me) == 3:
            canvas.create_text(940, 275, text = "Wood: %d" % data.p3Res["wood"], font = "Helvetica 25")
            canvas.create_text(940, 325, text = "Brick: %d" % data.p3Res["brick"], font = "Helvetica 25")
            canvas.create_text(940, 375, text = "Wheat: %d" % data.p3Res["wheat"], font = "Helvetica 25")
            canvas.create_text(940, 425, text = "Stone: %d" % data.p3Res["stone"], font = "Helvetica 25")
            canvas.create_text(940, 475, text = "Sheep: %d" % data.p3Res["sheep"], font = "Helvetica 25")
        if int(data.me) == 4:
            canvas.create_text(940, 275, text = "Wood: %d" % data.p4Res["wood"], font = "Helvetica 25")
            canvas.create_text(940, 325, text = "Brick: %d" % data.p4Res["brick"], font = "Helvetica 25")
            canvas.create_text(940, 375, text = "Wheat: %d" % data.p4Res["wheat"], font = "Helvetica 25")
            canvas.create_text(940, 425, text = "Stone: %d" % data.p4Res["stone"], font = "Helvetica 25")
            canvas.create_text(940, 475, text = "Sheep: %d" % data.p4Res["sheep"], font = "Helvetica 25")
        if data.phase == "build":
            if (int(data.me) == 1 and data.turn == 1) or (int(data.me) == 2 and data.turn == 2) or (int(data.me) == 3 and data.turn == 3) or (int(data.me) == 4 and data.turn == 4):
                canvas.create_rectangle((1300, 637.5), (1450, 712.5), width= 5)
                canvas.create_text(1375, 675, text = "End Turn", font = "Helvetica 25")
        if data.phase == "place1" or data.phase == "place2":
            if (int(data.me) == 1 and data.turn == 1) or (int(data.me) == 2 and data.turn == 2) or (int(data.me) == 3 and data.turn == 3) or (int(data.me) == 4 and data.turn == 4):
                displayPossibleSetInit(canvas, data)
        if data.phase == "placeR":
            if (int(data.me) == 1 and data.turn == 1) or (int(data.me) == 2 and data.turn == 2) or (int(data.me) == 3 and data.turn == 3) or (int(data.me) == 4 and data.turn == 4):
                displayPossibleRoadInit(canvas, data)
        if data.phase == 'buildR':
            if (int(data.me) == 1 and data.turn == 1) or (int(data.me) == 2 and data.turn == 2) or (int(data.me) == 3 and data.turn == 3) or (int(data.me) == 4 and data.turn == 4):
                displayPossibleRoad(canvas, data)
        if data.phase == 'buildS':
            if (int(data.me) == 1 and data.turn == 1) or (int(data.me) == 2 and data.turn == 2) or (int(data.me) == 3 and data.turn == 3) or (int(data.me) == 4 and data.turn == 4):
                displayPossibleSettle(canvas, data)
        if data.phase == 'buildC':
            if (int(data.me) == 1 and data.turn == 1) or (int(data.me) == 2 and data.turn == 2) or (int(data.me) == 3 and data.turn == 3) or (int(data.me) == 4 and data.turn == 4):
                displayPossibleCity(canvas, data)
        #boxes
        if (int(data.me) == 1 and data.turn == 1) or (int(data.me) == 2 and data.turn == 2) or (int(data.me) == 3 and data.turn == 3) or (int(data.me) == 4 and data.turn == 4):
            if data.phase == 'build' and isLegalRoad(data):
                canvas.create_rectangle(1105, 300, 1255, 375, width = 5)
                canvas.create_text(1180, 337.5, text = "Buy Road", font = "Helvetica 15")
            if data.phase == 'build' and isLegalSettle(data):
                canvas.create_rectangle(1105, 400, 1255, 475, width = 5)
                canvas.create_text(1180, 437.5, text = "Buy Settlement", font = "Helvetica 15")
            if data.phase == 'build' and isLegalCity(data):
                canvas.create_rectangle(1305, 300, 1455, 375, width = 5)
                canvas.create_text(1380, 337.5, text = "Buy City", font = "Helvetica 15")
            if data.phase == 'build' and isLegalTrade(data):
                canvas.create_rectangle(1305, 400, 1455, 475, width = 5)
                canvas.create_text(1380, 437.5, text = "Trade", font = "Helvetica 15")
            if data.phase == 'trade' and woodPossible(data):
                canvas.create_rectangle(1105, 250, 1255, 325, width = 5)
                canvas.create_text(1180, 287.5, text = "Trade Wood %s" % data.woodPort, font = "Helvetica 12")
            if data.phase == 'trade' and brickPossible(data):
                canvas.create_rectangle(1105, 350, 1255, 425, width = 5)
                canvas.create_text(1180, 387.5, text = "Trade Brick %s" % data.brickPort, font = "Helvetica 12")
            if data.phase == 'trade' and wheatPossible(data):
                canvas.create_rectangle(1105, 450, 1255, 525, width = 5)
                canvas.create_text(1180, 487.5, text = "Trade Wheat %s" % data.wheatPort, font = "Helvetica 12")
            if data.phase == 'trade' and stonePossible(data):
                canvas.create_rectangle(1305, 300, 1455, 375, width = 5)
                canvas.create_text(1380, 337.5, text = "Trade Stone %s" % data.stonePort, font = "Helvetica 12")
            if data.phase == 'trade' and sheepPossible(data):
                canvas.create_rectangle(1305, 400, 1455, 475, width = 5)
                canvas.create_text(1380, 437.5, text = "Trade Sheep %s" % data.sheepPort, font = "Helvetica 12")
            if data.phase == 'woodTrade':
                canvas.create_rectangle(1105, 300, 1255, 375, width = 5)
                canvas.create_text(1180, 337.5, text = "Get 1 Brick", font = "Helvetica 15")
                canvas.create_rectangle(1105, 400, 1255, 475, width = 5)
                canvas.create_text(1180, 437.5, text = "Get 1 Wheat", font = "Helvetica 15")
                canvas.create_rectangle(1305, 300, 1455, 375, width = 5)
                canvas.create_text(1380, 337.5, text = "Get 1 Stone", font = "Helvetica 15")
                canvas.create_rectangle(1305, 400, 1455, 475, width = 5)
                canvas.create_text(1380, 437.5, text = "Get 1 Sheep", font = "Helvetica 15")
            if data.phase == 'brickTrade':
                canvas.create_rectangle(1105, 300, 1255, 375, width = 5)
                canvas.create_text(1180, 337.5, text = "Get 1 Wood", font = "Helvetica 15")
                canvas.create_rectangle(1105, 400, 1255, 475, width = 5)
                canvas.create_text(1180, 437.5, text = "Get 1 Wheat", font = "Helvetica 15")
                canvas.create_rectangle(1305, 300, 1455, 375, width = 5)
                canvas.create_text(1380, 337.5, text = "Get 1 Stone", font = "Helvetica 15")
                canvas.create_rectangle(1305, 400, 1455, 475, width = 5)
                canvas.create_text(1380, 437.5, text = "Get 1 Sheep", font = "Helvetica 15")
                canvas.create_rectangle(1105, 300, 1255, 375, width = 5)
            if data.phase == 'wheatTrade':
                canvas.create_rectangle(1105, 300, 1255, 375, width = 5)
                canvas.create_text(1180, 337.5, text = "Get 1 Wood", font = "Helvetica 15")
                canvas.create_rectangle(1105, 400, 1255, 475, width = 5)
                canvas.create_text(1180, 437.5, text = "Get 1 Brick", font = "Helvetica 15")
                canvas.create_rectangle(1305, 300, 1455, 375, width = 5)
                canvas.create_text(1380, 337.5, text = "Get 1 Stone", font = "Helvetica 15")
                canvas.create_rectangle(1305, 400, 1455, 475, width = 5)
                canvas.create_text(1380, 437.5, text = "Get 1 Sheep", font = "Helvetica 15")
            if data.phase == 'stoneTrade':
                canvas.create_rectangle(1105, 300, 1255, 375, width = 5)
                canvas.create_text(1180, 337.5, text = "Get 1 Wood", font = "Helvetica 15")
                canvas.create_rectangle(1105, 400, 1255, 475, width = 5)
                canvas.create_text(1180, 437.5, text = "Get 1 Brick", font = "Helvetica 15")
                canvas.create_rectangle(1305, 300, 1455, 375, width = 5)
                canvas.create_text(1380, 337.5, text = "Get 1 Wheat", font = "Helvetica 15")
                canvas.create_rectangle(1305, 400, 1455, 475, width = 5)
                canvas.create_text(1380, 437.5, text = "Get 1 Sheep", font = "Helvetica 15")
            if data.phase == 'sheepTrade':
                canvas.create_rectangle(1105, 300, 1255, 375, width = 5)
                canvas.create_text(1180, 337.5, text = "Get 1 Wood", font = "Helvetica 15")
                canvas.create_rectangle(1105, 400, 1255, 475, width = 5)
                canvas.create_text(1180, 437.5, text = "Get 1 Brick", font = "Helvetica 15")
                canvas.create_rectangle(1305, 300, 1455, 375, width = 5)
                canvas.create_text(1380, 337.5, text = "Get 1 Wheat", font = "Helvetica 15")
                canvas.create_rectangle(1305, 400, 1455, 475, width = 5)
                canvas.create_text(1380, 437.5, text = "Get 1 Stone", font = "Helvetica 15")
    if data.screen == "end1":
        canvas.create_text(data.width/2, data.height/2, text = "Player 1 Won!", font = "Helvetica 85")
    if data.screen == "end2":
        canvas.create_text(data.width/2, data.height/2, text = "Player 2 Won!", font = "Helvetica 85")
    if data.screen == "end3":
        canvas.create_text(data.width/2, data.height/2, text = "Player 3 Won!", font = "Helvetica 85")
    if data.screen == "end4":
        canvas.create_text(data.width/2, data.height/2, text = "Player 4 Won!", font = "Helvetica 85")

###################################
#Animation Framework
###################################

def run(width=300, height=300, serverMsg=None, server=None):
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
    data.server = server
    data.serverMsg = serverMsg
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

serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

run(1555, 750, serverMsg, server)
