"""
Runtime: 5685 ms beats 26%
Memory: 75.09 MB beats 36%
Time taken: 1 hour 53 minutes 12 seconds, I looked at solution. Very hard problem.

========================================================================================

Maybe DP?

n = 1
"A", "L", "P"
Attendence award: 3 because they all match the criteria

n = 2
"AP", "AL", "AA"
"LA", "LP", "LL"
"PA", "PL", "PP"
Attentence awards: 8 because only "AA" is not eligible because there are 2 absences

Notice for each n+1 we add 'A', or 'L' or 'P to the end of each record.
Maybe DP can help us, since we don't need to remember or count A, L, or P.
We can also maybe use recursion with (n+1) = n + (n-1) or something, so its perfect for DP.

For each record we need to check: 
* count('A') < 2
* Never 'L' three times in a row

Total number of options at n:
3^n

For n = 3:
"APA", "APP", "APL"
"ALA", "ALP", "ALL"
"AAA", "AAP", "AAL"
"LAA", "LAP", "LAL"
"LPA", "LPP", "LPL"
"LLA", "LLP", "LLL"
"PAA", "PAP", "PAL"
"PLA", "PLP", "PLL"
"PPA", "PPP", "PPL"

From "Total Options" we need to remove all options that don't match this criteria:
answer = (total) - (don't match first rule) - (don't match second rule)

Don't match first rule:

"""
def checkRecord(n: int) -> int:
    # if n == 1:
    #     return 3
    # elif n == 2:
    #     return 8
    # totalOptions = 3 ** (n)

    # # Absent for 0 or 1 days total
    # absentFor0DaysTotal = (2/3)**n # For each day we either L or P (2/3) but not A
    # absentFor1DayTotal = (1/n)*(1/3)*(2/3)**(n-1) # All other days can be either L or P
    # absentSticlyFewerThan2DaysTotal = absentFor0DaysTotal + absentFor1DayTotal

    # # Student was never late 'L' for 3 or more consecutive days
    # # Pick first day, then second day, then third day
    # # Then pick 'L' for all three days
    # lateFor3OrMoreConsecutiveDays = (1/n) * (1/(n-1)) * (1/(n-2)) * ((1/3)**3)
    # notLateFor3OrMoreConsecutiveDays = 1-lateFor3OrMoreConsecutiveDays
    # print(totalOptions)
    # ans = totalOptions - (absentSticlyFewerThan2DaysTotal*totalOptions) - (notLateFor3OrMoreConsecutiveDays*totalOptions)
    # return ans % (10**9 + 7)

    memo = []
    # Create 3D Memo DP array. We have 3 variables: n, total_absences, consecutive lates
    # n: (n+1) possabilities
    # total_absences: 2 possabilities (0, 1, if its 2 we backtrack)
    # consecutive_lates: 3 possabilities (0, 1, 2, if its 3 we backtrack)
    # First dimension: n
    for i in range(n+1):
        # Second dimension: total_absences: 2 appends
        memo.append([[-1] * 3, [-1] * 3]) # Third dimension: consecutive_lates: 3 cells
    MOD = 1000000007
    def count_awards(n, total_absences, consecutive_lates):
        if total_absences >= 2 or consecutive_lates >= 3: 
            return 0
        if n == 0:
            return 1
        if memo[n][total_absences][consecutive_lates] != -1:
            return memo[n][total_absences][consecutive_lates]
        
        ans = count_awards(n-1, total_absences, 0)                         # Pick P, we reset consecutive lates
        ans += count_awards(n-1, total_absences+1, 0)                        # Pick A, total absence increased, reset consecutive lates
        ans += count_awards(n-1, total_absences, consecutive_lates + 1)     # Pick L, increase consecutive lates
        
        ans %= MOD
        memo[n][total_absences][consecutive_lates] = ans
        return ans
    
    return count_awards(n, 0, 0)

if __name__ == "__main__":
    assert checkRecord(1) == 3
    assert checkRecord(2) == 8
    assert checkRecord(3) == 19
    assert checkRecord(4) == 43
    assert checkRecord(5) == 94
    assert checkRecord(6) == 200
    assert checkRecord(10101) == 183236316