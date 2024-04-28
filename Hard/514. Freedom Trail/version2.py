"""
Runtime: 210 ms beats 41%
Memory: 17.3 MB beats 43%

Solution from neetcode.
"""
def findRotateSteps(ring: str, key: str) -> int:
    cache = {}
    def helper(r, k):
        if k == len(key):
            return 0
        if (r, k) in cache:
            return cache[(r, k)]
        
        res = float('inf')
        for i, c in enumerate(ring):
            if c == key[k]:
                min_dist = min(abs(r-i), len(ring) - abs(r-i))
                res = min(res, min_dist + 1 + helper(i, k+1))
        cache[(r, k)] = res
        return res
    return helper(0, 0)
if __name__ == "__main__":
    assert findRotateSteps(ring = "godding", key = "gd") == 4
    assert findRotateSteps(ring = "godding", key = "godding") == 13
    assert findRotateSteps(ring = "nyngl", key = "yyynnnnnnlllggg") == 19