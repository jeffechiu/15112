#################################################
# Hw2
#################################################

import cs112_s18_week2_linter
import math
import string

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Hw2 problems
#################################################

def roc2Answer():
    return "aBc\tdEf\n"

def sumOfSquaresOfDigits(x):
    sum = 0
    while x != 0:
        sum += (x%10)**2
        x//=10
    return sum

def isHappyNumber(x):
    if x <= 0:
        return False
    while x != 1:
        x = sumOfSquaresOfDigits(x)
        if x== 4:
            return False
    return True

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for factor in range(2, n):
        if n%factor == 0:
            return False
    return True

def nthHappyPrime(n):
    found = -1
    guess = 0
    while found < n:
        guess += 1
        if isHappyNumber(guess) and isPrime(guess):
            found += 1
    return guess
    
def patternedMessage(msg, pattern):
    newMsg = ""
    counter = 1
    newPattern= ""
    for character in msg:
        if not character in string.whitespace:
            newMsg += character
    for letter in pattern:
        if letter in string.whitespace:
            newPattern += letter
        if not letter in string.whitespace:
            newPattern += newMsg[counter-1:counter]
            if counter == len(newMsg):
                counter = 1
            else:
                counter += 1
    return newPattern

def quoteWordCount(script):
    wordCount, newLine, prevCharacter, finalCount = 0, "", "a", 0
    for line in script.splitlines():
        findColon = line.find(":")
        for char in line[:len(line)-1]:
            if not char in string.punctuation: newLine += char
        newLine += line[len(line)-1]
        for character in newLine[findColon+1:]:
            if newLine[findColon+1:][0] not in string.ascii_letters:
                prevCharacter = "!"
            if character not in string.ascii_letters:
                if prevCharacter in string.ascii_letters: wordCount += 1
            prevCharacter = character
        if newLine[-1] in string.ascii_letters: wordCount += 1
        prevCharacter, newLine = "a", ""
    return wordCount

##### Bonus #####

def makeBoard(n):
    board = ""
    for spaces in range(n):
        board += "8"
    return int(board)

def digitCount(n):
    strN = str(n)
    counter = 0
    for digit in str(n):
        if digit in string.digits:
            counter += 1
    return counter

def kthDigit(n, k):
    if n < 0:
        n *= -1
    n //= (10**k)
    return n%10

def replaceKthDigit (n, k, d):
    remainder = n%(10**(k+1))
    baseNum = n-remainder
    remNum = n%(10**k)
    addedNum = d*(10**k)
    return baseNum+addedNum+remNum

def getLeftmostDigit(n):
    while n>=10:
        n//=10
    return n

def clearLeftmostDigit(n):
    counter = 0
    leftDig = n
    while leftDig >= 10:
        leftDig //= 10
        counter += 1
    return n-leftDig*(10**counter)

def makeMove(board, position, move):
    if not (move == 1 or move == 2):
        return "move must be 1 or 2!"
    boardStr = str(board)
    if position > len(boardStr):
        return "offboard!"
    elif boardStr[position-1] != '8':
        return "occupied!"
    finalBoard = ""
    counter = 0
    for space in boardStr:
        counter += 1
        if position == counter:
            finalBoard += str(move)
        else:
            finalBoard += space
    return int(finalBoard)

def isWin(board):
    boardStr = str(board)
    for space in range(len(boardStr)):
        if boardStr[space] == '1':
            if space < len(boardStr) - 2:
                if boardStr[space+1] == '1':
                    if boardStr[space+2] == '2':
                        return True
    return False

def isFull(board):
    boardStr = str(board)
    for space in boardStr:
        if space == '8':
            return False
    return True

def play112(game):
    boardSize = getLeftmostDigit(game)
    board, moves = makeBoard(boardSize), clearLeftmostDigit(game)
    movesStr = str(moves)
    p1, p2 = "Player 1", "Player 2"
    if len(movesStr) > 1:
        for move in range(0, len(movesStr), 2):
            if makeMove(board, int(movesStr[move]),int(movesStr[move+1])) ==\
            "move must be 1 or 2!":
                if len(movesStr) % 4 == 0:
                    return ("%d: %s: move must be 1 or 2!" % (board, p2))
                return ("%d: %s: move must be 1 or 2!" % (board, p1))
            elif makeMove(board, int(movesStr[move]),int(movesStr[move+1])) ==\
            "occupied!":
                if len(movesStr) % 4 == 0:
                    return("%d: %s: occupied!" % (board, p2))
                return("%d: %s: occupied!" % (board, p1))
            elif makeMove(board, int(movesStr[move]),int(movesStr[move+1])) ==\
            "offboard!":
                if len(movesStr) % 4 == 0:
                    return("%d: %s: offboard!" % (board, p2))
                return("%d: %s: offboard!" % (board, p1))
            else:
                board = \
                makeMove(board, int(movesStr[move]),int(movesStr[move+1]))
            if isWin(board):
                if len(movesStr) % 4 == 0: return ("%d: %s wins!" % (board, p2))
                return ("%d: %s wins!" % (board, p1))
            if isFull(board):
                return ("%d: Tie!" % board)
    return ("%d: Unfinished!" % board)
        
        


