from getLegalRoad import *
from getLegalSettle import *
from getLegalCity import *

def isLegalRoad(data):
    if data.turn == 1:
        if data.p1Res['brick'] >= 1 and data.p1Res['wood'] >= 1 and len(getLegalRoad(data)) > 0:
            return True
        else:
            return False
    if data.turn == 2:
        if data.p2Res['brick'] >= 1 and data.p2Res['wood'] >= 1 and len(getLegalRoad(data)) > 0:
            return True
        else:
            return False
    if data.turn == 3:
        if data.p3Res['brick'] >= 1 and data.p3Res['wood'] >= 1 and len(getLegalRoad(data)) > 0:
            return True
        else:
            return False
    if data.turn == 4:
        if data.p4Res['brick'] >= 1 and data.p4Res['wood'] >= 1 and len(getLegalRoad(data)) > 0:
            return True
        else:
            return False

def isLegalSettle(data):
    if data.turn == 1:
        if data.p1Res['wood'] >= 1 and data.p1Res['brick'] >= 1 and data.p1Res['wheat'] >= 1 and data.p1Res['sheep'] >= 1 and len(getLegalSettle(data)) > 0:
            return True
        else:
            return False
    if data.turn == 2:
        if data.p2Res['wood'] >= 1 and data.p2Res['brick'] >= 1 and data.p2Res['wheat'] >= 1 and data.p2Res['sheep'] >= 1 and len(getLegalSettle(data)) > 0:
            return True
        else:
            return False
    if data.turn == 3:
        if data.p3Res['wood'] >= 1 and data.p3Res['brick'] >= 1 and data.p3Res['wheat'] >= 1 and data.p3Res['sheep'] >= 1 and len(getLegalSettle(data)) > 0:
            return True
        else:
            return False
    if data.turn == 4:
        if data.p4Res['wood'] >= 1 and data.p4Res['brick'] >= 1 and data.p4Res['wheat'] >= 1 and data.p4Res['sheep'] >= 1 and len(getLegalSettle(data)) > 0:
            return True
        else:
            return False

def isLegalCity(data):
    if data.turn == 1:
        if data.p1Res['wheat'] >= 2 and data.p1Res['stone'] >= 3 and len(getLegalCity(data)) > 0:
            return True
        else:
            return False
    if data.turn == 2:
        if data.p2Res['wheat'] >= 2 and data.p2Res['stone'] >= 3 and len(getLegalCity(data)) > 0:
            return True
        else:
            return False
    if data.turn == 3:
        if data.p3Res['wheat'] >= 2 and data.p3Res['stone'] >= 3 and len(getLegalCity(data)) > 0:
            return True
        else:
            return False
    if data.turn == 4:
        if data.p4Res['wheat'] >= 2 and data.p4Res['stone'] >= 3 and len(getLegalCity(data)) > 0:
            return True
        else:
            return False

def isLegalDev(data):
    if data.turn == 1:
        if data.p1Res['wheat'] >= 1 and data.p1Res['sheep'] >= 1 and data.p1Res['stone'] >= 1 and len(data.devCards) >= 1:
            return True
        else:
            return False
    if data.turn == 2:
        if data.p2Res['wheat'] >= 1 and data.p2Res['sheep'] >= 1 and data.p2Res['stone'] >= 1 and len(data.devCards) >= 1:
            return True
        else:
            return False
    if data.turn == 3:
        if data.p3Res['wheat'] >= 1 and data.p3Res['sheep'] >= 1 and data.p3Res['stone'] >= 1 and len(data.devCards) >= 1:
            return True
        else:
            return False
    if data.turn == 4:
        if data.p4Res['wheat'] >= 1 and data.p4Res['sheep'] >= 1 and data.p4Res['stone'] >= 1 and len(data.devCards) >= 1:
            return True
        else:
            return False

def isLegalPlayDev(data):
    if data.devPlayed: return False
    num = 0
    if data.turn == 1:
        for key in data.p1Dev:
            num += data.p1Dev[key]
    if data.turn == 2:
        for key in data.p2Dev:
            num += data.p2Dev[key]
    if data.turn == 3:
        for key in data.p3Dev:
            num += data.p3Dev[key]
    if data.turn == 4:
        for key in data.p4Dev:
            num += data.p4Dev[key]
    return num > 0