def createCoords():
    lst = []
    for num in range(1, 4):
        lst += [(num, 1)]
        lst += [(num, 12)]
    for num in range(1, 5):
        lst += [(num, 2)]
        lst += [(num, 3)]
        lst += [(num, 10)]
        lst += [(num, 11)]
    for num in range(1, 6):
        lst += [(num, 4)]
        lst += [(num, 5)]
        lst += [(num, 8)]
        lst += [(num, 9)]
    for num in range(1, 7):
        lst += [(num, 6)]
        lst += [(num, 7)]
    return lst

def getLegalSetInit(data):
    coords = createCoords()
    for coord in data.occupied:
        if coord == (1, 1):
            if (1, 2) in coords:
                coords.remove((1, 2))
            if (2, 2) in coords:
                coords.remove((2, 2))
            if (1, 1) in coords:
                coords.remove((1, 1))
        if coord == (2, 1):
            if (2, 2) in coords:
                coords.remove((2, 2))
            if (3, 2) in coords:
                coords.remove((3, 2))
            if (2, 1) in coords:
                coords.remove((2, 1))
        if coord == (3, 1):
            if (3, 2) in coords:
                coords.remove((3, 2))
            if (4, 2) in coords:
                coords.remove((4, 2))
            if (3, 1) in coords:
                coords.remove((3, 1))
        if coord == (1, 2):
            if (1, 1) in coords:
                coords.remove((1, 1))
            if (1, 3) in coords:
                coords.remove((1, 3))
            if (1, 2) in coords:
                coords.remove((1, 2))
        if coord == (2, 2):
            if (1, 1) in coords:
                coords.remove((1, 1))
            if (2, 1) in coords:
                coords.remove((2, 1))
            if (2, 3) in coords:
                coords.remove((2, 3))
            if (2, 2) in coords:
                coords.remove((2, 2))
        if coord == (3, 2):
            if (2, 1) in coords:
                coords.remove((2, 1))
            if (3, 1) in coords:
                coords.remove((3, 1))
            if (3, 3) in coords:
                coords.remove((3, 3))
            if (3, 2) in coords:
                coords.remove((3, 2))
        if coord == (4, 2):
            if (3, 1) in coords:
                coords.remove((3, 1))
            if (4, 3) in coords:
                coords.remove((4, 3))
            if (4, 2) in coords:
                coords.remove((4, 2))
        if coord == (1, 3):
            if (1, 2) in coords:
                coords.remove((1, 2))
            if (1, 4) in coords:
                coords.remove((1, 4))
            if (2, 4) in coords:
                coords.remove((2, 4))
            if (1, 3) in coords:
                coords.remove((1, 3))
        if coord == (2, 3):
            if (2, 2) in coords:
                coords.remove((2, 2))
            if (2, 4) in coords:
                coords.remove((2, 4))
            if (3, 4) in coords:
                coords.remove((3, 4))
            if (2, 3) in coords:
                coords.remove((2, 3))
        if coord == (3, 3):
            if (3, 2) in coords:
                coords.remove((3, 2))
            if (3, 4) in coords:
                coords.remove((3, 4))
            if (4, 4) in coords:
                coords.remove((4, 4))
            if (3, 3) in coords:
                coords.remove((3, 3))
        if coord == (4, 3):
            if (4, 2) in coords:
                coords.remove((4, 2))
            if (4, 4) in coords:
                coords.remove((4, 4))
            if (5, 4) in coords:
                coords.remove((5, 4))
            if (4, 3) in coords:
                coords.remove((4, 3))
        if coord == (1, 4):
            if (1, 3) in coords:
                coords.remove((1, 3))
            if (1, 5) in coords:
                coords.remove((1, 5))
            if (1, 4) in coords:
                coords.remove((1, 4))
        if coord == (2, 4):
            if (1, 3) in coords:
                coords.remove((1, 3))
            if (2, 3) in coords:
                coords.remove((2, 3))
            if (2, 5) in coords:
                coords.remove((2, 5))
            if (2, 4) in coords:
                coords.remove((2, 4))
        if coord == (3, 4):
            if (2, 3) in coords:
                coords.remove((2, 3))
            if (3, 3) in coords:
                coords.remove((3, 3))
            if (3, 5) in coords:
                coords.remove((3, 5))
            if (3, 4) in coords:
                coords.remove((3, 4))
        if coord == (4, 4):
            if (3, 3) in coords:
                coords.remove((3, 3))
            if (4, 3) in coords:
                coords.remove((4, 3))
            if (4, 5) in coords:
                coords.remove((4, 5))
            if (4, 4) in coords:
                coords.remove((4, 4))
        if coord == (5, 4):
            if (4, 3) in coords:
                coords.remove((4, 3))
            if (5, 5) in coords:
                coords.remove((5, 5))
            if (5, 4) in coords:
                coords.remove((5, 4))
        if coord == (1, 5):
            if (1, 4) in coords:
                coords.remove((1, 4))
            if (1, 6) in coords:
                coords.remove((1, 6))
            if (2, 6) in coords:
                coords.remove((2, 6))
            if (1, 5) in coords:
                coords.remove((1, 5))
        if coord == (2, 5):
            if (2, 4) in coords:
                coords.remove((2, 4))
            if (2, 6) in coords:
                coords.remove((2, 6))
            if (3, 6) in coords:
                coords.remove((3, 6))
            if (2, 5) in coords:
                coords.remove((2, 5))
        if coord == (3, 5):
            if (3, 4) in coords:
                coords.remove((3, 4))
            if (3, 6) in coords:
                coords.remove((3, 6))
            if (4, 6) in coords:
                coords.remove((4, 6))
            if (3, 5) in coords:
                coords.remove((3, 5))
        if coord == (4, 5):
            if (4, 4) in coords:
                coords.remove((4, 4))
            if (4, 6) in coords:
                coords.remove((4, 6))
            if (5, 6) in coords:
                coords.remove((5, 6))
            if (4, 5) in coords:
                coords.remove((4, 5))
        if coord == (5, 5):
            if (5, 4) in coords:
                coords.remove((5, 4))
            if (6, 6) in coords:
                coords.remove((6, 6))
            if (5, 5) in coords:
                coords.remove((5, 5))
        if coord == (1, 6):
            if (1, 5) in coords:
                coords.remove((1, 5))
            if (1, 7) in coords:
                coords.remove((1, 7))
            if (1, 6) in coords:
                coords.remove((1, 6))
        if coord == (2, 6):
            if (1, 5) in coords:
                coords.remove((1, 5))
            if (2, 5) in coords:
                coords.remove((2, 5))
            if (2, 7) in coords:
                coords.remove((2, 7))
            if (2, 6) in coords:
                coords.remove((2, 6))
        if coord == (3, 6):
            if (2, 5) in coords:
                coords.remove((2, 5))
            if (3, 5) in coords:
                coords.remove((3, 5))
            if (3, 7) in coords:
                coords.remove((3, 7))
            if (3, 6) in coords:
                coords.remove((3, 6))
        if coord == (4, 6):
            if (3, 5) in coords:
                coords.remove((3, 5))
            if (4, 5) in coords:
                coords.remove((4, 5))
            if (4, 7) in coords:
                coords.remove((4, 7))
            if (4, 6) in coords:
                coords.remove((4, 6))
        if coord == (5, 6):
            if (4, 5) in coords:
                coords.remove((4, 5))
            if (5, 5) in coords:
                coords.remove((5, 5))
            if (5, 7) in coords:
                coords.remove((5, 7))
            if (5, 6) in coords:
                coords.remove((5, 6))
        if coord == (6, 6):
            if (5, 5) in coords:
                coords.remove((5, 5))
            if (6, 7) in coords:
                coords.remove((6, 7))
            if (6, 6) in coords:
                coords.remove((6, 6))
        if coord == (1, 7):
            if (1, 6) in coords:
                coords.remove((1, 6))
            if (1, 8) in coords:
                coords.remove((1, 8))
            if (1, 7) in coords:
                coords.remove((1, 7))
        if coord == (2, 7):
            if (2, 6) in coords:
                coords.remove((2, 6))
            if (1, 8) in coords:
                coords.remove((1, 8))
            if (2, 8) in coords:
                coords.remove((2, 8))
            if (2, 7) in coords:
                coords.remove((2, 7))
        if coord == (3, 7):
            if (3, 6) in coords:
                coords.remove((3, 6))
            if (2, 8) in coords:
                coords.remove((2, 8))
            if (3, 8) in coords:
                coords.remove((3, 8))
            if (3, 7) in coords:
                coords.remove((3, 7))
        if coord == (4, 7):
            if (4, 6) in coords:
                coords.remove((4, 6))
            if (3, 8) in coords:
                coords.remove((3, 8))
            if (4, 8) in coords:
                coords.remove((4, 8))
            if (4, 7) in coords:
                coords.remove((4, 7))
        if coord == (5, 7):
            if (5, 6) in coords:
                coords.remove((5, 6))
            if (4, 8) in coords:
                coords.remove((4, 8))
            if (5, 8) in coords:
                coords.remove((5, 8))
            if (5, 7) in coords:
                coords.remove((5, 7))
        if coord == (6, 7):
            if (6, 6) in coords:
                coords.remove((6, 6))
            if (5, 8) in coords:
                coords.remove((5, 8))
            if (6, 7) in coords:
                coords.remove((6, 7))
        if coord == (1, 8):
            if (1, 7) in coords:
                coords.remove((1, 7))
            if (2, 7) in coords:
                coords.remove((2, 7))
            if (1, 9) in coords:
                coords.remove((1, 9))
            if (1, 8) in coords:
                coords.remove((1, 8))
        if coord == (2, 8):
            if (2, 7) in coords:
                coords.remove((2, 7))
            if (3, 7) in coords:
                coords.remove((3, 7))
            if (2, 9) in coords:
                coords.remove((2, 9))
            if (2, 8) in coords:
                coords.remove((2, 8))
        if coord == (3, 8):
            if (3, 7) in coords:
                coords.remove((3, 7))
            if (4, 7) in coords:
                coords.remove((4, 7))
            if (3, 9) in coords:
                coords.remove((3, 9))
            if (3, 8) in coords:
                coords.remove((3, 8))
        if coord == (4, 8):
            if (4, 7) in coords:
                coords.remove((4, 7))
            if (5, 7) in coords:
                coords.remove((5, 7))
            if (4, 9) in coords:
                coords.remove((4, 9))
            if (4, 8) in coords:
                coords.remove((4, 8))
        if coord == (5, 8):
            if (5, 7) in coords:
                coords.remove((5, 7))
            if (6, 7) in coords:
                coords.remove((6, 7))
            if (5, 9) in coords:
                coords.remove((5, 9))
            if (5, 8) in coords:
                coords.remove((5, 8))
        if coord == (1, 9):
            if (1, 8) in coords:
                coords.remove((1, 8))
            if (1, 10) in coords:
                coords.remove((1, 10))
            if (1, 9) in coords:
                coords.remove((1, 9))
        if coord == (2, 9):
            if (2, 8) in coords:
                coords.remove((2, 8))
            if (1, 10) in coords:
                coords.remove((1, 10))
            if (2, 10) in coords:
                coords.remove((2, 10))
            if (2, 9) in coords:
                coords.remove((2, 9))
        if coord == (3, 9):
            if (3, 8) in coords:
                coords.remove((3, 8))
            if (2, 10) in coords:
                coords.remove((2, 10))
            if (3, 10) in coords:
                coords.remove((3, 10))
            if (3, 9) in coords:
                coords.remove((3, 9))
        if coord == (4, 9):
            if (4, 8) in coords:
                coords.remove((4, 8))
            if (3, 10) in coords:
                coords.remove((3, 10))
            if (4, 10) in coords:
                coords.remove((4, 10))
            if (4, 9) in coords:
                coords.remove((4, 9))
        if coord == (5, 9):
            if (5, 8) in coords:
                coords.remove((5, 8))
            if (4, 10) in coords:
                coords.remove((4, 10))
            if (5, 9) in coords:
                coords.remove((5, 9))
        if coord == (1, 10):
            if (1, 9) in coords:
                coords.remove((1, 9))
            if (2, 9) in coords:
                coords.remove((2, 9))
            if (1, 11) in coords:
                coords.remove((1, 11))
            if (1, 10) in coords:
                coords.remove((1, 10))
        if coord == (2, 10):
            if (2, 9) in coords:
                coords.remove((2, 9))
            if (3, 9) in coords:
                coords.remove((3, 9))
            if (2, 11) in coords:
                coords.remove((2, 11))
            if (2, 10) in coords:
                coords.remove((2, 10))
        if coord == (3, 10):
            if (3, 9) in coords:
                coords.remove((3, 9))
            if (4, 9) in coords:
                coords.remove((4, 9))
            if (3, 11) in coords:
                coords.remove((3, 11))
            if (3, 10) in coords:
                coords.remove((3, 10))
        if coord == (4, 10):
            if (4, 9) in coords:
                coords.remove((4, 9))
            if (5, 9) in coords:
                coords.remove((5, 9))
            if (4, 11) in coords:
                coords.remove((4, 11))
            if (4, 10) in coords:
                coords.remove((4, 10))
        if coord == (1, 11):
            if (1, 10) in coords:
                coords.remove((1, 10))
            if (1, 12) in coords:
                coords.remove((1, 12))
            if (1, 11) in coords:
                coords.remove((1, 11))
        if coord == (2, 11):
            if (2, 10) in coords:
                coords.remove((2, 10))
            if (1, 12) in coords:
                coords.remove((1, 12))
            if (2, 12) in coords:
                coords.remove((2, 12))
            if (2, 11) in coords:
                coords.remove((2, 11))
        if coord == (3, 11):
            if (3, 10) in coords:
                coords.remove((3, 10))
            if (2, 12) in coords:
                coords.remove((2, 12))
            if (3, 12) in coords:
                coords.remove((3, 12))
            if (3, 11) in coords:
                coords.remove((3, 11))
        if coord == (4, 11):
            if (4, 10) in coords:
                coords.remove((4, 10))
            if (3, 12) in coords:
                coords.remove((3, 12))
            if (4, 11) in coords:
                coords.remove((4, 11))
        if coord == (1, 12):
            if (1, 11) in coords:
                coords.remove((1, 11))
            if (2, 11) in coords:
                coords.remove((2, 11))
            if (1, 12) in coords:
                coords.remove((1, 12))
        if coord == (2, 12):
            if (2, 11) in coords:
                coords.remove((2, 11))
            if (3, 11) in coords:
                coords.remove((3, 11))
            if (2, 12) in coords:
                coords.remove((2, 12))
        if coord == (3, 12):
            if (3, 11) in coords:
                coords.remove((3, 11))
            if (4, 11) in coords:
                coords.remove((4, 11))
            if (3, 12) in coords:
                coords.remove((3, 12))
    return coords

