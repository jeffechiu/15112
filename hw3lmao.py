import string

# def mostFrequentLetters(s):
#     count, most = 0, 0
#     curLet, final, newAlpha = "", "", ""
#     alpha = string.ascii_lowercase
#     while True:
#         #loop through the alphabet
#         for letter in alpha:
#             #get the indices of s
#             for i in range(len(s)):
#                 #compare to see if s[i] is the letter and if it is, increment a count variable
#                 if s[i].lower() == letter:
#                     count += 1
#             if count > most:
#                 #change the most into the count
#                 most = count
#                 #change the letter of the letter that shows up the most
#                 curLet = letter
#                 #reset count variable
#                 count = 0
#             #reset count variable
#             count = 0
#         if most == 0:
#             break
#         #add to final
#         final += curLet
#         #looping through entire alphabet again
#         for ltr in string.ascii_lowercase:
#             #only add letters that have not been added to final
#             if ltr not in final:
#                 newAlpha += ltr
#         #reset alphabet
#         alpha = newAlpha
#         #start a new alphabet
#         newAlpha = ""
#         #reset most
#         most = 0
#     return final



def longestCommonSubstring(s1, s2):
    final, temp = "", ""
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                for k in range(min(len(s1)-i, len(s2)-j)):
                    if s1[i+k] == s2[j+k]:
                        temp += s1[i+k]
                    else:
                        break
                if len(temp) > len(final):
                    final = temp
                elif len(temp) == len(final):
                    if temp < final:
                        final = temp
                temp = ""
    return final

def mostFrequentLetters(s):
    count, most = 0, 0
    curLet, tempS = "", ""
    final = ""
    for letter in string.ascii_letters:
        for idx in s:
            if letter == idx.lower():
                count += 1
                print(count)
        if count > most:
            most = count
            curLet = letter
        count = 0
        final += curLet
        print("final is ", final)
        for i in s:
            if i != letter:
                tempS += i
        s = tempS
    return final
                
def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")
    assert(mostFrequentLetters("We attack at Dawn") == "atwcdekn")
    s = "Note that digits, punctuation, and whitespace are not letters!"
    assert(mostFrequentLetters(s) == "teanioscdhpruglw")
    assert(mostFrequentLetters("") == "")
    print("Passed.")

def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed.")

def testAll():
    testMostFrequentLetters()
    testLongestCommonSubstring()

testAll()