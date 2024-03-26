
"""

Time taken: 23 mins
Runtime: 54 ms beats 47%
Memory: 16 MB beats 72%

Solution:
I immedietly found the right solution. I visualized in my head this:

PAYPALISHIRING
01232101232101

Basically we give each character their row number.

Chars of first row (0): PIN
Second row (1): ALSIG
Third row (2): YAHR
Fourth row (3): PI

We get: PINALSIGYAHRPI
"""
def convert(s: str, numRows: int) -> str:
    # Solution: start with index 0 until last index of string
    # Then set row for each character
    # Store the chararcter in datastructure that stores numRows strings
    if numRows == 1:
        return s
    
    string_array = ["" for _ in range(numRows)]
    curr_row, increasing = 0, True
    for c in s:
        if curr_row == (numRows - 1):
            increasing = False
        elif curr_row == 0:
            increasing = True

        string_array[curr_row] += c

        if increasing:
            curr_row += 1
        else:
            curr_row -= 1
    
    # Concatinste each string in the array
    final_str = ""
    for s in string_array:
        final_str += s
    return final_str

if __name__ == "__main__":
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convert("A", 1) == "A"
    assert convert("AB", 1) == "AB"
    assert convert("ABC", 1) == "ABC"
    assert convert("ABCD", 1) == "ABCD"