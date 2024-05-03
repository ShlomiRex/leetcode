"""
Runtime: 41 ms beats 16%
Memory: 16.5 MB beats 49%

More compact and readable code, same complexity
"""
def compareVersion(version1: str, version2: str) -> int:
    v1split, v2split = version1.split('.'), version2.split('.')
    v1len, v2len = len(v1split), len(v2split)
    num_revisions = max(v1len, v2len)
    for i in range(num_revisions):
        rev1 = int(v1split[i]) if i < v1len else 0
        rev2 = int(v2split[i]) if i < v2len else 0
        if rev1 > rev2: return 1
        elif rev2 > rev1: return -1
    return 0

if __name__ == "__main__":
    assert compareVersion()