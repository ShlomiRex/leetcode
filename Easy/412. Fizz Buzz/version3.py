"""
Runtime: 45 ms beats 43%
Memory: 17.6 MB beats 70%
Time taken: less than 1 minute
"""
from typing import List
def fizzBuzz(n: int) -> List[str]:
    res = []
    for i in range(1, n+1):
        if i % 15 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res

if __name__ == "__main__":
    assert fizzBuzz(3) == ["1", "2", "Fizz"]
    assert fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzBuzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]