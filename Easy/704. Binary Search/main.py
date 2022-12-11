from typing import List

def search(nums: List[int], target: int) -> int:
	if len(nums) == 0:
		return -1
	if len(nums) == 1:
		if target == nums[0]:
			return 0
		else:
			return -1
	
	i_low = 0
	i_high = len(nums) - 1
	
	while i_low <= i_high:
		i_mid = int((i_high + i_low)/2)
		mid = nums[i_mid]
		
		if target > mid:
			i_low = i_mid + 1
		elif target < mid:
			i_high = i_mid - 1
		else:
			return i_mid
	return -1


if __name__ == "__main__":
	# nums = [-1,0,3,5,9,12]
	# target = 9
	# assert search(nums, target) == 4

	# nums = [-1,0,3,5,9,12]
	# target = 2
	# assert search(nums, target) == -1

	# nums = [5]
	# target = 5
	# assert search(nums, target) == 0

	nums = [2,5]
	target = 5
	assert search(nums, target) == 1
	