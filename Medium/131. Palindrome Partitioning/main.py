"""
Runtime: 996 ms beats 5%
Memory: 35.24 MB beats 41%
Time taken: 45 minutes 31 seconds, but its more since the tab was unfocused

Brute force approach
Use backtracking to generate all possible partitions of the string, and at the end check if each partition is a palindrome.
"""
from typing import List
def partition(s: str) -> List[List[str]]:
    n = len(s)
    def isPalindrome(arr_of_str: List[str]) -> bool:
        for s in arr_of_str:
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
        return True

    def backtrack(i, ans):
        if i == n:
            return ans
        new_ans = []
        for curr_ans in ans:
            # Extend curr with s[i]
            a = curr_ans[:] + [s[i]]

            # Add s[i] to curr[-1]
            b = curr_ans[:]
            b[-1] += s[i]
            #b = curr_ans[:-1] + [b]

            new_ans.append(a)
            new_ans.append(b)
            #print(new_ans)
        ans = backtrack(i+1, new_ans)
        new_ans = []
        for curr_ans in ans:
            if isPalindrome(curr_ans):
                new_ans.append(curr_ans)
        return new_ans
    #print([[s[0]]])
    _ans = backtrack(1, [[s[0]]])
    #print("Final ans: ", _ans)
    return _ans

if __name__ == "__main__":
    assert partition("aab") == [["a","a","b"],["aa","b"]]
    assert partition("a") == [["a"]]

    assert partition("aaab") == [["a","a","a","b"],["a","aa","b"],["aa","a","b"],["aaa","b"]]
    assert partition("abcaa") == [["a","b","c","a","a"],["a","b","c","aa"]]
    assert partition("abbab") == [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]
    assert partition("abaca") == [["a","b","a","c","a"],["a","b","aca"],["aba","c","a"]]