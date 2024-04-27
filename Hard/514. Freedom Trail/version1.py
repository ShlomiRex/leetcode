"""
This is greedy solution.

Passed 55/303 test cases

Failed on test case:
ring = "nyngl"
keys = ""yyynnnnnnlllggg"
"""
def findRotateSteps(ring: str, key: str) -> int:
    ans = 0
    n = len(ring)
    ring = list(ring)
    
    for i, c in enumerate(key):
        # Find the character 'c' in dp such that its rotation (clockwise or counterclockwise) is minimal.
        for i in range(n):
            cw_char = ring[i]
            ccw_char = ring[(n-i) % n]
            if cw_char == c:
                # We found
                print(f"To get to '{c}' we need to rotate clockwise {i} times")
                ans += i + 1
                # Shift ring
                print(f"Before shifting ring: {ring}")
                positions = i % n
                ring[:] = ring[positions:] + ring[:positions]
                print(f"After shifting ring: {ring}")
                print(f"ans: {ans}")
                break
            elif ccw_char == c:
                print(f"To get to '{c}' we need to rotate counter-clockwise {i} times")
                ans += i + 1
                # Shift ring
                print(f"Before shifting ring: {ring}")
                positions = i % n
                ring[:] = ring[-positions:] + ring[:-positions]
                print(f"After shifting ring: {ring}")
                print(f"ans: {ans}")
                break
    print(f"Ans: {ans}")
    return ans
if __name__ == "__main__":
    #assert findRotateSteps(ring = "godding", key = "gd") == 4
    #assert findRotateSteps(ring = "godding", key = "godding") == 13
    assert findRotateSteps(ring = "nyngl", key = "yyynnnnnnlllggg") == 19