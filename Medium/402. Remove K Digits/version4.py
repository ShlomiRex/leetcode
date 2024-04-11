"""

"""
def removeKdigits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            k -= 1
            stack.pop()
        stack.append(digit)
    stack = stack[:len(stack) - k]
    res = "".join(stack).lstrip('0')
    return res if res else "0"

if __name__ == "__main__":
    # assert removeKdigits("1432219", 3) == "1219"
    # assert removeKdigits("10200", 1) == "200"
    # assert removeKdigits("10", 2) == "0"
    #assert removeKdigits("10001", 4) == "0"
    assert removeKdigits("1234567890", 9) == "0"

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
