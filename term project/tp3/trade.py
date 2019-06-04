def isLegalTrade(data):
    if data.turn == 1:
        if (1, 6) in data.p1Ex['settle'] or (1, 6) in data.p1Ex['city'] or (1, 7) in data.p1Ex['settle'] or (1, 7) in data.p1Ex['city']:
            if data.p1Res['stone'] >= 2:
                return True
        if data.p1Res['brick'] >= 4 or data.p1Res['wheat'] >= 4 or data.p1Res['wood'] >= 4 or data.p1Res['sheep'] >= 4 or data.p1Res['stone'] >= 4:
            return True
        if (1, 1) in data.p1Ex['settle'] or (1, 1) in data.p1Ex['city'] or (2, 2) in data.p1Ex['settle'] or (2, 2) in data.p1Ex['city'] or (5, 4) in data.p1Ex['settle'] or (5, 4) in data.p1Ex['city'] or (5, 5) in data.p1Ex['settle'] or (5, 5) in data.p1Ex['city'] or (1, 9) in data.p1Ex['settle'] or (1, 9) in data.p1Ex['city'] or (1, 10) in data.p1Ex['settle'] or (1, 10) in data.p1Ex['city'] or (1, 3) in data.p1Ex['settle'] or (1, 3) in data.p1Ex['city'] or (1, 4) in data.p1Ex['settle'] or (1, 4) in data.p1Ex['city']:
            if data.p1Res['brick'] >= 3 or data.p1Res['wheat'] >= 3 or data.p1Res['wood'] >= 3 or data.p1Res['sheep'] >= 3 or data.p1Res['stone'] >= 3:
                return True
        if (3, 1) in data.p1Ex['settle'] or (3, 1) in data.p1Ex['city'] or (4, 2) in data.p1Ex['settle'] or (4, 2) in data.p1Ex['city']:
            if data.p1Res['brick'] >= 2:
                return True
        if (5, 8) in data.p1Ex['settle'] or (5, 8) in data.p1Ex['city'] or (5, 9) in data.p1Ex['settle'] or (5, 9) in data.p1Ex['city']:
            if data.p1Res['wheat'] >= 2:
                return True
        if (3, 12) in data.p1Ex['settle'] or (3, 12) in data.p1Ex['city'] or (4, 11) in data.p1Ex['settle'] or (4, 11) in data.p1Ex['city']:
            if data.p1Res['wood'] >= 2:
                return True
        if (1, 12) in data.p1Ex['settle'] or (1, 12) in data.p1Ex['city'] or (2, 11) in data.p1Ex['settle'] or (2, 11) in data.p1Ex['city']:
            if data.p1Res['sheep'] >= 2:
                return True
    if data.turn == 2:
        if data.p2Res['brick'] >= 4 or data.p2Res['wheat'] >= 4 or data.p2Res['wood'] >= 4 or data.p2Res['sheep'] >= 4 or data.p2Res['stone'] >= 4:
            return True
        if (1, 1) in data.p2Ex['settle'] or (1, 1) in data.p2Ex['city'] or (2, 2) in data.p2Ex['settle'] or (2, 2) in data.p2Ex['city'] or (5, 4) in data.p2Ex['settle'] or (5, 4) in data.p2Ex['city'] or (5, 5) in data.p2Ex['settle'] or (5, 5) in data.p2Ex['city'] or (1, 9) in data.p2Ex['settle'] or (1, 9) in data.p2Ex['city'] or (1, 10) in data.p2Ex['settle'] or (1, 10) in data.p2Ex['city'] or (1, 3) in data.p2Ex['settle'] or (1, 3) in data.p2Ex['city'] or (1, 4) in data.p2Ex['settle'] or (1, 4) in data.p2Ex['city']:
            if data.p2Res['brick'] >= 3 or data.p2Res['wheat'] >= 3 or data.p2Res['wood'] >= 3 or data.p2Res['sheep'] >= 3 or data.p2Res['stone'] >= 3:
                return True
        if (3, 1) in data.p2Ex['settle'] or (3, 1) in data.p2Ex['city'] or (4, 2) in data.p2Ex['settle'] or (4, 2) in data.p2Ex['city']:
            if data.p2Res['brick'] >= 2:
                return True
        if (5, 8) in data.p2Ex['settle'] or (5, 8) in data.p2Ex['city'] or (5, 9) in data.p2Ex['settle'] or (5, 9) in data.p2Ex['city']:
            if data.p2Res['wheat'] >= 2:
                return True
        if (3, 12) in data.p2Ex['settle'] or (3, 12) in data.p2Ex['city'] or (4, 11) in data.p2Ex['settle'] or (4, 11) in data.p2Ex['city']:
            if data.p2Res['wood'] >= 2:
                return True
        if (1, 12) in data.p2Ex['settle'] or (1, 12) in data.p2Ex['city'] or (2, 11) in data.p2Ex['settle'] or (2, 11) in data.p2Ex['city']:
            if data.p2Res['sheep'] >= 2:
                return True
        if (1, 6) in data.p2Ex['settle'] or (1, 6) in data.p2Ex['city'] or (1, 7) in data.p2Ex['settle'] or (1, 7) in data.p2Ex['city']:
            if data.p2Res['stone'] >= 2:
                return True
    if data.turn == 3:
        if data.p3Res['brick'] >= 4 or data.p3Res['wheat'] >= 4 or data.p3Res['wood'] >= 4 or data.p3Res['sheep'] >= 4 or data.p3Res['stone'] >= 4:
            return True
        if (1, 1) in data.p3Ex['settle'] or (1, 1) in data.p3Ex['city'] or (2, 2) in data.p3Ex['settle'] or (2, 2) in data.p3Ex['city'] or (5, 4) in data.p3Ex['settle'] or (5, 4) in data.p3Ex['city'] or (5, 5) in data.p3Ex['settle'] or (5, 5) in data.p3Ex['city'] or (1, 9) in data.p3Ex['settle'] or (1, 9) in data.p3Ex['city'] or (1, 10) in data.p3Ex['settle'] or (1, 10) in data.p3Ex['city'] or (1, 3) in data.p3Ex['settle'] or (1, 3) in data.p3Ex['city'] or (1, 4) in data.p3Ex['settle'] or (1, 4) in data.p3Ex['city']:
            if data.p3Res['brick'] >= 3 or data.p3Res['wheat'] >= 3 or data.p3Res['wood'] >= 3 or data.p3Res['sheep'] >= 3 or data.p3Res['stone'] >= 3:
                return True
        if (3, 1) in data.p3Ex['settle'] or (3, 1) in data.p3Ex['city'] or (4, 2) in data.p3Ex['settle'] or (4, 2) in data.p3Ex['city']:
            if data.p3Res['brick'] >= 2:
                return True
        if (5, 8) in data.p3Ex['settle'] or (5, 8) in data.p3Ex['city'] or (5, 9) in data.p3Ex['settle'] or (5, 9) in data.p3Ex['city']:
            if data.p3Res['wheat'] >= 2:
                return True
        if (3, 12) in data.p3Ex['settle'] or (3, 12) in data.p3Ex['city'] or (4, 11) in data.p3Ex['settle'] or (4, 11) in data.p3Ex['city']:
            if data.p3Res['wood'] >= 2:
                return True
        if (1, 12) in data.p3Ex['settle'] or (1, 12) in data.p3Ex['city'] or (2, 11) in data.p3Ex['settle'] or (2, 11) in data.p3Ex['city']:
            if data.p3Res['sheep'] >= 2:
                return True
        if (1, 6) in data.p3Ex['settle'] or (1, 6) in data.p3Ex['city'] or (1, 7) in data.p3Ex['settle'] or (1, 7) in data.p3Ex['city']:
            if data.p3Res['stone'] >= 2:
                return True
    if data.turn == 4:
        if data.p4Res['brick'] >= 4 or data.p4Res['wheat'] >= 4 or data.p4Res['wood'] >= 4 or data.p4Res['sheep'] >= 4 or data.p4Res['stone'] >= 4:
            return True
        if (1, 1) in data.p4Ex['settle'] or (1, 1) in data.p4Ex['city'] or (2, 2) in data.p4Ex['settle'] or (2, 2) in data.p4Ex['city'] or (5, 4) in data.p4Ex['settle'] or (5, 4) in data.p4Ex['city'] or (5, 5) in data.p4Ex['settle'] or (5, 5) in data.p4Ex['city'] or (1, 9) in data.p4Ex['settle'] or (1, 9) in data.p4Ex['city'] or (1, 10) in data.p4Ex['settle'] or (1, 10) in data.p4Ex['city'] or (1, 3) in data.p4Ex['settle'] or (1, 3) in data.p4Ex['city'] or (1, 4) in data.p4Ex['settle'] or (1, 4) in data.p4Ex['city']:
            if data.p4Res['brick'] >= 3 or data.p4Res['wheat'] >= 3 or data.p4Res['wood'] >= 3 or data.p4Res['sheep'] >= 3 or data.p4Res['stone'] >= 3:
                return True
        if (3, 1) in data.p4Ex['settle'] or (3, 1) in data.p4Ex['city'] or (4, 2) in data.p4Ex['settle'] or (4, 2) in data.p4Ex['city']:
            if data.p4Res['brick'] >= 2:
                return True
        if (5, 8) in data.p4Ex['settle'] or (5, 8) in data.p4Ex['city'] or (5, 9) in data.p4Ex['settle'] or (5, 9) in data.p4Ex['city']:
            if data.p4Res['wheat'] >= 2:
                return True
        if (3, 12) in data.p4Ex['settle'] or (3, 12) in data.p4Ex['city'] or (4, 11) in data.p4Ex['settle'] or (4, 11) in data.p4Ex['city']:
            if data.p4Res['wood'] >= 2:
                return True
        if (1, 12) in data.p4Ex['settle'] or (1, 12) in data.p4Ex['city'] or (2, 11) in data.p4Ex['settle'] or (2, 11) in data.p4Ex['city']:
            if data.p4Res['sheep'] >= 2:
                return True
        if (1, 6) in data.p4Ex['settle'] or (1, 6) in data.p4Ex['city'] or (1, 7) in data.p4Ex['settle'] or (1, 7) in data.p4Ex['city']:
            if data.p4Res['stone'] >= 2:
                return True
    return False

