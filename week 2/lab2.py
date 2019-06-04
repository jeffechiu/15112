import random

def getKthDigit(n, k):
    if n < 0:
        n *= -1
    n //= (10**k)
    return n%10

def countMatchingDigits(x, y):
    strX, strY = str(x), str(y)
    count = 0
    for digit in strX:
        for yDigit in strY:
            if digit == yDigit:
                count += 1
    return count

def playPig():
    turn = 0
    p1Score = 0
    p2Score = 0
    curScore = 0
    while p1Score < 100 and p2Score < 100:
        turn += 1
        if turn % 2 == 0:
            print("Player 2's turn!")
        else:
            print("Player 1's turn!")
        curRoll = random.randint(1, 6)
        print("You rolled a %d!" % curRoll)
        if curRoll == 1:
            # curScore = 0
            if turn % 2 == 0:
                p2Score += curScore
                print("Your current score is %d." % p2Score)
            else:
                p1Score += curScore
                print("Your current score is %d." % p1Score)
        else:
            curScore += curRoll
            if turn % 2 == 0:
                p2Score += curScore
                print("Your current score is %d." % p2Score)
            else:
                p1Score += curScore
                print("Your current score is %d." % p1Score)
            move = input("Would you like to play or hold?")
            if move == "play":
                if turn % 2 == 0:
                    p2Score -= curScore
                    turn -= 1
                    continue
                else:
                    p1Score -= curScore
                    turn -= 1
                    continue
            elif move == "hold":
                curScore = 0
                continue
    if p1Score >= 100:
        print("Player 1 Wins!")
    elif p2Score >= 100:
        print("Player 2 Wins!")
                    
    
    
def testCountMatchingDigits():
    print('Testing countMatchingDigits()... ', end='')
    assert(countMatchingDigits(1234, 2071) == 2)
    assert(countMatchingDigits(2203, 1527) == 2)
    assert(countMatchingDigits(5, 1253) == 1)
    assert(countMatchingDigits(18737, 7) == 2)
    assert(countMatchingDigits(1220, 7322) == 4)
    assert(countMatchingDigits(1234, 5678) == 0)
    print('Passed!')

def testAll():
    testCountMatchingDigits()
    playPig()

def main():
    testAll()

if __name__ == '__main__':
    main()