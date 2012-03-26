def countCoinChange_1(cointypes, money):

    if(money == 0):
        return 1

    if(money < 0 or len(cointypes) <= 0):
        return 0

    return countCoinChange_1(cointypes[1:], money) + \
            countCoinChange_1(cointypes, money-cointypes[0])


def countMinCoinChange(cointypes, money):
    
    lastcoin = [0 for i in range(0, money+1)]
    usedcoin = [0 for i in range(0, money+1)]

    for x in range(1, money+1):
        mincoins = x
        for coin in cointypes:
            if coin <= x:
                if(usedcoin[x - coin] + 1 <= mincoins):
                    mincoins = usedcoin[x - coin] + 1
                    lastcoin[x] = coin
                    usedcoin[x] = mincoins                    
    trackprint(lastcoin, money)
    return usedcoin[money]
    
def trackprint(lastcoin, money):
    if money == 0:
        print ''
        return
    else:
        print lastcoin[money],
        trackprint(lastcoin, money-lastcoin[money])
        
if __name__ == '__main__':
    #cointypes = [ 50, 10, 1, 5, 25 ]
    #print countCoinChange_1(cointypes, 100)
    
    cointypes = [25, 21, 10, 5, 1]
    
    print countMinCoinChange(cointypes, 16)
    print countMinCoinChange(cointypes, 15)
    print countMinCoinChange(cointypes, 46)
    print countMinCoinChange(cointypes, 62)
    print countMinCoinChange(cointypes, 63)
    print countMinCoinChange(cointypes, 100)