def getRoadCoords():
    coords = []
    for i in range(6):
        coords += [(267.5+i*65, 93.75)]
        coords += [(267.5+i*65, 656.25)]
        coords += [(105+i*130, 375)]
    for i in range(4):
        coords += [(235+i*130, 150)]
        coords += [(235+i*130, 600)]
    for i in range(8):
        coords += [(202.5+i*65,206.25)]
        coords += [(202.5+i*65, 543.75)]
    for i in range(5):
        coords += [(170+i*130, 262.5)]
        coords += [(170+i*130, 487.5)]
    for i in range(10):
        coords += [(137.5+i*65, 318.75)]
        coords += [(137.5+i*65, 431.25)]
    return coords

def getLegalRoad(data):
    lst = []
    if data.prevCoord == (1, 1):
        if (267.5, 93.75) not in data.occupiedRoads:
            lst += [(267.5, 93.75)]
        if (332.5, 93.75) not in data.occupiedRoads:
            lst += [(332.5, 93.75)]
        if (267.5, 93.75) in data.occupiedRoads:
            data.roads = (1, 2)
        if (332.5, 93.75) in data.occupiedRoads:
            data.roads = (2, 2)
    if data.prevCoord == (2, 1):
        if (397.5, 93.75) not in data.occupiedRoads:
            lst += [(397.5, 93.75)]
            data.drawRoads += [(2, 2)]
        if (462.5, 93.75) not in data.occupiedRoads:
            lst += [(462.5, 93.75)]
            data.drawRoads += [(3, 2)]
        if (397.5, 93.75) in data.occupiedRoads:
            data.roads = (2, 2)
        if (462.5, 93.75) in data.occupiedRoads:
            data.roads = (3, 2)
    if data.prevCoord == (3, 1):
        if (527.5, 93.75) not in data.occupiedRoads:
            lst += [(527.5, 93.75)]
        if (592.5, 93.75) not in data.occupiedRoads:
            lst += [(592.5, 93.75)]
        if (527.5, 93.75) in data.occupiedRoads:
            data.roads = (3, 2)
        if (592.5, 93.75) in data.occupiedRoads:
            data.roads = (4, 2)
    if data.prevCoord == (1, 2):
        if (267.5, 93.75) not in data.occupiedRoads:
            lst += [(267.5, 93.75)]
        if (235, 150) not in data.occupiedRoads:
            lst += [(235, 150)]
        if (267.5, 93.75) in data.occupiedRoads:
            data.roads = (1, 1)
        if (235, 150) in data.occupiedRoads:
            data.roads = (1, 3)
    if data.prevCoord == (2, 2):
        if (332.5, 93.75) not in data.occupiedRoads:
            lst += [(332.5, 93.75)]
        if (397.5, 93.75) not in data.occupiedRoads:
            lst += [(397.5, 93.75)]
        if (365, 150) not in data.occupiedRoads:
            lst += [(365, 150)]
        if (332.5, 93.75) in data.occupiedRoads:
            data.roads = (1, 1)
        if (397.5, 93.75) in data.occupiedRoads:
            data.roads = (2, 1)
        if (365, 150) in data.occupiedRoads:
            data.roads = (2, 3)
    if data.prevCoord == (3, 2):
        if (462.5, 93.75) not in data.occupiedRoads:
            lst += [(462.5, 93.75)]
        if (527.5, 93.75) not in data.occupiedRoads:
            lst += [(527.5, 93.75)]
        if (495, 150) not in data.occupiedRoads:
            lst += [(495, 150)]
        if (462.5, 93.75) in data.occupiedRoads:
            data.roads = (2, 1)
        if (527.5, 93.75) in data.occupiedRoads:
            data.roads = (3, 1)
        if (495, 150) in data.occupiedRoads:
            data.roads = (3, 3)
    if data.prevCoord == (4, 2):
        if (592.5, 93.75) not in data.occupiedRoads:
            lst += [(592.5, 93.75)]
        if (625, 150) not in data.occupiedRoads:
            lst += [(625, 150)]
        if (592.5, 93.75) in data.occupiedRoads:
            data.roads = (3, 1)
        if (625, 150) in data.occupiedRoads:
            data.roads = (4, 3)
    if data.prevCoord == (1, 3):
        if (235, 150) not in data.occupiedRoads:
            lst += [(235, 150)]
        if (202.5, 206.25) not in data.occupiedRoads:
            lst += [(202.5, 206.25)]
        if (267.5, 206.25) not in data.occupiedRoads:
            lst += [(267.5, 206.25)]
        if (235, 150) in data.occupiedRoads:
            data.roads = (1, 2)
        if (202.5, 206.25) in data.occupiedRoads:
            data.roads = (1, 4)
        if (267.5, 206.25) in data.occupiedRoads:
            data.roads = (2, 4)
    if data.prevCoord == (2, 3):
        if (365, 150) not in data.occupiedRoads:
            lst += [(365, 150)]
        if (332.5, 206.25) not in data.occupiedRoads:
            lst += [(332.5, 206.25)]
        if (397.5, 206.25) not in data.occupiedRoads:
            lst += [(397.5, 206.25)]
        if (365, 150) in data.occupiedRoads:
            data.roads = (2, 2)
        if (332.5, 206.25) in data.occupiedRoads:
            data.roads = (2, 4)
        if (397.5, 206.25) in data.occupiedRoads:
            data.roads = (3, 4)
    if data.prevCoord == (3, 3):
        if (495, 150) not in data.occupiedRoads:
            lst += [(495, 150)]
        if (462.5, 206.25) not in data.occupiedRoads:
            lst += [(462.5, 206.25)]
        if (527.5, 206.25) not in data.occupiedRoads:
            lst += [(527.5, 206.25)]
        if (495, 150) in data.occupiedRoads:
            data.roads = (3, 2)
        if (462.5, 206.25) in data.occupiedRoads:
            data.roads = (3, 4)
        if (527.5, 206.25) in data.occupiedRoads:
            data.roads = (4, 4)
    if data.prevCoord == (4, 3):
        if (625, 150) not in data.occupiedRoads:
            lst += [(625, 150)]
        if (592.5, 206.25) not in data.occupiedRoads:
            lst += [(592.5, 206.25)]
        if (657.5, 206.25) not in data.occupiedRoads:
            lst += [(657.5, 206.25)]
        if (625, 150) in data.occupiedRoads:
            data.roads = (4, 2)
        if (592.5, 206.25) in data.occupiedRoads:
            data.roads = (4, 4)
        if (657.5, 206.25) in data.occupiedRoads:
            data.roads = (5, 4)
    if data.prevCoord == (1, 4):
        if (202.5, 206.25) not in data.occupiedRoads:
            lst += [(202.5, 206.25)]
        if (170, 262.5) not in data.occupiedRoads:
            lst += [(170, 262.5)]
        if (202.5, 206.25) in data.occupiedRoads:
            data.roads = (1, 3)
        if (170, 262.5) in data.occupiedRoads:
            data.roads = (1, 5)
    if data.prevCoord == (2, 4):
        if (267.5, 206.25) not in data.occupiedRoads:
            lst += [(267.5, 206.25)]
        if (332.5, 206.25) not in data.occupiedRoads:
            lst += [(332.5, 206.25)]
        if (300, 262.5) not in data.occupiedRoads:
            lst += [(300, 262.5)]
        if (267.5, 206.25) in data.occupiedRoads:
            data.roads = (1, 3)
        if (332.5, 206.25) in data.occupiedRoads:
            data.roads = (2, 3)
        if (300, 262.5) in data.occupiedRoads:
            data.roads = (2, 5)
    if data.prevCoord == (3, 4):
        if (397.5, 206.25) not in data.occupiedRoads:
            lst += [(397.5, 206.25)]
        if (462.5, 206.25) not in data.occupiedRoads:
            lst += [(462.5, 206.25)]
        if (430, 262.5) not in data.occupiedRoads:
            lst += [(430, 262.5)]
        if (397.5, 206.25) in data.occupiedRoads:
            data.roads = (2, 3)
        if (462.5, 206.25) in data.occupiedRoads:
            data.roads = (3, 3)
        if (430, 262.5) in data.occupiedRoads:
            data.roads = (3, 5)
    if data.prevCoord == (4, 4):
        if (527.5, 206.25) not in data.occupiedRoads:
            lst += [(527.5, 206.25)]
        if (592.5, 206.25) not in data.occupiedRoads:
            lst += [(592.5, 206.25)]
        if (560, 262.5) not in data.occupiedRoads:
            lst += [(560, 262.5)]
        if (527.5, 206.25) in data.occupiedRoads:
            data.roads = (3, 3)
        if (592.5, 206.25) in data.occupiedRoads:
            data.roads = (4, 3)
        if (560, 262.5) in data.occupiedRoads:
            data.roads = (4, 5)
    if data.prevCoord == (5, 4):
        if (657.5, 206.25) not in data.occupiedRoads:
            lst += [(657.5, 206.25)]
        if (690, 262.5) not in data.occupiedRoads:
            lst += [(690, 262.5)]
        if (657.5, 206.25) in data.occupiedRoads:
            data.roads = (4, 3)
        if (690, 262.5) in data.occupiedRoads:
            data.roads = (5, 5)
    if data.prevCoord == (1, 5):
        if (170, 262.5) not in data.occupiedRoads:
            lst += [(170, 262.5)]
        if (137.5, 318.75) not in data.occupiedRoads:
            lst += [(137.5, 318.75)]
        if (202.5, 318.75) not in data.occupiedRoads:
            lst += [(202.5, 318.75)]
        if (170, 262.5) in data.occupiedRoads:
            data.roads = (1, 4)
        if (137.5, 318.75) in data.occupiedRoads:
            data.roads = (1, 6)
        if (202.5, 318.75) in data.occupiedRoads:
            data.roads = (2, 6)
    if data.prevCoord == (2, 5):
        if (300, 262.5) not in data.occupiedRoads:
            lst += [(300, 262.5)]
        if (267.5, 318.75) not in data.occupiedRoads:
            lst += [(267.5, 318.75)]
        if (332.5, 318.75) not in data.occupiedRoads:
            lst += [(332.5, 318.75)]
        if (300, 262.5) in data.occupiedRoads:
            data.roads = (2, 4)
        if (267.5, 318.75) in data.occupiedRoads:
            data.roads = (2, 6)
        if (332.5, 318.75) in data.occupiedRoads:
            data.roads = (3, 6)
    if data.prevCoord == (3, 5):
        if (430, 262.5) not in data.occupiedRoads:
            lst += [(430, 262.5)]
        if (397.5, 318.75) not in data.occupiedRoads:
            lst += [(397.5, 318.75)]
        if (462.5, 318.75) not in data.occupiedRoads:
            lst += [(462.5, 318.75)]
        if (430, 262.5) in data.occupiedRoads:
            data.roads = (3, 4)
        if (397.5, 318.75) in data.occupiedRoads:
            data.roads = (3, 6)
        if (462.5, 318.75) in data.occupiedRoads:
            data.roads = (4, 6)
    if data.prevCoord == (4, 5):
        if (560, 262.5) not in data.occupiedRoads:
            lst += [(560, 262.5)]
        if (527.5, 318.75) not in data.occupiedRoads:
            lst += [(527.5, 318.75)]
        if (592.5, 318.75) not in data.occupiedRoads:
            lst += [(592.5, 318.75)]
        if (560, 262.5) in data.occupiedRoads:
            data.roads = (4, 4)
        if (527.5, 318.75) in data.occupiedRoads:
            data.roads = (4, 6)
        if (592.5, 318.75) in data.occupiedRoads:
            data.roads = (5, 6)
    if data.prevCoord == (5, 5):
        if (690, 262.5) not in data.occupiedRoads:
            lst += [(690, 262.5)]
        if (657.5, 318.75) not in data.occupiedRoads:
            lst += [(657.5, 318.75)]
        if (722.5, 318.75) not in data.occupiedRoads:
            lst += [(722.5, 318.75)]
        if (690, 262.5) in data.occupiedRoads:
            data.roads = (5, 4)
        if (657.5, 318.75) in data.occupiedRoads:
            data.roads = (5, 6)
        if (722.5, 318.75) in data.occupiedRoads:
            data.roads = (6, 6)
    if data.prevCoord == (1, 6):
        if (137.5, 318.75) not in data.occupiedRoads:
            lst += [(137.5, 318.75)]
        if (105, 375) not in data.occupiedRoads:
            lst += [(105, 375)]
        if (137.5, 318.75) in data.occupiedRoads:
            data.roads = (1, 5)
        if (105, 375) in data.occupiedRoads:
            data.roads = (1, 7)
    if data.prevCoord == (2, 6):
        if (202.5, 318.75) not in data.occupiedRoads:
            lst += [(202.5, 318.75)]
        if (267.5, 318.75) not in data.occupiedRoads:
            lst += [(267.5, 318.75)]
        if (235, 375) not in data.occupiedRoads:
            lst += [(235, 375)]
        if (202.5, 318.75) in data.occupiedRoads:
            data.roads = (1, 5)
        if (267.5, 318.75) in data.occupiedRoads:
            data.roads = (2, 5)
        if (235, 375) in data.occupiedRoads:
            data.roads = (2, 7)
    if data.prevCoord == (3, 6):
        if (332.5, 318.75) not in data.occupiedRoads:
            lst += [(332.5, 318.75)]
        if (397.5, 318.75) not in data.occupiedRoads:
            lst += [(397.5, 318.75)]
        if (365, 375) not in data.occupiedRoads:
            lst += [(365, 375)]
        if (332.5, 318.75) in data.occupiedRoads:
            data.roads = (2, 5)
        if (397.5, 318.75) in data.occupiedRoads:
            data.roads = (3, 5)
        if (365, 375) in data.occupiedRoads:
            data.roads = (3, 7)
    if data.prevCoord == (4, 6):
        if (462.5, 318.75) not in data.occupiedRoads:
            lst += [(462.5, 318.75)]
        if (527.5, 318.75) not in data.occupiedRoads:
            lst += [(527.5, 318.75)]
        if (495, 375) not in data.occupiedRoads:
            lst += [(495, 375)]
        if (462.5, 318.75) in data.occupiedRoads:
            data.roads = (3, 5)
        if (527.5, 318.75) in data.occupiedRoads:
            data.roads = (4, 5)
        if (495, 375) in data.occupiedRoads:
            data.roads = (4, 7)
    if data.prevCoord == (5, 6):
        if (592.5, 318.75) not in data.occupiedRoads:
            lst += [(592.5, 318.75)]
        if (657.5, 318.75) not in data.occupiedRoads:
            lst += [(657.5, 318.75)]
        if (625, 375) not in data.occupiedRoads:
            lst += [(625, 375)]
        if (592.5, 318.75) in data.occupiedRoads:
            data.roads = (4, 5)
        if (657.5, 318.75) in data.occupiedRoads:
            data.roads = (5, 5)
        if (625, 375) in data.occupiedRoads:
            data.roads = (5, 7)
    if data.prevCoord == (6, 6):
        if (722.5, 318.75) not in data.occupiedRoads:
            lst += [(722.5, 318.75)]
        if (755, 375) not in data.occupiedRoads:
            lst += [(755, 375)]
        if (722.5, 318.75) in data.occupiedRoads:
            data.roads = (5, 5)
        if (755, 375) in data.occupiedRoads:
            data.roads = (6, 7)
    if data.prevCoord == (1, 7):
        if (105, 375) not in data.occupiedRoads:
            lst += [(105, 375)]
        if (137.5, 431.25) not in data.occupiedRoads:
            lst += [(137.5, 431.25)]
        if (105, 375) in data.occupiedRoads:
            data.roads = (1, 6)
        if (137.5, 431.25) in data.occupiedRoads:
            data.roads = (1, 8)
    if data.prevCoord == (2, 7):
        if (235, 375) not in data.occupiedRoads:
            lst += [(235, 375)]
        if (202.5, 431.25) not in data.occupiedRoads:
            lst += [(202.5, 431.25)]
        if (267.5, 431.25) not in data.occupiedRoads:
            lst += [(267.5, 431.25)]
        if (235, 375) in data.occupiedRoads:
            data.roads = (2, 6)
        if (202.5, 431.25) in data.occupiedRoads:
            data.roads = (1, 8)
        if (267.5, 431.25) in data.occupiedRoads:
            data.roads = (2, 8)
    if data.prevCoord == (3, 7):
        if (365, 375) not in data.occupiedRoads:
            lst += [(365, 375)]
        if (332.5, 431.25) not in data.occupiedRoads:
            lst += [(332.5, 431.25)]
        if (397.5, 431.25) not in data.occupiedRoads:
            lst += [(397.5, 431.25)]
        if (365, 375) in data.occupiedRoads:
            data.roads = (3, 6)
        if (332.5, 431.25) in data.occupiedRoads:
            data.roads = (2, 8)
        if (397.5, 431.25) in data.occupiedRoads:
            data.roads = (3, 8)
    if data.prevCoord == (4, 7):
        if (495, 375) not in data.occupiedRoads:
            lst += [(495, 375)]
        if (462.5, 431.25) not in data.occupiedRoads:
            lst += [(462.5, 431.25)]
        if (527.5, 431.25) not in data.occupiedRoads:
            lst += [(527.5, 431.25)]
        if (495, 375) in data.occupiedRoads:
            data.roads = (4, 6)
        if (462.5, 431.25) in data.occupiedRoads:
            data.roads = (3, 8)
        if (527.5, 4312.5) in data.occupiedRoads:
            data.roads = (4, 8)
    if data.prevCoord == (5, 7):
        if (625, 375) not in data.occupiedRoads:
            lst += [(625, 375)]
        if (592.5, 431.25) not in data.occupiedRoads:
            lst += [(592.5, 431.25)]
        if (657.5, 431.25) not in data.occupiedRoads:
            lst += [(657.5, 431.25)]
        if (625, 375) in data.occupiedRoads:
            data.roads = (5, 6)
        if (592.5, 431.25) in data.occupiedRoads:
            data.roads = (4, 8)
        if (657.5, 431.25) in data.occupiedRoads:
            data.roads = (5, 8)
    if data.prevCoord == (6, 7):
        if (755, 375) not in data.occupiedRoads:
            lst += [(755, 375)]
        if (722.5, 431.25) not in data.occupiedRoads:
            lst += [(722.5, 431.25)]
        if (755, 375) in data.occupiedRoads:
            data.roads = (6, 6)
        if (722.5, 431.25) in data.occupiedRoads:
            data.roads = (5, 8)
    if data.prevCoord == (1, 8):
        if (137.5, 431.25) not in data.occupiedRoads:
            lst += [(137.5, 431.25)]
        if (202.5, 431.25) not in data.occupiedRoads:
            lst += [(202.5, 431.25)]
        if (170, 487.5) not in data.occupiedRoads:
            lst += [(170, 487.5)]
        if (137.5, 431.25) in data.occupiedRoads:
            data.roads = (1, 7)
        if (202.5, 431.25) in data.occupiedRoads:
            data.roads = (2, 7)
        if (170, 487.5) in data.occupiedRoads:
            data.roads = (1, 9)
    if data.prevCoord == (2, 8):
        if (267.5, 431.25) not in data.occupiedRoads:
            lst += [(267.5, 431.25)]
        if (332.5, 431.25) not in data.occupiedRoads:
            lst += [(332.5, 431.25)]
        if (300, 487.5) not in data.occupiedRoads:
            lst += [(300, 487.5)]
        if (267.5, 431.25) in data.occupiedRoads:
            data.roads = (2, 7)
        if (332.5, 431.25) in data.occupiedRoads:
            data.roads = (3, 7)
        if (300, 487.5) in data.occupiedRoads:
            data.roads = (2, 9)
    if data.prevCoord == (3, 8):
        if (397.5, 431.25) not in data.occupiedRoads:
            lst += [(397.5, 431.25)]
        if (462.5, 431.25) not in data.occupiedRoads:
            lst += [(462.5, 431.25)]
        if (430, 487.5) not in data.occupiedRoads:
            lst += [(430, 487.5)]
        if (397.5, 431.25) in data.occupiedRoads:
            data.roads = (3, 7)
        if (462.5, 431.25) in data.occupiedRoads:
            data.roads = (4, 7)
        if (430, 487.5) in data.occupiedRoads:
            data.roads = (3, 9)
    if data.prevCoord == (4, 8):
        if (527.5, 431.25) not in data.occupiedRoads:
            lst += [(527.5, 431.25)]
        if (592.5, 431.25) not in data.occupiedRoads:
            lst += [(592.5, 431.25)]
        if (560, 487.5) not in data.occupiedRoads:
            lst += [(560, 487.5)]
        if (527.5, 431.25) in data.occupiedRoads:
            data.roads = (4, 7)
        if (592.5, 431.25) in data.occupiedRoads:
            data.roads = (5, 7)
        if (560, 487.5) in data.occupiedRoads:
            data.roads = (4, 9)
    if data.prevCoord == (5, 8):
        if (657.5, 431.25) not in data.occupiedRoads:
            lst += [(657.5, 431.25)]
        if (722.5, 431.25) not in data.occupiedRoads:
            lst += [(722.5, 431.25)]
        if (690, 487.5) not in data.occupiedRoads:
            lst += [(690, 487.5)]
        if (657.5, 431.25) in data.occupiedRoads:
            data.roads = (5, 7)
        if (722.5, 431.25) in data.occupiedRoads:
            data.roads = (6, 7)
        if (690, 487.5) in data.occupiedRoads:
            data.roads = (5, 9)
    if data.prevCoord == (1, 9):
        if (170, 487.5) not in data.occupiedRoads:
            lst += [(170, 487.5)]
        if (202.5, 543.75) not in data.occupiedRoads:
            lst += [(202.5, 543.75)]
        if (170, 487.5) in data.occupiedRoads:
            data.roads = (1, 8)
        if (202.5, 543.75) in data.occupiedRoads:
            data.roads = (1, 10)
    if data.prevCoord == (2, 9):
        if (300, 487.5) not in data.occupiedRoads:
            lst += [(300, 487.5)]
        if (267.5, 543.75) not in data.occupiedRoads:
            lst += [(267.5, 543.75)]
        if (332.5, 543.75) not in data.occupiedRoads:
            lst += [(332.5, 543.75)]
        if (300, 487.5) in data.occupiedRoads:
            data.roads = (2, 8)
        if (267.5, 543.75) in data.occupiedRoads:
            data.roads = (1, 10)
        if (332.5, 543.75) in data.occupiedRoads:
            data.roads = (2, 10)
    if data.prevCoord == (3, 9):
        if (430, 487.5) not in data.occupiedRoads:
            lst += [(430, 487.5)]
        if (397.5, 543.75) not in data.occupiedRoads:
            lst += [(397.5, 543.75)]
        if (462.5, 543.75) not in data.occupiedRoads:
            lst += [(462.5, 543.75)]
        if (430, 487.5) in data.occupiedRoads:
            data.roads = (3, 8)
        if (397.5, 543.75) in data.occupiedRoads:
            data.roads = (2, 10)
        if (462.5, 543.75) in data.occupiedRoads:
            data.roads = (3, 10)
    if data.prevCoord == (4, 9):
        if (560, 487.5) not in data.occupiedRoads:
            lst += [(560, 487.5)]
        if (527.5, 543.75) not in data.occupiedRoads:
            lst += [(527.5, 543.75)]
        if (592.5, 543.75) not in data.occupiedRoads:
            lst += [(592.5, 543.75)]
        if (560, 487.5) in data.occupiedRoads:
            data.roads = (4, 8)
        if (527.5, 543.75) in data.occupiedRoads:
            data.roads = (3, 10)
        if (592.5, 543.75) in data.occupiedRoads:
            data.roads = (4, 10)
    if data.prevCoord == (5, 9):
        if (690, 487.5) not in data.occupiedRoads:
            lst += [(690, 487.5)]
        if (657.5, 543.75) not in data.occupiedRoads:
            lst += [(657.5, 543.75)]
        if (690, 487.5) in data.occupiedRoads:
            data.roads = (5, 8)
        if (657.5, 543.75) in data.occupiedRoads:
            data.roads = (4, 10)
    if data.prevCoord == (1, 10):
        if (202.5, 543.75) not in data.occupiedRoads:
            lst += [(202.5, 543.75)]
        if (267.5, 543.75) not in data.occupiedRoads:
            lst += [(267.5, 543.75)]
        if (235, 600) not in data.occupiedRoads:
            lst += [(235, 600)]
        if (202.5, 543.75) in data.occupiedRoads:
            data.roads = (1, 9)
        if (267.5, 543.75) in data.occupiedRoads:
            data.roads = (2, 9)
        if (235, 600) in data.occupiedRoads:
            data.roads = (1, 11)
    if data.prevCoord == (2,10):
        if (332.5, 543.75) not in data.occupiedRoads:
            lst += [(332.5, 543.75)]
        if (397.5, 543.75) not in data.occupiedRoads:
            lst += [(397.5, 543.75)]
        if (365, 600) not in data.occupiedRoads:
            lst += [(365, 600)]
        if (332.5, 543.75) in data.occupiedRoads:
            data.roads = (2, 9)
        if (397.5, 543.75) in data.occupiedRoads:
            data.roads = (3, 9)
        if (365, 600) in data.occupiedRoads:
            data.roads = (2, 11)
    if data.prevCoord == (3, 10):
        if (462.5, 543.75) not in data.occupiedRoads:
            lst += [(462.5, 543.75)]
        if (527.5, 543.75) not in data.occupiedRoads:
            lst += [(527.5, 543.75)]
        if (495, 600) not in data.occupiedRoads:
            lst += [(495, 600)]
        if (462.5, 543.75) in data.occupiedRoads:
            data.roads = (3, 9)
        if (527.5, 543.75) in data.occupiedRoads:
            data.roads = (4, 9)
        if (495, 600) in data.occupiedRoads:
            data.roads = (3, 11)
    if data.prevCoord == (4, 10):
        if (592.5, 543.75) not in data.occupiedRoads:
            lst += [(592.5, 543.75)]
        if (657.5, 543.75) not in data.occupiedRoads:
            lst += [(657.5, 543.75)]
        if (625, 600) not in data.occupiedRoads:
            lst += [(625, 600)]
        if (592.5, 543.75) in data.occupiedRoads:
            data.roads = (4, 9)
        if (657.5, 543.75) in data.occupiedRoads:
            data.roads = (5, 9)
        if (625, 600) in data.occupiedRoads:
            data.roads = (4, 11)
    if data.prevCoord == (1, 11):
        if (235, 600) not in data.occupiedRoads:
            lst += [(235, 600)]
        if (267.5, 656.25) not in data.occupiedRoads:
            lst += [267.5, 656.25]
        if (235, 600) in data.occupiedRoads:
            data.roads = (1, 10)
        if (267.5, 656.25) in data.occupiedRoads:
            data.roads = (1, 12)
    if data.prevCoord == (2, 11):
        if (365, 600) not in data.occupiedRoads:
            lst += [(365, 600)]
        if (332.5, 656.25) not in data.occupiedRoads:
            lst += [(332.5, 656.25)]
        if (397.5, 656.25) not in data.occupiedRoads:
            lst += [(397.5, 656.25)]
        if (365, 600) in data.occupiedRoads:
            data.roads = (2, 10)
        if (332.5, 656.25) in data.occupiedRoads:
            data.roads = (1, 12)
        if (397.5, 656.25) in data.occupiedRoads:
            data.roads = (2, 12)
    if data.prevCoord == (3, 11):
        if (495, 600) not in data.occupiedRoads:
            lst += [(495, 600)]
        if (462.5, 656.25) not in data.occupiedRoads:
            lst += [(462.5, 656.25)]
        if (527.5, 656.25) not in data.occupiedRoads:
            lst += [(527.5, 656.25)]
        if (495, 600) in data.occupiedRoads:
            data.roads = (3, 10)
        if (462.5, 656.25) in data.occupiedRoads:
            data.roads = (2, 12)
        if (527.5, 656.25) in data.occupiedRoads:
            data.roads = (3, 12)
    if data.prevCoord == (4, 11):
        if (625, 600) not in data.occupiedRoads:
            lst += [(625, 600)]
        if (592.5, 600) not in data.occupiedRoads:
            lst += [(592.5, 656.25)]
        if (625, 600) in data.occupiedRoads:
            data.roads = (4, 10)
        if (592.5, 600) in data.occupiedRoads:
            data.roads = (3, 12)
    if data.prevCoord == (1, 12):
        if (267.5, 656.25) not in data.occupiedRoads:
            lst += [(267.5, 656.25)]
        if (332.5, 656.25) not in data.occupiedRoads:
            lst += [(332.5, 656.25)]
        if (267.5, 656.25) in data.occupiedRoads:
            data.drawRoads = (1, 11)
        if (332.5, 656.25) in data.occupiedRoads:
            data.drawRoads = (2, 11)
    if data.prevCoord == (2, 12):
        if (397.5, 656.25) not in data.occupiedRoads:
            lst += [(397.5, 656.25)]
        if (462.5, 656.25) not in data.occupiedRoads:
            lst += [(462.5, 656.25)]
        if (397.5, 656.25) in data.occupiedRoads:
            data.roads = (2, 11)
        if (462.5, 656.25) in data.occupiedRoads:
            data.roads = (3, 11)
    if data.prevCoord == (3, 12):
        if (527.5, 656.25) not in data.occupiedRoads:
            lst += [(527.5, 656.25)] 
        if (592.5, 656.25) not in data.occupiedRoads:
            lst += [(592.5, 656.25)]
        if (527.5, 656.25) in data.occupiedRoads:
            data.roads = (3, 11)
        if (592.5, 656.25) in data.occupiedRoads:
            data.roads = (4, 11)
    return lst