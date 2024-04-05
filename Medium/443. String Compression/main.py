"""
Runtime: 58 ms beats 58%
Memory: 16.7 MB beats 80%
Time taken: 24 minutes 16 seconds

I immedietly knew what I had to do. There are no tricks here. No complex algorithms. Just plain iteration.
"""
from typing import List
def compress(chars: List[str]) -> int:
    l, r = 0, 0

    def count_char(starting_index, char) -> (int, int):
        count = 0
        while starting_index < len(chars) and chars[starting_index] == char:
            count += 1
            starting_index += 1
        return count, starting_index

    while r < len(chars):
        count, finish_index = count_char(r, chars[r])
        chars[l] = chars[r] # Mark character
        l += 1
        if count > 1:
            count_lst = list(str(count))
            # Mark frequency
            for digit in count_lst:
                chars[l] = digit
                l += 1
        r = finish_index # r changed while counting, update
    return l

if __name__ == "__main__":
    chars = ["a","a","b","b","c","c","c"]
    assert compress(chars) == 6
    assert chars[:-1] == ["a","2","b","2","c","3"] # Last element doesn't matter (i.e. modified list length is 6)

    chars = ["a"]
    assert compress(chars) == 1
    assert chars == ["a"]

    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    assert compress(chars) == 4
    assert chars[:4] == ["a","b","1","2"]
