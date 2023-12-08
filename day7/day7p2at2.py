from functools import cmp_to_key
from collections import Counter
from itertools import count

def fiveOfAKindFinder(hand: str):
    assert len(hand) == 5
    return len(set(hand)) == 1

def fourOfAKindFinder(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if len(handSet) != 2:
        return False
    if hand.count(handSet[0]) == 4 or hand.count(handSet[1]) == 4:
        return True
    return False

def fullHouseFinder(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if len(handSet) != 2:
        return False
    if hand.count(handSet[0]) == 3 or hand.count(handSet[0]) == 2 and hand.count(handSet[1]) == 3 or hand.count(handSet[1]) == 2:
        return True
    return False

def threeOfAKindFinder(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if len(handSet) != 3:
        return False
    for val in handSet:
        if hand.count(val) == 3:
            return True
    return False

def twoPairFinder(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if len(handSet) != 3:
        return False
    storageNum = 0
    for val in handSet:
        if hand.count(val) == 2:
            storageNum += 1
    if storageNum == 2:
        return True
    return False

def onePairFinder(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if len(handSet) != 4:
        return False
    for val in handSet:
        if hand.count(val) == 2:
            return True
    return False
        
    
    
def highCardFinder(hand: str):
    assert len(hand) == 5
    return len(set(hand)) == 5

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

def handConverter(hand: str):
    if not "J" in hand:
        return hand
    countedHand = Counter(hand)
    hand = hand.replace("J",countedHand.most_common(1)[0][0])
    return hand

def compareHands(hand1:str,hand2:str):
    hand1 = handConverter(hand1[0])
    hand2 = handConverter(hand2[0])
    cardStrengthOrder = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
    hand1Type = handIdentifier(hand1)
    hand2Type = handIdentifier(hand2)
    for (k1,v1),(k2,v2) in zip(hand1Type.items(),hand2Type.items()):
        if v1 and not v2:
            return 1
        if v2 and not v1:
            return -1
    for c1,c2 in zip(hand1,hand2):
        c1i ,c2i = cardStrengthOrder.index(c1), cardStrengthOrder.index(c2)
        if c1i < c2i:
            return 1
        elif c1i > c2i:
            return -1
    return 0
            
def main():
    with open("day7/example.txt","r") as file:
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
