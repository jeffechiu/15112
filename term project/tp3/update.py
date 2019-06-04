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