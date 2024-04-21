"""
Runtime: 724 ms beats 75%
Memory: 27.5 MB beats 11%

I used neetcode. I didn't understand when to increment L,R. Apperantly we don't increment L, we only set it to lowest price.
"""
from typing import List
def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1: return 0
    maxProfit = 0
    l, r = 0, 1
    while r < n:
        # If price going down, we have new low, set left pointer
        if prices[l] >= prices[r]: l = r
        # Else, price going up, calculate new max profit
        else: maxProfit = max(maxProfit, prices[r]-prices[l])
        # in any case we increment r
        r += 1
    return maxProfit

if __name__ == "__main__":
    assert maxProfit([7,1,5,3,6,4]) == 5
    assert maxProfit([7,6,4,3,1]) == 0
