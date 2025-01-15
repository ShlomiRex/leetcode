"""
Runtime complexity: O(n1 + n2)
Time taken: 8:24

The code is a mess but it works
The idea is to check the index i: if its even, then we choose character from word1. If its odd, then we choose character from word2.
If we finished with word1, then we fill chars with word2, and vice versa.
"""
def mergeAlternately(word1: str, word2: str) -> str:
    n1 = len(word1)
    n2 = len(word2)
    chars = [0] * (n1 + n2)
    word1_i = 0
    word2_i = 0
    for i in range(n1 + n2):
        if i % 2 == 0:
            if word1_i <= n1-1:
                c = word1[word1_i]
                word1_i += 1
            else:
                c = word2[word2_i]
                word2_i += 1
        else:
            if word2_i <= n2-1:
                c = word2[word2_i]
                word2_i += 1
            else:
                c = word1[word1_i]
                word1_i += 1
        chars[i] = c

    return ''.join(chars)

if __name__ == "__main__":
    assert mergeAlternately("abc", "pqr") == "apbqcr"
    assert mergeAlternately("ab", "pqrs") == "apbqrs"
    assert mergeAlternately("abcd", "pq") == "apbqcd"
