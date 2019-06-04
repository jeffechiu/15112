import random
from essentials import *
from update import *
from getLegalRoad import *
from getLegalSettle import *
from getLegalCity import *

def buildRoad(event, data):
        coordsRoad = getLegalRoad(data)
        for coord in coordsRoad:
            #define limits in which to press button
            smallX = coord[0]-10
            bigX = coord[0]+10
            smallY = coord[1]-10
            bigY = coord[1]+10
            #if button pressed
            if smallX<event.x<bigX and smallY<event.y<bigY:
                #take out resources from player, and add road to the list of resources owned
                if data.turn == 1:
                    data.p1Ex["road"] += [coord]
                    data.p1Res['wood'] -= 1
                    data.p1Res['brick'] -= 1
                    msg = "road %f %f\n" % (coord[0], coord[1])
                    print("sending: ", msg)
                    data.server.send(msg.encode())
                if data.turn == 2:
                    data.p2Ex["road"] += [coord]
                    data.p2Res['wood'] -= 1
                    data.p2Res['brick'] -= 1
                    msg = "road %f %f\n" % (coord[0], coord[1])
                    print("sending: ", msg)
                    data.server.send(msg.encode())
                if data.turn == 3:
                    data.p3Ex["road"] += [coord]
                    data.p3Res['wood'] -= 1
                    data.p3Res['brick'] -= 1
                    msg = "road %f %f\n" % (coord[0], coord[1])
                    print("sending: ", msg)
                    data.server.send(msg.encode())
                if data.turn == 4:
                    data.p4Ex["road"] += [coord]
                    data.p4Res['wood'] -= 1
                    data.p4Res['brick'] -= 1
                    msg = "road %f %f\n" % (coord[0], coord[1])
                    print("sending: ", msg)
                    data.server.send(msg.encode())
                #update the occupied roads, and revert back to build phase
                updateOccRoads(data)
                data.phase = "build"

def buildSettle(event, data):
    coordsSet = getLegalSettle(data)
    for coord in coordsSet:
        #define limits in which to press button
        smallX = coord[0]-10
        bigX = coord[0]+10
        smallY = coord[1]-10
        bigY = coord[1]+10
        #if button pressed
        if smallX<event.x<bigX and smallY<event.y<bigY:
            #take out resources from player, and add settlement to the list of resources owned
            if data.turn == 1:
                data.p1Ex["settle"] += [reverseCoords(coord)]
                data.p1Res['wood'] -= 1
                data.p1Res['brick'] -= 1
                data.p1Res['wheat'] -= 1
                data.p1Res['sheep'] -= 1
                msg = "settle %f %f\n" % (coord[0], coord[1])
                print("sending: ", msg)
                data.server.send(msg.encode())
                #if building settlement causes player to equal or go above 10 points, end game
            if data.turn == 2:
                data.p2Ex["settle"] += [reverseCoords(coord)]
                data.p2Res['wood'] -= 1
                data.p2Res['brick'] -= 1
                data.p2Res['wheat'] -= 1
                data.p2Res['sheep'] -= 1
                msg = "settle %f %f\n" % (coord[0], coord[1])
                print("sending: ", msg)
                data.server.send(msg.encode())
            if data.turn == 3:
                data.p3Ex["settle"] += [reverseCoords(coord)]
                data.p3Res['wood'] -= 1
                data.p3Res['brick'] -= 1
                data.p3Res['wheat'] -= 1
                data.p3Res['sheep'] -= 1
                msg = "settle %f %f\n" % (coord[0], coord[1])
                print("sending: ", msg)
                data.server.send(msg.encode())
            if data.turn == 4:
                data.p4Ex["settle"] += [reverseCoords(coord)]
                data.p4Res['wood'] -= 1
                data.p4Res['brick'] -= 1
                data.p4Res['wheat'] -= 1
                data.p4Res['sheep'] -= 1
                msg = "settle %f %f\n" % (coord[0], coord[1])
                print("sending: ", msg)
                data.server.send(msg.encode())
            #update the occupied expansions, and revert back to build phase
            updateOccupied(data)
            if data.p1Sc >= 10:
                data.screen = "end1"        
                msg = "end1 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())       
            if data.p2Sc >= 10:
                data.screen = "end2"
                msg = "end2 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())
            if data.p3Sc >= 10:
                data.screen = "end3"
                msg = "end3 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())
            if data.p4Sc >= 10:
                data.screen = "end4"
                msg = "end4 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())
            data.phase = "build"

