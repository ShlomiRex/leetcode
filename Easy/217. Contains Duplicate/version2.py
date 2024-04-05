"""
Runtime: 426 ms beats 37%
Memory: 31.92 MB beats 65%
Using hashset instead of hashmap is a little faster and we also don't need to store number of occurances, we only the store visited numbers.
"""
from typing import List
def containsDuplicate(nums: List[int]) -> bool:
	hashset = set()
	for n in nums:
		if n in hashset:
			return True
		hashset.add(n)
	return False

if __name__ == "__main__":
	assert containsDuplicate([1,2,3,1]) == True
	assert containsDuplicate([1,2,3,4]) == False
	assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
