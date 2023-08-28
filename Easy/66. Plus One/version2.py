def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    new_digits = [0] * (len(digits) + 1)
    new_digits[0] = 1
    return new_digits


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
