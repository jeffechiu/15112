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

def collectResources(data):
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

def collectInitResources(data, coord):
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