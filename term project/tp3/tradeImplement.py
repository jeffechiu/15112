def tradeWood(event, data):
    if data.turn == 1:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.woodPort == "4:1":
                data.p1Res['wood'] -= 4
                data.p1Res['brick'] += 1
            if data.woodPort == "3:1":
                data.p1Res['wood'] -= 3
                data.p1Res['brick'] += 1
            if data.woodPort == "2:1":
                data.p1Res['wood'] -= 2
                data.p1Res['brick'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.woodPort == "4:1":
                data.p1Res['wood'] -= 4
                data.p1Res['wheat'] += 1
            if data.woodPort == "3:1":
                data.p1Res['wood'] -= 3
                data.p1Res['wheat'] += 1
            if data.woodPort == "2:1":
                data.p1Res['wood'] -= 2
                data.p1Res['wheat'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.woodPort == "4:1":
                data.p1Res['wood'] -= 4
                data.p1Res['stone'] += 1
            if data.woodPort == "3:1":
                data.p1Res['wood'] -= 3
                data.p1Res['stone'] += 1
            if data.woodPort == "2:1":
                data.p1Res['wood'] -= 2
                data.p1Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.woodPort == "4:1":
                data.p1Res['wood'] -= 4
                data.p1Res['sheep'] += 1
            if data.woodPort == "3:1":
                data.p1Res['wood'] -= 3
                data.p1Res['sheep'] += 1
            if data.woodPort == "2:1":
                data.p1Res['wood'] -= 2
                data.p1Res['sheep'] += 1
    if data.turn == 2:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.woodPort == "4:1":
                data.p2Res['wood'] -= 4
                data.p2Res['brick'] += 1
            if data.woodPort == "3:1":
                data.p2Res['wood'] -= 3
                data.p2Res['brick'] += 1
            if data.woodPort == "2:1":
                data.p2Res['wood'] -= 2
                data.p2Res['brick'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.woodPort == "4:1":
                data.p2Res['wood'] -= 4
                data.p2Res['wheat'] += 1
            if data.woodPort == "3:1":
                data.p2Res['wood'] -= 3
                data.p2Res['wheat'] += 1
            if data.woodPort == "2:1":
                data.p2Res['wood'] -= 2
                data.p2Res['wheat'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.woodPort == "4:1":
                data.p2Res['wood'] -= 4
                data.p2Res['stone'] += 1
            if data.woodPort == "3:1":
                data.p2Res['wood'] -= 3
                data.p2Res['stone'] += 1
            if data.woodPort == "2:1":
                data.p2Res['wood'] -= 2
                data.p2Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.woodPort == "4:1":
                data.p2Res['wood'] -= 4
                data.p2Res['sheep'] += 1
            if data.woodPort == "3:1":
                data.p2Res['wood'] -= 3
                data.p2Res['sheep'] += 1
            if data.woodPort == "2:1":
                data.p2Res['wood'] -= 2
                data.p2Res['sheep'] += 1
    if data.turn == 3:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.woodPort == "4:1":
                data.p3Res['wood'] -= 4
                data.p3Res['brick'] += 1
            if data.woodPort == "3:1":
                data.p3Res['wood'] -= 3
                data.p3Res['brick'] += 1
            if data.woodPort == "2:1":
                data.p3Res['wood'] -= 2
                data.p3Res['brick'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.woodPort == "4:1":
                data.p3Res['wood'] -= 4
                data.p3Res['wheat'] += 1
            if data.woodPort == "3:1":
                data.p3Res['wood'] -= 3
                data.p3Res['wheat'] += 1
            if data.woodPort == "2:1":
                data.p3Res['wood'] -= 2
                data.p3Res['wheat'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.woodPort == "4:1":
                data.p3Res['wood'] -= 4
                data.p3Res['stone'] += 1
            if data.woodPort == "3:1":
                data.p3Res['wood'] -= 3
                data.p3Res['stone'] += 1
            if data.woodPort == "2:1":
                data.p3Res['wood'] -= 2
                data.p3Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.woodPort == "4:1":
                data.p3Res['wood'] -= 4
                data.p3Res['sheep'] += 1
            if data.woodPort == "3:1":
                data.p3Res['wood'] -= 3
                data.p3Res['sheep'] += 1
            if data.woodPort == "2:1":
                data.p3Res['wood'] -= 2
                data.p3Res['sheep'] += 1
    if data.turn == 4:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.woodPort == "4:1":
                data.p4Res['wood'] -= 4
                data.p4Res['brick'] += 1
            if data.woodPort == "3:1":
                data.p4Res['wood'] -= 3
                data.p4Res['brick'] += 1
            if data.woodPort == "2:1":
                data.p4Res['wood'] -= 2
                data.p4Res['brick'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.woodPort == "4:1":
                data.p4Res['wood'] -= 4
                data.p4Res['wheat'] += 1
            if data.woodPort == "3:1":
                data.p4Res['wood'] -= 3
                data.p4Res['wheat'] += 1
            if data.woodPort == "2:1":
                data.p4Res['wood'] -= 2
                data.p4Res['wheat'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.woodPort == "4:1":
                data.p4Res['wood'] -= 4
                data.p4Res['stone'] += 1
            if data.woodPort == "3:1":
                data.p4Res['wood'] -= 3
                data.p4Res['stone'] += 1
            if data.woodPort == "2:1":
                data.p4Res['wood'] -= 2
                data.p4Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.woodPort == "4:1":
                data.p4Res['wood'] -= 4
                data.p4Res['sheep'] += 1
            if data.woodPort == "3:1":
                data.p4Res['wood'] -= 3
                data.p4Res['sheep'] += 1
            if data.woodPort == "2:1":
                data.p4Res['wood'] -= 2
                data.p4Res['sheep'] += 1
    data.phase = "build"

def tradeBrick(event, data):
    if data.turn == 1:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.brickPort == "4:1":
                data.p1Res['brick'] -= 4
                data.p1Res['wood'] += 1
            if data.brickPort == "3:1":
                data.p1Res['brick'] -= 3
                data.p1Res['wood'] += 1
            if data.brickPort == "2:1":
                data.p1Res['brick'] -= 2
                data.p1Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.brickPort == "4:1":
                data.p1Res['brick'] -= 4
                data.p1Res['wheat'] += 1
            if data.brickPort == "3:1":
                data.p1Res['brick'] -= 3
                data.p1Res['wheat'] += 1
            if data.brickPort == "2:1":
                data.p1Res['brick'] -= 2
                data.p1Res['wheat'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.brickPort == "4:1":
                data.p1Res['brick'] -= 4
                data.p1Res['stone'] += 1
            if data.brickPort == "3:1":
                data.p1Res['brick'] -= 3
                data.p1Res['stone'] += 1
            if data.brickPort == "2:1":
                data.p1Res['brick'] -= 2
                data.p1Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.brickPort == "4:1":
                data.p1Res['brick'] -= 4
                data.p1Res['sheep'] += 1
            if data.brickPort == "3:1":
                data.p1Res['brick'] -= 3
                data.p1Res['sheep'] += 1
            if data.brickPort == "2:1":
                data.p1Res['brick'] -= 2
                data.p1Res['sheep'] += 1
    if data.turn == 2:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.brickPort == "4:1":
                data.p2Res['brick'] -= 4
                data.p2Res['wood'] += 1
            if data.brickPort == "3:1":
                data.p2Res['brick'] -= 3
                data.p2Res['wood'] += 1
            if data.brickPort == "2:1":
                data.p2Res['brick'] -= 2
                data.p2Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.brickPort == "4:1":
                data.p2Res['brick'] -= 4
                data.p2Res['wheat'] += 1
            if data.brickPort == "3:1":
                data.p2Res['brick'] -= 3
                data.p2Res['wheat'] += 1
            if data.brickPort == "2:1":
                data.p2Res['brick'] -= 2
                data.p2Res['wheat'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.brickPort == "4:1":
                data.p2Res['brick'] -= 4
                data.p2Res['stone'] += 1
            if data.brickPort == "3:1":
                data.p2Res['brick'] -= 3
                data.p2Res['stone'] += 1
            if data.brickPort == "2:1":
                data.p2Res['brick'] -= 2
                data.p2Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.brickPort == "4:1":
                data.p2Res['brick'] -= 4
                data.p2Res['sheep'] += 1
            if data.brickPort == "3:1":
                data.p2Res['brick'] -= 3
                data.p2Res['sheep'] += 1
            if data.brickPort == "2:1":
                data.p2Res['brick'] -= 2
                data.p2Res['sheep'] += 1
    if data.turn == 3:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.brickPort == "4:1":
                data.p3Res['brick'] -= 4
                data.p3Res['wood'] += 1
            if data.brickPort == "3:1":
                data.p3Res['brick'] -= 3
                data.p3Res['wood'] += 1
            if data.brickPort == "2:1":
                data.p3Res['brick'] -= 2
                data.p3Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.brickPort == "4:1":
                data.p3Res['brick'] -= 4
                data.p3Res['wheat'] += 1
            if data.brickPort == "3:1":
                data.p3Res['brick'] -= 3
                data.p3Res['wheat'] += 1
            if data.brickPort == "2:1":
                data.p3Res['brick'] -= 2
                data.p3Res['wheat'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.brickPort == "4:1":
                data.p3Res['brick'] -= 4
                data.p3Res['stone'] += 1
            if data.brickPort == "3:1":
                data.p3Res['brick'] -= 3
                data.p3Res['stone'] += 1
            if data.brickPort == "2:1":
                data.p3Res['brick'] -= 2
                data.p3Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.brickPort == "4:1":
                data.p3Res['brick'] -= 4
                data.p3Res['sheep'] += 1
            if data.brickPort == "3:1":
                data.p3Res['brick'] -= 3
                data.p3Res['sheep'] += 1
            if data.brickPort == "2:1":
                data.p3Res['brick'] -= 2
                data.p3Res['sheep'] += 1
    if data.turn == 4:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.brickPort == "4:1":
                data.p4Res['brick'] -= 4
                data.p4Res['wood'] += 1
            if data.brickPort == "3:1":
                data.p4Res['brick'] -= 3
                data.p4Res['wood'] += 1
            if data.brickPort == "2:1":
                data.p4Res['brick'] -= 2
                data.p4Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.brickPort == "4:1":
                data.p4Res['brick'] -= 4
                data.p4Res['wheat'] += 1
            if data.brickPort == "3:1":
                data.p4Res['brick'] -= 3
                data.p4Res['wheat'] += 1
            if data.brickPort == "2:1":
                data.p4Res['brick'] -= 2
                data.p4Res['wheat'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.brickPort == "4:1":
                data.p4Res['brick'] -= 4
                data.p4Res['stone'] += 1
            if data.brickPort == "3:1":
                data.p4Res['brick'] -= 3
                data.p4Res['stone'] += 1
            if data.brickPort == "2:1":
                data.p4Res['brick'] -= 2
                data.p4Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.brickPort == "4:1":
                data.p4Res['brick'] -= 4
                data.p4Res['sheep'] += 1
            if data.brickPort == "3:1":
                data.p4Res['brick'] -= 3
                data.p4Res['sheep'] += 1
            if data.brickPort == "2:1":
                data.p4Res['brick'] -= 2
                data.p4Res['sheep'] += 1
    data.phase = "build"

def tradeWheat(event, data):
    if data.turn == 1:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.wheatPort == "4:1":
                data.p1Res['wheat'] -= 4
                data.p1Res['wood'] += 1
            if data.wheatPort == "3:1":
                data.p1Res['wheat'] -= 3
                data.p1Res['wood'] += 1
            if data.wheatPort == "2:1":
                data.p1Res['wheat'] -= 2
                data.p1Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.wheatPort == "4:1":
                data.p1Res['wheat'] -= 4
                data.p1Res['brick'] += 1
            if data.wheatPort == "3:1":
                data.p1Res['wheat'] -= 3
                data.p1Res['brick'] += 1
            if data.wheatPort == "2:1":
                data.p1Res['wheat'] -= 2
                data.p1Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.wheatPort == "4:1":
                data.p1Res['wheat'] -= 4
                data.p1Res['stone'] += 1
            if data.wheatPort == "3:1":
                data.p1Res['wheat'] -= 3
                data.p1Res['stone'] += 1
            if data.wheatPort == "2:1":
                data.p1Res['wheat'] -= 2
                data.p1Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.wheatPort == "4:1":
                data.p1Res['wheat'] -= 4
                data.p1Res['sheep'] += 1
            if data.wheatPort == "3:1":
                data.p1Res['wheat'] -= 3
                data.p1Res['sheep'] += 1
            if data.wheatPort == "2:1":
                data.p1Res['wheat'] -= 2
                data.p1Res['sheep'] += 1
    if data.turn == 2:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.wheatPort == "4:1":
                data.p2Res['wheat'] -= 4
                data.p2Res['wood'] += 1
            if data.wheatPort == "3:1":
                data.p2Res['wheat'] -= 3
                data.p2Res['wood'] += 1
            if data.wheatPort == "2:1":
                data.p2Res['wheat'] -= 2
                data.p2Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.wheatPort == "4:1":
                data.p2Res['wheat'] -= 4
                data.p2Res['brick'] += 1
            if data.wheatPort == "3:1":
                data.p2Res['wheat'] -= 3
                data.p2Res['brick'] += 1
            if data.wheatPort == "2:1":
                data.p2Res['wheat'] -= 2
                data.p2Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.wheatPort == "4:1":
                data.p2Res['wheat'] -= 4
                data.p2Res['stone'] += 1
            if data.wheatPort == "3:1":
                data.p2Res['wheat'] -= 3
                data.p2Res['stone'] += 1
            if data.wheatPort == "2:1":
                data.p2Res['wheat'] -= 2
                data.p2Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.wheatPort == "4:1":
                data.p2Res['wheat'] -= 4
                data.p2Res['sheep'] += 1
            if data.wheatPort == "3:1":
                data.p2Res['wheat'] -= 3
                data.p2Res['sheep'] += 1
            if data.wheatPort == "2:1":
                data.p2Res['wheat'] -= 2
                data.p2Res['sheep'] += 1
    if data.turn == 3:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.wheatPort == "4:1":
                data.p3Res['wheat'] -= 4
                data.p3Res['wood'] += 1
            if data.wheatPort == "3:1":
                data.p3Res['wheat'] -= 3
                data.p3Res['wood'] += 1
            if data.wheatPort == "2:1":
                data.p3Res['wheat'] -= 2
                data.p3Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.wheatPort == "4:1":
                data.p3Res['wheat'] -= 4
                data.p3Res['brick'] += 1
            if data.wheatPort == "3:1":
                data.p3Res['wheat'] -= 3
                data.p3Res['brick'] += 1
            if data.wheatPort == "2:1":
                data.p3Res['wheat'] -= 2
                data.p3Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.wheatPort == "4:1":
                data.p3Res['wheat'] -= 4
                data.p3Res['stone'] += 1
            if data.wheatPort == "3:1":
                data.p3Res['wheat'] -= 3
                data.p3Res['stone'] += 1
            if data.wheatPort == "2:1":
                data.p3Res['wheat'] -= 2
                data.p3Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.wheatPort == "4:1":
                data.p3Res['wheat'] -= 4
                data.p3Res['sheep'] += 1
            if data.wheatPort == "3:1":
                data.p3Res['wheat'] -= 3
                data.p3Res['sheep'] += 1
            if data.wheatPort == "2:1":
                data.p3Res['wheat'] -= 2
                data.p3Res['sheep'] += 1
    if data.turn == 4:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.wheatPort == "4:1":
                data.p4Res['wheat'] -= 4
                data.p4Res['wood'] += 1
            if data.wheatPort == "3:1":
                data.p4Res['wheat'] -= 3
                data.p4Res['wood'] += 1
            if data.wheatPort == "2:1":
                data.p4Res['wheat'] -= 2
                data.p4Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.wheatPort == "4:1":
                data.p4Res['wheat'] -= 4
                data.p4Res['brick'] += 1
            if data.wheatPort == "3:1":
                data.p4Res['wheat'] -= 3
                data.p4Res['brick'] += 1
            if data.wheatPort == "2:1":
                data.p4Res['wheat'] -= 2
                data.p4Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.wheatPort == "4:1":
                data.p4Res['wheat'] -= 4
                data.p4Res['stone'] += 1
            if data.wheatPort == "3:1":
                data.p4Res['wheat'] -= 3
                data.p4Res['stone'] += 1
            if data.wheatPort == "2:1":
                data.p4Res['wheat'] -= 2
                data.p4Res['stone'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.wheatPort == "4:1":
                data.p4Res['wheat'] -= 4
                data.p4Res['sheep'] += 1
            if data.wheatPort == "3:1":
                data.p4Res['wheat'] -= 3
                data.p4Res['sheep'] += 1
            if data.wheatPort == "2:1":
                data.p4Res['wheat'] -= 2
                data.p4Res['sheep'] += 1
    data.phase = "build"

def tradeStone(event, data):
    if data.turn == 1:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.stonePort == "4:1":
                data.p1Res['stone'] -= 4
                data.p1Res['wood'] += 1
            if data.stonePort == "3:1":
                data.p1Res['stone'] -= 3
                data.p1Res['wood'] += 1
            if data.stonePort == "2:1":
                data.p1Res['stone'] -= 2
                data.p1Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.stonePort == "4:1":
                data.p1Res['stone'] -= 4
                data.p1Res['brick'] += 1
            if data.stonePort == "3:1":
                data.p1Res['stone'] -= 3
                data.p1Res['brick'] += 1
            if data.stonePort == "2:1":
                data.p1Res['stone'] -= 2
                data.p1Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.stonePort == "4:1":
                data.p1Res['stone'] -= 4
                data.p1Res['wheat'] += 1
            if data.stonePort == "3:1":
                data.p1Res['stone'] -= 3
                data.p1Res['wheat'] += 1
            if data.stonePort == "2:1":
                data.p1Res['stone'] -= 2
                data.p1Res['wheat'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.stonePort == "4:1":
                data.p1Res['stone'] -= 4
                data.p1Res['sheep'] += 1
            if data.stonePort == "3:1":
                data.p1Res['stone'] -= 3
                data.p1Res['sheep'] += 1
            if data.stonePort == "2:1":
                data.p1Res['stone'] -= 2
                data.p1Res['sheep'] += 1
    if data.turn == 2:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.stonePort == "4:1":
                data.p2Res['stone'] -= 4
                data.p2Res['wood'] += 1
            if data.stonePort == "3:1":
                data.p2Res['stone'] -= 3
                data.p2Res['wood'] += 1
            if data.stonePort == "2:1":
                data.p2Res['stone'] -= 2
                data.p2Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.stonePort == "4:1":
                data.p2Res['stone'] -= 4
                data.p2Res['brick'] += 1
            if data.stonePort == "3:1":
                data.p2Res['stone'] -= 3
                data.p2Res['brick'] += 1
            if data.stonePort == "2:1":
                data.p2Res['stone'] -= 2
                data.p2Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.stonePort == "4:1":
                data.p2Res['stone'] -= 4
                data.p2Res['wheat'] += 1
            if data.stonePort == "3:1":
                data.p2Res['stone'] -= 3
                data.p2Res['wheat'] += 1
            if data.stonePort == "2:1":
                data.p2Res['stone'] -= 2
                data.p2Res['wheat'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.stonePort == "4:1":
                data.p2Res['stone'] -= 4
                data.p2Res['sheep'] += 1
            if data.stonePort == "3:1":
                data.p2Res['stone'] -= 3
                data.p2Res['sheep'] += 1
            if data.stonePort == "2:1":
                data.p2Res['stone'] -= 2
                data.p2Res['sheep'] += 1
    if data.turn == 3:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.stonePort == "4:1":
                data.p3Res['stone'] -= 4
                data.p3Res['wood'] += 1
            if data.stonePort == "3:1":
                data.p3Res['stone'] -= 3
                data.p3Res['wood'] += 1
            if data.stonePort == "2:1":
                data.p3Res['stone'] -= 2
                data.p3Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.stonePort == "4:1":
                data.p3Res['stone'] -= 4
                data.p3Res['brick'] += 1
            if data.stonePort == "3:1":
                data.p3Res['stone'] -= 3
                data.p3Res['brick'] += 1
            if data.stonePort == "2:1":
                data.p3Res['stone'] -= 2
                data.p3Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.stonePort == "4:1":
                data.p3Res['stone'] -= 4
                data.p3Res['wheat'] += 1
            if data.stonePort == "3:1":
                data.p3Res['stone'] -= 3
                data.p3Res['wheat'] += 1
            if data.stonePort == "2:1":
                data.p3Res['stone'] -= 2
                data.p3Res['wheat'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.stonePort == "4:1":
                data.p3Res['stone'] -= 4
                data.p3Res['sheep'] += 1
            if data.stonePort == "3:1":
                data.p3Res['stone'] -= 3
                data.p3Res['sheep'] += 1
            if data.stonePort == "2:1":
                data.p3Res['stone'] -= 2
                data.p3Res['sheep'] += 1
    if data.turn == 4:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.stonePort == "4:1":
                data.p4Res['stone'] -= 4
                data.p4Res['wood'] += 1
            if data.stonePort == "3:1":
                data.p4Res['stone'] -= 3
                data.p4Res['wood'] += 1
            if data.stonePort == "2:1":
                data.p4Res['stone'] -= 2
                data.p4Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.stonePort == "4:1":
                data.p4Res['stone'] -= 4
                data.p4Res['brick'] += 1
            if data.stonePort == "3:1":
                data.p4Res['stone'] -= 3
                data.p4Res['brick'] += 1
            if data.stonePort == "2:1":
                data.p4Res['stone'] -= 2
                data.p4Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.stonePort == "4:1":
                data.p4Res['stone'] -= 4
                data.p4Res['wheat'] += 1
            if data.stonePort == "3:1":
                data.p4Res['stone'] -= 3
                data.p4Res['wheat'] += 1
            if data.stonePort == "2:1":
                data.p4Res['stone'] -= 2
                data.p4Res['wheat'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.stonePort == "4:1":
                data.p4Res['stone'] -= 4
                data.p4Res['sheep'] += 1
            if data.stonePort == "3:1":
                data.p4Res['stone'] -= 3
                data.p4Res['sheep'] += 1
            if data.stonePort == "2:1":
                data.p4Res['stone'] -= 2
                data.p4Res['sheep'] += 1
    data.phase = "build"

def tradeSheep(event, data):
    if data.turn == 1:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.sheepPort == "4:1":
                data.p1Res['sheep'] -= 4
                data.p1Res['wood'] += 1
            if data.sheepPort == "3:1":
                data.p1Res['sheep'] -= 3
                data.p1Res['wood'] += 1
            if data.sheepPort == "2:1":
                data.p1Res['sheep'] -= 2
                data.p1Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.sheepPort == "4:1":
                data.p1Res['sheep'] -= 4
                data.p1Res['brick'] += 1
            if data.sheepPort == "3:1":
                data.p1Res['sheep'] -= 3
                data.p1Res['brick'] += 1
            if data.sheepPort == "2:1":
                data.p1Res['sheep'] -= 2
                data.p1Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.sheepPort == "4:1":
                data.p1Res['sheep'] -= 4
                data.p1Res['wheat'] += 1
            if data.sheepPort == "3:1":
                data.p1Res['sheep'] -= 3
                data.p1Res['wheat'] += 1
            if data.sheepPort == "2:1":
                data.p1Res['sheep'] -= 2
                data.p1Res['wheat'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.sheepPort == "4:1":
                data.p1Res['sheep'] -= 4
                data.p1Res['stone'] += 1
            if data.sheepPort == "3:1":
                data.p1Res['sheep'] -= 3
                data.p1Res['stone'] += 1
            if data.sheepPort == "2:1":
                data.p1Res['sheep'] -= 2
                data.p1Res['stone'] += 1
    if data.turn == 2:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.sheepPort == "4:1":
                data.p2Res['sheep'] -= 4
                data.p2Res['wood'] += 1
            if data.sheepPort == "3:1":
                data.p2Res['sheep'] -= 3
                data.p2Res['wood'] += 1
            if data.sheepPort == "2:1":
                data.p2Res['sheep'] -= 2
                data.p2Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.sheepPort == "4:1":
                data.p2Res['sheep'] -= 4
                data.p2Res['brick'] += 1
            if data.sheepPort == "3:1":
                data.p2Res['sheep'] -= 3
                data.p2Res['brick'] += 1
            if data.sheepPort == "2:1":
                data.p2Res['sheep'] -= 2
                data.p2Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.sheepPort == "4:1":
                data.p2Res['sheep'] -= 4
                data.p2Res['wheat'] += 1
            if data.sheepPort == "3:1":
                data.p2Res['sheep'] -= 3
                data.p2Res['wheat'] += 1
            if data.sheepPort == "2:1":
                data.p2Res['sheep'] -= 2
                data.p2Res['wheat'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.sheepPort == "4:1":
                data.p2Res['sheep'] -= 4
                data.p2Res['stone'] += 1
            if data.sheepPort == "3:1":
                data.p2Res['sheep'] -= 3
                data.p2Res['stone'] += 1
            if data.sheepPort == "2:1":
                data.p2Res['sheep'] -= 2
                data.p2Res['stone'] += 1
    if data.turn == 3:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.sheepPort == "4:1":
                data.p3Res['sheep'] -= 4
                data.p3Res['wood'] += 1
            if data.sheepPort == "3:1":
                data.p3Res['sheep'] -= 3
                data.p3Res['wood'] += 1
            if data.sheepPort == "2:1":
                data.p3Res['sheep'] -= 2
                data.p3Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.sheepPort == "4:1":
                data.p3Res['sheep'] -= 4
                data.p3Res['brick'] += 1
            if data.sheepPort == "3:1":
                data.p3Res['sheep'] -= 3
                data.p3Res['brick'] += 1
            if data.sheepPort == "2:1":
                data.p3Res['sheep'] -= 2
                data.p3Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.sheepPort == "4:1":
                data.p3Res['sheep'] -= 4
                data.p3Res['wheat'] += 1
            if data.sheepPort == "3:1":
                data.p3Res['sheep'] -= 3
                data.p3Res['wheat'] += 1
            if data.sheepPort == "2:1":
                data.p3Res['sheep'] -= 2
                data.p3Res['wheat'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.sheepPort == "4:1":
                data.p3Res['sheep'] -= 4
                data.p3Res['stone'] += 1
            if data.sheepPort == "3:1":
                data.p3Res['sheep'] -= 3
                data.p3Res['stone'] += 1
            if data.sheepPort == "2:1":
                data.p3Res['sheep'] -= 2
                data.p3Res['stone'] += 1
    if data.turn == 4:
        if 1105 < event.x < 1255 and 300 < event.y < 375:
            if data.sheepPort == "4:1":
                data.p4Res['sheep'] -= 4
                data.p4Res['wood'] += 1
            if data.sheepPort == "3:1":
                data.p4Res['sheep'] -= 3
                data.p4Res['wood'] += 1
            if data.sheepPort == "2:1":
                data.p4Res['sheep'] -= 2
                data.p4Res['wood'] += 1
        if 1105 < event.x < 1255 and 400 < event.y < 475:
            if data.sheepPort == "4:1":
                data.p4Res['sheep'] -= 4
                data.p4Res['brick'] += 1
            if data.sheepPort == "3:1":
                data.p4Res['sheep'] -= 3
                data.p4Res['brick'] += 1
            if data.sheepPort == "2:1":
                data.p4Res['sheep'] -= 2
                data.p4Res['brick'] += 1
        if 1305 < event.x < 1455 and 300 < event.y < 375:
            if data.sheepPort == "4:1":
                data.p4Res['sheep'] -= 4
                data.p4Res['wheat'] += 1
            if data.sheepPort == "3:1":
                data.p4Res['sheep'] -= 3
                data.p4Res['wheat'] += 1
            if data.sheepPort == "2:1":
                data.p4Res['sheep'] -= 2
                data.p4Res['wheat'] += 1
        if 1305 < event.x < 1455 and 400 < event.y < 475:
            if data.sheepPort == "4:1":
                data.p4Res['sheep'] -= 4
                data.p4Res['stone'] += 1
            if data.sheepPort == "3:1":
                data.p4Res['sheep'] -= 3
                data.p4Res['stone'] += 1
            if data.sheepPort == "2:1":
                data.p4Res['sheep'] -= 2
                data.p4Res['stone'] += 1
    data.phase = "build"