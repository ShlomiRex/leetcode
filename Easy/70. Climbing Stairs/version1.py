"""

Memory limit exceeded.

Reason: I use dynamic memory which can hold a lot of permutations. This is an easy question, so my guess they want the output to be fibunachi number?

Use dynamic programming. Calculate climbStairs(1) then climbStairs(2) and so on.
The climbStairs(i) requires the output of climbStairs(i-1), with added "1 or 2 steps".

"""
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    dp = [[1]]
    # Do the steps calc
    for i in range(2, n+1):
        # print(f"n = {i}")
        # Here we use permute_i because we add to dp array, so its growing, so we cant do: "for permute in dp".
        for permute_i in range(len(dp)):
            permute = dp[permute_i]
            # print(f"Current permute: {permute}")
            last_step = permute[-1]

            if last_step == 1:
                # print("Last step is 1")
                # Combine last steps (1+1=2) as new permutation
                new_permute = permute[:-1] # Exclude last element (since we combine, we remove one '1' and instead set it with '2')
                new_permute.append(2)
                # print(f"New permute: {new_permute}")
                dp.append(new_permute)

            # Always add 1
            permute.append(1)
            # print(f"DP: {dp}")

    return len(dp)

if __name__ == "__main__":
    # assert climbStairs(1) == 1
    # assert climbStairs(2) == 2
    # assert climbStairs(3) == 3
    # assert climbStairs(4) == 5
    assert climbStairs(5) == 8
    