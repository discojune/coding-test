class Solution:
    def removeStars(self, s: str) -> str:
        from collections import deque

        s = deque(list(s))

        output = deque([])
        while s:
            c = s.popleft()

            if c == "*":
                output.pop()
            
            else:
                output.append(c)

        return ''.join(output)

            


