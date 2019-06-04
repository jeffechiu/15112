import random

#taken from notes
def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

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

def reverseCoords(coord):
    if coord[1] == 75:
        x = (coord[0]-170)//130
        y = 1
    if coord[1] == 112.5:
        x = (coord[0]-105)//130
        y = 2
    if coord[1] == 187.5:
        x = (coord[0]-105)//130
        y = 3
    if coord[1] == 225:
        x = (coord[0] - 40)//130
        y = 4
    if coord[1] == 300:
        x = (coord[0] - 40)//130
        y = 5
    if coord[1] == 337.5:
        x = (coord[0] + 25)//130
        y = 6
    if coord[1] == 412.5:
        x = (coord[0] + 25)//130
        y = 7
    if coord[1] == 450:
        x = (coord[0] - 40)//130
        y = 8
    if coord[1] == 525:
        x = (coord[0] - 40)//130
        y = 9
    if coord[1] == 562.5:
        x = (coord[0] - 105)//130
        y = 10
    if coord[1] == 637.5:
        x = (coord[0] - 105)//130
        y = 11
    if coord[1] == 675:
        x = (coord[0] - 170)//130
        y = 12
    return ((x, y))