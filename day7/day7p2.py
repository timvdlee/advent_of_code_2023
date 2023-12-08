from functools import cmp_to_key

def fiveOfAKindFinder(hand: str):
    assert len(hand) == 5
    handSet = set(hand)
    if len(handSet) == 1:
        return True
    if len(handSet) != 2:
        return False
    if not "J" in handSet:
        return False
    return True

    

def fourOfAKindFinderWithoutJ(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if len(handSet) != 2:
        return False
    if hand.count(handSet[0]) == 4 or hand.count(handSet[1]) == 4:
        return True
    return False

def fourOfAKindFinder(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if fourOfAKindFinderWithoutJ(hand):
        return True
    if len(handSet) != 3:
        return False
    if not "J" in handSet:
        return False
    for hValue in handSet:
        if hand.count(hValue) == 3:
            return True
    return True


def fullHouseFinderWithoutJ(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if len(handSet) != 2:
        return False
    if hand.count(handSet[0]) == 3 or hand.count(handSet[0]) == 2 and hand.count(handSet[1]) == 3 or hand.count(handSet[1]) == 2:
        return True
    return False


def fullHouseFinder(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if fullHouseFinderWithoutJ(hand):
        return True
    if len(handSet) != 3:
        return False
    if "J" not in handSet:
        return False
    if hand.count("J") != 1:
        return False
    for hval in handSet:
        if hval != "J":
            if hand.count(hval) != 2:
                return False
    return True



def threeOfAKindFinderWithoutJ(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if len(handSet) != 3:
        return False
    for val in handSet:
        if hand.count(val) == 3:
            return True
    return False

def threeOfAKindFinder(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if threeOfAKindFinderWithoutJ(hand):
        return True
    if len(handSet) != 4:
        return False
    if not "J" in handSet:
        return False
    for val in handSet:
        if hand.count(val) == 2:
            return True
    return False # Watch



# def twoPairFinderWithoutJ(hand: str):
#     assert len(hand) == 5
#     handSet = list(set(hand))
#     if len(handSet) != 3:
#         return False
#     storageNum = 0
#     for val in handSet:
#         if hand.count(val) == 2:
#             storageNum += 1
#     if storageNum == 2:
#         return True
#     return False

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

def onePairFinderWithoutJ(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if len(handSet) != 4:
        return False
    for val in handSet:
        if hand.count(val) == 2:
            return True
    return False

def onePairFinder(hand: str):
    assert len(hand) == 5
    handSet = list(set(hand))
    if onePairFinderWithoutJ(hand):
        return True
    if "J" not in handSet:
        return False
    return True

        
    
def highCardFinder(hand: str):
    assert len(hand) == 5
    return len(set(hand)) == 5

def handIdentifier(hand: str):
    returnDict = {"fiveOfAKind":fiveOfAKindFinder(hand),
            "fourOfAKind":fourOfAKindFinder(hand),
            "fullHouse":fullHouseFinder(hand),
            "threeOfAKind":threeOfAKindFinder(hand),
            "twoPair":twoPairFinder(hand),
            "onePair":onePairFinder(hand),
            "highCard":highCardFinder(hand)
            }
    if not any(list(returnDict.values())[:6]):
        if "J" in hand:
            print(hand,returnDict)
    trueFound = False
    for k,v in returnDict.items():
        if trueFound:
            returnDict[k] = False
        if v:
            trueFound = True
    return returnDict

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
    awns = sum(pointsPergame)
    print(awns)
        

if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print('--- %s seconds ---' % (time.time() - start_time))
