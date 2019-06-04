from essentials import *

def getLegalCity(data):
    coords = []
    if data.turn == 1:
        if len(data.p1Ex['settle']) > 0:
            for i in data.p1Ex['settle']:
                coords += [coordConverter((i))]
    if data.turn == 2:
        if len(data.p2Ex['settle']) > 0:
            for i in data.p2Ex['settle']:
                coords += [coordConverter((i))]
    if data.turn == 3:
        if len(data.p3Ex['settle']) > 0:
            for i in data.p3Ex['settle']:
                coords += [coordConverter((i))]
    if data.turn == 4:
        if len(data.p4Ex['settle']) > 0:
            for i in data.p4Ex['settle']:
                coords += [coordConverter((i))]
    return coords