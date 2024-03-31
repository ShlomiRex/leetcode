"""
Runtime: 54 ms beats 24%
Memory: 16 MB beats 100%
Time taken: 4 minutes 47 seconds
"""
from typing import List
def minOperations(logs: List[str]) -> int:
    folder_level = 0
    for op in logs:
        if op == "../" and folder_level > 0:
            folder_level -= 1
        elif op != "./" and op != "../":
            # i.e. the operation "x/"
            folder_level += 1
    return folder_level

if __name__ == "__main__":
    assert minOperations(["d1/","d2/","./","d3/","../","d31/"]) == 3
    assert minOperations(["d1/","../","../","../"]) == 0