#################################################
# Hw2 Test Functions
#################################################

def roc2(s):
    a = 0
    b = 0
    for i in range(1, len(s), 2):
        if s[i] in s[:i]:
            continue
        elif s[i] in string.whitespace:
            a += 1
        elif "A" <= s[i] <= "Z":
            b += 1
    return len(s) < 10 and a > 1 and a == b

def testRoc2Answer():
    print("Testing roc2Answer()...", end="")
    answer = roc2Answer()
    assert(roc2(answer) == True)
    print("Passed.")

def testSumOfSquaresOfDigits():
    print('Testing sumOfSquaresOfDigits()... ', end='')
    assert(sumOfSquaresOfDigits(5) == 25)
    assert(sumOfSquaresOfDigits(12) == 5)
    assert(sumOfSquaresOfDigits(234) == 29)
    print('Passed!')

def testIsHappyNumber():
    print('Testing isHappyNumber()... ', end='')
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print('Passed!')

def testNthHappyPrime():
    print('Testing nthHappyPrime()... ', end='')
    assert(nthHappyPrime(0) == 7)
    assert(nthHappyPrime(1) == 13)
    assert(nthHappyPrime(2) == 19)
    assert(nthHappyPrime(3) == 23)
    assert(nthHappyPrime(4) == 31)
    assert(nthHappyPrime(5) == 79)
    assert(nthHappyPrime(6) == 97)
    print('Passed!')
    
def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    pattern1 = """
***************
******   ******
***************
"""
    result1 = """
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
    assert(patternedMessage("Go Pirates!!!", pattern1).strip("\n") == 
            result1.strip("\n"))

    pattern2 = """
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""
    result2 = """
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
    assert(patternedMessage("Three Diamonds!",pattern2).strip("\n") == 
            result2.strip("\n"))

    pattern3 = """
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
"""
    result3 = """
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    assert(patternedMessage("Go Steelers!",pattern3).strip("\n") == 
            result3.strip("\n"))

    pattern4 = """
*** *** ***
** ** ** **
"""
    result4 = """
A-C D?A -CD
?A -C D? A-
"""
    assert(patternedMessage("A-C D?", pattern4).strip("\n") == 
            result4.strip("\n"))
    
    assert(patternedMessage("A", "x y z").strip("\n") == "A A A".strip("\n"))
    assert(patternedMessage("The pattern is empty!", "").strip("\n") == "")
    print("Passed!")

def testQuoteWordCount():
    print("Testing simpleScreenplayWordCount()...", end="")
    quote1 = "Buttercup: You mock my pain.\n" + \
             "Man in Black: Life is pain, Highness. " + \
             "Anyone who says differently is selling something."
    assert(quoteWordCount(quote1) == 15)
    quote2 = "Inigo Montoya: Hello. My name is Inigo Montoya. " + \
             "You killed my father. Prepare to die."
    assert(quoteWordCount(quote2) == 13)
    quote3 = "Costello: You know the fellows' names?\n" + \
             "Abbott: Yes.\n" + \
             "Costello: Well, then who's playing first?\n" + \
             "Abbott: Yes.\n" + \
             "Costello: I mean the fellow's name on first base.\n" + \
             "Abbott: Who."
    assert(quoteWordCount(quote3) == 21)
    quote4 = "Martin Luther King Jr.: " + \
             "The first question which the priest and the Levite asked was:" + \
             " 'If I stop to help this man, what will happen to me?' " + \
             "But... the good Samaritan reversed the question: " + \
             "'If I do not stop to help this man, what will happen to him?'"
    assert(quoteWordCount(quote4) == 44)
    quote5 = "Unknown: Only half of programming is coding. " + \
             "The other 90 percent is debugging."
    assert(quoteWordCount(quote5) == 11) # yes, 11; 90 doesn't count as a word
    quote6 = "Judge Clarence Thomas: "
    assert(quoteWordCount(quote6) == 0)
    quote7 = "Tommy Tutone: 867 - 5309"
    assert(quoteWordCount(quote7) == 0)
    assert(quoteWordCount("") == 0)
    print("Passed!")

