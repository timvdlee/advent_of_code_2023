from functools import cmp_to_key
from collections import Counter

def fiveOfAKindFinder(hand: str):
    assert len(hand) == 5
    handCont = Counter(hand)
    del handCont["J"]
    handCont["p"] = 0
    jCount = hand.count("J")
    return handCont.most_common(1)[0][1] + jCount == 5


def fourOfAKindFinder(hand: str):
    assert len(hand) == 5
    handCont = Counter(hand)
    del handCont["J"]
    handCont["p"] = 0
    jCount = hand.count("J")
    return handCont.most_common(1)[0][1] + jCount == 4


def fullHouseFinder(hand: str):
    assert len(hand) == 5
    handCont = Counter(hand)
    del handCont["J"]
    handCont["p"] = 0
    mostComm = handCont.most_common()
    jCount = hand.count("J")
    return mostComm[0][1] + jCount == 3 and mostComm[1][1] == 2


def threeOfAKindFinder(hand: str):
    assert len(hand) == 5
    handCont = Counter(hand)
    del handCont["J"]
    handCont["p"] = 0
    jCount = hand.count("J")
    return handCont.most_common(1)[0][1] + jCount == 3


def twoPairFinder(hand: str):
    assert len(hand) == 5
    jCount = hand.count("J")
    handCont = Counter(hand)
    del handCont["J"]
    handCont["p"] = 0
    mostComm = handCont.most_common()
    return mostComm[0][1] + jCount == 2 and mostComm[1][1] == 2


def onePairFinder(hand: str):
    assert len(hand) == 5
    handCont = Counter(hand)
    del handCont["J"]
    handCont["p"] = 0
    mostComm = handCont.most_common()
    jCount = hand.count("J")
    return mostComm[0][1] + jCount == 2    
    
def highCardFinder(hand: str):
    assert len(hand) == 5
    handCont = Counter(hand)
    return len(handCont) == 5



def handIdentifier(hand: str):
    return {"fiveOfAKind":fiveOfAKindFinder(hand),
            "fourOfAKind":fourOfAKindFinder(hand),
            "fullHouse":fullHouseFinder(hand),
            "threeOfAKind":threeOfAKindFinder(hand),
            "twoPair":twoPairFinder(hand),
            "onePair":onePairFinder(hand),
            "highCard":highCardFinder(hand)
            }



def inputParser(content: str):
    return [[l.split(" ")[0],int(l.split(" ")[1])] for l in content.splitlines()]

def compareHands(hand1:str,hand2:str):
    hand1,hand2 = hand1[0],hand2[0]
    cardStrengthOrder = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
    hand1Type = handIdentifier(hand1)
    hand2Type = handIdentifier(hand2)
    for (k1,v1),(k2,v2) in zip(hand1Type.items(),hand2Type.items()):
        if v1 and not v2:
            return 1
        if v2 and not v1:
            return -1
        if v1 and v2:
            break
    for c1,c2 in zip(hand1,hand2):
        c1i ,c2i = cardStrengthOrder.index(c1), cardStrengthOrder.index(c2)
        if c1i < c2i:
            return 1
        elif c1i > c2i:
            return -1
    return 0
            
def main():
    with open("day7/input.txt","r") as file:
        handsList = inputParser(file.read().strip())

    sortedHandsList = sorted(handsList,key=cmp_to_key(compareHands),reverse=True)
    totalHands = len(sortedHandsList)
    pointsPergame = []
    for i,sortedHand in enumerate(sortedHandsList):
        pointsPergame.append((totalHands-i)*sortedHand[1])
    print(sum(pointsPergame))
        

if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    
    print('--- %s seconds ---' % (time.time() - start_time))
