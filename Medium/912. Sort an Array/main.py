from typing import List

"""
Runtime: 1038 ms, faster than 38.62% of Python3 online submissions for Sort an Array.
Memory Usage: 22.9 MB, less than 21.12% of Python3 online submissions for Sort an Array.
"""

def mergeSorted(left: List[int], right: List[int]) -> List[int]:
	l = 0
	r = 0
	res = []
	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			res.append(left[l])
			l += 1
		else:
			res.append(right[r])
			r += 1
	if l < len(left):
		res.extend(left[l:])
	else:
		res.extend(right[r:])
	return res
	

def mergeSort(nums: List[int]) -> List[int]:
	if len(nums) == 1:
		return nums
	lhalf = int(len(nums)/2)
	firstHalf = nums[:lhalf]
	secondHalf = nums[lhalf:]
 
	firstHalfSorted = mergeSort(firstHalf)
	secondHalfSorted = mergeSort(secondHalf)
	return mergeSorted(firstHalfSorted, secondHalfSorted)

if __name__ == "__main__":
	# res = mergeSorted([1, 3], [2,4,6])
	# print(res)
	# assert res == [1,2,3,4,6]

	# res = mergeSorted([100], [2,6,101])
	# print(res)
	# assert res == [2,6,100,101]
	
	nums = [5,2,3,1]
	res = mergeSort(nums)
	print(res)
	assert res == [1,2,3,5]
	
	nums = [1]
	res = mergeSort(nums)
	print(res)
	assert res == [1]
 
	nums = [1, -1, 3, -2, 4, 5, 6, -6, 2]
	res = mergeSort(nums)
	print(res)
	assert res == [-6, -2, -1, 1, 2, 3, 4, 5, 6]
	