def testMakeBoard():
    print("Testing makeBoard()...", end="")
    assert(makeBoard(1) == 8)
    assert(makeBoard(2) == 88)
    assert(makeBoard(3) == 888)
    print("Passed!")
    
def testDigitCount():
    print("Testing digitCount()...", end="")
    assert(digitCount(0) == 1)
    assert(digitCount(5) == digitCount(-5) == 1)
    assert(digitCount(42) == digitCount(-42) == 2)
    assert(digitCount(121) == digitCount(-121) == 3)
    print("Passed!")

def testKthDigit():
    print("Testing kthDigit()...", end="")
    assert(kthDigit(789, 0) == kthDigit(-789, 0) == 9)
    assert(kthDigit(789, 1) == kthDigit(-789, 1) == 8)
    assert(kthDigit(789, 2) == kthDigit(-789, 2) == 7)
    assert(kthDigit(789, 3) == kthDigit(-789, 3) == 0)
    assert(kthDigit(789, 4) == kthDigit(-789, 4) == 0)
    print("Passed!")
    
def testReplaceKthDigit():
    print("Testing replaceKthDigit()...", end="")
    assert(replaceKthDigit(789, 0, 6) == 786)
    assert(replaceKthDigit(789, 1, 6) == 769)
    assert(replaceKthDigit(789, 2, 6) == 689)
    assert(replaceKthDigit(789, 3, 6) == 6789)
    assert(replaceKthDigit(789, 4, 6) == 60789)
    print("Passed!")
    
def testGetLeftMostDigit():
    print("Testing getLeftMostDigit()...", end="")
    assert(getLeftmostDigit(7089) == 7)
    assert(getLeftmostDigit(89) == 8)
    assert(getLeftmostDigit(9) == 9)
    assert(getLeftmostDigit(0) == 0)
    print("Passed!")
    
def testClearLeftMostDigit():
    print("Testing clearLeftMostDigit()...", end="")
    assert(clearLeftmostDigit(789) == 89)
    assert(clearLeftmostDigit(89) == 9)
    assert(clearLeftmostDigit(9) == 0)
    assert(clearLeftmostDigit(0) == 0)
    assert(clearLeftmostDigit(60789) == 789)
    print("Passed!")

def testMakeMove():
    print("Testing makeMove()...", end="")
    assert(makeMove(8, 1, 1) == 1)
    assert(makeMove(888888, 1, 1) == 188888)
    assert(makeMove(888888, 2, 1) == 818888)
    assert(makeMove(888888, 5, 2) == 888828)
    assert(makeMove(888888, 6, 2) == 888882)
    assert(makeMove(888888, 6, 3) == "move must be 1 or 2!")
    assert(makeMove(888888, 7, 1) == "offboard!")
    assert(makeMove(888881, 6, 1) == "occupied!")
    print("Passed!")
    
def testIsWin():
    print("Testing isWin()...", end="")
    assert(isWin(888888) == False)
    assert(isWin(112888) == True)
    assert(isWin(811288) == True)
    assert(isWin(888112) == True)
    assert(isWin(211222) == True)
    assert(isWin(212212) == False)
    print("Passed!")
    
def testIsFull():
    print("Testing isFull()...", end="")
    assert(isFull(888888) == False)
    assert(isFull(121888) == False)
    assert(isFull(812188) == False)
    assert(isFull(888121) == False)
    assert(isFull(212122) == True)
    assert(isFull(212212) == True)
    print("Passed!")

def testBonusPlay112():
    print("Testing play112()... ", end="")
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print("Passed!")

#################################################
# Hw2 Main
#################################################

def testAll():
    testRoc2Answer()
    testSumOfSquaresOfDigits()
    testIsHappyNumber()
    testNthHappyPrime()
    testPatternedMessage()
    testQuoteWordCount()
    testMakeBoard()
    testDigitCount()
    testKthDigit()
    testReplaceKthDigit()
    testGetLeftMostDigit()
    testClearLeftMostDigit()
    testMakeMove()
    testIsWin()
    testIsFull()
    testBonusPlay112()

def main():
    cs112_s18_week2_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
