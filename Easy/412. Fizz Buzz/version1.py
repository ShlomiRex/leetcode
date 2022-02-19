from typing import List

"""
Runtime: 76 ms, faster than 20.32% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15.2 MB, less than 21.71% of Python3 online submissions for Fizz Buzz.
"""

def fizzBuzz(n: int) -> List[str]:
	ans = []
	for i in range(1, n+1):
		div3 = (i % 3 == 0)
		div5 = (i % 5 == 0)
		curr = ""
		if div3:
			curr += "Fizz"
		if div5:
			curr += "Buzz"
		if len(curr) == 0:
			ans.append(str(i))
		else:
			ans.append(curr)
	return ans


if __name__ == "__main__":
    n = 3
    res = fizzBuzz(n)
    print(res)
    assert res == ["1", "2", "Fizz"]

    n = 5
    res = fizzBuzz(n)
    print(res)
    assert res == ["1", "2", "Fizz", "4", "Buzz"]

    n = 15
    res = fizzBuzz(n)
    print(res)
    assert res == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                   "FizzBuzz"]
