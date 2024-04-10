"""
Runtime: 36 ms beats 49%
Memory: 16.5 MB beats 45%
Time taken: 15 minutes
"""
def toGoatLatin(sentence: str) -> str:
    res = ""
    words = sentence.split()
    for i, word in enumerate(words):
        word_res = word
        if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            word_res += "ma"
        else:
            word_res = word[1:] + word[0] + "ma"
        word_res += (i+1)*"a"
        res += word_res + " "
    return res[:-1]

if __name__ == "__main__":
    assert toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"