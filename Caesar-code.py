#Author:Yoshiki Hoshinaga
#Date June 1

#part 1
def index(elem,seq):
    if (len(seq) == 0):
        return -1
    elif seq[0]==elem:
        return 0
    else:
        ret = index(elem,seq[1:])
        if ret == -1:
            return -1
        else:
            return ret + 1

#part 2
def jscore(s1, s2):
    score=0
    for i in range(len(s1)):
        if s1[i] in s2:
            score += 1
            s2 = s2.replace(s1[i], '', 1)
    return score

#part 3
def lcs(s1,s2):
    if len(s1)==0 or len(s2)==0:
        return ""
    if s1[-1] == s2[-1]:
        return lcs(s1[:-1], s2[:-1]) + s1[-1]
    sub1 = lcs(s1[:-1], s2)
    sub2 = lcs(s1, s2[:-1])
    if len(sub1) > len(sub2):
        return sub1
    else:
        return sub2

if __name__ == '__main__':
#test
    print(index(5, [4, 10, 5, 3, 7, 5]))
    print(index('hi', ['well', 'hi', 'there']))
    print(index('b', 'banana'))
    print(index('a', 'banana'))
    print(index('i', 'team'))
    print(index('hi', ['hello', 111, True]))
    print(index('a', ''))
    print(index(42, [])) 
    print(jscore('diner', 'syrup'))
    print(jscore('always', 'bananas'))
    print(jscore('always', 'walking'))
    print(jscore('recursion', 'excursion'))
    print(jscore('recursion', ''))
    print(lcs('human','chimp'))
    print(lcs('gattaca', 'tacgaacta'))
    print(lcs('wow', 'whew'))
    print(lcs('', 'whew'))
    print(lcs('abcdefgh', 'efghabcd'))
