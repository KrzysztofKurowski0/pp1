def game(hand1,hand2):
    cards = {
    "A":"10",
    "Q":"10",
    "K":"10",
    "J":"10",
    "9":"9",
    "8":"8",
    "7":"7",
    "6":"6",
    "5":"5",
    "4":"4",
    "3":"3",
    "2":"2",
    "1":"1"
    }
    hand1val = 0
    hand2val = 0
    for i in range(len(hand1)):
        for k,v in cards.items():
            if hand1[i] == k:
                hand1val+=int(v)
            else:
                continue
    for j in range(len(hand2)):
        for k,v in cards.items():
            if hand2[j] == k:
                hand2val+=int(v)
            else:
                continue
    if hand1val>hand2val:
        return True
    else:
        return False

print(game("AJK1","AAA"))

