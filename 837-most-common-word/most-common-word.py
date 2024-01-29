class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[!?',;.]", ' ', paragraph)

        paragraph_words = paragraph.lower().split()

        word_counter = collections.Counter(paragraph_words)

        for word, count in word_counter.most_common():
            if word not in banned:
                return word

            