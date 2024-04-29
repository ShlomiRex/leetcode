from typing import List

"""
Note: This version doesn't, yet, output unique combinations, but raher, all combinations.
"""

def create_tree_level(candidates: List[int], curr_combo: List[int], target: int):
    res = []
    for n in candidates:
        res.append([curr_combo + [n], target - n])
    return res


def combinationSum(candidates: List[int], target: int):
    res = []

    tree_level = create_tree_level(candidates, [], target)

    # Stack / queue that stores leafs of the tree, such that will later create level for them
    q = tree_level

    while q:
        # Create level for each leaf
        combo, new_target = q.pop()
        if new_target > 0:
            leafs = create_tree_level(candidates, combo, new_target)
            q.extend(leafs)

        elif new_target == 0:
            # We found combo that sums to target!
            res.append(combo)
        else:
            # Do nothing, this path is impossible
            pass

    return res


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    res = combinationSum(candidates, target)
    print(res)
    assert res == [[2, 2, 3], [7]]

    candidates = [2, 3, 5]
    target = 8
    res = combinationSum(candidates, target)
    print(res)
    assert res == [[2,2,2,2],[2,3,3],[3,5]]