def woodPossible(data):
    if data.turn == 1:
        if (3, 12) in data.p1Ex['settle'] or (3, 12) in data.p1Ex['city'] or (4, 11) in data.p1Ex['settle'] or (4, 11) in data.p1Ex['city']:
            if data.p1Res['wood'] >= 2:
                data.woodPort = "2:1"
                return True
        if (1, 1) in data.p1Ex['settle'] or (1, 1) in data.p1Ex['city'] or (2, 2) in data.p1Ex['settle'] or (2, 2) in data.p1Ex['city'] or (5, 4) in data.p1Ex['settle'] or (5, 4) in data.p1Ex['city'] or (5, 5) in data.p1Ex['settle'] or (5, 5) in data.p1Ex['city'] or (1, 9) in data.p1Ex['settle'] or (1, 9) in data.p1Ex['city'] or (1, 10) in data.p1Ex['settle'] or (1, 10) in data.p1Ex['city'] or (1, 3) in data.p1Ex['settle'] or (1, 3) in data.p1Ex['city'] or (1, 4) in data.p1Ex['settle'] or (1, 4) in data.p1Ex['city']:
            if data.p1Res['wood'] >= 3:
                data.woodPort = "3:1"
                return True
        if data.p1Res['wood'] >= 4:
            data.woodPort = "4:1"
            return True
    if data.turn == 2:
        if (3, 12) in data.p2Ex['settle'] or (3, 12) in data.p2Ex['city'] or (4, 11) in data.p2Ex['settle'] or (4, 11) in data.p2Ex['city']:
            if data.p2Res['wood'] >= 2:
                data.woodPort = "2:1"
                return True
        if (1, 1) in data.p2Ex['settle'] or (1, 1) in data.p2Ex['city'] or (2, 2) in data.p2Ex['settle'] or (2, 2) in data.p2Ex['city'] or (5, 4) in data.p2Ex['settle'] or (5, 4) in data.p2Ex['city'] or (5, 5) in data.p2Ex['settle'] or (5, 5) in data.p2Ex['city'] or (1, 9) in data.p2Ex['settle'] or (1, 9) in data.p2Ex['city'] or (1, 10) in data.p2Ex['settle'] or (1, 10) in data.p2Ex['city'] or (1, 3) in data.p2Ex['settle'] or (1, 3) in data.p2Ex['city'] or (1, 4) in data.p2Ex['settle'] or (1, 4) in data.p2Ex['city']:
            if data.p2Res['wood'] >= 3:
                data.woodPort = "3:1"
                return True
        if data.p2Res['wood'] >= 4:
            data.woodPort = "4:1"
            return True
    if data.turn == 3:
        if (3, 12) in data.p3Ex['settle'] or (3, 12) in data.p3Ex['city'] or (4, 11) in data.p3Ex['settle'] or (4, 11) in data.p3Ex['city']:
            if data.p3Res['wood'] >= 2:
                data.woodPort = "2:1"
                return True
        if (1, 1) in data.p3Ex['settle'] or (1, 1) in data.p3Ex['city'] or (2, 2) in data.p3Ex['settle'] or (2, 2) in data.p3Ex['city'] or (5, 4) in data.p3Ex['settle'] or (5, 4) in data.p3Ex['city'] or (5, 5) in data.p3Ex['settle'] or (5, 5) in data.p3Ex['city'] or (1, 9) in data.p3Ex['settle'] or (1, 9) in data.p3Ex['city'] or (1, 10) in data.p3Ex['settle'] or (1, 10) in data.p3Ex['city'] or (1, 3) in data.p3Ex['settle'] or (1, 3) in data.p3Ex['city'] or (1, 4) in data.p3Ex['settle'] or (1, 4) in data.p3Ex['city']:
            if data.p3Res['wood'] >= 3:
                data.woodPort = "3:1"
                return True
        if data.p3Res['wood'] >= 4:
            data.woodPort = "4:1"
            return True
    if data.turn == 4:
        if (3, 12) in data.p4Ex['settle'] or (3, 12) in data.p4Ex['city'] or (4, 11) in data.p4Ex['settle'] or (4, 11) in data.p4Ex['city']:
            if data.p4Res['wood'] >= 2:
                data.woodPort = "2:1"
                return True
        if (1, 1) in data.p4Ex['settle'] or (1, 1) in data.p4Ex['city'] or (2, 2) in data.p4Ex['settle'] or (2, 2) in data.p4Ex['city'] or (5, 4) in data.p4Ex['settle'] or (5, 4) in data.p4Ex['city'] or (5, 5) in data.p4Ex['settle'] or (5, 5) in data.p4Ex['city'] or (1, 9) in data.p4Ex['settle'] or (1, 9) in data.p4Ex['city'] or (1, 10) in data.p4Ex['settle'] or (1, 10) in data.p4Ex['city'] or (1, 3) in data.p4Ex['settle'] or (1, 3) in data.p4Ex['city'] or (1, 4) in data.p4Ex['settle'] or (1, 4) in data.p4Ex['city']:
            if data.p4Res['wood'] >= 3:
                data.woodPort = "3:1"
                return True
        if data.p4Res['wood'] >= 4:
            data.woodPort = "4:1"
            return True
    return False

