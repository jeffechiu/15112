from essentials import *

def drawSettlement(canvas, x, y, color):
    canvas.create_oval((x-15, y-15), (x+15, y+15), fill = color, width = 2)

def drawCity(canvas, x, y, color):
    canvas.create_rectangle((x-15, y-15), (x+15, y+15), fill = color, width = 2)

def drawRoad(canvas, x1, y1, x2, y2, color):
    canvas.create_line(x1, y1, x2, y2, fill = color, width = 8)    

def drawExpansions(canvas, data):
    for key in data.p1Ex:
        for i in data.p1Ex[key]:
            if key == "settle": expans = "s"
            elif key == "city": expans = "c"
            elif key == "road": expans = "r"
            if expans == "r":
                if i[1] % 0.5 != 0:
                    y1 = i[1] - 18.75
                    y2 = i[1] + 18.75
                    x1 = i[0] + 32.5
                    x2 = i[0] - 32.5
                    for coords in data.allCoords:
                        if coordConverter(coords) == (x1, y1) or coordConverter(coords) == (x2, y2):
                            drawRoad(canvas, x1, y1, x2, y2, data.pColors[0])
                            break
                        if coords == data.allCoords[-1]:
                            drawRoad(canvas, x1, y2, x2, y1, data.pColors[0])
                else:
                    y1 = i[1]-37.5
                    y2 = i[1] + 37.5
                    x = i[0]
                    drawRoad(canvas, x, y1, x, y2, data.pColors[0])
            if i[1] == 1:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 75, data.pColors[0])
                else:
                    drawCity(canvas, 170+130*i[0], 75, data.pColors[0])
            if i[1] == 2:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 112.5, data.pColors[0])
                else:
                    drawCity(canvas, 105+130*i[0], 112.5, data.pColors[0])
            if i[1] == 3:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 187.5, data.pColors[0])
                else:
                    drawCity(canvas, 105+130*i[0], 187.5, data.pColors[0])
            if i[1] == 4:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 225, data.pColors[0])
                else:
                    drawCity(canvas, 40+130*i[0], 225, data.pColors[0])
            if i[1] == 5:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 300, data.pColors[0])
                else:
                    drawCity(canvas, 40+130*i[0], 300, data.pColors[0])
            if i[1] == 6:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 337.5, data.pColors[0])
                else:
                    drawCity(canvas, -25+130*i[0], 337.5, data.pColors[0])
            if i[1] == 7:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 412.5, data.pColors[0])
                else:
                    drawCity(canvas, -25+130*i[0], 412.5, data.pColors[0])
            if i[1] == 8:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 450, data.pColors[0])
                else:
                    drawCity(canvas, 40+130*i[0], 450, data.pColors[0])
            if i[1] == 9:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 525, data.pColors[0])
                else:
                    drawCity(canvas, 40+130*i[0], 525, data.pColors[0])
            if i[1] == 10:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 562.5, data.pColors[0])
                else:
                    drawCity(canvas, 105+130*i[0], 562.5, data.pColors[0])
            if i[1] == 11:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 637.5, data.pColors[0])
                else:
                    drawCity(canvas, 105+130*i[0], 637.5, data.pColors[0])
            if i[1] == 12:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 675, data.pColors[0])
                else:
                    drawCity(canvas, 170+130*i[0], 675, data.pColors[0])
        for i in data.p2Ex[key]:
            if key == "settle": expans = "s"
            elif key == "city": expans = "c"
            elif key == "road": expans = "r"
            if expans == "r":
                if i[1] % 0.5 != 0:
                    y1 = i[1] - 18.75
                    y2 = i[1] + 18.75
                    x1 = i[0] + 32.5
                    x2 = i[0] - 32.5
                    for coords in data.allCoords:
                        if coordConverter(coords) == (x1, y1) or coordConverter(coords) == (x2, y2):
                            drawRoad(canvas, x1, y1, x2, y2, data.pColors[1])
                            break
                        if coords == data.allCoords[-1]:
                            drawRoad(canvas, x1, y2, x2, y1, data.pColors[1])
                else:
                    y1 = i[1]-37.5
                    y2 = i[1] + 37.5
                    x = i[0]
                    drawRoad(canvas, x, y1, x, y2, data.pColors[1])
            if i[1] == 1:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 75, data.pColors[1])
                else:
                    drawCity(canvas, 170+130*i[0], 75, data.pColors[1])
            if i[1] == 2:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 112.5, data.pColors[1])
                else:
                    drawCity(canvas, 105+130*i[0], 112.5, data.pColors[1])
            if i[1] == 3:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 187.5, data.pColors[1])
                else:
                    drawCity(canvas, 105+130*i[0], 187.5, data.pColors[1])
            if i[1] == 4:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 225, data.pColors[1])
                else:
                    drawCity(canvas, 40+130*i[0], 225, data.pColors[1])
            if i[1] == 5:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 300, data.pColors[1])
                else:
                    drawCity(canvas, 40+130*i[0], 300, data.pColors[1])
            if i[1] == 6:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 337.5, data.pColors[1])
                else:
                    drawCity(canvas, -25+130*i[0], 337.5, data.pColors[1])
            if i[1] == 7:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 412.5, data.pColors[1])
                else:
                    drawCity(canvas, -25+130*i[0], 412.5, data.pColors[1])
            if i[1] == 8:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 450, data.pColors[1])
                else:
                    drawCity(canvas, 40+130*i[0], 450, data.pColors[1])
            if i[1] == 9:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 525, data.pColors[1])
                else:
                    drawCity(canvas, 40+130*i[0], 525, data.pColors[1])
            if i[1] == 10:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 562.5, data.pColors[1])
                else:
                    drawCity(canvas, 105+130*i[0], 562.5, data.pColors[1])
            if i[1] == 11:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 637.5, data.pColors[1])
                else:
                    drawCity(canvas, 105+130*i[0], 637.5, data.pColors[1])
            if i[1] == 12:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 675, data.pColors[1])
                else:
                    drawCity(canvas, 170+130*i[0], 675, data.pColors[1])
        for i in data.p3Ex[key]:
            if key == "settle": expans = "s"
            elif key == "city": expans = "c"
            elif key == "road": expans = "r"
            if expans == "r":
                if i[1] % 0.5 != 0:
                    y1 = i[1] - 18.75
                    y2 = i[1] + 18.75
                    x1 = i[0] + 32.5
                    x2 = i[0] - 32.5
                    for coords in data.allCoords:
                        if coordConverter(coords) == (x1, y1) or coordConverter(coords) == (x2, y2):
                            drawRoad(canvas, x1, y1, x2, y2, data.pColors[2])
                            break
                        if coords == data.allCoords[-1]:
                            drawRoad(canvas, x1, y2, x2, y1, data.pColors[2])
                else:
                    y1 = i[1]-37.5
                    y2 = i[1] + 37.5
                    x = i[0]
                    drawRoad(canvas, x, y1, x, y2, data.pColors[2])
            if i[1] == 1:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 75, data.pColors[2])
                else:
                    drawCity(canvas, 170+130*i[0], 75, data.pColors[2])
            if i[1] == 2:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 112.5, data.pColors[2])
                else:
                    drawCity(canvas, 105+130*i[0], 112.5, data.pColors[2])
            if i[1] == 3:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 187.5, data.pColors[2])
                else:
                    drawCity(canvas, 105+130*i[0], 187.5, data.pColors[2])
            if i[1] == 4:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 225, data.pColors[2])
                else:
                    drawCity(canvas, 40+130*i[0], 225, data.pColors[2])
            if i[1] == 5:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 300, data.pColors[2])
                else:
                    drawCity(canvas, 40+130*i[0], 300, data.pColors[2])
            if i[1] == 6:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 337.5, data.pColors[2])
                else:
                    drawCity(canvas, -25+130*i[0], 337.5, data.pColors[2])
            if i[1] == 7:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 412.5, data.pColors[2])
                else:
                    drawCity(canvas, -25+130*i[0], 412.5, data.pColors[2])
            if i[1] == 8:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 450, data.pColors[2])
                else:
                    drawCity(canvas, 40+130*i[0], 450, data.pColors[2])
            if i[1] == 9:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 525, data.pColors[2])
                else:
                    drawCity(canvas, 40+130*i[0], 525, data.pColors[2])
            if i[1] == 10:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 562.5, data.pColors[2])
                else:
                    drawCity(canvas, 105+130*i[0], 562.5, data.pColors[2])
            if i[1] == 11:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 637.5, data.pColors[2])
                else:
                    drawCity(canvas, 105+130*i[0], 637.5, data.pColors[2])
            if i[1] == 12:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 675, data.pColors[2])
                else:
                    drawCity(canvas, 170+130*i[0], 675, data.pColors[2])
        for i in data.p4Ex[key]:
            if key == "settle": expans = "s"
            elif key == "city": expans = "c"
            elif key == "road": expans = "r"
            if expans == "r":
                if i[1] % 0.5 != 0:
                    y1 = i[1] - 18.75
                    y2 = i[1] + 18.75
                    x1 = i[0] + 32.5
                    x2 = i[0] - 32.5
                    for coords in data.allCoords:
                        if coordConverter(coords) == (x1, y1) or coordConverter(coords) == (x2, y2):
                            drawRoad(canvas, x1, y1, x2, y2, data.pColors[3])
                            break
                        if coords == data.allCoords[-1]:
                            drawRoad(canvas, x1, y2, x2, y1, data.pColors[3])
                else:
                    y1 = i[1]-37.5
                    y2 = i[1] + 37.5
                    x = i[0]
                    drawRoad(canvas, x, y1, x, y2, data.pColors[3])
            if i[1] == 1:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 75, data.pColors[3])
                else:
                    drawCity(canvas, 170+130*i[0], 75, data.pColors[3])
            if i[1] == 2:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 112.5, data.pColors[3])
                else:
                    drawCity(canvas, 105+130*i[0], 112.5, data.pColors[3])
            if i[1] == 3:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 187.5, data.pColors[3])
                else:
                    drawCity(canvas, 105+130*i[0], 187.5, data.pColors[3])
            if i[1] == 4:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 225, data.pColors[3])
                else:
                    drawCity(canvas, 40+130*i[0], 225, data.pColors[3])
            if i[1] == 5:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 300, data.pColors[3])
                else:
                    drawCity(canvas, 40+130*i[0], 300, data.pColors[3])
            if i[1] == 6:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 337.5, data.pColors[3])
                else:
                    drawCity(canvas, -25+130*i[0], 337.5, data.pColors[3])
            if i[1] == 7:
                if expans == "s":
                    drawSettlement(canvas, -25+130*i[0], 412.5, data.pColors[3])
                else:
                    drawCity(canvas, -25+130*i[0], 412.5, data.pColors[3])
            if i[1] == 8:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 450, data.pColors[3])
                else:
                    drawCity(canvas, 40+130*i[0], 450, data.pColors[3])
            if i[1] == 9:
                if expans == "s":
                    drawSettlement(canvas, 40+130*i[0], 525, data.pColors[3])
                else:
                    drawCity(canvas, 40+130*i[0], 525, data.pColors[3])
            if i[1] == 10:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 562.5, data.pColors[3])
                else:
                    drawCity(canvas, 105+130*i[0], 562.5, data.pColors[3])
            if i[1] == 11:
                if expans == "s":
                    drawSettlement(canvas, 105+130*i[0], 637.5, data.pColors[3])
                else:
                    drawCity(canvas, 105+130*i[0], 637.5, data.pColors[3])
            if i[1] == 12:
                if expans == "s":
                    drawSettlement(canvas, 170+130*i[0], 675, data.pColors[3])
                else:
                    drawCity(canvas, 170+130*i[0], 675, data.pColors[3])