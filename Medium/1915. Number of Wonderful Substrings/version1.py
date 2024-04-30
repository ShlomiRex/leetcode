"""
Time Limit Exceeded, passed 48/88 test cases

Brute force approach

ccjjc
{
    c: 3
    j: 2
}
At most one letter (c) appears odd number of times (3).

abab
{
    a: 2
    b: 2
}
Wonderful, at most one letter (in this case no letter) appears odd number of times.

ab
{
    a: 1
    b: 1
}
Not wonderful, two letters (a,b) appear odd number of times.


Brute force approach: for each substring, create hashmap of frequencies of letters. 
Check hashmap if wonderful or not. Return count of substrings wonderful.

To get substring we have 2 pointers: start and end. For loop inside for loop. Runtime complexity: O(n^2)
"""
from collections import defaultdict, Counter
def wonderfulSubstrings(word: str) -> int:
    n = len(word)
    ans = 0
    for i in range(n):
        freq = defaultdict(int)
        for j in range(i+1, n+1):
            substring = word[i:j]
            freq = Counter(substring)
            odd_freq_count, is_wonderful = 0, True
            for freq_val in freq.values():
                if freq_val % 2 == 1:
                    odd_freq_count += 1
                if odd_freq_count >= 2:
                    is_wonderful = False
                    break
            if is_wonderful:
                ans += 1
    return ans

if __name__ == "__main__":
    assert wonderfulSubstrings("aba") == 4
    assert wonderfulSubstrings("aabb") == 9
    assert wonderfulSubstrings("he") == 2