def brickPossible(data):
    if data.turn == 1:
        if (3, 1) in data.p1Ex['settle'] or (3, 1) in data.p1Ex['city'] or (4, 2) in data.p1Ex['settle'] or (4, 2) in data.p1Ex['city']:
            if data.p1Res['brick'] >= 2:
                data.brickPort = "2:1"
                return True
        if (1, 1) in data.p1Ex['settle'] or (1, 1) in data.p1Ex['city'] or (2, 2) in data.p1Ex['settle'] or (2, 2) in data.p1Ex['city'] or (5, 4) in data.p1Ex['settle'] or (5, 4) in data.p1Ex['city'] or (5, 5) in data.p1Ex['settle'] or (5, 5) in data.p1Ex['city'] or (1, 9) in data.p1Ex['settle'] or (1, 9) in data.p1Ex['city'] or (1, 10) in data.p1Ex['settle'] or (1, 10) in data.p1Ex['city'] or (1, 3) in data.p1Ex['settle'] or (1, 3) in data.p1Ex['city'] or (1, 4) in data.p1Ex['settle'] or (1, 4) in data.p1Ex['city']:
            if data.p1Res['brick'] >= 3:
                data.brickPort = "3:1"
                return True
        if data.p1Res['brick'] >= 4:
            data.brickPort = "4:1"
            return True
    if data.turn == 2:
        if (3, 1) in data.p2Ex['settle'] or (3, 1) in data.p2Ex['city'] or (4, 2) in data.p2Ex['settle'] or (4, 2) in data.p2Ex['city']:
            if data.p2Res['brick'] >= 2:
                data.brickPort = "2:1"
                return True
        if (1, 1) in data.p2Ex['settle'] or (1, 1) in data.p2Ex['city'] or (2, 2) in data.p2Ex['settle'] or (2, 2) in data.p2Ex['city'] or (5, 4) in data.p2Ex['settle'] or (5, 4) in data.p2Ex['city'] or (5, 5) in data.p2Ex['settle'] or (5, 5) in data.p2Ex['city'] or (1, 9) in data.p2Ex['settle'] or (1, 9) in data.p2Ex['city'] or (1, 10) in data.p2Ex['settle'] or (1, 10) in data.p2Ex['city'] or (1, 3) in data.p2Ex['settle'] or (1, 3) in data.p2Ex['city'] or (1, 4) in data.p2Ex['settle'] or (1, 4) in data.p2Ex['city']:
            if data.p2Res['brick'] >= 3:
                data.brickPort = "3:1"
                return True
        if data.p2Res['brick'] >= 4:
            data.brickPort = "4:1"
            return True
    if data.turn == 3:
        if (3, 1) in data.p3Ex['settle'] or (3, 1) in data.p3Ex['city'] or (4, 2) in data.p3Ex['settle'] or (4, 2) in data.p3Ex['city']:
            if data.p3Res['brick'] >= 2:
                data.brickPort = "2:1"
                return True
        if (1, 1) in data.p3Ex['settle'] or (1, 1) in data.p3Ex['city'] or (2, 2) in data.p3Ex['settle'] or (2, 2) in data.p3Ex['city'] or (5, 4) in data.p3Ex['settle'] or (5, 4) in data.p3Ex['city'] or (5, 5) in data.p3Ex['settle'] or (5, 5) in data.p3Ex['city'] or (1, 9) in data.p3Ex['settle'] or (1, 9) in data.p3Ex['city'] or (1, 10) in data.p3Ex['settle'] or (1, 10) in data.p3Ex['city'] or (1, 3) in data.p3Ex['settle'] or (1, 3) in data.p3Ex['city'] or (1, 4) in data.p3Ex['settle'] or (1, 4) in data.p3Ex['city']:
            if data.p3Res['brick'] >= 3:
                data.brickPort = "3:1"
                return True
        if data.p3Res['brick'] >= 4:
            data.brickPort = "4:1"
            return True
    if data.turn == 4:
        if (3, 1) in data.p4Ex['settle'] or (3, 1) in data.p4Ex['city'] or (4, 2) in data.p4Ex['settle'] or (4, 2) in data.p4Ex['city']:
            if data.p4Res['brick'] >= 2:
                data.brickPort = "2:1"
                return True
        if (1, 1) in data.p4Ex['settle'] or (1, 1) in data.p4Ex['city'] or (2, 2) in data.p4Ex['settle'] or (2, 2) in data.p4Ex['city'] or (5, 4) in data.p4Ex['settle'] or (5, 4) in data.p4Ex['city'] or (5, 5) in data.p4Ex['settle'] or (5, 5) in data.p4Ex['city'] or (1, 9) in data.p4Ex['settle'] or (1, 9) in data.p4Ex['city'] or (1, 10) in data.p4Ex['settle'] or (1, 10) in data.p4Ex['city'] or (1, 3) in data.p4Ex['settle'] or (1, 3) in data.p4Ex['city'] or (1, 4) in data.p4Ex['settle'] or (1, 4) in data.p4Ex['city']:
            if data.p4Res['brick'] >= 3:
                data.brickPort = "3:1"
                return True
        if data.p4Res['brick'] >= 4:
            data.brickPort = "4:1"
            return True
    return False

