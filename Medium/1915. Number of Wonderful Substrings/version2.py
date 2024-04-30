"""
Time limit exceeded

Passed 87/88 test cases

How to do it in O(n)?
By using bit masks!
Because the constraints are: word consists only of 'a' to 'j' letters (10 letters) we can keep track of even/odd letters.
Bit 0 means even, bit 1 means odd.
For example: aba, we start with bitmasks: [0, 0, 0, ..., 0] (ten times zero)
First char: a [1, 0, 0, ...]
b: [1, 1, 0, 0, ...]
a: [0, 1, 0, 0, ...]

and so on.

Video explaining: https://www.youtube.com/watch?v=6jDMVwOXb2E

Basically its similar to prefix sum, in question "Subarray Sum Equals K"
We basically count number of prefix sum, in this case, prefix bitmasks XOR.
"""
from collections import defaultdict, Counter
def wonderfulSubstrings(word: str) -> int:
    ans = 0
    count = defaultdict(int)
    bitmasks = [0]*10
    # Convert binary array [0, 1, 0, 1, ...] to number in decimal
    def conv(is_odd):
        b = 0
        for i in range(len(is_odd)):
            b *= 2
            if is_odd[i] == 1:
                b += 1
        return b

    count[0] = 1 # All bitmasks are off, which means count of '0' is 1 at the start.
    for char in word:
        ind = ord(char) - ord('a')
        bitmasks[ind] ^= 1 # We flip the bit (XOR)
        ans += count[conv(bitmasks)]
        # TODO: Understand why we do this V
        for i in range(10):
            bitmasks[i] ^= 1
            ans += count[conv(bitmasks)]
            bitmasks[i] ^= 1
        count[conv(bitmasks)] += 1
    return ans

if __name__ == "__main__":
    assert wonderfulSubstrings("aba") == 4
    assert wonderfulSubstrings("aabb") == 9
    assert wonderfulSubstrings("he") == 2