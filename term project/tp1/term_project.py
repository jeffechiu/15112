import pygame, sys, random

#########################################
#Game Board
#########################################

"""
- start with one class of players
- add instances for all 4 players to add settlements, resources, etc to
"""

#get lists for pieces to put in
def threeRow(pieces):
    row = []
    for i in range(3):
        tile = random.choice(pieces)
        pieces.remove(tile)
        row += [tile]
    return row    

def fourRow(pieces):
    row = []
    for i in range(4):
        tile = random.choice(pieces)
        pieces.remove(tile)
        row += [tile]
    return row

def fiveRow(pieces):
    row = []
    for i in range(5):
        tile = random.choice(pieces)
        pieces.remove(tile)
        row += [tile]
    return row

#draw tiles based off of colors
def drawTile(pieces, x, y, row):
    for i in range(len(row)):
        if row[i] == 'wood':
            color = WOOD
        elif row[i] == 'brick':
            color = BRICK
        elif row[i] == 'wheat':
            color = WHEAT
        elif row[i] == 'sheep':
            color = SHEEP
        elif row[i] == 'stone':
            color = STONE
        else:
            color = DESERT
        pygame.draw.polygon(screen, color, [[x+(i*130), y],[x+65+(i*130), y+37.5],[x+65+(i*130), y+112.5],
            [x+(i*130), y+150], [x-65+(i*130), y+112.5], [x-65+(i*130), y+37.5]])

#put all tiles into one list
def compileTiles(firstRow, secondRow, thirdRow, fourthRow, lastRow):
    allTiles = []
    for tiles in firstRow:
        allTiles += [tiles]
    for tiles in secondRow:
        allTiles += [tiles]
    for tiles in thirdRow:
        allTiles += [tiles]
    for tiles in fourthRow:
        allTiles += [tiles]
    for tiles in lastRow:
        allTiles += [tiles]
    return allTiles

#randomize list of numbers
def getNums():
    nums = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
    numsOrder = []
    for i in range(18):
        num = random.choice(nums)
        nums.remove(num)
        numsOrder += [num]
    return numsOrder

#add 'desert' tile into list of numbers so that it matches tile list
def createFinalNums(nums, allTiles):
    desertLoc = allTiles.index('desert')
    nums.insert(desertLoc, 'desert')
    return nums

#draw all the numbers onto the board
def drawFirstNums(nums, allTiles, y):
    newFont = pygame.font.SysFont('Helvetica', 20, bold =True)
    for i in range(3):
        if not nums[i] == 'desert':
            if nums[i] == 6 or nums[i] == 8:
                text = newFont.render(str(nums[i]), True, RED)
            else:
                text = newFont.render(str(nums[i]), True, BLACK)
            screen.blit(text, (245+i*130, y))

def drawSecondNums(nums, allTiles, y):
    newFont = pygame.font.SysFont('Helvetica', 20, bold =True)
    for i in range(4):
        if not nums[3+i] == 'desert':
            if nums[3+i] == 6 or nums[3+i] == 8:
                text = newFont.render(str(nums[3+i]), True, RED)
            else:
                text = newFont.render(str(nums[3+i]), True, BLACK)
            screen.blit(text, (180+i*130, y))

def drawThirdNums(nums, allTiles, y):
    newFont = pygame.font.SysFont('Helvetica', 20, bold =True)
    for i in range(5):
        if not nums[7+i] == 'desert':
            if nums[7+i] == 6 or nums[7+i] == 8:
                text = newFont.render(str(nums[7+i]), True, RED)
            else:
                text = newFont.render(str(nums[7+i]), True, BLACK)
            screen.blit(text, (115+i*130, y))
                

def drawFourthNums(nums, allTiles, y):
    newFont = pygame.font.SysFont('Helvetica', 20, bold =True)
    for i in range(4):
        if not nums[12+i] == 'desert':
            if nums[12+i] == 6 or nums[12+i] == 8:
                text = newFont.render(str(nums[12+i]), True, RED)
            else:
                text = newFont.render(str(nums[12+i]), True, BLACK)
            screen.blit(text, (180+i*130, y))
    

def drawFifthNums(nums, allTiles, y):
    newFont = pygame.font.SysFont('Helvetica', 20, bold =True)
    for i in range(3):
        if not nums[16+i] == 'desert':
            if nums[16+i] == 6 or nums[16+i] == 8:
                text = newFont.render(str(nums[16+i]), True, RED)
            else:
                text = newFont.render(str(nums[16+i]), True, BLACK)
            screen.blit(text, (245+i*130, y))

#########################################
#Resources/Drawing Cards
#########################################

def dices():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceRoll = dice1+dice2
    diceFont = pygame.font.SysFont('Helvetica', 120)
    text = diceFont.render(str(diceRoll), True, BLACK)
    screen.blit(text, (1000, 300))
    return dice1+dice2

def drawDice(diceRoll):
    

#########################################
#Initialization Stuff
#########################################
pygame.init()
clock = pygame.time.Clock()

size = width, height = 1500, 750

screen = pygame.display.set_mode(size)

WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0

WHEAT = 255, 255, 0
BRICK = 124, 10, 2
STONE = 128, 128, 128
WOOD = 0, 100, 0
SHEEP = 0, 255, 0
DESERT = 204, 204, 0

pieces = ['wood', 'wood', 'wood', 'wood', 'brick', 'brick', 'brick', 'sheep', 'sheep',
'sheep', 'sheep', 'wheat', 'wheat', 'wheat', 'wheat', 'stone', 'stone', 'stone', 'desert']

firstRow = threeRow(pieces)
secondRow = fourRow(pieces)
thirdRow = fiveRow(pieces)
fourthRow = fourRow(pieces)
lastRow = threeRow(pieces)

allTiles = compileTiles(firstRow, secondRow, thirdRow, fourthRow, lastRow)
print(allTiles)

nums = getNums()
finalNums = createFinalNums(nums, allTiles)
print(nums)

playing = True
while playing:
    time = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    screen.fill(WHITE)
    drawTile(pieces, 245, 75, firstRow)
    drawTile(pieces, 180, 187.5, secondRow)
    drawTile(pieces, 115, 300, thirdRow)
    drawTile(pieces, 180, 412.5, fourthRow)
    drawTile(pieces, 245, 525, lastRow)
    
    drawFirstNums(finalNums, allTiles, 131.25)
    drawSecondNums(finalNums, allTiles, 243.75)
    drawThirdNums(finalNums, allTiles, 356.25)
    drawFourthNums(finalNums, allTiles, 468.75)
    drawFifthNums(finalNums, allTiles, 581.25)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                diceRoll = dices()
                print(diceRoll)

    pygame.display.flip()

pygame.quit()