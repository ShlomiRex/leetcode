"""
Runtime: 44 ms, faster than 77.13% of Python3 online submissions for Remove K Digits.
Memory Usage: 14.1 MB, less than 93.92% of Python3 online submissions for Remove K Digits.
"""

# Pseudo Algorithm - I completely invented this way (no hints or help)
"""
1) for i in range(k):
    1.1) Start scanning the number from left to right (digit by digit)
        1.1.1) If the digit is greater than prev digit (increasing), or equal to previous digit, keep scanning
        1.1.2) If the current digit is less than previous digit (decreasing) then remove previous digit
        1.1.3) When reached last digit, then stop here, and remove the last digit
"""

# Examples
"""
num = 12345
k = 3
All digits increasing - so for i=0 we get to last digit, and remove '5'.
All digits increasing - so for i=1 we get to last digit, and remove '4'.
All digits increasing - so for i=2 we get to last digit, and remove '3'.
We are left with '12' which is the correct answer.
"""
"""
num = 54321
k = 3
All digits decreasing - so for i=0 we at the digit '4', which is less than previous digit '5', so we stop here and remove '5'.
All digits decreasing - so for i=1 we at the digit '3', which is less than previous digit '4', so we stop here and remove '4'.
All digits decreasing - so for i=3 we at the digit '2', which is less than previous digit '3', so we stop here and remove '3'.
We are left with '21' which is the correct answer.
"""


def removeKdigits(num: str, k: int) -> str:
    l = len(num)
    if k == l:
        return "0"
    for _ in range(k):
        num = remove1Digit(num)

        # Strip leading zeroes, if there is any
        strip_end = 0
        for i in range(len(num)):
            digit = num[i]
            if digit == "0":
                strip_end += 1
            else:
                break
        num = num[strip_end:]
        if len(num) == 0:
            return "0"
    return num


def remove1Digit(num: str) -> str:
    prev_digit = num[0]
    for i in range(1, len(num)):
        curr_digit = num[i]
        # If increasing or equal to
        if curr_digit >= prev_digit:
            # Keep scanning
            pass
        # If decreasing
        elif curr_digit < prev_digit or curr_digit == "0":
            # Then remove previous digit
            return num[:i-1] + num[i:]
        prev_digit = curr_digit
    return num[:-1]

if __name__ == "__main__":
    res = remove1Digit("12345")
    assert res == "1234"
    res = remove1Digit("1234")
    assert res == "123"
    res = remove1Digit("54321")
    assert res == "4321"

    num = "12345"
    k = 3
    res = removeKdigits(num, k)
    print(res)
    assert res == "12"

    num = "54321"
    k = 3
    res = removeKdigits(num, k)
    print(res)
    assert res == "21"

    num = "1432219"
    k = 3
    res = removeKdigits(num, k)
    print(res)
    assert res == "1219"

    num = "1444322"
    k = 3
    res = removeKdigits(num, k)
    print(res)
    assert res == "1322"

    num = "10200"
    k = 1
    res = removeKdigits(num, k)
    print(res)
    assert res == "200"

    num = "109"
    k = 1
    res = removeKdigits(num, k)
    print(res)
    assert res == "9"

    num = "109"
    k = 2
    res = removeKdigits(num, k)
    print(res)
    assert res == "0"

    num = "109"
    k = 3
    res = removeKdigits(num, k)
    print(res)
    assert res == "0"

    num = "100"
    k = 1
    res = removeKdigits(num, k)
    print(res)
    assert res == "0"

    num = "10001"
    k = 4
    res = removeKdigits(num, k)
    print(res)
    assert res == "0"

    num = "100101"
    k = 4
    res = removeKdigits(num, k)
    print(res)
    assert res == "0"

    num = "100101"
    k = 1
    res = removeKdigits(num, k)
    print(res)
    assert res == "101"

