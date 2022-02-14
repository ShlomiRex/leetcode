from typing import List

"""
Runtime: 285 ms, faster than 43.46% of Python3 online submissions for Reverse String.
Memory Usage: 18.4 MB, less than 74.90% of Python3 online submissions for Reverse String.
"""

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    if s is None:
        return
    l = len(s)
    mid_i = int(l / 2)
    for i in range(mid_i):
        n1 = s[i]
        n2 = s[l - i - 1]
        s[i] = n2
        s[l - i - 1] = n1


if __name__ == "__main__":
    i = ["h", "e", "l", "l", "o"]
    reverseString(i)
    assert i == ["o", "l", "l", "e", "h"]

    i = None
    reverseString(i)
    assert i is None

    i = []
    reverseString(i)
    assert i == []

    i = ['a']
    reverseString(i)
    assert i == ['a']


