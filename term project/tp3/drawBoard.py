def drawTile(data, canvas, x, y, tiles):
    for i in range(len(tiles)):
        if tiles[i] == 'wood':
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.WOOD, outline = 'black', width = 3)
        elif tiles[i] == 'brick':
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.BRICK, outline = 'black', width = 3)
        elif tiles[i] == 'sheep':
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.SHEEP, outline = 'black', width = 3)
        elif tiles[i] == 'wheat':
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.WHEAT, outline = 'black', width = 3)
        elif tiles[i] == 'stone':
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.STONE, outline = 'black', width = 3)
        else:
            canvas.create_polygon([(x+i*130, y), (x+65+i*130, y+37.5), (x+65+i*130, y+112.5),
            (x+i*130, y+150), (x-65+i*130, y+112.5), (x-65+i*130, y+37.5)], fill = data.DESERT, outline = 'black', width = 3)

def drawNums(data, canvas, x, y, numLst):
    for i in range(len(numLst)):
        if not numLst[i] == 'desert':
            if numLst[i] == 6 or numLst[i] == 8:
                canvas.create_text(x+i*130, y, text = str(numLst[i]), fill = "red", font = "Helvetica 20")
            else:
                canvas.create_text(x+i*130, y, text = str(numLst[i]), fill = "black", font = "Helvetica 20")

def drawBoard(canvas, data):
    drawTile(data, canvas, 300, 75, data.first)
    drawTile(data, canvas, 235, 187.5, data.second)
    drawTile(data, canvas, 170, 300, data.third)
    drawTile(data, canvas, 235, 412.5, data.fourth)
    drawTile(data, canvas, 300, 525, data.fifth)
    drawNums(data, canvas, 300, 150, data.firN)
    drawNums(data, canvas, 235, 262.5, data.seN)
    drawNums(data, canvas, 170, 375, data.thN)
    drawNums(data, canvas, 235, 487.5, data.foN)
    drawNums(data, canvas, 300, 600, data.fifN)

def drawPorts(canvas, data):
    #Port 1
    canvas.create_oval((150, 130), (190, 170), fill = "black", width = 0)
    canvas.create_line((170, 225), (170, 150), width = 5)
    canvas.create_line((235, 187.5), (170, 150), width = 5)
    canvas.create_text((170, 150), text = "3:1", font = "Helvetica 13 bold", fill = "white")
    #Port 2
    canvas.create_oval((345, 17.5), (385, 57.5), fill = "black", width = 0)
    canvas.create_line((300, 75), (365, 37.5), width = 5)
    canvas.create_line((365, 112.5), (365, 37.5), width = 5)
    canvas.create_text((365, 37.5), text = "3:1", font = "Helvetica 13 bold", fill = "white")
    #Port 3
    canvas.create_oval((605, 17.5), (645, 57.5), fill = data.BRICK, width = 0)
    canvas.create_line((560, 75), (625, 37.5), fill = data.BRICK, width = 5)
    canvas.create_line((625, 112.5), (625, 37.5), fill = data.BRICK, width = 5)
    canvas.create_text((625, 37.5), text = "2:1", font = "Helvetica 13 bold", fill = "white")
    #Port 4
    canvas.create_oval((735, 242.5), (775, 282.5), fill = "black", width = 0)
    canvas.create_line((690, 225), (755, 262.5), width = 5)
    canvas.create_line((690, 300), (755, 262.5), width = 5)
    canvas.create_text((755, 262.5), text = "3:1", font = "Helvetica 13 bold", fill = "white")
    #Port 5
    canvas.create_oval((735, 467.5), (775, 507.5), fill = data.WHEAT, width = 0)
    canvas.create_line((690, 450), (755, 487.5), fill = data.WHEAT, width = 5)
    canvas.create_line((690, 525), (755, 487.5), fill = data.WHEAT, width = 5)
    canvas.create_text((755, 487.5), text = "2:1", font = "Helvetica 13 bold", fill = "black")
    #Port 6
    canvas.create_oval((605, 692.5), (645, 732.5), fill = data.WOOD, width = 0)
    canvas.create_line((625, 637.5), (625, 712.5), fill = data.WOOD, width = 5)
    canvas.create_line((560, 675), (625, 712.5), fill = data.WOOD, width = 5)
    canvas.create_text((625, 712.5), text = "2:1", font = "Helvetica 13 bold", fill = "white")
    #Port 7
    canvas.create_oval((345, 692.5), (385, 732.5), fill = data.SHEEP, width = 0)
    canvas.create_line((365, 637.5), (365, 712.5), fill = data.SHEEP, width = 5)
    canvas.create_line((300, 675), (365, 712.5), fill = data.SHEEP, width = 5)
    canvas.create_text((365, 712.5), text = "2:1", font = "Helvetica 13 bold", fill = "white")
    #Port 8
    canvas.create_oval((150, 580), (190, 620), fill = "black", width = 0)
    canvas.create_line((170, 525), (170, 600), fill = "black", width = 5)
    canvas.create_line((235, 562.5), (170, 600), fill = "black", width = 5)
    canvas.create_text((170, 600), text = "3:1", font = "Helvetica 13 bold", fill = "white")
    #Port 9
    canvas.create_oval((20, 355), (60, 395), fill = data.STONE, width = 0)
    canvas.create_line((105, 337.5), (40, 375), fill = data.STONE, width = 5)
    canvas.create_line((105, 412.5), (40, 375), fill = data.STONE, width = 5)
    canvas.create_text((40, 375), text = "2:1", font = "Helvetica 13 bold", fill = "white")