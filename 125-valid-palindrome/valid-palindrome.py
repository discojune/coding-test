class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric characters
        s = s.lower().strip()
        s = list(filter(str.isalnum, s))

        while len(s) > 1:
            if s.pop(0) != s.pop():
                return False

        
        return True