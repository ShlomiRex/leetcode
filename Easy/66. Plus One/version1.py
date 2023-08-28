def plusOne(digits):
    l = len(digits)

    if digits[l-1] != 9:
        digits[l-1] += 1
    else:
        carry = True
        i = l - 1
        while carry and i > -1:
            if digits[i] == 9:
                digits[i] = 0
            else:
                carry = False
                digits[i] += 1
            i -= 1
        if carry:
            digits = [0] * (l+1)
            digits[0] = 1
    return digits


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(plusOne(arr))

    arr = [1, 2, 9]
    print(plusOne(arr))

    arr = [1, 9, 9]
    print(plusOne(arr))

    arr = [9, 9, 9]
    print(plusOne(arr))

    arr = [9]
    print(plusOne(arr))

    arr = [8, 9, 9]
    print(plusOne(arr))