def wheatPossible(data):
    if data.turn == 1:
        if (5, 8) in data.p1Ex['settle'] or (5, 8) in data.p1Ex['city'] or (5, 9) in data.p1Ex['settle'] or (5, 9) in data.p1Ex['city']:
            if data.p1Res['wheat'] >= 2:
                data.wheatPort = "2:1"
                return True
        if (1, 1) in data.p1Ex['settle'] or (1, 1) in data.p1Ex['city'] or (2, 2) in data.p1Ex['settle'] or (2, 2) in data.p1Ex['city'] or (5, 4) in data.p1Ex['settle'] or (5, 4) in data.p1Ex['city'] or (5, 5) in data.p1Ex['settle'] or (5, 5) in data.p1Ex['city'] or (1, 9) in data.p1Ex['settle'] or (1, 9) in data.p1Ex['city'] or (1, 10) in data.p1Ex['settle'] or (1, 10) in data.p1Ex['city'] or (1, 3) in data.p1Ex['settle'] or (1, 3) in data.p1Ex['city'] or (1, 4) in data.p1Ex['settle'] or (1, 4) in data.p1Ex['city']:
            if data.p1Res['wheat'] >= 3:
                data.wheatPort = "3:1"
                return True
        if data.p1Res['wheat'] >= 4:
            data.wheatPort = "4:1"
            return True
    if data.turn == 2:
        if (5, 8) in data.p2Ex['settle'] or (5, 8) in data.p2Ex['city'] or (5, 9) in data.p2Ex['settle'] or (5, 9) in data.p2Ex['city']:
            if data.p2Res['wheat'] >= 2:
                data.wheatPort = "2:1"
                return True
        if (1, 1) in data.p2Ex['settle'] or (1, 1) in data.p2Ex['city'] or (2, 2) in data.p2Ex['settle'] or (2, 2) in data.p2Ex['city'] or (5, 4) in data.p2Ex['settle'] or (5, 4) in data.p2Ex['city'] or (5, 5) in data.p2Ex['settle'] or (5, 5) in data.p2Ex['city'] or (1, 9) in data.p2Ex['settle'] or (1, 9) in data.p2Ex['city'] or (1, 10) in data.p2Ex['settle'] or (1, 10) in data.p2Ex['city'] or (1, 3) in data.p2Ex['settle'] or (1, 3) in data.p2Ex['city'] or (1, 4) in data.p2Ex['settle'] or (1, 4) in data.p2Ex['city']:
            if data.p2Res['wheat'] >= 3:
                data.wheatPort = "3:1"
                return True
        if data.p2Res['wheat'] >= 4:
            data.wheatPort = "4:1"
            return True
    if data.turn == 3:
        if (5, 8) in data.p3Ex['settle'] or (5, 8) in data.p3Ex['city'] or (5, 9) in data.p3Ex['settle'] or (5, 9) in data.p3Ex['city']:
            if data.p3Res['wheat'] >= 2:
                data.wheatPort = "2:1"
                return True
        if (1, 1) in data.p3Ex['settle'] or (1, 1) in data.p3Ex['city'] or (2, 2) in data.p3Ex['settle'] or (2, 2) in data.p3Ex['city'] or (5, 4) in data.p3Ex['settle'] or (5, 4) in data.p3Ex['city'] or (5, 5) in data.p3Ex['settle'] or (5, 5) in data.p3Ex['city'] or (1, 9) in data.p3Ex['settle'] or (1, 9) in data.p3Ex['city'] or (1, 10) in data.p3Ex['settle'] or (1, 10) in data.p3Ex['city'] or (1, 3) in data.p3Ex['settle'] or (1, 3) in data.p3Ex['city'] or (1, 4) in data.p3Ex['settle'] or (1, 4) in data.p3Ex['city']:
            if data.p3Res['wheat'] >= 3:
                data.wheatPort = "3:1"
                return True
        if data.p3Res['wheat'] >= 4:
            data.wheatPort = "4:1"
            return True
    if data.turn == 4:
        if (5, 8) in data.p4Ex['settle'] or (5, 8) in data.p4Ex['city'] or (5, 9) in data.p4Ex['settle'] or (5, 9) in data.p4Ex['city']:
            if data.p4Res['wheat'] >= 2:
                data.wheatPort = "2:1"
                return True
        if (1, 1) in data.p4Ex['settle'] or (1, 1) in data.p4Ex['city'] or (2, 2) in data.p4Ex['settle'] or (2, 2) in data.p4Ex['city'] or (5, 4) in data.p4Ex['settle'] or (5, 4) in data.p4Ex['city'] or (5, 5) in data.p4Ex['settle'] or (5, 5) in data.p4Ex['city'] or (1, 9) in data.p4Ex['settle'] or (1, 9) in data.p4Ex['city'] or (1, 10) in data.p4Ex['settle'] or (1, 10) in data.p4Ex['city'] or (1, 3) in data.p4Ex['settle'] or (1, 3) in data.p4Ex['city'] or (1, 4) in data.p4Ex['settle'] or (1, 4) in data.p4Ex['city']:
            if data.p4Res['wheat'] >= 3:
                data.wheatPort = "3:1"
                return True
        if data.p4Res['wheat'] >= 4:
            data.wheatPort = "4:1"
            return True
    return False

