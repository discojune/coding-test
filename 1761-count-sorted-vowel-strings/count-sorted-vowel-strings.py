class Solution:
    def countVowelStrings(self, n: int) -> int:

        vowels = ["a", "e", "i", "o", "u"]

        memoization = []
        for _ in range(n):
            
            temp = set()
            if not memoization:
                for i, vowel in enumerate(vowels):
                    temp.add(vowel)

                memoization = temp

                continue

                
            for mem_string in memoization:
                for vowel in vowels:
                    if mem_string[-1] < vowel:
                        continue
                    string = mem_string + vowel
                    temp.add(string)

            memoization = temp

        return len(memoization)

