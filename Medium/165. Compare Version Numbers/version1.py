"""
Runtime: 41 ms beats 16%
Memory: 16.5 MB beats 49%
Time taken: 6 minutes 45 seconds

revision = '.'
revision: contains leading zeroes and at least one character
"""
def compareVersion(version1: str, version2: str) -> int:
    v1split = version1.split('.')
    v2split = version2.split('.')
    num_revisions = max(len(v1split), len(v2split))
    for i in range(num_revisions):
        if i < len(v1split):
            rev1 = int(v1split[i])
        else:
            rev1 = 0
        
        if i < len(v2split):
            rev2 = int(v2split[i])
        else:
            rev2 = 0
        
        # Version 1 > Version 2
        if rev1 > rev2:
            return 1
        # Version 2 > Version 1
        elif rev2 > rev1:
            return -1
    return 0

if __name__ == "__main__":
    assert compareVersion()