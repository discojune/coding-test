class Solution:
    def minFlips(self, target: str) -> int:
        steps = 0
        current_bit = '0'  # s is initially all zeros
        
        for bit in target:
            if bit != current_bit:
                steps += 1
                current_bit = bit
        
        return steps
