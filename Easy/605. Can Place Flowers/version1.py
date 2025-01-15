"""
Runtime complexity: O(n)
Time taken: 28:08

This question is harder than it looks because of all the edge cases.
"""

from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if n == 0:
        return True
    
    num_available = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            continue
        
        if i >= 1:
            left = flowerbed[i-1]
        else:
            left = 0
        
        if i <= len(flowerbed)-2:
            right = flowerbed[i+1]
        else:
            right = 0
        
        # check can place flower
        if left == 0 and right == 0:
            num_available += 1
            flowerbed[i] = 1 # plant the flower

        # Exit condition
        if num_available == n:
            return True
    return False

if __name__ == "__main__":
    assert canPlaceFlowers([1,0,0,0,1], 1) == True
    assert canPlaceFlowers([1,0,0,0,1], 2) == False
    assert canPlaceFlowers([1,0,0,0,0,1], 2) == False
    assert canPlaceFlowers([1], 0) == True
    assert canPlaceFlowers([1], 1) == False
    assert canPlaceFlowers([1, 0], 1) == False
    assert canPlaceFlowers([1, 0], 2) == False
    