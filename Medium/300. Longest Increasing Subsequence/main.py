from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    assert lengthOfLIS(nums) == 4

    nums = [0,1,0,3,2,3]
    assert lengthOfLIS(nums) == 4

    nums = [7,7,7,7,7,7,7]
    assert lengthOfLIS(nums) == 1
