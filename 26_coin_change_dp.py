def dpMakeChange(coinValueList,change):
    minCoins = [0]*(amnt+1)
    for cents in range(change+1):
       coinCount = cents
       for j in [c for c in coinValueList if c <= cents]:
             if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
       minCoins[cents] = coinCount
    return minCoins[change]

amnt = 63
clist = [1,5,10,21,25]
   
dpMakeChange(clist, amnt)