def stonePossible(data):
    if data.turn == 1:
        if (1, 6) in data.p1Ex['settle'] or (1, 6) in data.p1Ex['city'] or (1, 7) in data.p1Ex['settle'] or (1, 7) in data.p1Ex['city']:
            if data.p1Res['stone'] >= 2:
                data.stonePort = "2:1"
                return True
        if (1, 1) in data.p1Ex['settle'] or (1, 1) in data.p1Ex['city'] or (2, 2) in data.p1Ex['settle'] or (2, 2) in data.p1Ex['city'] or (5, 4) in data.p1Ex['settle'] or (5, 4) in data.p1Ex['city'] or (5, 5) in data.p1Ex['settle'] or (5, 5) in data.p1Ex['city'] or (1, 9) in data.p1Ex['settle'] or (1, 9) in data.p1Ex['city'] or (1, 10) in data.p1Ex['settle'] or (1, 10) in data.p1Ex['city'] or (1, 3) in data.p1Ex['settle'] or (1, 3) in data.p1Ex['city'] or (1, 4) in data.p1Ex['settle'] or (1, 4) in data.p1Ex['city']:
            if data.p1Res['stone'] >= 3: 
                data.stonePort = "3:1"
                return True
        if data.p1Res['stone'] >= 4:
            data.stonePort = "4:1"
            return True
    if data.turn == 2:
        if (1, 6) in data.p2Ex['settle'] or (1, 6) in data.p2Ex['city'] or (1, 7) in data.p2Ex['settle'] or (1, 7) in data.p2Ex['city']:
            if data.p2Res['stone'] >= 2:
                data.stonePort = "2:1"
                return True
        if (1, 1) in data.p2Ex['settle'] or (1, 1) in data.p2Ex['city'] or (2, 2) in data.p2Ex['settle'] or (2, 2) in data.p2Ex['city'] or (5, 4) in data.p2Ex['settle'] or (5, 4) in data.p2Ex['city'] or (5, 5) in data.p2Ex['settle'] or (5, 5) in data.p2Ex['city'] or (1, 9) in data.p2Ex['settle'] or (1, 9) in data.p2Ex['city'] or (1, 10) in data.p2Ex['settle'] or (1, 10) in data.p2Ex['city'] or (1, 3) in data.p2Ex['settle'] or (1, 3) in data.p2Ex['city'] or (1, 4) in data.p2Ex['settle'] or (1, 4) in data.p2Ex['city']:
            if data.p2Res['stone'] >= 3:
                data.stonePort = "3:1"
                return True
        if data.p2Res['stone'] >= 4:
            data.stonePort = "4:1"
            return True
    if data.turn == 3:
        if (1, 6) in data.p3Ex['settle'] or (1, 6) in data.p3Ex['city'] or (1, 7) in data.p3Ex['settle'] or (1, 7) in data.p3Ex['city']:
            if data.p3Res['stone'] >= 2:
                data.stonePort = "2:1"
                return True
        if (1, 1) in data.p3Ex['settle'] or (1, 1) in data.p3Ex['city'] or (2, 2) in data.p3Ex['settle'] or (2, 2) in data.p3Ex['city'] or (5, 4) in data.p3Ex['settle'] or (5, 4) in data.p3Ex['city'] or (5, 5) in data.p3Ex['settle'] or (5, 5) in data.p3Ex['city'] or (1, 9) in data.p3Ex['settle'] or (1, 9) in data.p3Ex['city'] or (1, 10) in data.p3Ex['settle'] or (1, 10) in data.p3Ex['city'] or (1, 3) in data.p3Ex['settle'] or (1, 3) in data.p3Ex['city'] or (1, 4) in data.p3Ex['settle'] or (1, 4) in data.p3Ex['city']:
            if data.p3Res['stone'] >= 3:
                data.stonePort = "3:1"
                return True
        if data.p3Res['stone'] >= 4:
            data.stonePort = "4:1"
            return True
    if data.turn == 4:
        if (1, 6) in data.p4Ex['settle'] or (1, 6) in data.p4Ex['city'] or (1, 7) in data.p4Ex['settle'] or (1, 7) in data.p4Ex['city']:
            if data.p4Res['stone'] >= 2:
                data.stonePort = "2:1"
                return True
        if (1, 1) in data.p4Ex['settle'] or (1, 1) in data.p4Ex['city'] or (2, 2) in data.p4Ex['settle'] or (2, 2) in data.p4Ex['city'] or (5, 4) in data.p4Ex['settle'] or (5, 4) in data.p4Ex['city'] or (5, 5) in data.p4Ex['settle'] or (5, 5) in data.p4Ex['city'] or (1, 9) in data.p4Ex['settle'] or (1, 9) in data.p4Ex['city'] or (1, 10) in data.p4Ex['settle'] or (1, 10) in data.p4Ex['city'] or (1, 3) in data.p4Ex['settle'] or (1, 3) in data.p4Ex['city'] or (1, 4) in data.p4Ex['settle'] or (1, 4) in data.p4Ex['city']:
            if data.p4Res['stone'] >= 3:
                data.stonePort = "3:1"
                return True
        if data.p4Res['stone'] >= 4:
            data.stonePort = "4:1"
            return True
    return False

