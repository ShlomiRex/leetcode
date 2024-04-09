"""
Runtime: 31 ms beats 95%
Memory: 16.5 MB beats 59%
"""
from typing import Counter, List
def countStudents(students: List[int], sandwiches: List[int]) -> int:
    res, cnt = len(students), Counter(students)
    for s in sandwiches:
        if cnt[s] > 0: res, cnt[s] = res-1, cnt[s]-1
        else: return res
    return res

if __name__ == "__main__":
    assert countStudents([1,1,0,0], [0,1,0,1]) == 0
    assert countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]) == 3