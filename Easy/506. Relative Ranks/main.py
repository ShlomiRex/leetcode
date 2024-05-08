from typing import List
def findRelativeRanks(score: List[int]) -> List[str]:
    # Unique scores, perhaps keys?
    sorted_score = score[:]
    sorted_score.sort(reverse=True)
    hashmap = {}
    for i in range(len(sorted_score)):
        hashmap[sorted_score[i]] = i+1
    res = []
    for i in range(len(score)):
        if score[i] == sorted_score[0]:
            res.append("Gold Medal")
        elif score[i] == sorted_score[1]:
            res.append("Silver Medal")
        elif score[i] == sorted_score[2]:
            res.append("Bronze Medal")
        else:
            res.append(str(hashmap[score[i]]))
    return res

if __name__ == "__main__":
    assert findRelativeRanks([5,4,3,2,1]) == ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
    assert findRelativeRanks([10,3,8,9,4]) == ["Gold Medal","5","Bronze Medal","Silver Medal","4"]