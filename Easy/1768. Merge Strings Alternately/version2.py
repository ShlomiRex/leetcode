"""
Taken from editorial solution. Much more elegant code.
"""
def mergeAlternately(word1, word2):
    result = []
    n = max(len(word1), len(word2))
    for i in range(n):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]

    return "".join(result)

if __name__ == "__main__":
    assert mergeAlternately("abc", "pqr") == "apbqcr"
    assert mergeAlternately("ab", "pqrs") == "apbqrs"
    assert mergeAlternately("abcd", "pq") == "apbqcd"
