class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        
        trapped_water = 0

        while left < right:
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)

            if max_left <= max_right:
                trapped_water += max_left - height[left]
                left += 1

            else:
                trapped_water += max_right - height[right]
                right -= 1

        return trapped_water







            