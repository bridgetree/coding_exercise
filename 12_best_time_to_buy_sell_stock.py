# DP

def maxProfit1(prices):
    if not prices:
        return 0
    loc = glo = 0
    for i in range(1, len(prices)):
        loc = max(loc+prices[i]-prices[i-1], 0)
        glo = max(glo, loc)
    return glo
