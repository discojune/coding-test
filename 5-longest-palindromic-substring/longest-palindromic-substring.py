class Solution:
    def longestPalindrome(self, s: str) -> str:
        palin_length = len(s)

        while palin_length > 1:
            for i in range(len(s) - palin_length + 1):
                word = s[i:i+palin_length]
                if word == word[::-1]:
                    return word

            palin_length -= 1

        return s[0]