"""
Runtime: 812 ms beats 50%
Memory: 43.6 MB beats 8%
Time taken: 9 minutes 4 seconds

This is greedy approach.
"""
from typing import List
def maximumHappinessSum(happiness: List[int], k: int) -> int:
    # select i
    # decrease all non-i and non-selected i's until now hapiness by 1
    # [1,2,3]
    # Select 3: [0, 1]
    # Select 0: [1]
    # 3+0 = 3 not max

    # Greedy: pick all max hapiness
    decrease_count, ans = 0, 0
    happiness.sort(reverse=True)
    for i in range(k):
        ans += max(0, (happiness[i] - decrease_count))
        decrease_count += 1
    return ans

if __name__ == "__main__":
    assert maximumHappinessSum(happiness = [1,2,3], k = 2) == 4
    assert maximumHappinessSum(happiness = [1,1,1,1], k = 2) == 1
    assert maximumHappinessSum(happiness = [2,3,4,5], k = 1) == 5