def buildCity(event, data):
    coordsCity = getLegalCity(data)
    for coord in coordsCity:
        smallX = coord[0] - 10
        bigX = coord[0] + 10
        smallY = coord[1] - 10
        bigY = coord[1] + 10
        if smallX<event.x<bigX and smallY<event.y<bigY:
            if data.turn == 1:
                data.p1Ex["city"] += [reverseCoords(coord)]
                data.p1Ex["settle"].remove(reverseCoords(coord))
                data.p1Res['wheat'] -= 2
                data.p1Res['stone'] -= 3
                msg = "city %f %f\n" % (coord[0], coord[1])
                print("sending: ", msg)
                data.server.send(msg.encode())
            if data.turn == 2:
                data.p2Ex["city"] += [reverseCoords(coord)]
                data.p2Ex["settle"].remove(reverseCoords(coord))
                data.p2Res['wheat'] -= 2
                data.p2Res['stone'] -= 3
                msg = "city %f %f\n" % (coord[0], coord[1])
                print("sending: ", msg)
                data.server.send(msg.encode())
            if data.turn == 3:
                data.p3Ex["city"] += [reverseCoords(coord)]
                data.p3Ex["settle"].remove(reverseCoords(coord))
                data.p3Res['wheat'] -= 2
                data.p3Res['stone'] -= 3
                msg = "city %f %f\n" % (coord[0], coord[1])
                print("sending: ", msg)
                data.server.send(msg.encode())
            if data.turn == 4:
                data.p4Ex["city"] += [reverseCoords(coord)]
                data.p4Ex["settle"].remove(reverseCoords(coord))
                data.p4Res['wheat'] -= 2
                data.p4Res['stone'] -= 3
                msg = "city %f %f\n" % (coord[0], coord[1])
                print("sending: ", msg)
                data.server.send(msg.encode())
            updateOccupied(data)
            if data.p1Sc >= 10:
                data.screen = "end1"        
                msg = "end1 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())       
            if data.p2Sc >= 10:
                data.screen = "end2"
                msg = "end2 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())
            if data.p3Sc >= 10:
                data.screen = "end3"
                msg = "end3 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())
            if data.p4Sc >= 10:
                data.screen = "end4"
                msg = "end4 5\n"
                print("sending: ", msg)
                data.server.send(msg.encode())
            data.phase = "build"

def buyDev(data):
    card = random.choice(data.devCards)
    data.devCards.remove(card)
    if card == 'knight':
        data.tempCards += ['knight']
        data.phase = 'knight'
    if card == 'road':
        data.tempCards += ['road']
        data.phase = 'road'
    if card == 'monopoly':
        data.tempCards += ['monopoly']
        data.phase = 'monopoly'
    if card == 'resource':
        data.tempCards += ['resource']
        data.phase = 'resource'
    if data.turn == 1:
        data.p1Res['sheep'] -= 1
        data.p1Res['wheat'] -= 1
        data.p1Res['stone'] -= 1
        if card == 'point':
            data.p1Dev['point'] += 1
            data.phase = 'point'
    if data.turn == 2:
        data.p2Res['sheep'] -= 1
        data.p2Res['wheat'] -= 1
        data.p2Res['stone'] -= 1
        if card == 'point':
            data.p2Dev['point'] += 1
            data.phase = 'point'
    if data.turn == 3:
        data.p3Res['sheep'] -= 1
        data.p3Res['wheat'] -= 1
        data.p3Res['stone'] -= 1
        if card == 'point':
            data.p3Dev['point'] += 1
            data.phase = 'point'
    if data.turn == 4:
        data.p4Res['sheep'] -= 1
        data.p4Res['wheat'] -= 1
        data.p4Res['stone'] -= 1
        if card == 'point':
            data.p4Dev['point'] += 1
            data.phase = 'point'

# def playDev(event, data):
    