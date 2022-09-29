#Author:Yoshiki Hoshinaga
#Date: June 1 2020
# Caesar cipher / decipher
#

# A template for a helper function called rot that we recommend writing
# as part of your work on the encipher function.
def rot(c, n):
    """ your docstring goes here """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.



#### Put your code for the encipher function below. ####


# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_probability(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

#### Put your code for the decipher function below. ####

#part 1
def encipher(s,n):
    result =''
    for ch in s:
        if 'a' <= ch <='z':
            ch = chr(ord('a')+(ord(ch)-ord('a')+n)%26)
        elif 'A' <= ch <= 'Z':
            ch = chr(ord('A')+(ord(ch)-ord('A')+n)%26)
        result += ch
    return result

#part2
def decipherHelper(s, rotated):
        output = ""
        for ch in s:
                if (65 <= ord(ch) and ord(ch) <= 90):
                        if (ord(ch) - rotated < 65):
                            ch = chr(26 + ord(ch) - rotated)
                        else:
                            ch = chr(ord(ch) - rotated)
                elif (97 <= ord(ch) and ord(ch) <= 122):
                        if (ord(ch) - rotated < 97):
                            ch = chr(26 + ord(ch) - rotated)
                        else:
                            ch= chr(ord(ch) - rotated)
                output += ch
        return output


def decipher(s):
    Score = 0
    ScoreStr = 'incorrect value'
    
    for i in range(26):
        output = decipherHelper(s, i)
        tscore = sum([letter_probability(ch) for ch in output])
        if tscore > Score:
            Score, ScoreStr = tscore, output

    return ScoreStr



if __name__ == '__main__':

    #Test 1
    print(encipher('hello',1))
    print(encipher('hello',2))
    print(encipher('hello',4))
    print(encipher('XYZ',3))
    print(encipher('xyz',3))
    print(encipher('#caesar!',2))

    #Test 2
    print(decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.'))
    print(decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.'))
    print(decipher('python'))
    print(decipher('kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj'))
    print(decipher('uzfqxxusqzoq bxge otmdmofqd ue ftq samx ar fdgq qpgomfuaz'))
    print(decipher(('Xli Psrk erh Amrhmrk Vseh')))
    print(decipher(''))