def sheepPossible(data):
    if data.turn == 1:
        if (1, 12) in data.p1Ex['settle'] or (1, 12) in data.p1Ex['city'] or (2, 11) in data.p1Ex['settle'] or (2, 11) in data.p1Ex['city']:
            if data.p1Res['sheep'] >= 2:
                data.sheepPort = "2:1"
                return True
        if (1, 1) in data.p1Ex['settle'] or (1, 1) in data.p1Ex['city'] or (2, 2) in data.p1Ex['settle'] or (2, 2) in data.p1Ex['city'] or (5, 4) in data.p1Ex['settle'] or (5, 4) in data.p1Ex['city'] or (5, 5) in data.p1Ex['settle'] or (5, 5) in data.p1Ex['city'] or (1, 9) in data.p1Ex['settle'] or (1, 9) in data.p1Ex['city'] or (1, 10) in data.p1Ex['settle'] or (1, 10) in data.p1Ex['city'] or (1, 3) in data.p1Ex['settle'] or (1, 3) in data.p1Ex['city'] or (1, 4) in data.p1Ex['settle'] or (1, 4) in data.p1Ex['city']:
            if data.p1Res['sheep'] >= 3:
                data.sheepPort = "3:1"
                return True
        if data.p1Res['sheep'] >= 4:
            data.sheepPort = "4:1"
            return True
    if data.turn == 2:
        if (1, 12) in data.p2Ex['settle'] or (1, 12) in data.p2Ex['city'] or (2, 11) in data.p2Ex['settle'] or (2, 11) in data.p2Ex['city']:
            if data.p2Res['sheep'] >= 2: 
                data.sheepPort = "2:1"
                return True
        if (1, 1) in data.p2Ex['settle'] or (1, 1) in data.p2Ex['city'] or (2, 2) in data.p2Ex['settle'] or (2, 2) in data.p2Ex['city'] or (5, 4) in data.p2Ex['settle'] or (5, 4) in data.p2Ex['city'] or (5, 5) in data.p2Ex['settle'] or (5, 5) in data.p2Ex['city'] or (1, 9) in data.p2Ex['settle'] or (1, 9) in data.p2Ex['city'] or (1, 10) in data.p2Ex['settle'] or (1, 10) in data.p2Ex['city'] or (1, 3) in data.p2Ex['settle'] or (1, 3) in data.p2Ex['city'] or (1, 4) in data.p2Ex['settle'] or (1, 4) in data.p2Ex['city']:
            if data.p2Res['sheep'] >= 3:
                data.sheepPort = "3:1"
                return True
        if data.p2Res['sheep'] >= 4:
            data.sheepPort = "4:1"
            return True
    if data.turn == 3:
        if (1, 12) in data.p3Ex['settle'] or (1, 12) in data.p3Ex['city'] or (2, 11) in data.p3Ex['settle'] or (2, 11) in data.p3Ex['city']:
            if data.p3Res['sheep'] >= 2:
                data.sheepPort = "2:1"
                return True
        if (1, 1) in data.p3Ex['settle'] or (1, 1) in data.p3Ex['city'] or (2, 2) in data.p3Ex['settle'] or (2, 2) in data.p3Ex['city'] or (5, 4) in data.p3Ex['settle'] or (5, 4) in data.p3Ex['city'] or (5, 5) in data.p3Ex['settle'] or (5, 5) in data.p3Ex['city'] or (1, 9) in data.p3Ex['settle'] or (1, 9) in data.p3Ex['city'] or (1, 10) in data.p3Ex['settle'] or (1, 10) in data.p3Ex['city'] or (1, 3) in data.p3Ex['settle'] or (1, 3) in data.p3Ex['city'] or (1, 4) in data.p3Ex['settle'] or (1, 4) in data.p3Ex['city']:
            if data.p3Res['sheep'] >= 3:
                data.sheepPort = "3:1"
                return True
        if data.p3Res['sheep'] >= 4: 
            data.sheepPort = "4:1"
            return True
    if data.turn == 4:
        if (1, 12) in data.p4Ex['settle'] or (1, 12) in data.p4Ex['city'] or (2, 11) in data.p4Ex['settle'] or (2, 11) in data.p4Ex['city']:
            if data.p4Res['sheep'] >= 2:
                data.sheepPort = "2:1"
                return True
        if (1, 1) in data.p4Ex['settle'] or (1, 1) in data.p4Ex['city'] or (2, 2) in data.p4Ex['settle'] or (2, 2) in data.p4Ex['city'] or (5, 4) in data.p4Ex['settle'] or (5, 4) in data.p4Ex['city'] or (5, 5) in data.p4Ex['settle'] or (5, 5) in data.p4Ex['city'] or (1, 9) in data.p4Ex['settle'] or (1, 9) in data.p4Ex['city'] or (1, 10) in data.p4Ex['settle'] or (1, 10) in data.p4Ex['city'] or (1, 3) in data.p4Ex['settle'] or (1, 3) in data.p4Ex['city'] or (1, 4) in data.p4Ex['settle'] or (1, 4) in data.p4Ex['city']:
            if data.p4Res['sheep'] >= 3:
                data.sheepPort = "3:1"
                return True
        if data.p4Res['sheep'] >= 4:
            data.sheepPort = "4:1"
            return True