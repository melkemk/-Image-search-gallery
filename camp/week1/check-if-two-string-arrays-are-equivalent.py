class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1="".join(map(str,word1))
        string2="".join(map(str,word2))
        print(string1)
        return string1==string2