from typing import List

"""
Runtime: 53 ms, faster than 37.94% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.1 MB, less than 73.33% of Python3 online submissions for Longest Common Prefix.
"""

def longestCommonPrefix(strs: List[str]) -> str:
    if strs is None or len(strs) == 0:
        return ""

    longest_common_prefix = ""


	# Check at each str at index 'index' if the char is common to every other string.
	# If it is, increment index, and append the common char to the longest_common_prefix.
	# Else, we are done.
    index = 0
    while True:
        if index >= len(strs[0]):
            break

		# Take example char to be checked at every other string.
        common_char = strs[0][index]
        is_common_to_all = True

		# Check if all strings have this common prefix at index 'index'.
        for str in strs:
            if index < len(str):
                if str[index] != common_char:
                    is_common_to_all = False
                    break
            else:
                return longest_common_prefix

		# All strings have common prefix at index 'index'. Add it to the longest_common_prefix.
        if is_common_to_all:
            longest_common_prefix += common_char
        else:
			# No common prefix at index 'index'. We are done.
            break

        index = index + 1

    return longest_common_prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    res = longestCommonPrefix(strs)
    print(res)
    assert res == "fl"

    strs = ["test", "te"]
    res = longestCommonPrefix(strs)
    print(res)
    assert res == "te"

    strs = ["t", "test"]
    res = longestCommonPrefix(strs)
    print(res)
    assert res == "t"

    strs = ["test"]
    res = longestCommonPrefix(strs)
    print(res)
    assert res == "test"

    strs = ["t"]
    res = longestCommonPrefix(strs)
    print(res)
    assert res == "t"

    strs = ["abc", "abcd", "abc", "abcdef"]
    res = longestCommonPrefix(strs)
    print(res)
    assert res == "abc"

    strs = ["dog", "racecar", "car"]
    res = longestCommonPrefix(strs)
    print(res)
    assert res == ""
