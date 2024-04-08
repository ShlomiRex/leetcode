"""
Runtime: 35 ms beats 84%
Memory: 16.4 MB beats 95%
Time taken: 38 minutes, i had to look at solution since I was trying to implement the simulation with stack and queue...

The order does matter here

Students: [1,1,1,1]
Sandwiches: [0,1,1,1]
Then output is 4, none of the students want to eat first sandwich

But if sandwiches is: [1,1,1,0]
Then output is 1 (first 3 students want to eat sandwich on top of the stack)
"""
from collections import defaultdict
from typing import List
def countStudents(students: List[int], sandwiches: List[int]) -> int:
    res = len(students) # We assume all students are hungry

    # Count preferred shapes of students
    cnt = defaultdict(int)
    for s in students:
        cnt[s] += 1
    
    # Now lets see who we can feed, we go by the top of the stack, this is the tricky part
    # We iterate over sandwiches just like stack, we don't iterate over students, this is the trick.
    for s in sandwiches:
        if cnt[s] > 0:
            res -= 1 # We feed this kid
            cnt[s] -= 1 # We are left with less sandwiches of this shape
        # We don't have left sandwiches left of that shape
        else:
            return res # Immedietly return because non are willing to eat the top of the stack so that means everyone else is hungry (check comments above)
    return res

if __name__ == "__main__":
    assert countStudents([1,1,0,0], [0,1,0,1]) == 0
    assert countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]) == 3