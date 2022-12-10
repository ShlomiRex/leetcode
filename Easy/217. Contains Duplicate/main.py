from typing import List


def containsDuplicate(nums: List[int]) -> bool:
	hashmap = {}
	for n in nums:
		if n not in hashmap:
			hashmap[n] = True
		else:
			return True
	return False

if __name__ == "__main__":
	assert containsDuplicate([1,2,3,1]) == True
	assert containsDuplicate([1,2,3,4]) == False
	assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
