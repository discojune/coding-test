class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_min_len = min(len(word1), len(word2))

        word_output = []
        for i in range(word_min_len):
            word_output.append(word1[i])
            word_output.append(word2[i])

        if len(word1) == word_min_len:
            word_output.append(word2[word_min_len:])
        elif len(word2) == word_min_len:
            word_output.append(word1[word_min_len:])


        return ''.join(word_output)